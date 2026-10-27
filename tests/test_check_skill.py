"""Regression checks for the SEA package validator; standard library only."""
import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

REPOSITORY = Path(__file__).resolve().parents[1]
SOURCE = REPOSITORY / 'sea'
SPEC = importlib.util.spec_from_file_location('sea_check', SOURCE / 'scripts/check_skill.py')
EXPECTED_RESOURCES = ["references/engineering-judgment.md","references/engineering-workflow.md","references/data-structures-and-algorithms.md","references/readability-and-product-design.md","references/requirements.md","references/architecture-and-stack.md","references/design-and-diagrams.md","references/verification-and-delivery.md","references/quant-trading.md","references/project-management.md","references/configuration-and-change.md","references/git-and-collaboration.md","references/versioning-and-release.md","references/operations-and-maintenance.md","references/portability.md","references/sources.md","assets/engineering-record.md","assets/project-profile.md"]
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='sea-regression-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'sea'
        shutil.copytree(SOURCE, self.root, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))

    def change_description(self, value):
        path = self.root / 'SKILL.md'
        lines = path.read_text(encoding='utf-8').splitlines()
        lines[2] = 'description: ' + value
        path.write_text('\n'.join(lines) + '\n', encoding='utf-8')

    def test_current_package(self):
        _, links = CHECK.validate(self.root)
        self.assertEqual({target for target, _ in links}, set(EXPECTED_RESOURCES))

    def test_optional_host_metadata_can_be_absent(self):
        (self.root / 'agents/openai.yaml').unlink()
        CHECK.validate(self.root)

    def test_malformed_description_is_rejected(self):
        self.change_description('"invalid "quote"')
        with self.assertRaisesRegex(ValueError, 'double-quoted'):
            CHECK.validate(self.root)

    def test_empty_description_is_rejected(self):
        self.change_description('"   "')
        with self.assertRaisesRegex(ValueError, 'description'):
            CHECK.validate(self.root)

    def test_duplicate_field_is_rejected(self):
        path = self.root / 'SKILL.md'
        text = path.read_text(encoding='utf-8').replace('name: sea\n', 'name: sea\nname: sea\n', 1)
        path.write_text(text, encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            CHECK.validate(self.root)

    def test_missing_reference_is_rejected(self):
        (self.root / 'references/requirements.md').unlink()
        with self.assertRaisesRegex(ValueError, 'Missing'):
            CHECK.validate(self.root)

    def test_stale_present_metadata_is_rejected(self):
        (self.root / 'agents/openai.yaml').write_text('interface:\n  default_prompt: "Use $old"\n', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Stale'):
            CHECK.validate(self.root)

    def test_portable_edition_is_complete_and_deterministic(self):
        first = Path(self.temp.name) / 'first.md'
        second = Path(self.temp.name) / 'second.md'
        CHECK.build_portable(self.root, first)
        CHECK.build_portable(self.root, second)
        text = first.read_text(encoding='utf-8')
        self.assertEqual(first.read_bytes(), second.read_bytes())
        self.assertEqual(text.count('# Appendix '), len(EXPECTED_RESOURCES))
        self.assertNotIn('](references/', text)
        self.assertNotIn('](assets/', text)
        for relative in EXPECTED_RESOURCES:
            self.assertIn((self.root/relative).read_text(encoding='utf-8'), text)

    def test_builder_cannot_overwrite_skill_sources(self):
        with self.assertRaisesRegex(ValueError, 'outside'):
            CHECK.build_portable(self.root, self.root/'SKILL.md')

    def test_missing_management_reference_is_rejected(self):
        for relative in ('project-management.md', 'configuration-and-change.md',
                         'git-and-collaboration.md', 'versioning-and-release.md',
                         'operations-and-maintenance.md'):
            with self.subTest(reference=relative):
                path = self.root / 'references' / relative
                content = path.read_bytes()
                path.unlink()
                try:
                    with self.assertRaisesRegex(ValueError, 'Missing'):
                        CHECK.validate(self.root)
                finally:
                    path.write_bytes(content)


if __name__ == '__main__':
    unittest.main()
