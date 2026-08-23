---
name: deslopinator-9000-default
description: Write, rewrite, or review general prose without AI writing patterns. Use for READMEs, pull-request text, documentation, comments, prompts, essays, release notes, and other prose that needs clear human wording. Use the strict sibling for procedures, runbooks, safety text, and error messages.
---

# Deslopinator 9000: Default

Use STE-flavored rules for general prose, then remove remaining formulaic AI patterns.

## Sources

Read these shared sources before work:

1. [STE writing rules](../../vendor/woosal1337/ep01/ste-writing-skill.md)
2. [Stop-slop rules](../../shared/stop-slop/rules.md)

Read the [phrase](../../shared/stop-slop/references/phrases.md), [structure](../../shared/stop-slop/references/structures.md), and [example](../../shared/stop-slop/references/examples.md) references when the input matches those branches.

## Precedence

Resolve conflicts in this order:

1. Preserve facts, identifiers, code, commands, numbers, conditions, scope qualifiers, and safety wording.
2. Apply STE-flavored mode.
3. Apply stop-slop style rules.

Make the smallest change that fixes each violation. Keep purposeful voice when it does not conflict with higher-priority rules.

## Workflow

1. Classify the request as **write**, **rewrite**, or **review**.
2. Apply the sources and precedence rules.
3. Lint with `python3 ../../vendor/woosal1337/ep01/ste-lint.py <draft>`.
4. Fix reported categories and lint again when needed. Stop after two lint passes.
5. Return the operation-specific output.

## Output

- **Write:** requested text, a short applied-rules list, then `Lint: flavored, score v2, <score> violations/100 words`.
- **Rewrite:** revised text, a table with `Original | Revision | Rule`, then the lint line.
- **Review:** a table with `Rule | Original | Suggested`, then the lint line. Do not include a rewritten body.

If the input complies, keep it unchanged and say so. Write no extra preamble or closing text.
