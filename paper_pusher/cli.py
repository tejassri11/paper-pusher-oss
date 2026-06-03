from __future__ import annotations

import argparse
from pathlib import Path

from paper_pusher.claim_audit.audit import audit_claims, load_claims, load_evidence
from paper_pusher.evidence_package.matrix import render_audit_report, render_matrix
from paper_pusher.figure_table_review.checklist import render_checklist
from paper_pusher.reviewer_response.response import render_response_skeleton


def run(claims_path: str, evidence_path: str, output_dir: str) -> None:
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    claims = load_claims(claims_path)
    evidence = load_evidence(evidence_path)
    audited = audit_claims(claims, evidence)
    (out / "claim_evidence_matrix.md").write_text(render_matrix(audited, evidence), encoding="utf-8")
    (out / "claim_audit_report.md").write_text(render_audit_report(audited), encoding="utf-8")
    (out / "reviewer_response_skeleton.md").write_text(render_response_skeleton(audited), encoding="utf-8")
    (out / "figure_table_checklist.md").write_text(render_checklist(), encoding="utf-8")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("claims")
    parser.add_argument("evidence")
    parser.add_argument("output_dir")
    args = parser.parse_args(argv)
    run(args.claims, args.evidence, args.output_dir)


if __name__ == "__main__":
    main()
