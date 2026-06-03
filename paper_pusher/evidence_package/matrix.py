from __future__ import annotations


def render_matrix(audited_claims: list[dict], evidence: dict[str, dict]) -> str:
    lines = ["# Claim-Evidence Matrix", "", "| Claim | Strength | Evidence | Audit |", "|---|---:|---|---|"]
    for claim in audited_claims:
        evidence_ids = claim.get("evidence", [])
        if isinstance(evidence_ids, str):
            evidence_ids = [evidence_ids]
        evidence_text = ", ".join(f"{eid}: {evidence.get(eid, {}).get('summary', 'missing')}" for eid in evidence_ids)
        lines.append(f"| {claim.get('id')} - {claim.get('text')} | {claim.get('strength')} | {evidence_text} | {claim.get('audit')} |")
    return "\n".join(lines) + "\n"


def render_audit_report(audited_claims: list[dict]) -> str:
    lines = ["# Claim Audit Report", ""]
    for claim in audited_claims:
        lines.append(f"- **{claim.get('id')}**: {claim.get('audit')} - {claim.get('text')}")
    return "\n".join(lines) + "\n"
