from pathlib import Path

p=Path('index.html')
h=p.read_text(encoding='utf-8')

# Riyadh Elm University: the profile generator uses the old temporary jpg name.
# Prefer the verified Wikimedia logo downloaded as PNG; otherwise use a clean wordmark.
reu_old='<img src="assets/partner-reu.jpg" alt="جامعة رياض العلم" loading="lazy">'
if Path('assets/partner-reu.png').exists():
    h=h.replace(reu_old,'<img src="assets/partner-reu.png" alt="جامعة رياض العلم" loading="lazy">')
else:
    h=h.replace(reu_old,'<div class="partner-wordmark-mark">REU</div>')

fallbacks={
'assets/partner-lulu.png':('<img src="assets/partner-lulu.png" alt="لولو هايبر ماركت" loading="lazy">','<div class="partner-wordmark-mark">LuLu</div>'),
'assets/partner-diriyah.jpg':('<img src="assets/partner-diriyah.jpg" alt="جمعية الدرعية" loading="lazy">','<div class="partner-wordmark-mark">الدرعية</div>'),
'assets/partner-shgardi.png':('<img src="assets/partner-shgardi.png" alt="تطبيق شقردي" loading="lazy">','<div class="partner-wordmark-mark">شقردي</div>'),
'assets/partner-century.jpg':('<img src="assets/partner-century.jpg" alt="مجمع عيادات المئوية الاستشارية" loading="lazy">','<div class="partner-wordmark-mark">المئوية</div>'),
}
for asset,(img,fallback) in fallbacks.items():
    if not Path(asset).exists():
        h=h.replace(img,fallback)

p.write_text(h,encoding='utf-8')
