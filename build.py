import json

with open('/home/claude/imgs.json') as f:
    imgs = json.load(f)

SUPABASE_URL = 'https://qubwootdatrbpyipkrvw.supabase.co'
SUPABASE_KEY = 'sb_publishable_soPXNzg_s8aLgyi6bsQEXw_sRpOEzZU'
ADMIN_PASSWORD = 'stayona2025'

html = open('/home/claude/template.html').read()

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

with open('/mnt/user-data/outputs/stayona-final.html', 'w') as f:
    f.write(html)

print('Done! Size:', len(html), 'bytes')
