"""A local rebuild must not retain a previous deployment's canonical URLs."""
import os
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
from bs4 import BeautifulSoup
import site_content

class MetadataTests(unittest.TestCase):
    def test_switching_back_to_local_build_removes_previous_deployment_urls(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            (root/'dist').mkdir()
            file = root/'dist/guide.html'
            file.write_text('<html><head><title>Guide</title><meta name="description" content="Example guide"></head><body><main>Guide</main></body></html>')
            with patch.object(site_content, 'ROOT', root):
                with patch.dict(os.environ, {'VIB_SITE_URL':'https://preview.example/vib/'}):
                    site_content.apply_shared_content()
                first=BeautifulSoup(file.read_text(),'html.parser')
                self.assertEqual(first.select_one('link[rel=canonical]')['href'],'https://preview.example/vib/guide.html')
                with patch.dict(os.environ, {'VIB_SITE_URL':''}):
                    site_content.apply_shared_content()
                second=BeautifulSoup(file.read_text(),'html.parser')
                self.assertIsNone(second.select_one('link[rel=canonical]'))
                self.assertIsNone(second.find('meta',property='og:url'))
                self.assertIsNone(second.find('meta',property='og:image'))

    def test_invalid_launch_base_is_rejected(self):
        with patch.dict(os.environ, {'VIB_SITE_URL':'http://localhost/?token=not-real'}):
            with self.assertRaisesRegex(ValueError,'HTTPS base URL'):
                site_content.apply_shared_content()

class SharedContentTests(unittest.TestCase):
    def test_reapplying_shared_content_does_not_duplicate_notices_or_controls(self):
        import shutil
        with TemporaryDirectory() as temp:
            root=Path(temp)
            (root/'dist').mkdir()
            for name in ['index.html','sample-swift.html']:
                shutil.copyfile(site_content.ROOT/'dist'/name,root/'dist'/name)
            with patch.object(site_content,'ROOT',root),patch.dict(os.environ,{'VIB_SITE_URL':''}):
                site_content.apply_shared_content()
                site_content.apply_shared_content()
            report=BeautifulSoup((root/'dist/sample-swift.html').read_text(),'html.parser')
            for selector in ['.sample-notice','.photo-reference-note','.score-context']:
                self.assertEqual(len(report.select(selector)),1,selector)
            home=BeautifulSoup((root/'dist/index.html').read_text(),'html.parser')
            self.assertEqual(len(home.select('.hero-motion')),0)
            self.assertEqual(len(home.select('[data-motion-toggle]')),1)
            self.assertEqual(len(home.select('[data-motion-toggle]')),1)

    def test_report_missing_required_structure_fails_with_useful_error(self):
        with TemporaryDirectory() as temp:
            root=Path(temp)
            (root/'dist').mkdir()
            (root/'dist/sample-test.html').write_text('<html><head><title>Test</title></head><body><div class="swift-report"></div></body></html>')
            with patch.object(site_content,'ROOT',root),patch.dict(os.environ,{'VIB_SITE_URL':''}):
                with self.assertRaisesRegex(ValueError,'sample-test.html.*required report'):
                    site_content.apply_shared_content()

class SampleScopeTests(unittest.TestCase):
    def test_sample_filename_cannot_silently_omit_sample_context(self):
        with TemporaryDirectory() as temp:
            root=Path(temp);(root/'dist').mkdir()
            (root/'dist/sample-test.html').write_text('<html><head><title>Test</title></head><body>Missing report container</body></html>')
            with patch.object(site_content,'ROOT',root),patch.dict(os.environ,{'VIB_SITE_URL':''}):
                with self.assertRaisesRegex(ValueError,'required report'):
                    site_content.apply_shared_content()
