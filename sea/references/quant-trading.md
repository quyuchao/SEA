# Quantitative trading extension

Load only for trading, market data, backtesting, or model research. Verify changing market rules and interface capabilities using current primary sources and project constraints.

- Isolate research, backtest, shadow, paper, and authorized live environments, state, configuration, and permissions. Research output must not directly place live orders.
- Distinguish market occurrence, data availability, signal, submission, and execution times. Check time zones, calendars, delays, adjustments, and revisions to prevent future leakage.
- Record data, strategy, model, configuration, cost, and runtime versions. Separate training/validation/test appropriately; repeatedly inspected holdouts are not untouched.
- Define cash, reservations, positions, sellable quantities, fees, executions, and equity, including units, precision, and authoritative ledger. Check relevant conservation rules.
- Design order states, idempotency, partial fills, duplicate/out-of-order reports, cancellation races, timeouts, and uncertain outcomes. Reconcile before retrying effects.
- Distinguish message deduplication from economic-execution deduplication: different reports can describe the same fill. Without stable execution identity or protocol guarantees, state the limits and use reconciliation instead of claiming complete deduplication.
- Check trading units, halts, price limits, settlement/T+1, costs, slippage, liquidity, and corporate actions by market. Do not generalize one market's rules.
- Treat risk, ledger, and execution changes as critical. Follow the project's conservative stop policy when essential prerequisites cannot be confirmed.
- Validate account/schema migrations using isolated copies and compare balances, reservations, positions, orders, and history. Software checks do not prove strategy validity; backtests do not establish live returns.
- Define migration boundaries when introducing vn.py, Qlib, or another framework. Avoid two execution/ledger writers with unclear ownership.
