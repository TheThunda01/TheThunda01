import json
from pathlib import Path
import tempfile
import unittest

from scripts.check_portfolio_docs import (
    PRACTICAL_HEADINGS, README_HEADINGS, REVIEW_HEADINGS,
    inspect_markdown, inspect_repository,
)


class DocumentationChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "docs").mkdir()
        for relative, headings in [
            ("README.md", README_HEADINGS),
            ("docs/practical-use.md", PRACTICAL_HEADINGS),
            ("docs/literature-review.md", REVIEW_HEADINGS),
        ]:
            (self.root / relative).write_text("# Project\n\n" + "\n\n".join(
                "## " + heading + "\n\nExplanation." for heading in headings), encoding="utf-8")
        self.log = {
            "search_date": "2026-10-20", "scope": "A bounded test",
            "inclusion_criteria": ["Direct relevance"],
            "exclusion_criteria": ["Different question"],
            "searches": [{"source": "Example", "query": "Exact query"}],
            "screening": [{"id": "example", "decision": "include"}],
        }
        self.write_log()

    def write_log(self):
        (self.root / "docs/search-log.json").write_text(json.dumps(self.log), encoding="utf-8")

    def test_complete_contract_passes(self):
        self.assertEqual(inspect_repository(self.root), [])

    def test_missing_guide_is_reported(self):
        (self.root / "docs/practical-use.md").unlink()
        self.assertTrue(any("Missing file" in e for e in inspect_repository(self.root)))

    def test_heading_order_and_extra_heading_are_detected(self):
        path = self.root / "README.md"
        path.write_text(path.read_text() + "\n## Unspecified section\n")
        self.assertTrue(any("shared order" in e for e in inspect_repository(self.root)))

    def test_code_examples_and_remote_links_are_not_local_targets(self):
        path = self.root / "README.md"
        with path.open("a") as stream:
            stream.write("\n[Remote](https://example.invalid/path)\n[Anchor](#why-this-project)\n")
            stream.write("\n```markdown\n## Example heading\n[Example](missing.md)\n```\n")
        self.assertEqual(inspect_markdown(path, README_HEADINGS), [])

    def test_real_missing_relative_link_is_reported(self):
        path = self.root / "README.md"
        with path.open("a") as stream:
            stream.write("\n[Missing](docs/missing.md)\n")
        self.assertTrue(any("missing relative link" in e for e in inspect_repository(self.root)))

    def test_search_dates_and_records_must_be_explicit(self):
        self.log["search_date"] = "2026-02-30"
        self.write_log()
        self.assertTrue(any("search-log.json" in e for e in inspect_repository(self.root)))
        self.log["search_date"] = "2026-10-20"
        self.log["searches"] = []
        self.log["screening"] = []
        self.write_log()
        errors = inspect_repository(self.root)
        self.assertTrue(any("nonempty list" in e for e in errors))
        self.assertTrue(any("record decisions" in e for e in errors))

    def test_missing_search_keys_are_reported(self):
        del self.log["scope"]
        self.write_log()
        self.assertTrue(any("missing scope" in e for e in inspect_repository(self.root)))


if __name__ == "__main__":
    unittest.main()
