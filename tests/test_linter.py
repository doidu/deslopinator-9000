#!/usr/bin/env python3
import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINTER = ROOT / "vendor/woosal1337/ep01/ste-lint.py"


def lint(text: str, strict: bool = False) -> dict:
    with tempfile.NamedTemporaryFile("w", suffix=".md", encoding="utf-8") as draft:
        draft.write(text)
        draft.flush()
        command = ["python3", str(LINTER), "--json"]
        if strict:
            command.append("--strict")
        command.append(draft.name)
        return json.loads(subprocess.run(command, check=True, capture_output=True, text=True).stdout)


def main() -> None:
    default = lint("The operator starts the service.")
    strict = lint("However, the operator should follow the guide.", strict=True)
    assert default["mode"] == "flavored" and default["score_version"] == 2
    assert default["total"] == 0
    assert strict["mode"] == "strict" and strict["violations"]["strict_banned_word"] == 3
    print("linter smoke tests passed: flavored and strict")


if __name__ == "__main__":
    main()
