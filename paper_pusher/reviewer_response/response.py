from __future__ import annotations


def render_response_skeleton(audited_claims: list[dict]) -> str:
    lines = ["# Reviewer Response Skeleton", ""]
    for claim in audited_claims:
        lines.extend([
            f"## Comment related to {claim.get('id')}",
            "",
            "**Response.** Thank you for the suggestion. We revised the claim boundary and evidence linkage.",
            "",
            "**Change made.** [Describe manuscript or documentation change here.]",
            "",
            f"**Evidence link.** Claim audit status: `{claim.get('audit')}`.",
            "",
        ])
    return "\n".join(lines)
