---
name: deslopinator-9000-strict
description: Write, rewrite, or review controlled technical prose with strict wording. Use for procedures, runbooks, safety text, warnings, cautions, operational instructions, and error messages where consistency and unambiguous action matter. Use the default sibling for READMEs, PRs, essays, and general prose.
---

# Deslopinator 9000: Strict

Use strict Simplified Technical English rules, then remove remaining formulaic AI patterns.

## Sources

Read these shared sources before work:

1. [STE writing rules](../../vendor/woosal1337/ep01/ste-writing-skill.md)
2. [Recurring STE errors](../../vendor/woosal1337/ep01/ste-recurring-errors.md)
3. [Stop-slop rules](../../shared/stop-slop/rules.md)

Read the [phrase](../../shared/stop-slop/references/phrases.md), [structure](../../shared/stop-slop/references/structures.md), and [example](../../shared/stop-slop/references/examples.md) references when the input matches those branches.

## Precedence

Resolve conflicts in this order:

1. Preserve facts, identifiers, code, commands, numbers, conditions, scope qualifiers, and safety wording.
2. Apply strict STE mode.
3. Apply stop-slop style rules.

Make the smallest change that fixes each violation. Never weaken a warning, caution, requirement, or quoted error string.

## Workflow

1. Classify the request as **write**, **rewrite**, or **review**.
2. Apply the sources and precedence rules.
3. Lint with `python3 ../../vendor/woosal1337/ep01/ste-lint.py --strict <draft>`.
4. Fix reported categories and lint again when needed. Stop after two lint passes.
5. Return the operation-specific output.

## Output

- **Write:** requested text, a short applied-rules list, then `Lint: strict, score v2, <score> violations/100 words`.
- **Rewrite:** revised text, a table with `Original | Revision | Rule`, then the lint line.
- **Review:** a table with `Rule | Original | Suggested`, then the lint line. Do not include a rewritten body.

If the input complies, keep it unchanged and say so. Write no extra preamble or closing text.
