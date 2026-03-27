import json

import os

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(script_dir, 'imgs.json')) as f:
    imgs = json.load(f)

SUPABASE_URL = 'https://qubwootdatrbpyipkrvw.supabase.co'
SUPABASE_KEY = 'sb_publishable_soPXNzg_s8aLgyi6bsQEXw_sRpOEzZU'
ADMIN_PASSWORD = 'stayona2025'
WA_NUMBER = '66XXXXXXXXXX'  # TODO: replace with real WhatsApp number e.g. 66812345678

html = open(os.path.join(script_dir, 'template.html')).read()

html = html.replace('%%PARTNER_BANNER%%', imgs['partner_banner'])
html = html.replace('%%BANNER%%', imgs['banner'])
html = html.replace('%%LOGO%%', imgs['logo'])
html = html.replace('%%LOGO_WHITE%%', imgs['logo_white'])
html = html.replace('%%FAV32%%', imgs['fav32'])
html = html.replace('%%FAV180%%', imgs['fav180'])
html = html.replace('%%FAV192%%', imgs['fav192'])
html = html.replace('%%IMG1%%', imgs['img1'])
html = html.replace('%%IMG2%%', imgs['img2'])
html = html.replace('%%IMG3%%', imgs['img3'])
html = html.replace('%%IMG4%%', imgs['img4'])
html = html.replace('%%IMG5%%', imgs['img5'])
html = html.replace('%%IMG6%%', imgs['img6'])
html = html.replace('%%IMG7%%', imgs['img7'])
html = html.replace('%%QR%%', imgs['qr'])
html = html.replace('%%SUPABASE_URL%%', SUPABASE_URL)
html = html.replace('%%SUPABASE_KEY%%', SUPABASE_KEY)
html = html.replace('%%ADMIN_PASSWORD%%', ADMIN_PASSWORD)
html = html.replace('%%WA_NUMBER%%', WA_NUMBER)

with open(os.path.join(script_dir, 'stayona-final.html'), 'w') as f:
    f.write(html)

with open(os.path.join(script_dir, 'index.html'), 'w') as f:
    f.write(html)

# Build list-your-property page
lyp = open(os.path.join(script_dir, 'list-your-property-template.html')).read()
lyp = lyp.replace('%%PARTNER_BANNER%%', imgs['partner_banner'])
lyp = lyp.replace('%%LOGO%%', imgs['logo'])
lyp = lyp.replace('%%FAV32%%', imgs['fav32'])
lyp = lyp.replace('%%FAV180%%', imgs['fav180'])
lyp = lyp.replace('%%FAV192%%', imgs['fav192'])
lyp = lyp.replace('%%SUPABASE_URL%%', SUPABASE_URL)
lyp = lyp.replace('%%SUPABASE_KEY%%', SUPABASE_KEY)
lyp = lyp.replace('%%WA_NUMBER%%', WA_NUMBER)

with open(os.path.join(script_dir, 'list-your-property.html'), 'w') as f:
    f.write(lyp)

print('Done! Size:', len(html), 'bytes')
