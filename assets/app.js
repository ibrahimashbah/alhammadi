(() => {
  const html = document.documentElement;
  const saved = localStorage.getItem('alhammadi-lang');
  const initial = saved === 'en' ? 'en' : 'ar';

  function setLang(lang) {
    html.lang = lang;
    html.dir = lang === 'ar' ? 'rtl' : 'ltr';
    localStorage.setItem('alhammadi-lang', lang);
    document.querySelectorAll('[data-lang-switch]').forEach(btn => {
      btn.textContent = lang === 'ar' ? 'EN' : 'عربي';
      btn.setAttribute('aria-label', lang === 'ar' ? 'Switch to English' : 'التبديل إلى العربية');
    });
    const arTitle = document.body.dataset.titleAr;
    const enTitle = document.body.dataset.titleEn;
    if (arTitle && enTitle) document.title = lang === 'ar' ? arTitle : enTitle;
  }
  setLang(initial);

  document.querySelectorAll('[data-lang-switch]').forEach(btn => {
    btn.addEventListener('click', () => setLang(html.lang === 'ar' ? 'en' : 'ar'));
  });

  const header = document.querySelector('.site-header');
  const onScroll = () => header?.classList.toggle('is-sticky', window.scrollY > 72);
  onScroll();
  window.addEventListener('scroll', onScroll, {passive:true});

  const menuBtn = document.querySelector('[data-menu-toggle]');
  const nav = document.querySelector('.nav');
  const closeMenu = () => {
    nav?.classList.remove('mobile-open');
    document.body.classList.remove('menu-open');
    if (menuBtn) {
      menuBtn.textContent = '☰';
      menuBtn.setAttribute('aria-expanded','false');
      menuBtn.setAttribute('aria-label', html.lang === 'ar' ? 'فتح القائمة' : 'Open menu');
    }
  };
  menuBtn?.addEventListener('click', () => {
    const open = nav?.classList.toggle('mobile-open');
    document.body.classList.toggle('menu-open', !!open);
    menuBtn.setAttribute('aria-expanded', String(!!open));
    menuBtn.textContent = open ? '×' : '☰';
    menuBtn.setAttribute('aria-label', open ? (html.lang === 'ar' ? 'إغلاق القائمة' : 'Close menu') : (html.lang === 'ar' ? 'فتح القائمة' : 'Open menu'));
  });
  nav?.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMenu));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeMenu(); });
  window.addEventListener('resize', () => { if (window.innerWidth > 1050) closeMenu(); }, {passive:true});

  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: .10, rootMargin: '0px 0px -24px 0px' });
    document.querySelectorAll('.reveal').forEach(el => io.observe(el));
  } else {
    document.querySelectorAll('.reveal').forEach(el => el.classList.add('in'));
  }

  // Reuse imagery from the current Al Hammadi website, with graceful fallbacks if a legacy asset is unavailable.
  document.querySelectorAll('.visual-panel > img').forEach(img => {
    const fail = () => img.closest('.visual-panel')?.classList.add('image-missing');
    img.addEventListener('error', fail, {once:true});
    if (img.complete && img.naturalWidth === 0) fail();
  });
  document.querySelectorAll('.partner-logo img').forEach(img => {
    const fail = () => img.closest('.partner-logo')?.classList.add('image-missing');
    img.addEventListener('error', fail, {once:true});
    if (img.complete && img.naturalWidth === 0) fail();
  });
  document.querySelectorAll('.practice-icon, .practice-detail-head img').forEach(img => {
    const fail = () => { img.style.display = 'none'; };
    img.addEventListener('error', fail, {once:true});
    if (img.complete && img.naturalWidth === 0) fail();
  });

  const form = document.querySelector('[data-consultation-form]');
  form?.addEventListener('submit', (ev) => {
    ev.preventDefault();
    const fd = new FormData(form);
    const ar = html.lang === 'ar';
    const msg = ar
      ? `طلب استشارة قانونية\n\nالاسم: ${fd.get('name') || ''}\nرقم التواصل: ${fd.get('phone') || ''}\nالبريد: ${fd.get('email') || ''}\nالموضوع: ${fd.get('subject') || ''}\n\nملخص المسألة:\n${fd.get('message') || ''}`
      : `Legal consultation request\n\nName: ${fd.get('name') || ''}\nPhone: ${fd.get('phone') || ''}\nEmail: ${fd.get('email') || ''}\nSubject: ${fd.get('subject') || ''}\n\nMatter summary:\n${fd.get('message') || ''}`;
    window.open(`https://wa.me/966555334489?text=${encodeURIComponent(msg)}`, '_blank', 'noopener');
  });
})();
