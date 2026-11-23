"""Check the actual static output without third-party packages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse,unquote
import json,re
import xml.etree.ElementTree as ET
root=Path(__file__).resolve().parents[1]/'dist'
class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.nodes=[]
    def handle_starttag(self,tag,attrs):
        self.nodes.append((tag,dict(attrs)))
    def tags(self,t):
        return [attrs for tag,attrs in self.nodes if tag==t]
seen=set()
total=0
for page in sorted(root.rglob('index.html')):
    d=Document()
    d.feed(page.read_text())
    lang=d.tags('html')[0]['lang']
    assert d.tags('html')[0]['dir']==('rtl' if lang=='fa' else 'ltr'),page
    for tag in ['main','h1','title']:
        assert len(d.tags(tag))==1,(page,tag)
    ids=[a['id'] for _,a in d.nodes if 'id' in a]
    assert len(ids)==len(set(ids)),page
    canonical=next(x['href'] for x in d.tags('link') if x.get('rel')=='canonical')
    if page.parent!=root:
        assert canonical not in seen,canonical
        seen.add(canonical)
    assert {a.get('hreflang') for a in d.tags('link') if a.get('rel')=='alternate'}=={'en','fa','x-default'}
    assert next(a['content'] for a in d.tags('meta') if a.get('name')=='description').strip()
    for tag,a in d.nodes:
        for key in ['href','src']:
            if key not in a:continue
            u=urlparse(a[key])
            if u.scheme or u.netloc: continue
            if not u.path:
                if u.fragment:assert u.fragment in ids,(page,u.fragment)
                continue
            dest=page.parent/unquote(u.path)
            if dest.is_dir():dest/= 'index.html'
            assert dest.is_file(),(page,a[key])
            total+=1
    assert all(a.get('aria-label') or 'id' in a for a in d.tags('button'))
for url in re.findall(r'url\(([^)]+)\)',(root/'assets/style.css').read_text()):
    assert (root/'assets'/url).is_file(),url
site=ET.parse(root/'sitemap.xml');assert {e.text for e in site.findall('./{*}url/{*}loc')}==seen
assert (root/'assets/share.png').is_file()
print(f'{len(seen)} localized pages plus root, {total} internal references, sitemap, alternate languages, metadata and font files passed.')
