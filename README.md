# deslopinator-9000

Private Pi skill repository for two prose modes:

- `deslopinator-9000-default`: READMEs, pull requests, documentation, comments, prompts, essays, release notes, and general prose.
- `deslopinator-9000-strict`: procedures, runbooks, safety text, operational instructions, and error messages.

Pi discovers both nested `SKILL.md` files when this repository is under `~/.pi/agent/skills/`. Restart Pi after installation or replacement.

## Sources

This repository combines an installed copy of Hardik Pandya's `stop-slop` skill with three files from `woosal1337/blog` commit [`5a6632666a32b594c421a5a5b8db7670a6a4efd1`](https://github.com/woosal1337/blog/tree/5a6632666a32b594c421a5a5b8db7670a6a4efd1/videos/ep01-the-cure-for-ai-slop).

Pinned file hashes:

| File | SHA-256 |
| --- | --- |
| `ste-writing-skill.md` | `6531af7599488591e56f129268b3c300b2253f225be6c366e32f08651a45971b` |
| `ste-recurring-errors.md` | `d721d9f415e4f4d94624d3c3727e6e82a5311eaaf31db28ba6ade7e5c8dae880` |
| `ste-lint.py` | `bedba551157b7cf6378ecf97d29e6606496c49a8df83d7778e5f330e48c9595e` |

See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) before copying or publishing files. This repository has no blanket license.

## Check

```bash
python3 tests/test_linter.py
```
