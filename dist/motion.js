/* VIB V5 paper trail: optional GSAP + matching ScrollTrigger 3.15.1 enhancement. */
(() => {
  'use strict';
  const root = document.documentElement;
  const gsap = window.gsap;
  const ScrollTrigger = window.ScrollTrigger;
  const motionControl = document.querySelector('[data-motion-toggle]');
  const preferenceKey = 'vib-reduced-motion';
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let userReduced = false;
  try { userReduced = sessionStorage.getItem(preferenceKey) === 'true'; } catch { /* Current-page preference still works without storage. */ }
  const isReduced = () => userReduced || reduceMotion.matches;
  const syncPreference = () => {
    const reduced = isReduced();
    root.dataset.motion = reduced ? 'reduced' : 'full';
    if (reduced) root.style.scrollBehavior = 'auto';
    else root.style.removeProperty('scroll-behavior');
    if (motionControl) {
      motionControl.hidden = false;
      motionControl.textContent = reduced ? 'Reduce motion: on' : 'Reduce motion: off';
      motionControl.setAttribute('aria-pressed', String(reduced));
      motionControl.disabled = reduceMotion.matches;
    }
  };
  const pauseMedia = () => {
    if (!document.hidden && !isReduced()) return;
    document.querySelectorAll('video').forEach(video => {
      if (video.paused) return;
      video.pause();
      const control = video.closest('.motion-slot, .process-art, [data-motion]')?.querySelector('.motion-toggle');
      if (control) control.textContent = 'Play illustration';
    });
  };
  const refreshPreference = () => {
    syncPreference();
    pauseMedia();
    // Revert active contexts immediately, including in-flight transforms and chart strokes.
    if (gsap?.matchMediaRefresh) gsap.matchMediaRefresh();
  };
  reduceMotion.addEventListener('change', refreshPreference);
  motionControl?.addEventListener('click', () => {
    userReduced = !userReduced;
    try { sessionStorage.setItem(preferenceKey, String(userReduced)); } catch { /* Retain the choice for this document. */ }
    refreshPreference();
  });
  document.addEventListener('visibilitychange', pauseMedia);
  syncPreference();
  pauseMedia();

  // HTML/CSS are the complete reading experience. No styles are hidden in anticipation of JS.
  if (!gsap || !ScrollTrigger || !gsap.matchMedia) return;
  gsap.registerPlugin(ScrollTrigger);
  root.dataset.motionEngine = 'gsap-' + gsap.version;
  const timing = Object.freeze({ arrival: 0.48, paper: 0.58, reveal: 0.4, replace: 0.22, chart: 0.65 });
  const media = gsap.matchMedia();
  const revealSeen = new WeakSet();
  const chartsSeen = new WeakSet();
  let arrived = false;
  const isVisible = element => Boolean(element && element.getClientRects().length && !element.closest('[hidden]'));

  media.add({
    desktop: '(min-width: 768px)',
    mobile: '(max-width: 767px)',
    reduced: '(prefers-reduced-motion: reduce)'
  }, context => {
    if (context.conditions.reduced || userReduced) return;
    const distance = context.conditions.desktop ? 12 : 7;
    const frames = { report: 0, process: 0 };
    const pending = { report: null, process: null };

    context.add('drawChart', path => {
      if (!isVisible(path) || chartsSeen.has(path) || typeof path.getTotalLength !== 'function') return;
      const length = path.getTotalLength();
      if (!length) return;
      chartsSeen.add(path);
      gsap.fromTo(path, { strokeDasharray: length, strokeDashoffset: length }, {
        strokeDashoffset: 0, duration: timing.chart, ease: 'power2.out', immediateRender: false,
        clearProps: 'strokeDasharray,strokeDashoffset', overwrite: 'auto'
      });
    });
    const drawChart = path => context.drawChart(path);

    if (!arrived) {
      arrived = true;
      const copy = document.querySelector('.hero-copy');
      if (isVisible(copy)) gsap.from(copy, {
        y: distance, opacity: 0.82, duration: timing.arrival, ease: 'power2.out',
        immediateRender: false, clearProps: 'transform,opacity'
      });
      // Settle the already visible sheets into their authored poses; never rotate, pin or follow the pointer.
      const papers = [...document.querySelectorAll('.archive > .under, .archive > .under-two, .archive > .main-sheet, .archive > .folder-tab')].filter(isVisible);
      if (papers.length) gsap.from(papers, {
        y: distance, opacity: 0.84, duration: timing.paper, stagger: 0.045,
        ease: 'power2.out', immediateRender: false, clearProps: 'transform,opacity', overwrite: 'auto'
      });
    }

    // The comparison remains readable before entry. Opacity alone preserves its authored paper rotations.
    const slips = [...document.querySelectorAll('.service-slip, .declaration-slip')].filter(isVisible);
    const comparison = document.querySelector('.comparison');
    if (slips.length && comparison && !revealSeen.has(comparison)) {
      ScrollTrigger.create({ trigger: comparison, start: 'top 90%', once: true,
        onEnter: () => {
          revealSeen.add(comparison);
          context.add(() => gsap.from(slips, {
            opacity: 0.8, duration: timing.reveal, stagger: 0.07, ease: 'power2.out',
            immediateRender: false, clearProps: 'opacity', overwrite: 'auto'
          }));
        }
      });
    }

    document.querySelectorAll('[data-reveal]').forEach(section => {
      if (revealSeen.has(section) || !isVisible(section) || section.closest('.hero, .comparison')) return;
      const items = [...section.querySelectorAll('[data-reveal-item]')].filter(isVisible);
      const targets = items.length ? items : [section];
      ScrollTrigger.create({ trigger: section, start: 'top 90%', once: true,
        onEnter: () => {
          revealSeen.add(section);
          context.add(() => gsap.from(targets, {
            y: distance, opacity: 0.82, duration: timing.reveal, stagger: items.length ? 0.04 : 0,
            ease: 'power2.out', immediateRender: false, clearProps: 'transform,opacity', overwrite: 'auto'
          }));
        }
      });
    });
    document.querySelectorAll('.record-line').forEach(path => {
      if (!isVisible(path)) return;
      ScrollTrigger.create({ trigger: path.closest('.chart') || path, start: 'top 88%', once: true,
        onEnter: () => drawChart(path) });
    });

    // Application owns content, selected state, focus and layout; motion only acknowledges the replacement.
    context.add('replacePanel', (kind, event) => {
      pending[kind] = event.detail?.panel || event.detail?.target;
      cancelAnimationFrame(frames[kind]);
      frames[kind] = requestAnimationFrame(() => context.add(() => {
        frames[kind] = 0;
        let panel = pending[kind];
        if (typeof panel === 'string') panel = document.querySelector(panel);
        if (!(panel instanceof Element)) panel = document.querySelector(kind === 'process'
          ? '.desk-paper' : '[role="tabpanel"]:not([hidden]), .sample-panel:not([hidden])');
        if (!isVisible(panel)) return;
        gsap.fromTo(panel, { y: kind === 'process' ? 3 : 4, opacity: 0.82 }, {
          y: 0, opacity: 1, duration: timing.replace, ease: 'power2.out', immediateRender: false,
          clearProps: 'transform,opacity', overwrite: 'auto'
        });
        panel.querySelectorAll('.record-line').forEach(drawChart);
        ScrollTrigger.refresh();
      }));
    });
    const onReportChange = event => context.replacePanel('report', event);
    const onProcessChange = event => context.replacePanel('process', event);
    document.addEventListener('vib:report-change', onReportChange);
    document.addEventListener('vib:process-change', onProcessChange);
    return () => {
      Object.values(frames).forEach(cancelAnimationFrame);
      document.removeEventListener('vib:report-change', onReportChange);
      document.removeEventListener('vib:process-change', onProcessChange);
    };
  });

  if (document.readyState === 'complete') ScrollTrigger.refresh();
  else window.addEventListener('load', () => ScrollTrigger.refresh(), { once: true });
  document.fonts?.ready.then(() => ScrollTrigger.refresh());
})();
