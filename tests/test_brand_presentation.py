"""The public VIB copy must not carry the removed operator branding."""
import re
import unittest
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]


class BrandPresentationTests(unittest.TestCase):
    def test_generated_pages_have_no_removed_operator_branding(self):
        for path in sorted((ROOT / 'dist').glob('*.html')):
            with self.subTest(route=path.name):
                soup = BeautifulSoup(path.read_text(), 'html.parser')
                copy = soup.get_text(' ', strip=True)
                metadata = ' '.join(tag.get('content', '') for tag in soup.select('meta[content]'))
                self.assertIsNone(re.search(r'cars24|auto\s*iq', copy + metadata, re.I))


if __name__ == '__main__':
    unittest.main()
