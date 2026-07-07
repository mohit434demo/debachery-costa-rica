import os, io, base64
from PIL import Image, ImageDraw

base = r"C:\Users\mohitdhande\OneDrive - Microsoft\Documents\Microsoft Scout\Costa Rica Trip Dashboard"
imgdir = os.path.join(base, "images")

def embed(fn, maxw, q=80):
    im = Image.open(os.path.join(imgdir, fn))
    if im.mode in ("RGBA","P","LA"): im=im.convert("RGB")
    w,h=im.size
    if w>maxw: im=im.resize((maxw,int(h*maxw/w)),Image.LANCZOS)
    b=io.BytesIO(); im.save(b,"JPEG",quality=q,optimize=True)
    return "data:image/jpeg;base64,"+base64.b64encode(b.getvalue()).decode()

def img(fn, maxw=820, q=80):
    p=os.path.join(imgdir,fn)
    if os.path.exists(p): return embed(fn,maxw,q)
    im=Image.new("RGB",(820,460)); d=ImageDraw.Draw(im)
    for y in range(460):
        t=y/460; d.line([(0,y),(820,y)],fill=(int(177-117*t),int(31-1*t),int(75-30*t)))
    d.text((40,210),fn.rsplit(".",1)[0].replace("-"," ").title(),fill=(255,255,255))
    b=io.BytesIO(); im.save(b,"JPEG",quality=80)
    return "data:image/jpeg;base64,"+base64.b64encode(b.getvalue()).decode()

I={
 "hero":img("hero.jpg",1500,76),
 "sjo":img("sjo-airport.webp"),"jaco":img("jaco.jpg"),"airbnb":img("airbnb.avif"),
 "dinner1":img("dinner-night1.jpg"),"chill":img("airbnb-chill.avif"),
}

days=[
 {"id":"jul22","tab":"Wed 22","kick":"Jul 22 · Wednesday · Day 1","title":"Fly in & land in Jaco",
  "chips":["~85°F / 29°C, humid","Green season","Arrival day"],
  "secs":[
   {"tag":"Morning","time":"7:00 AM depart ORD","title":"Fly to San Jose (SJO)","img":I["sjo"],
    "body":"Wheels up from Chicago. <strong>AA 1902</strong> ORD &rarr; DFW <strong>7:02-9:40a</strong>, a 1:26 layover in Dallas, then <strong>AA 1053</strong> DFW &rarr; SJO <strong>11:06a-2:17p</strong>. Sleep on the plane - big week ahead.",
    "facts":["AA 1902 + AA 1053","Land SJO 2:17p","1:26 layover DFW"],"map":"Juan+Santamaria+International+Airport+SJO",
    "hop":"Private shuttle SJO &rarr; Jaco, ~95 km / ~1.5 hrs via Rte 27 &amp; the Costanera"},
   {"tag":"Afternoon","time":"~4:00 PM","title":"Arrive Jaco & check in","img":I["airbnb"],"badge":"Code 15326",
    "body":"Roll into the Airbnb on <strong>C. Bohio, Jaco</strong> (Playa Hermosa Palms), drop bags, claim beds. The activity-planning portal uses code <strong>15326</strong>. Change into shorts - you made it to the Pacific.",
    "facts":["C. Bohio, Jaco 61101","Sleeps 16","Pura Vida"],"map":"C.+Bohio,+Jaco,+61101,+Puntarenas,+Costa+Rica",
    "link":("View Airbnb listing","https://www.airbnb.com/rooms/1477522906306087782?adults=16&check_in=2026-07-22&check_out=2026-07-26"),
    "supplies":[("MegaSuper Jaco (groceries)","MegaSuper+Jaco","conv"),("Automercado Jaco","Automercado+Jaco","conv"),("Maxi Pali (beer & supplies)","Maxi+Pali+Jaco","liq"),("Licorera Jaco (liquor)","Licorera+Jaco+Costa+Rica","liq")],
    "hop":"Quick supply run, then ~10 min into Jaco centro for dinner"},
   {"tag":"Evening","time":"8:00 PM","title":"First-night dinner","img":I["dinner1"],
    "body":"Nothing fancy - a casual, crowd-friendly first meal. Pizza is a safe call for the group; grab a few pies and cold cervezas.",
    "facts":["Casual","Big group OK","No reservation"],"map":"Jaco+Costa+Rica+restaurants",
    "food":[("Pizza Hut Jaco","Pizza+Hut+Jaco"),("Amancio's Pizza & Pasta","Amancios+Jaco"),("Graffiti Restro Cafe","Graffiti+Restro+Cafe+Jaco")]},
   {"tag":"Night","time":"Late","title":"Chill at the Airbnb","img":I["chill"],
    "body":"Back to the house - cards, music, first round of drinks by the pool. Easy night one; the real chaos starts tomorrow.",
    "facts":["Pool hang","Early-ish night","Rest up"],"map":"C.+Bohio,+Jaco,+61101,+Puntarenas,+Costa+Rica","rest":"Late · settle in, plan the 6 AM La Fortuna pickup"},
 ]},
]

def fct(fs): return "".join(f'<span class="fact">{x}</span>' for x in fs)

def food(f):
    if not f: return ""
    return '<div class="food"><span class="foodhdr">&#127829; Eat</span>'+"".join(f'<a class="foodlink" href="https://www.google.com/maps/search/?api=1&query={q}" target="_blank">{n}</a>' for n,q in f)+'</div>'

def supplies(s):
    if not s: return ""
    out='<div class="food supp"><span class="foodhdr">&#128722; Stock up</span>'
    for n,q,k in s:
        out+=f'<a class="foodlink {k}" href="https://www.google.com/maps/search/?api=1&query={q}" target="_blank">{n}</a>'
    return out+'</div>'

def card(i,s):
    b=f'<span class="badge">{s["badge"]}</span>' if s.get("badge") else ""
    lu='<div class="lunch">This is where you\'ll have lunch</div>' if s.get("lunch") else ""
    hop=f'<div class="hop"><span class="hi">&#128652;</span><span>{s["hop"]}</span></div>' if s.get("hop") else ""
    rt=s.get("rest")
    rest=(f'<div class="rest"><span class="ri">&#127796;</span><div><strong>Relax at the Airbnb</strong><span>{rt if isinstance(rt,str) else "Regroup at the house"}</span></div></div>') if rt else ""
    lk=s.get("link")
    lka=f'<a class="ml lkx" href="{lk[1]}" target="_blank">{lk[0]}</a>' if lk else ""
    return f'''{rest}<article class="card"><div class="dot">{i+1}</div><div class="photo"><img src="{s['img']}" loading="lazy"></div>
<div class="cb"><div class="ct"><span class="tg">{s['tag']}</span><span class="tm">{s['time']}</span></div><h3>{s['title']}{b}</h3><p>{s['body']}</p>{lu}{food(s.get('food'))}{supplies(s.get('supplies'))}<div class="facts">{fct(s['facts'])}</div><a class="ml" href="https://www.google.com/maps/search/?api=1&query={s['map']}" target="_blank">Open in Maps</a>{lka}</div></article>{hop}'''

tabs="".join(f'<button class="tab" data-d="{d["id"]}" onclick="show(\'{d["id"]}\')">{d["tab"]}</button>' for d in days)
panels=""
for d in days:
    cards="".join(card(i,s) for i,s in enumerate(d["secs"]))
    hero=d.get("hero",I["hero"])
    panels+=f'''<section class="panel" id="{d['id']}"><header class="hero"><img src="{hero}"><div class="sc"></div><div class="ht"><div class="kick">{d['kick']}</div><h1>{d['title']}</h1><div class="chips">{''.join(f'<span class="chip">{c}</span>' for c in d['chips'])}</div></div></header><main class="wrap">{cards}<div class="foot">Manish &amp; Sagar's DeBACHery · Costa Rica · Jul 22-26 · tap any spot for Maps</div></main></section>'''

html=f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>DeBACHery · Costa Rica · Jul 22-26</title>
<script>(()=>{{const p=new URLSearchParams(location.search).get("scoutTheme");document.documentElement.setAttribute("data-theme",p||(matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light"));}})();</script>
<style>
:root{{color-scheme:light;--bg:#f7f4ef;--ev:#fcfbf8;--sf:#fff;--ss:#f5f5f5;--bd:#dedede;--bs:#919191;--tx:#242424;--tm:#5c5c5c;--ts:#6f6f6f;--ac:#b11f4b;--af:#fff;--as:rgba(177,31,75,.08);--lk:#0078d4;--gr:#1f8a5b;--gs:rgba(31,138,91,.10)}}
html[data-theme="dark"]{{color-scheme:dark;--bg:#3d3b3a;--ev:#343231;--sf:#292929;--ss:#2e2e2e;--bd:#474747;--bs:#5f5f5f;--tx:#dedede;--tm:#919191;--ts:#b0b0b0;--ac:#fd8ea1;--af:#1a1a1a;--as:rgba(253,142,161,.14);--lk:#4da6ff;--gr:#5cc999;--gs:rgba(92,201,153,.14)}}
*{{box-sizing:border-box;margin:0;padding:0}}body{{background:var(--bg);color:var(--tx);font-family:"Segoe UI",Aptos,Calibri,-apple-system,sans-serif;line-height:1.55}}
.nav{{position:sticky;top:0;z-index:9;display:flex;gap:6px;overflow-x:auto;padding:10px 12px;background:var(--ev);border-bottom:1px solid var(--bd)}}
.tab{{flex:0 0 auto;border:1px solid var(--bd);background:var(--sf);color:var(--tm);font-weight:700;font-size:13.5px;padding:8px 14px;border-radius:999px;cursor:pointer}}
.tab.on{{background:var(--ac);color:var(--af);border-color:var(--ac)}}
.panel{{display:none}}.panel.on{{display:block}}.wrap{{max-width:780px;margin:0 auto;padding:0 16px 56px}}
.hero{{position:relative;height:280px;overflow:hidden}}.hero img{{width:100%;height:100%;object-fit:cover}}.sc{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.15),rgba(0,0,0,.62))}}.ht{{position:absolute;left:0;right:0;bottom:0;max-width:780px;margin:0 auto;padding:18px;color:#fff}}.kick{{display:inline-block;font-size:13px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;background:var(--ac);color:var(--af);padding:5px 12px;border-radius:999px}}.hero h1{{font-size:30px;margin:10px 0;text-shadow:0 2px 14px rgba(0,0,0,.55)}}.chips{{display:flex;gap:8px;flex-wrap:wrap}}.chip{{background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.35);padding:4px 10px;border-radius:999px;font-size:12.5px}}
.card{{position:relative;background:var(--sf);border:1px solid var(--bd);border-radius:16px;overflow:hidden;box-shadow:0 0 2px rgba(0,0,0,.12),0 1px 2px rgba(0,0,0,.14);margin-top:22px}}.dot{{position:absolute;top:14px;left:14px;z-index:2;width:30px;height:30px;border-radius:50%;background:var(--ac);color:var(--af);font-weight:700;display:flex;align-items:center;justify-content:center}}.photo{{height:200px}}.photo img{{width:100%;height:100%;object-fit:cover;display:block}}.cb{{padding:16px 18px}}.ct{{display:flex;gap:10px;margin-bottom:6px}}.tg{{font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--ac);font-weight:700}}.tm{{font-size:13px;color:var(--ts)}}h3{{font-size:19px;margin-bottom:7px}}.badge{{font-size:11px;font-weight:700;color:var(--af);background:var(--ac);padding:2px 8px;border-radius:999px;margin-left:8px}}p{{color:var(--tm);font-size:15px}}.lunch{{margin-top:10px;padding:8px 12px;background:var(--as);border-left:3px solid var(--ac);border-radius:6px;font-size:13.5px;font-weight:600}}.food{{display:flex;flex-wrap:wrap;gap:7px;margin:12px 0 4px;align-items:center}}.foodhdr{{font-size:12.5px;font-weight:700;color:var(--ts)}}.foodlink{{font-size:12.5px;color:var(--ac);text-decoration:none;background:var(--as);border:1px solid var(--ac);padding:4px 10px;border-radius:999px}}.supp .foodlink{{color:var(--gr);background:var(--gs);border-color:var(--gr)}}.facts{{display:flex;flex-wrap:wrap;gap:7px;margin:13px 0 12px}}.fact{{font-size:12.5px;background:var(--ss);border:1px solid var(--bd);padding:4px 10px;border-radius:999px;color:var(--ts)}}.ml{{font-size:13px;font-weight:600;color:var(--lk);text-decoration:none}}.lkx{{margin-left:14px}}.hop{{display:flex;align-items:center;gap:10px;margin:14px 0;padding:11px 16px;background:var(--as);border:1px solid var(--ac);border-left:4px solid var(--ac);border-radius:10px;font-size:13.5px;font-weight:600}}.hi{{font-size:17px}}.rest{{display:flex;align-items:center;gap:14px;margin-top:14px;padding:14px 18px;background:var(--ev);border:1px dashed var(--bs);border-radius:14px}}.ri{{font-size:22px}}.rest div{{display:flex;flex-direction:column}}.rest span{{color:var(--ts);font-size:13px}}.foot{{text-align:center;margin-top:32px;color:var(--ts);font-size:12.5px}}@media(max-width:560px){{.hero{{height:230px}}.hero h1{{font-size:23px}}}}
</style></head><body>
<nav class="nav">{tabs}</nav>{panels}
<script>function show(id){{document.querySelectorAll('.panel').forEach(p=>p.classList.toggle('on',p.id===id));document.querySelectorAll('.tab').forEach(t=>t.classList.toggle('on',t.dataset.d===id));window.scrollTo(0,0);}}show('{days[0]["id"]}');</script>
</body></html>'''
open(os.path.join(base,"index.html"),"w",encoding="utf-8").write(html)
print("Wrote index.html",round(len(html)/1024),"KB, days:",len(days))
