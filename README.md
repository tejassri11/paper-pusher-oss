# paper-pusher

`paper-pusher` is an early-stage toolkit for organizing research workflow evidence: claims, evidence tables, figure/table checks, reviewer-response scaffolds, Codex handoff notes, and lightweight project memory.

It is not a paper-writing service and does not generate scientific claims for you. The goal is to make small research teams and student researchers more disciplined about traceability, claim strength, reviewer responses, and reproducible project notes.

## What it does

- Builds a claim-evidence matrix from toy `claims.yaml` and `evidence.csv` inputs.
- Flags claims that appear stronger than their available evidence.
- Generates a reviewer-response skeleton.
- Generates a figure/table review checklist.
- Provides reusable templates for handoff and project-memory notes.

## Privacy boundary

This repository contains only toy examples. It does not include private manuscripts, real experimental data, reviewer letters, figures, or unpublished results.

## Quick start

```bash
python -m paper_pusher.cli examples/claims.yaml examples/evidence.csv examples/outputs
```

Generated files:

- `claim_evidence_matrix.md`
- `claim_audit_report.md`
- `reviewer_response_skeleton.md`
- `figure_table_checklist.md`

## Development

```bash
python -m pytest
```

## License

MIT is recommended for this clean-room workflow toolkit.
