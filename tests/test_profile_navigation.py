"""Exercise the checked-in landing pages as well as the checker fixtures."""
import json
from pathlib import Path
import unittest
from urllib.parse import urlsplit
import re

from scripts.editorial_checks import local_link_errors, without_fences

ROOT = Path(__file__).resolve().parents[1]


class ProfileNavigationTest(unittest.TestCase):
    def test_landing_pages_have_working_local_links(self):
        for name in ("README.md", "PROJECT_GUIDE.md", "PORTFOLIO_PLAN.md",
                     "PORTFOLIO_STANDARDS.md", "MAINTENANCE.md"):
            with self.subTest(page=name):
                self.assertEqual(local_link_errors(ROOT / name), [])

    def test_guide_links_to_each_manifest_project(self):
        manifest = json.loads((ROOT / "portfolio.json").read_text(encoding="utf-8"))
        guide = without_fences((ROOT / "PROJECT_GUIDE.md").read_text(encoding="utf-8"))
        links = [urlsplit(url) for url in re.findall(r"\]\((https?://[^ )]+)\)", guide)]
        paths = {tuple(link.path.strip("/").split("/")[:2]) for link in links
                 if link.netloc == "github.com"}
        for repo in manifest["repositories"]:
            with self.subTest(repo=repo):
                self.assertIn((manifest["owner"], repo), paths)
