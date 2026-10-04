from pathlib import Path

GTM_ID = "GTM-K4NQ35MP"
GA4_ID = "G-EKLZ186349"

head_block = f'''<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','{GTM_ID}');</script>
<!-- End Google Tag Manager -->

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA4_ID}');
</script>
'''

body_block = f'''<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
'''

for html_path in Path('.').glob('*.html'):
    text = html_path.read_text(encoding='utf-8')

    if GTM_ID not in text:
        text = text.replace('<head>', '<head>\n' + head_block, 1)
        text = text.replace('<body', body_block + '\n<body', 1)
    elif GA4_ID not in text:
        text = text.replace('</head>', head_block.split('<!-- Google tag (gtag.js) -->', 1)[1].join(['<!-- Google tag (gtag.js) -->', '\n</head>']), 1)

    html_path.write_text(text, encoding='utf-8')
