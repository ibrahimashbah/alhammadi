from pathlib import Path
import re

index=Path('index.html')
h=index.read_text(encoding='utf-8')

partners='''<section class="section partner-section profile-partners">
  <div class="container">
    <div class="section-head reveal"><div><span class="eyebrow"><span class="lang-ar">شركاء النجاح</span><span class="lang-en">Success partners</span></span><h2 class="title-lg"><span class="lang-ar">ثقة نعتز بها، ومسؤولية نلتزم بها.</span><span class="lang-en">Trust we value. Responsibility we honour.</span></h2></div></div>
    <div class="partners-grid profile-partners-grid">
      <div class="partner-logo reveal"><img src="assets/source-images/aramco.png" alt="أرامكو السعودية" loading="lazy"><span><span class="lang-ar">أرامكو السعودية</span><span class="lang-en">Saudi Aramco</span></span></div>
      <div class="partner-logo reveal partner-wordmark"><div class="partner-wordmark-mark">HAH</div><span><span class="lang-ar">شركة HAH البريطانية</span><span class="lang-en">HAH, United Kingdom</span></span></div>
      <div class="partner-logo reveal"><img src="assets/partner-lulu.png" alt="لولو هايبر ماركت" loading="lazy"><span><span class="lang-ar">لولو هايبر ماركت</span><span class="lang-en">LuLu Hypermarket</span></span></div>
      <div class="partner-logo reveal"><img src="assets/partner-reu.jpg" alt="جامعة رياض العلم" loading="lazy"><span><span class="lang-ar">جامعة رياض العلم</span><span class="lang-en">Riyadh Elm University</span></span></div>
      <div class="partner-logo reveal"><img src="assets/partner-diriyah.jpg" alt="جمعية الدرعية" loading="lazy"><span><span class="lang-ar">جمعية الدرعية</span><span class="lang-en">Diriyah Society</span></span></div>
      <div class="partner-logo reveal partner-wordmark"><div class="partner-wordmark-mark">AHC</div><span><span class="lang-ar">شركة الحمادي للتجارة والصناعة والمقاولات</span><span class="lang-en">Al Hammadi Trading, Industry & Contracting Co.</span></span></div>
      <div class="partner-logo reveal partner-wordmark"><div class="partner-wordmark-mark">AH</div><span><span class="lang-ar">شركة أبناء الحبيل للتجارة والصناعة والزراعة والمقاولات</span><span class="lang-en">Abnaa Al-Hubail Trading, Industry, Agriculture & Contracting Co.</span></span></div>
      <div class="partner-logo reveal partner-wordmark"><div class="partner-wordmark-mark">HM</div><span><span class="lang-ar">شركة حلول مكس للخرسانة</span><span class="lang-en">Holol Mix Concrete Co.</span></span></div>
      <div class="partner-logo reveal partner-wordmark"><div class="partner-wordmark-mark">IO</div><span><span class="lang-ar">البخور الذكي</span><span class="lang-en">Intelligent Oud</span></span></div>
      <div class="partner-logo reveal partner-wordmark"><div class="partner-wordmark-mark">ثنة</div><span><span class="lang-ar">شركة ثنة</span><span class="lang-en">Thannah Co.</span></span></div>
      <div class="partner-logo reveal"><img src="assets/partner-shgardi.png" alt="تطبيق شقردي" loading="lazy"><span><span class="lang-ar">تطبيق شقردي</span><span class="lang-en">Shgardi App</span></span></div>
      <div class="partner-logo reveal partner-wordmark"><div class="partner-wordmark-mark">رواق</div><span><span class="lang-ar">شركة رواق للتطوير العقاري</span><span class="lang-en">Riwaq Real Estate Development Co.</span></span></div>
      <div class="partner-logo reveal partner-wordmark"><div class="partner-wordmark-mark">BE</div><span><span class="lang-ar">شركة بناء الحدث</span><span class="lang-en">Build Event</span></span></div>
      <div class="partner-logo reveal"><img src="assets/partner-century.jpg" alt="مجمع عيادات المئوية الاستشارية" loading="lazy"><span><span class="lang-ar">مجمع عيادات المئوية الاستشارية</span><span class="lang-en">Century Consultancy Clinics Complex</span></span></div>
    </div>
  </div>
</section>'''
h=re.sub(r'<section class="section partner-section(?: profile-partners)?">[\s\S]*?</section>',partners,h,count=1)

# Profile wording for official sources; keep the useful official links already built into the site.
h=h.replace('<span class="lang-ar">المعرفة القانونية</span><span class="lang-en">Legal knowledge</span>','<span class="lang-ar">مصادر معرفية</span><span class="lang-en">Legal resources</span>')
h=h.replace('<span class="lang-ar">الوصول إلى المصدر الرسمي، بوضوح واختصار.</span><span class="lang-en">Direct access to official legal sources, clearly and concisely.</span>','<span class="lang-ar">مراجع رسمية للأنظمة واللوائح والأحكام والأدلة الإرشادية.</span><span class="lang-en">Official references for laws, regulations, judgments and guidance.</span>')
h=h.replace('<span class="lang-ar">قسم مرجعي يسهّل الوصول إلى أبرز الجهات والمنصات الرسمية ذات الصلة بالممارسة القانونية في المملكة العربية السعودية.</span><span class="lang-en">A reference section providing direct access to key official institutions and platforms relevant to legal practice in Saudi Arabia.</span>','<span class="lang-ar">مراجع رسمية تتيح الوصول إلى الأنظمة واللوائح والأحكام والأدلة الإرشادية في المملكة.</span><span class="lang-en">Official sources providing access to laws, regulations, judgments and guidance in the Kingdom.</span>')

# Profile-aligned footer tagline while retaining navigation, X, Google Maps and contact enhancements.
h=re.sub(r'(<div class="footer-brand">[\s\S]*?<a class="brand"[\s\S]*?</a>)\s*<p>[\s\S]*?</p>',r'\1<p><span class="lang-ar">معرفة قانونية. رأي مستقل. التزام بمصالحك.</span><span class="lang-en">Legal knowledge. Independent judgment. Commitment to your interests.</span></p>',h,count=1)

h=re.sub(r'href="assets/styles\.css(?:\?[^\"]*)?"','href="assets/styles.css?v=20261004-profile-full"',h)
h=re.sub(r'src="assets/app\.js(?:\?[^\"]*)?"','src="assets/app.js?v=20261004-profile-full"',h)
index.write_text(h,encoding='utf-8')

css=Path('assets/styles.css')
c=css.read_text(encoding='utf-8')
if '/* Profile partners */' not in c:
    c+='''\n/* Profile partners */\n.profile-pillars .section-head{margin-bottom:48px}\n.profile-expertise .copy p{color:rgba(255,255,255,.75)}\n.profile-partners-grid{grid-template-columns:repeat(4,minmax(0,1fr))}\n.profile-partners-grid .partner-logo{min-height:200px;padding:24px 18px}\n.profile-partners-grid .partner-logo>img{width:auto;height:72px;max-width:150px;object-fit:contain;filter:grayscale(1) contrast(.9);opacity:.82;margin-inline:auto}\n.profile-partners-grid .partner-logo:hover>img{filter:grayscale(0);opacity:1}\n.partner-wordmark{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}\n.partner-wordmark-mark{min-width:72px;min-height:72px;padding:0 12px;display:grid;place-items:center;border:1px solid rgba(8,10,11,.15);color:var(--night);font-size:22px;font-weight:700;background:rgba(255,255,255,.55)}\n.profile-partners-grid .partner-logo>span{margin-top:18px;max-width:230px;line-height:1.55}\n@media(max-width:1050px){.profile-partners-grid{grid-template-columns:repeat(3,minmax(0,1fr))}}\n@media(max-width:760px){.profile-partners-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.profile-partners-grid .partner-logo{min-height:170px;padding:18px 12px}.profile-partners-grid .partner-logo>img{height:58px;max-width:120px}.partner-wordmark-mark{min-width:60px;min-height:60px;font-size:18px}}\n'''
css.write_text(c,encoding='utf-8')
