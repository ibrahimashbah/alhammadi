from pathlib import Path

p=Path('index.html')
h=p.read_text(encoding='utf-8')

fallbacks={
'assets/partner-lulu.png':('<img src="assets/partner-lulu.png" alt="لولو هايبر ماركت" loading="lazy">','<div class="partner-wordmark-mark">LuLu</div>'),
'assets/partner-reu.png':('<img src="assets/partner-reu.png" alt="جامعة رياض العلم" loading="lazy">','<div class="partner-wordmark-mark">REU</div>'),
'assets/partner-diriyah.jpg':('<img src="assets/partner-diriyah.jpg" alt="جمعية الدرعية" loading="lazy">','<div class="partner-wordmark-mark">الدرعية</div>'),
'assets/partner-shgardi.png':('<img src="assets/partner-shgardi.png" alt="تطبيق شقردي" loading="lazy">','<div class="partner-wordmark-mark">شقردي</div>'),
'assets/partner-century.jpg':('<img src="assets/partner-century.jpg" alt="مجمع عيادات المئوية الاستشارية" loading="lazy">','<div class="partner-wordmark-mark">المئوية</div>'),
}
for asset,(img,fallback) in fallbacks.items():
    if not Path(asset).exists():
        h=h.replace(img,fallback)
p.write_text(h,encoding='utf-8')
