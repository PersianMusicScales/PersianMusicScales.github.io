"""Generate the Persian Music Scales bilingual static edition with Python 3."""
import json,os,shutil,sys
from html import escape
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET
from figures import dial
R=Path(__file__).resolve().parents[1]
O=R/'dist'
BASE=os.environ.get('SITE_URL','https://persianmusicscales.github.io').rstrip('/')
PREVIEW=os.environ.get('PREVIEW','0')=='1'
if not urlparse(BASE).netloc: raise ValueError('SITE_URL requires an absolute URL')
if O.exists(): shutil.rmtree(O)
O.mkdir()
shutil.copytree(R/'assets',O/'assets')
def write(path,data):
    p=O/path
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(data)
P={}
for f in sorted((R/'content').glob('*.json')):
    new=json.loads(f.read_text())
    if P.keys() & new.keys(): raise ValueError(f'Duplicate page in {f}')
    P.update(new)
MODES='shur nava segah chahargah homayoun mahur rast-panjgah esfahan abu-ata bayat-e-tork afshari dashti'.split()
APP='https://persianmusicscales.github.io/Persian-Music-Scales-App/index.html?lang='
ATLAS='https://persianmusicscales.github.io/urmawi-advar-atlas/'
def route(k,l):
    slug='' if k=='home' else ('modes/' if k in MODES else '')+k+'/'
    return l+'/'+slug
def link(url,t,css=''):
    return f'<a class="{css}" href="{escape(url,quote=True)}">{escape(t)}</a>'
def logo():
    return '<svg viewBox="0 0 40 40" width="39" height="39" aria-hidden="true" fill="none" stroke="currentColor"><circle cx="20" cy="20" r="17"/><circle cx="20" cy="20" r="12"/><path d="m20 4 14 24H6Zm0 32L6 12h28Z"/><circle cx="20" cy="20" r="3"/></svg>'
def page(k,l,root=False):
    fa=l=='fa'
    def T(a,b):return b if fa else a
    path=route(k,l)
    up='./' if root else '../'*path.count('/')
    def loc(j,lang=l):return up+route(j,lang)
    def il(j,t,c=''):return link(loc(j),t,c)
    p=P[k][l]
    alt='en' if fa else 'fa'
    brand=T('Persian Music Scales','گام‌های موسیقی ایرانی')
    nav=[('theory',T('Theory','مبانی')),('modes',T('Modes','دستگاه‌ها')),('tools',T('Tools','ابزارها')),('history',T('History','تاریخ')),('research',T('Research','پژوهش'))]
    navlinks=''.join(f'<a href="{loc(j)}"'+(' aria-current="page"' if j==k else '')+'>'+t+'</a>' for j,t in nav)
    header=f'<header><div class="bar"><a class="brand" href="{loc("home")}">{logo()}{brand}</a><nav aria-label="{T("Main","اصلی")}">{navlinks}</nav><div class="actions"><a lang="{alt}" hreflang="{alt}" href="{loc(k,alt)}">{T("فارسی","English")}</a><button id="theme" aria-label="{T("Change color theme","تغییر حالت رنگ")}">◐</button><button id="menu" hidden aria-expanded="false" aria-controls="mobile">{T("Menu","فهرست")}</button></div></div><nav id="mobile" hidden>{navlinks}</nav></header>'
    def plate():
        return f'<figure class="plate"><figcaption>{T("INTERVAL STUDY","مطالعهٔ فاصله‌ها")} <span>{T("MODEL · 24 EDO","مدل · ۲۴ قسمت مساوی")}</span></figcaption>{dial(l)}<div class="dialctrl"><button data-step="-1" aria-label="{T("Previous pitch position","جایگاه قبلی")}">−</button><output aria-live="polite" data-unit="{T("cents","سنت")}">0 {T("cents","سنت")}</output><button data-step="1" aria-label="{T("Next pitch position","جایگاه بعدی")}">+</button></div><small>{T("One step = 50 cents in this model.","هر گام در این مدل برابر با ۵۰ سنت است.")}</small></figure>'
    def cards(items):
        return '<div class="cards">'+''.join(f'<a href="{loc(j)}"><span class="glyph" aria-hidden="true">{g}</span><h3>{escape(P[j][l]["title"])}</h3><p>{escape(P[j][l]["lead"])}</p></a>' for j,g in items)+'</div>'
    def index():
        return '<div class="filter" hidden><label for="filter">'+T('Find a mode','جست‌وجوی دستگاه یا آواز')+'</label><input id="filter" type="search"></div><p id="empty" hidden>'+T('No matching entry.','مدخلی پیدا نشد.')+'</p>'+''.join('<section><h2>'+t+'</h2><div class="modes">'+''.join(f'<a data-search="{escape(P[j]["fa"]["title"]+" "+P[j]["en"]["title"]+" "+j)}" href="{loc(j)}"><strong>{escape(P[j][l]["title"])}</strong><span lang="{alt}">{escape(P[j][alt]["title"])}</span></a>' for j in keys)+'</div></section>' for t,keys in [(T('Dastgah','دستگاه‌ها'),MODES[:7]),(T('Avaz','آوازها'),MODES[7:])])
    if k=='home':
        main=f'<section class="hero"><div class="herocopy"><div class="eyebrow">{T("PERSIAN CLASSICAL MUSIC","موسیقی دستگاهی ایران")}</div><h1>{T("Persian Music <em>Scales</em>","گام‌های <em>موسیقی ایرانی</em>")}</h1><p>{escape(p["lead"])}</p><div class="buttons">{il("modes",T("Explore the modes","آشنایی با دستگاه‌ها"),"primary")}{link(APP+l,T("Launch interactive app","ورود به برنامه"),"secondary")}</div></div>{plate()}</section><section class="paths"><div class="eyebrow">{T("FIELD GUIDE","راهنمای مطالعه")}</div><h2>{T("Ways to explore","مسیرهای مطالعه")}</h2>{cards([("theory","♩"),("tools","∿"),("history","⌁")])}</section>'
        main+=f'<section class="atlasfeature"><div><div class="eyebrow">{T("HISTORICAL MUSIC THEORY","نظریهٔ تاریخی موسیقی")}</div><h2>{T("One string, two ratios","یک سیم، دو نسبت")}</h2><p>{T("Halve the sounding length of a string and its frequency doubles. Follow that relationship from a monochord to the interval cycles of Ṣafī al-Dīn al-Urmawī.","طول بخش مرتعش سیم را نصف کنید تا بسامد آن دو برابر شود. این رابطه را از تقسیم سیم تا دورهای صفی‌الدین ارموی دنبال کنید.")}</p>{il("history",T("Discover the Advar Atlas","آشنایی با اطلس ادوار"),"secondary")}</div><figure dir="ltr"><div class="string"><i></i></div><b>1 : 1</b><div class="string half"><i></i></div><b>1 : 2</b><figcaption>{T("Relative sounding length at constant tension and linear density.","طول نسبی بخش مرتعش سیم در کشش و چگالی خطی ثابت.")}</figcaption></figure></section>'
    else:
        bread=il('home',brand)+' / '+(il('modes',T('Modes','دستگاه‌ها'))+' / ' if k in MODES else '')+escape(p['title'])
        main=f'<div class="crumb">{bread}</div><article><div class="eyebrow">{brand}</div><h1>{escape(p["title"])}</h1><p class="lead">{escape(p["lead"])}</p>'
        if k=='modes':main+=index()
        if k=='notation':main+=plate()
        main+='<div class="prose">'+''.join(f'<section><h2>{escape(h)}</h2><p>{escape(v)}</p></section>' for h,v in p.get('sections',[]))+'</div>'
        if k=='theory':main+=il('notation',T('Study the interval circle','مطالعهٔ دایرهٔ فاصله‌ها'),'primary')+' '+il('modes',T('Browse the modes','فهرست دستگاه‌ها و آوازها'),'secondary')
        if k in MODES:main+=link(APP+l,T('Explore in the application','کاوش در برنامه'),'primary')+' '+il('modes',T('All modes','همهٔ دستگاه‌ها و آوازها'),'secondary')
        if k=='tools':main+=link(APP+l,T('Open the scale explorer','ورود به برنامهٔ گام‌ها'),'primary')
        if k=='history':main+=link(ATLAS+'?lang='+l,T('Open the Advar Atlas','ورود به اطلس ادوار'),'primary')
        relatives={'shur':['abu-ata','bayat-e-tork','afshari','dashti','nava'],'homayoun':['esfahan'],'esfahan':['homayoun'],'mahur':['rast-panjgah'],'rast-panjgah':['mahur'],'nava':['shur'],**{x:['shur'] for x in MODES[8:]}}
        if k in relatives:main+='<aside><h2>'+T('Related modes','دستگاه‌ها و آوازهای مرتبط')+'</h2>'+ ' · '.join(il(j,P[j][l]['title']) for j in relatives[k])+'</aside>'
        if p.get('links'):main+='<aside><h2>'+T('Sources & further reading','منابع و مطالعهٔ بیشتر')+'</h2><ul>'+''.join('<li>'+link(url,label)+'</li>' for label,url in p['links'])+'</ul></aside>'
        main+='</article>'
    footer=f'<footer><div><strong>{brand}</strong><p>{T("A project by Dr. Pouya Hosseini","پروژه‌ای از دکتر پویا حسینی")}</p></div><div>{il("about",T("About the project","دربارهٔ پروژه"))}{il("research",T("Research & references","پژوهش و منابع"))}{il("search",T("Search the site","جست‌وجو در سایت"))}</div></footer>'
    if k=='search':
        items=[(j,a[l]['title'],a[l]['lead']) for j,a in P.items() if j not in ('search','home')]
        main=main.replace('</article>','<div class="filter" hidden><label for="filter">'+T('Search pages','جست‌وجوی صفحه‌ها')+'</label><input id="filter" type="search"></div><p id="empty" hidden>'+T('No matching pages.','صفحه‌ای پیدا نشد.')+'</p><ul class="results">'+''.join(f'<li data-search="{escape(title+" "+lead+" "+P[j][alt]["title"])}">{il(j,title)}<p>{escape(lead)}</p></li>' for j,title,lead in items)+'</ul></article>')
    title=escape(p['title']+' · '+brand) if k!='home' else brand
    meta=escape(p['lead'],quote=True)
    alts=''.join(f'<link rel="alternate" hreflang="{a}" href="{BASE}/{route(k,a)}">' for a in ['en','fa'])
    structured=json.dumps({'@context':'https://schema.org','@type':'WebPage','name':p['title'],'inLanguage':l,'url':BASE+'/'+path},ensure_ascii=False)
    noindex='<meta name="robots" content="noindex,nofollow">' if PREVIEW else ''
    return f'''<!doctype html><html lang="{l}" dir="{T("ltr","rtl")}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">{noindex}<title>{title}</title><meta name="description" content="{meta}"><link rel="canonical" href="{BASE}/{path}">{alts}<link rel="alternate" hreflang="x-default" href="{BASE}/{route(k,"en")}"><meta property="og:title" content="{title}"><meta property="og:description" content="{meta}"><meta property="og:type" content="website"><meta property="og:url" content="{BASE}/{path}"><meta property="og:image" content="{BASE}/assets/share.png"><link rel="icon" href="{up}assets/icon.svg"><link rel="stylesheet" href="{up}assets/style.css"><script src="{up}assets/theme.js"></script><script src="{up}assets/ui.js" defer></script><script type="application/ld+json">{structured}</script></head><body><a class="skip" href="#content">{T("Skip to content","رفتن به محتوا")}</a>{header}<main id="content">{main}</main>{footer}</body></html>'''
for k in P:
    for lang in ['en','fa']:
        write(route(k,lang)+'index.html',page(k,lang))
write('index.html',page('home','en',True))
write('assets/icon.svg',logo().replace('<svg ','<svg xmlns="http://www.w3.org/2000/svg" color="#699b8b" '))
write('.nojekyll','')
s=ET.Element('urlset',xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')
for k in P:
    for l in ['en','fa']:ET.SubElement(ET.SubElement(s,'url'),'loc').text=BASE+'/'+route(k,l)
write('sitemap.xml',ET.tostring(s,encoding='unicode'))
write('robots.txt','User-agent: *\n'+('Disallow: /\n' if PREVIEW else 'Allow: /\nSitemap: '+BASE+'/sitemap.xml\n'))
print('Generated',len(P)*2+1,'HTML pages')
