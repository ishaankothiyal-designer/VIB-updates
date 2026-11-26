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
        self.assertIn('vehicle history reports', copy.get_text(' ', strip=True).lower())
        self.assertIsNotNone(home.select_one('.case-overview'))
        self.assertEqual(len(home.select('.case-selector')),4)
        self.assertIsNone(copy.select_one('[data-motion-toggle]'))
        action = copy.find('a', href='#sample-reports')
        self.assertIsNotNone(action, 'Visitors need a sample action before the large car illustration')
        self.assertIn('sample', action.get_text().lower())

    def test_registration_is_the_next_section_after_the_complete_hero(self):
        home=page('index.html')
        hero=home.select_one('.hero')
        self.assertIsNone(hero.select_one('form'), 'Keep the opening story separate from vehicle entry')
        self.assertEqual(hero.find_next_sibling('section').get('id'),'vehicle-check')
        self.assertEqual(home.select_one('#vehicle-check').find_next_sibling('section').get('id'),'sample-reports')

    def test_vehicle_entry_stays_local_and_collects_no_phone_number(self):
        home = page('index.html')
        form = home.select_one('#vehicle-check form')
        self.assertIsNotNone(form)
        self.assertEqual(form.get('action'), '#vehicle-check')
        self.assertFalse(form.select('input[name]'), 'No fallback query-string submission of a registration')
        self.assertFalse(home.select('input[type=tel]'))
        self.assertIsNotNone(home.select_one('#vehicle-feedback[role=status]'))
        for path in (ROOT/'dist').glob('*.html'):
            for link in page(path.name).find_all('a', href=True):
                self.assertNotEqual(link['href'], 'https://vehicleinformationbureau.com/')

    def test_all_routes_share_home_navigation_and_design_layer(self):
        from urllib.parse import urlsplit
        for path in sorted((ROOT/'dist').glob('*.html')):
            with self.subTest(route=path.name):
                soup=page(path.name)
                expected='#vehicle-check' if path.name=='index.html' else 'index.html#vehicle-check'
                self.assertEqual(soup.select_one('.site-header .header-action')['href'],expected)
                self.assertEqual(soup.select_one('.site-header .mobile-report')['href'],expected)
                self.assertEqual(len(soup.select('.site-footer .footer-signature')),1)
                styles=[urlsplit(tag['href']).path for tag in soup.select('link[rel=stylesheet]')]
                self.assertEqual(styles.count('refinements.css'),1)
                self.assertEqual(styles[-1],'refinements.css')
                for script in soup.select('script[src]'):
                    if urlsplit(script['src']).path in ['motion.js','vehicle-entry.js','scroll-stories.js']:
                        self.assertIn('?v=',script['src'],'Updated HTML must load matching shared behavior')

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

    def test_report_heading_line_break_keeps_words_separated(self):
        for path in sorted((ROOT/'dist').glob('sample-*.html')):
            with self.subTest(route=path.name):
                title=page(path.name).select_one('#coverage-gaps h2').get_text()
                self.assertIn('is still',title)

    def test_own_car_availability_is_not_misrepresented(self):
        home = page('index.html')
        self.assertIn('not connected', home.select_one('#vehicle-check').get_text().lower())
        self.assertIn('not saved or sent', home.select_one('#vehicle-check').get_text().lower())

if __name__ == '__main__':
    unittest.main()
