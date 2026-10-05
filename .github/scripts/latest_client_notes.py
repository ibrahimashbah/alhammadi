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
h = re.sub(r'href="assets/styles\.css(?:\?[^\"]*)?"', 'href="assets/styles.css?v=20261005-contact-fix"', h)
h = re.sub(r'src="assets/app\.js(?:\?[^\"]*)?"', 'src="assets/app.js?v=20261005-contact-fix"', h)
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
