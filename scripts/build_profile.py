"""Build original, self-contained SVG artwork for the GitHub profile."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
ASSETS.mkdir(exist_ok=True)

def svg(name, width, height, title, body):
    content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" role="img" aria-labelledby="title">
<title id="title">{escape(title)}</title>
{body}
</svg>\n'''
    (ASSETS / name).write_text(content, encoding='utf-8', newline='\n')

def text(x, y, value, size=16, fill='#EDEBE6', weight=400, tracking=0, family='Arial, Helvetica, sans-serif'):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-family="{family}" font-size="{size}" font-weight="{weight}" letter-spacing="{tracking}">{escape(value)}</text>'

hero = '''<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1136" y2="360" gradientUnits="userSpaceOnUse"><stop stop-color="#151B20"/><stop offset="1" stop-color="#080D11"/></linearGradient>
<pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="0.8" fill="#56616A" opacity="0.24"/></pattern>
</defs>
<rect width="1136" height="360" rx="16" fill="url(#bg)"/>
<rect x="690" y="24" width="420" height="300" fill="url(#dots)"/>
<path d="M48 41H82" stroke="#E7A776" stroke-width="3"/>
'''
hero += text(96,46,'WRIGHT / ENGINEERING PORTFOLIO',12,'#B6BFC5',400,2)
hero += text(44,153,'WRIGHT',100,'#F4F0E9',600,-5)
hero += text(48,207,'Hardware. Software. Intelligence.',27,'#E7A776',400,-.5)
hero += text(48,246,'From idea to a working system.',19,'#AEB9C1')
hero += '<path d="M48 285H658" stroke="#354049"/>'
hero += text(48,318,'AI HARDWARE',11,'#C6CFD5',400,1.5)
hero += text(207,318,'EMBEDDED SYSTEMS',11,'#C6CFD5',400,1.5)
hero += text(426,318,'MVP DEVELOPMENT',11,'#C6CFD5',400,1.5)
hero += '''<g stroke-linejoin="round">
<path d="M748 244L894 172L1040 244L894 318Z" fill="#111C24" stroke="#354A58"/>
<path d="M748 195L894 123L1040 195L894 269Z" fill="#172630" stroke="#597381"/>
<path d="M748 146L894 74L1040 146L894 220Z" fill="#243A43" stroke="#9BB9BE"/>
<path d="M804 146L894 102L984 146L894 192Z" fill="#17262D" stroke="#63868B"/>
<path d="M862 146L894 130L926 146L894 162Z" fill="#E7A776" stroke="#F5D1AA"/>
<path d="M748 146V244M894 220V318M1040 146V244" stroke="#526C78" stroke-dasharray="3 6"/>
<path d="M926 146H1060V94H1090M862 146H729V96H700M894 162V245" stroke="#E7A776" stroke-width="1.5"/>
<circle cx="1090" cy="94" r="4" fill="#E7A776"/><circle cx="700" cy="96" r="4" fill="#E7A776"/><circle cx="894" cy="245" r="4" fill="#E7A776"/>
</g>'''
svg('hero.svg',1136,360,'Wright — AI Hardware & Embedded Systems Engineer. From idea to a working system.',hero)

arts = {
'dispenser': '''<path d="M410 165V59H557V165M433 60V86H533V60M483 87V125L492 136L501 125V87" stroke="#A0B7BC" stroke-width="3"/>
<path d="M444 169H541M453 158H532V178H453Z" stroke="#667F89" stroke-width="2"/>
<path d="M484 143V145M500 148V150M491 151V153" stroke="#E7A776" stroke-width="3"/>
<circle cx="410" cy="59" r="5" fill="#E7A776"/><circle cx="557" cy="59" r="5" fill="#E7A776"/>''',
'inkseat': '''<path d="M423 65H555L548 155H416Z" fill="#E4E2D9" stroke="#A1B9BB" stroke-width="2"/>
<path d="M423 65L405 168H565L555 65M416 155L405 168M548 155L565 168" stroke="#6D8991" stroke-width="2"/>
<rect x="436" y="88" width="26" height="26" rx="3" fill="#B17F5B"/>
<path d="M472 92H532M472 102H518M436 128H531M436 137H503" stroke="#46585B" stroke-width="3"/>
<path d="M570 52Q585 63 585 81M577 43Q595 57 595 81" stroke="#E7A776" stroke-width="2"/>''',
'shiyin': '''<rect x="404" y="66" width="177" height="98" rx="12" stroke="#698791" stroke-width="2"/>
<path d="M421 116H430M437 100V132M446 88V144M455 104V128M464 97V135M473 108V124M482 81V151M491 99V133M500 105V127M509 91V141M518 104V128M527 99V133M536 110V122M545 103V129M554 116H564" stroke="#A9C2C6" stroke-width="3" stroke-linecap="round"/>
<path d="M482 81V151" stroke="#E7A776" stroke-width="3"/>
<circle cx="416" cy="48" r="3" fill="#E7A776"/><path d="M428 48H486" stroke="#57717C"/>''',
'house': '''<path d="M410 63L456 48L507 66L564 49V161L507 178L456 161L410 178Z" fill="#142029" stroke="#69838E" stroke-width="2"/>
<path d="M456 48V161M507 66V178M410 114L456 101L507 119L564 100" stroke="#3F5965"/>
<path d="M430 148L458 127L487 137L533 100" stroke="#E7A776" stroke-width="2" stroke-dasharray="4 5"/>
<path d="M533 73C514 73 512 94 533 112C554 94 552 73 533 73Z" fill="#E7A776"/>
<circle cx="533" cy="88" r="5" fill="#18242B"/><circle cx="430" cy="148" r="4" fill="#9DB6BE"/>'''
}
cards = [('dispenser','01 / EDGE AI & AUTOMATION','dispenser-ai','Local intelligence. Physical action.'),('inkseat','02 / CONNECTED HARDWARE','InkSeat','Low-power displays. Connected.'),('shiyin','03 / SPEECH & APPLICATIONS','Shiyin AI','Audio into context.'),('house','04 / AI & WEB APPLICATIONS','House Hunting','Location meets intelligence.')]
for key, label, title, subtitle in cards:
    body='<rect width="620" height="220" rx="10" fill="#121B22"/><path d="M30 190H590" stroke="#2B3A44"/>'
    body+=text(30,40,label,10,'#AABBC5',400,1.5)
    body+=text(28,106,title,36,'#F1EEE8',500,-1)
    body+=text(30,140,subtitle,14,'#B1C0C8')
    body+='<path d="M30 167H57" stroke="#E7A776" stroke-width="2"/>'
    body+=arts[key]
    svg(f'{key}.svg',620,220,title+' — '+subtitle,body)

print('Built hero.svg and four original project illustrations.')
