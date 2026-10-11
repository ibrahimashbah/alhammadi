from pathlib import Path
import re

# Apply the latest client-requested wording after all profile/compact transforms.
index = Path('index.html')
h = index.read_text(encoding='utf-8')

# Hero tagline: remove the full stops for a cleaner visual treatment.
h = h.replace(
    '<span class="lang-ar">معرفة قانونية.<br>رأي مستقل.<br>التزام بمصالحك.</span>',
    '<span class="lang-ar">معرفة قانونية<br>رأي مستقل<br>التزام بمصالحك</span>'
)
h = h.replace(
    '<span class="lang-en">Legal knowledge.<br>Independent judgment.<br>Commitment to your interests.</span>',
    '<span class="lang-en">Legal knowledge<br>Independent judgment<br>Commitment to your interests</span>'
)

# Restore the original compact six-partner presentation requested by the client.
partners = '''<section class="section partner-section">
  <div class="container">
    <div class="section-head reveal"><div><span class="eyebrow"><span class="lang-ar">شركاء النجاح</span><span class="lang-en">Success partners</span></span><h2 class="title-lg"><span class="lang-ar">شركاء نجاح نفخر بالعمل معهم.</span><span class="lang-en">Selected organisations presented among the firm’s success partners.</span></h2></div><p><span class="lang-ar">نعتز بثقة الجهات التي تعاملت معها الشركة، ونلتزم بالحفاظ على سرية العلاقة المهنية وطبيعتها.</span><span class="lang-en">We value the trust of organisations the firm has worked with while respecting the confidentiality and nature of every professional relationship.</span></p></div>
    <div class="partners-grid">
      <div class="partner-logo reveal"><img src="assets/source-images/tourism.png" alt="وزارة السياحة" loading="lazy"><span><span class="lang-ar">وزارة السياحة</span><span class="lang-en">Ministry of Tourism</span></span></div>
      <div class="partner-logo reveal"><img src="assets/source-images/commerce.png" alt="وزارة التجارة" loading="lazy"><span><span class="lang-ar">وزارة التجارة</span><span class="lang-en">Ministry of Commerce</span></span></div>
      <div class="partner-logo reveal"><img src="assets/source-images/industry.png" alt="وزارة الصناعة والثروة المعدنية" loading="lazy"><span><span class="lang-ar">وزارة الصناعة والثروة المعدنية</span><span class="lang-en">Ministry of Industry and Mineral Resources</span></span></div>
      <div class="partner-logo reveal"><img src="assets/source-images/sama.png" alt="البنك المركزي السعودي" loading="lazy"><span><span class="lang-ar">البنك المركزي السعودي</span><span class="lang-en">Saudi Central Bank</span></span></div>
      <div class="partner-logo reveal"><img src="assets/source-images/aramco.png" alt="أرامكو السعودية" loading="lazy"><span><span class="lang-ar">أرامكو السعودية</span><span class="lang-en">Saudi Aramco</span></span></div>
      <div class="partner-logo reveal"><img src="assets/source-images/justice.svg" alt="وزارة العدل" loading="lazy"><span><span class="lang-ar">وزارة العدل</span><span class="lang-en">Ministry of Justice</span></span></div>
    </div>
  </div>
</section>'''
h = re.sub(
    r'<section class="section partner-section(?: profile-partners)?">[\s\S]*?</section>',
    partners,
    h,
    count=1,
)

# Keep the integrated legal expertise section.
# Remove only the consultation summary form card requested by the client.
h = re.sub(
    r'\s*<div class="form-card reveal">[\s\S]*?</form>\s*</div>',
    '',
    h,
    count=1,
)

# With the form removed, make the contact section a clean single-column block.
h = h.replace(
    '<div class="container contact-grid">',
    '<div class="container contact-grid contact-grid-single">',
    1,
)
h = h.replace(
    'لطلب استشارة قانونية أو للاستفسار عن خدمات الشركة، تواصل معنا مباشرة عبر الهاتف أو واتساب، أو أرسل ملخصاً للمسألة من خلال النموذج.',
    'لطلب استشارة قانونية أو للاستفسار عن خدمات الشركة، تواصل معنا مباشرة عبر الهاتف أو واتساب.'
)
h = h.replace(
    'For legal consultations or service enquiries, contact us directly by phone or WhatsApp, or send a brief summary through the form.',
    'For legal consultations or service enquiries, contact us directly by phone or WhatsApp.'
)

# Refresh asset query to avoid stale iPhone/Safari cache.
h = re.sub(r'href="assets/styles\.css(?:\?[^\"]*)?"', 'href="assets/styles.css?v=20261011-six-partners"', h)
h = re.sub(r'src="assets/app\.js(?:\?[^\"]*)?"', 'src="assets/app.js?v=20261011-six-partners"', h)
index.write_text(h, encoding='utf-8')

# Make the remaining contact content balanced after removing the form.
css = Path('assets/styles.css')
c = css.read_text(encoding='utf-8')
if '/* Single-column contact after form removal */' not in c:
    c += '''\n/* Single-column contact after form removal */\n.contact-grid-single {\n  grid-template-columns: minmax(0, 1fr) !important;\n  max-width: 900px;\n  margin-inline: auto;\n}\n'''
css.write_text(c, encoding='utf-8')

# Google review count requested by the client.
app = Path('assets/app.js')
s = app.read_text(encoding='utf-8')
s = re.sub(r'\d+\s+تقييم(?:ًا)? على Google', '243 تقييمًا على Google', s)
s = re.sub(r'\d+\s+Google reviews', '243 Google reviews', s)
app.write_text(s, encoding='utf-8')
