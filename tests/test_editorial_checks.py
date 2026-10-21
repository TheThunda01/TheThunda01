import json
from pathlib import Path
import tempfile
import unittest

from scripts.editorial_checks import audit_errors, heading_ids, inspect_editorial_review, local_link_errors


class EditorialChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "docs").mkdir()
        for name in ("glossary.md", "assumptions.md", "review-2026-10-20.md"):
            (self.root / "docs" / name).write_text("# Guide\n\nA complete example.\n")
        (self.root / "README.md").write_text("# Example\n\n" + "\n".join(
            f"[Guide](docs/{name})" for name in
            ("glossary.md", "assumptions.md", "review-2026-10-20.md", "reference-audit.json")))
        self.audit = {"review_date": "2026-10-20", "scope": "Cited sources", "limits": "Not a systematic review",
                      "references": [{"id": "r1", "source_type": "article", "title": "Example", "authors": ["A. Author"],
                                      "year": 2025, "url": "https://example.org/article", "checked_on": "2026-10-20",
                                      "access_level": "abstract", "metadata_status": "verified",
                                      "supported_claims": ["Method background"], "limitations": ["Abstract inspected"], "corrections": []}]}
        self.write_audit()

    def write_audit(self):
        (self.root / "docs/reference-audit.json").write_text(json.dumps(self.audit))

    def test_complete_editorial_record_passes(self):
        self.assertEqual(inspect_editorial_review(self.root, "2026-10-20"), [])

    def test_missing_guide_and_readme_link_are_detected(self):
        (self.root / "docs/glossary.md").unlink()
        (self.root / "README.md").write_text("# Example\n")
        errors = inspect_editorial_review(self.root, "2026-10-20")
        self.assertTrue(any("Missing or empty" in e for e in errors))
        self.assertTrue(any("not linked" in e for e in errors))

    def test_duplicate_ids_and_missing_support_are_detected(self):
        self.audit["references"].append(dict(self.audit["references"][0], supported_claims=[]))
        self.write_audit()
        errors = audit_errors(self.root / "docs/reference-audit.json")
        self.assertTrue(any("unique" in e for e in errors))
        self.assertTrue(any("source role" in e for e in errors))

    def test_access_and_bibliographic_field_errors_are_detected(self):
        self.audit["references"][0].update(year="2025", url="javascript:example", checked_on="2026-02-30",
                                            access_level="complete", metadata_status="assumed")
        self.write_audit()
        errors = audit_errors(self.root / "docs/reference-audit.json")
        self.assertEqual(len(errors), 5)

    def test_local_fragments_and_fenced_examples(self):
        path = self.root / "docs/glossary.md"
        path.write_text("# Example (guide)\n\n## Repeated\n\n## Repeated\n\n"
                        "[Valid](#repeated-1)\n[Missing](#absent)\n"
                        "```md\n[Example](not-a-real-file.md)\n```\n")
        self.assertEqual(heading_ids(path.read_text()), {"example-guide", "repeated", "repeated-1"})
        errors = local_link_errors(path)
        self.assertEqual(len(errors), 1)
        self.assertIn("#absent", errors[0])


if __name__ == "__main__":
    unittest.main()
