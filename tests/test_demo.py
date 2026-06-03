from pathlib import Path

from paper_pusher.cli import run


def test_demo_outputs(tmpdir):
    root = Path(__file__).resolve().parents[1]
    run(root / "examples" / "claims.yaml", root / "examples" / "evidence.csv", str(tmpdir))
    report = tmpdir.join("claim_audit_report.md").read_text("utf-8")
    assert "C1" in report
    assert "overstated" in report
    assert tmpdir.join("figure_table_checklist.md").exists()
