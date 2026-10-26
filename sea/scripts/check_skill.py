"""Validate SEA structure and build a self-contained Markdown edition (stdlib only)."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def validate(root: Path) -> tuple[str, list[tuple[str, Path]]]:
    core = (root / 'SKILL.md').read_text(encoding='utf-8')
    match = re.match(r'^---\n(.*?)\n---(?:\n|$)', core, re.DOTALL)
    if not match:
        raise ValueError('Missing SEA frontmatter')
    values = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        field = re.fullmatch(r'(name|description):[ \t]*(.+)', line)
        if not field or field.group(1) in values:
            raise ValueError('Unsupported or duplicate SEA frontmatter field')
        values[field.group(1)] = field.group(2)
    if set(values) != {'name', 'description'}:
        raise ValueError('SEA requires name and description')
    try:
        description = json.loads(values['description'])
    except json.JSONDecodeError as exc:
        raise ValueError('Description must be a JSON double-quoted string') from exc
    if (values['name'] != 'sea' or root.name != 'sea'
            or not isinstance(description, str) or not description.strip()):
        raise ValueError('Invalid SEA name or description')
    if len(core.splitlines()) > 500:
        raise ValueError('Core exceeds 500 lines')
    links = []
    for target in re.findall(r'\]\(([^)]+)\)', core):
        if target.startswith(('https://', 'http://', '#')):
            continue
        path = (root / target).resolve()
        if not path.is_relative_to(root.resolve()) or not path.is_file():
            raise ValueError(f'Missing or unsafe reference: {target}')
        links.append((target, path))
    for path in root.rglob('*'):
        if path.is_symlink():
            raise ValueError(f'Symlink not allowed in portable package: {path.name}')
        if path.is_file() and path.suffix in {'.md', '.py', '.yaml'}:
            text = path.read_text(encoding='utf-8')
            if '\ufffd' in text or (path.suffix != '.py' and '[TODO:' in text):
                raise ValueError(f'Encoding error or placeholder: {path.name}')
            if path.suffix == '.md':
                fences = re.findall(r'^```', text, re.MULTILINE)
                if len(fences) % 2:
                    raise ValueError(f'Unbalanced Markdown fences: {path.name}')
    metadata_path = root / 'agents' / 'openai.yaml'
    if metadata_path.exists():
        if not metadata_path.is_file():
            raise ValueError('Agent metadata must be a file when provided')
        metadata = metadata_path.read_text(encoding='utf-8')
        if '$sea' not in metadata or 'engineer-software' in metadata:
            raise ValueError('Stale agent metadata')
    return core, links


def build_portable(root: Path, output: Path) -> None:
    core, links = validate(root)
    output = output.resolve()
    if output.is_relative_to(root.resolve()):
        raise ValueError('Write the portable edition outside the skill directory')
    sections = []
    for index, (target, path) in enumerate(links, 1):
        core = core.replace(f']({target})', f'](#appendix-{index})')
        sections.append(f'\n\n# Appendix {index}\n\n' + path.read_text(encoding='utf-8'))
    result = core + ''.join(sections)
    if re.search(r'\]\((?:references|assets)/', result):
        raise ValueError('Unresolved reference in portable edition')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(result, encoding='utf-8', newline='\n')
    print(f'Portable edition: {output.name} ({len(result.encode("utf-8"))} bytes)')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    parser.add_argument('--portable', type=Path)
    args = parser.parse_args()
    try:
        _, links = validate(args.root)
        print(f'SEA structure valid: {len(links)} local references')
        print('This validates structure, not engineering behavior or cross-platform loading.')
        if args.portable:
            build_portable(args.root, args.portable)
    except (ValueError, OSError) as exc:
        parser.exit(1, f'{exc}\n')


if __name__ == '__main__':
    main()
