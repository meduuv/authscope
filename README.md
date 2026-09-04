# AuthScope

> Analyze authentication event data without touching the live system.

AuthScope provides small, dependency-free helpers for reviewing authentication logs and event records. It is built for local analysis, triage and reporting.

## Features

- Count successful and failed authentication events
- Detect repeated failures by principal
- Summarize authentication activity
- Work entirely on supplied event data
- Produce results suitable for scripts and reports

## Workflow

```text
auth events
    ↓
parse / normalize
    ↓
aggregate
    ↓
identify patterns
    ↓
summarize
```

## Example

```python
from authscope import summarize

report = summarize(events)
print(report)
```

See the implementation and tests for the exact supported event format.

## Scope

AuthScope performs offline analysis only. It does not attempt logins, access accounts or modify authentication systems.

## Development

```bash
python -m pytest
```

## License

MIT. See `LICENSE`.

## Author

Built by **Medu** · https://guns.lol/meduu