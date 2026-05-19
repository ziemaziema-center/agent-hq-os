# SPDX-License-Identifier: MIT
from pathlib import Path
from datetime import datetime, timezone

root = Path(__file__).resolve().parent
output = root / "output"
output.mkdir(exist_ok=True)

note = output / "validation_first_note.md"
note.write_text(
    "# Validation-first Note\n\n"
    "Validation-first means defining the check before making the change. "
    "In this demo, the check is intentionally small: this file must exist "
    "and include the phrase validation-first.\n",
    encoding="utf-8",
)

text = note.read_text(encoding="utf-8")
if "validation-first" not in text:
    failure = root / "telemetry" / "FAILURE_TELEMETRY.md"
    failure.write_text(failure.read_text(encoding="utf-8") + "\n- Demo validation failed: phrase missing.\n", encoding="utf-8")
    raise SystemExit("FAIL: validation-first phrase missing")

timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
daily = root / "telemetry" / "DAILY_EXECUTION_LOG.md"
success = root / "telemetry" / "SUCCESS_TELEMETRY.md"
daily.write_text(daily.read_text(encoding="utf-8") + f"\n## {timestamp}\n\n- Ran local demo workspace bootstrap.\n- Created `output/validation_first_note.md`.\n- Validation passed.\n", encoding="utf-8")
success.write_text(success.read_text(encoding="utf-8") + f"\n## {timestamp}\n\n- Pattern: define validation before local change.\n- Evidence: `output/validation_first_note.md` exists and contains `validation-first`.\n", encoding="utf-8")
print("PASS: Agent HQ OS demo workspace initialized")
print(f"Created: {note.relative_to(root)}")
