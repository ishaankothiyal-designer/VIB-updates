"""Regression contracts for the preview journey and sample interpretation."""
import unittest
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
def page(name):
    return BeautifulSoup((ROOT / 'dist' / name).read_text(), 'html.parser')

class UserJourneyTests(unittest.TestCase):
    def test_opening_explains_preview_and_gives_stable_sample_action(self):
        home = page('index.html')
        copy = home.select_one('.hero-copy')
        self.assertIn('preview', copy.get_text(' ', strip=True).lower())
        action = copy.find('a', href='#sample-reports')
        self.assertIsNotNone(action, 'Visitors need a sample action before the large car illustration')
        self.assertIn('sample', action.get_text().lower())

    def test_every_sample_can_be_selected_without_javascript_or_random_routing(self):
        import json
        home = page('index.html')
        chooser = home.select_one('#sample-reports')
        self.assertIsNotNone(chooser, 'A visitor must be able to choose the car example')
        for car in json.loads((ROOT/'dist/cars.json').read_text())['cars']:
            link = chooser.find('a', href=f'sample-{car["id"]}.html')
            self.assertIsNotNone(link, car['id'])
            self.assertIn(car['name'], link.get_text(' ', strip=True))

    def test_story_evidence_and_explanation_share_a_reading_container(self):
        home = page('index.html')
        self.assertFalse(home.select('.story-stage'), 'Detached pinned layers can cover their own explanation')
        self.assertEqual(len(home.select('#report-contents .story-step')), 6)
        for item in home.select('#report-contents .story-step'):
            self.assertIsNotNone(item.select_one('.story-copy'))
            self.assertIsNotNone(item.select_one('.evidence-card'))

    def test_all_ten_reports_explain_sample_score_and_reference_photos_up_front(self):
        import json
        for car in json.loads((ROOT/'dist/cars.json').read_text())['cars']:
            with self.subTest(car=car['id']):
                report = page(f'sample-{car["id"]}.html')
                notice = report.select_one('.sample-notice')
                self.assertIsNotNone(notice)
                self.assertIn('fictional', notice.get_text().lower())
                self.assertIn('preset', report.select_one('.condition-snapshot').get_text().lower())
                self.assertIn('reference', report.select_one('#photos').get_text().lower())
                self.assertIn('not', report.select_one('.photo-reference-note').get_text().lower())
                self.assertNotIn('The complete timeline', report.get_text())

    def test_own_car_availability_is_not_misrepresented(self):
        home = page('index.html')
        self.assertIn('live vehicle lookup is not available', home.get_text(' ', strip=True).lower())
        self.assertFalse(home.select('input[type=tel],input[name=registration],button[type=submit]'))

if __name__ == '__main__':
    unittest.main()
