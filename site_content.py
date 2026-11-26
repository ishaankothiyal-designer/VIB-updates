"""Shared preview context and navigation applied after all report generators."""
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlsplit
import os

ROOT = Path(__file__).resolve().parent

def apply_shared_content():
    base_url = os.environ.get('VIB_SITE_URL', '').strip()
    if base_url:
        parsed = urlsplit(base_url)
        if parsed.scheme != 'https' or not parsed.netloc or parsed.query or parsed.fragment:
            raise ValueError('VIB_SITE_URL must be an HTTPS base URL without query or fragment')
        base_url = base_url.rstrip('/') + '/'
    for path in sorted((ROOT/'dist').glob('*.html')):
        soup = BeautifulSoup(path.read_text(), 'html.parser')
        if not soup.title:
            raise ValueError(f'{path.name}: required page title is missing')
        report = soup.select_one('.swift-report')
        is_sample = path.name == 'sample.html' or path.name.startswith('sample-')
        if is_sample != bool(report):
            raise ValueError(f'{path.name}: required report container and sample filename do not match')
        if path.name == 'index.html' and soup.select_one('[data-motion-toggle]') and not soup.select_one('.hero-copy'):
            raise ValueError(f'{path.name}: hero-copy container missing for motion toggle')
        if report and (any(soup.select_one(selector) is None for selector in ['.photo-heading','.condition-snapshot']) or soup.select_one('.condition-snapshot').find('span',recursive=False) is None):
            raise ValueError(f'{path.name}: required report gallery or score structure is missing')
        for anchor in soup.select('.site-header a, .site-footer a'):
            if anchor.get('href') == 'sample.html':
                anchor['href'] = 'index.html#sample-reports'
                anchor.string = 'Explore samples'
            if anchor.get('href') == 'index.html#process':
                anchor.string = 'Use the findings'
        if not soup.select_one('link[href="journey.css"]'):
            link = soup.new_tag('link', rel='stylesheet', href='journey.css')
            soup.head.append(link)
        for label in soup.find_all(string=lambda s: s and s.strip() == 'The complete timeline'):
            label.replace_with('Available records timeline')
        report = soup.select_one('.swift-report')
        if report:
            if not soup.title.get_text().startswith('Sample report'):
                soup.title.string = 'Sample report · ' + soup.title.get_text()
            notice = BeautifulSoup('<aside class="sample-notice" aria-label="About this sample"><strong>Sample report</strong><p>The vehicle history and amounts are fictional. The condition score is preset. Use this example to understand the report, not to assess a real car.</p><a href="index.html#sample-reports">Choose a different sample</a></aside>', 'html.parser').aside
            if not report.select_one('.sample-notice'):
                report.insert(0, notice)
            gallery_note = soup.new_tag('p', attrs={'class':'photo-reference-note'})
            gallery_note.string = 'Reference photos for this model. They do not verify the fictional history shown here. Photo capture dates are unavailable.'
            if not soup.select_one('.photo-reference-note'):
                soup.select_one('.photo-heading').insert_after(gallery_note)
            score = soup.select_one('.condition-snapshot')
            score.find('span', recursive=False).string = 'Example condition score'
            score_note = soup.new_tag('p', attrs={'class':'score-context'})
            score_note.string = 'Preset for this sample. Not a physical inspection or a guarantee.'
            if not score.select_one('.score-context'):
                score.append(score_note)
            for a in soup.select('.report-toolbar a'):
                if a.get('href') == 'index.html':
                    a['href'] = 'index.html#sample-reports'
                    a.string = 'All sample reports'
        if path.name == 'index.html':
            control = soup.select_one('[data-motion-toggle]')
            if control and not soup.select_one('.hero-motion'):
                slot = soup.new_tag('div', attrs={'class':'hero-motion'})
                slot.append(control.extract())
                soup.select_one('.hero-copy').append(slot)
        for a in soup.select('a[href="sample.html"]'):
            a['href'] = 'index.html#sample-reports'
            a.string = 'Explore sample reports'
        if not soup.select_one('noscript.preview-navigation-fallback'):
            fallback = BeautifulSoup('<noscript class="preview-navigation-fallback"><style>.site-header .menu-toggle,.site-header .header-action{display:none}.site-header .header-inner{flex-wrap:wrap;padding-block:16px}.site-header #main-nav{display:flex;position:static;flex-basis:100%;flex-direction:row;flex-wrap:wrap;gap:8px 20px;padding:0;border:0}.site-header #main-nav .mobile-report{display:inline-flex}</style></noscript>', 'html.parser').noscript
            soup.head.append(fallback)
        # Social metadata is useful locally; absolute canonical/image URLs require the approved launch base.
        description = soup.select_one('meta[name="description"]')
        meta = {'og:title': soup.title.get_text(), 'og:type':'website', 'og:description':description['content'] if description else 'Explore sample vehicle history reports and buyer guides.'}
        if base_url:
            canonical = urljoin(base_url, 'sample-swift.html' if path.name == 'sample.html' else path.name)
            meta.update({'og:url':canonical, 'og:image':urljoin(base_url, 'assets/report-folio.webp')})
            tag = soup.select_one('link[rel="canonical"]') or soup.new_tag('link', rel='canonical')
            tag['href'] = canonical
            if not tag.parent:soup.head.append(tag)
        if not base_url:
            for stale in soup.select('link[rel=canonical], meta[property="og:url"], meta[property="og:image"]'):
                stale.decompose()
        for prop, content in meta.items():
            tag = soup.find('meta', property=prop) or soup.new_tag('meta', property=prop)
            tag['content'] = content
            if not tag.parent:soup.head.append(tag)
        path.write_text(str(soup))
