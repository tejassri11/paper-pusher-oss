from __future__ import annotations

import csv
from pathlib import Path


STRENGTH_ORDER = {"exploratory": 0, "moderate": 1, "strong": 2}


def load_claims(path: str | Path) -> list[dict]:
    """Parse a tiny YAML subset used by the toy examples."""
    claims: list[dict] = []
    current: dict | None = None
    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line == "claims:":
            continue
        if line.startswith("- id:"):
            if current:
                claims.append(current)
            current = {"id": line.split(":", 1)[1].strip()}
            continue
        if current is None:
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            value = value.strip().strip('"')
            if value.startswith("[") and value.endswith("]"):
                value = [x.strip() for x in value[1:-1].split(",") if x.strip()]
            current[key.strip()] = value
    if current:
        claims.append(current)
    return claims


def load_evidence(path: str | Path) -> dict[str, dict]:
    with Path(path).open("r", encoding="utf-8", newline="") as f:
        return {row["id"]: row for row in csv.DictReader(f)}


def audit_claims(claims: list[dict], evidence: dict[str, dict]) -> list[dict]:
    results = []
    for claim in claims:
        evidence_ids = claim.get("evidence", [])
        if isinstance(evidence_ids, str):
            evidence_ids = [evidence_ids]
        support_levels = [evidence[eid].get("support", "weak") for eid in evidence_ids if eid in evidence]
        strong_support = support_levels.count("strong")
        strength = str(claim.get("strength", "moderate")).lower()
        risk = "ok"
        if STRENGTH_ORDER.get(strength, 1) >= 2 and strong_support == 0:
            risk = "overstated"
        elif not support_levels:
            risk = "missing_evidence"
        results.append({**claim, "support_levels": support_levels, "audit": risk})
    return results
