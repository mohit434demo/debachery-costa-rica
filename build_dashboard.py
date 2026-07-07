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
 "hero_lafortuna":img("lafortuna.jpg",1500),"shuttle":img("shuttle.jpg"),
 "falls":img("fortuna-waterfall.jpg"),"crlunch":img("cr-lunch.jpg"),"arenal":img("lafortuna.jpg"),
 "springs":img("hot-springs.webp"),"crdinner":img("cr-dinner.jpg"),
}

days=[
 {"id":"jul22","tab":"Wed 22","kick":"Jul 22 · Wednesday · Day 1","title":"Fly in & land in Jaco",
  "chips":["~85°F / 29°C, humid","Green season","Arrival day"],
  "secs":[
   {"tag":"Morning","time":"7:00 AM depart ORD","title":"Fly to San Jose (SJO)","img":I["sjo"],
    "body":"<strong>AA 1902</strong> ORD &rarr; DFW 7:02-9:40a. 1:26 layover. <strong>AA 1053</strong> DFW &rarr; SJO 11:06a-2:17p. Chicago group; NYC crew routes separately.",
    "facts":["AA 1902 + AA 1053","Land SJO 2:17p","Chicago group"],"map":"Juan+Santamaria+International+Airport+SJO",
    "hop":"Private shuttle SJO &rarr; Jaco, ~95 km / ~1.5 hrs"},
   {"tag":"Afternoon","time":"~4:00 PM","title":"Arrive Jaco & check in","img":I["airbnb"],"badge":"Code 15326",
    "body":"Check in and drop bags. Airbnb at <a href=\"https://www.google.com/maps/search/?api=1&query=C.+Bohio,+Jaco,+61101,+Puntarenas,+Costa+Rica\" target=\"_blank\">C. Bohio, Jaco 61101</a>. Activity portal code <strong>15326</strong>.",
    "facts":["C. Bohio, Jaco 61101","Sleeps 16"],"map":"C.+Bohio,+Jaco,+61101,+Puntarenas,+Costa+Rica",
    "link":("View Airbnb listing","https://www.airbnb.com/rooms/1477522906306087782?adults=16&check_in=2026-07-22&check_out=2026-07-26"),
    "supplies":[("Mas x Menos Jaco","Mas+x+Menos+Jaco","conv"),("Super Trust-Mart Jaco","Super+Trust-Mart+Jaco","conv"),("Licorera Jaco (liquor)","Licorera+Jaco+Costa+Rica","liq")],
    "hop":"Supply run, then ~10 min to Jaco centro for dinner"},
   {"tag":"Evening","time":"8:00 PM","title":"First-night dinner","img":I["dinner1"],
    "body":"Casual group dinner. Pizza is an easy call for the first night.",
    "facts":["Casual","Big group OK","No reservation"],"map":"Jaco+Costa+Rica+restaurants",
    "food":[("Pizza Hut Jaco","Pizza+Hut+Jaco"),("Amancio's Pizza & Pasta","Amancios+Jaco"),("Graffiti Restro Cafe","Graffiti+Restro+Cafe+Jaco")]},
   {"tag":"Night","time":"Late","title":"Chill at the Airbnb","img":I["chill"],
    "body":"Back at the house. La Fortuna pickup is 6 AM.",
    "facts":["Pool hang","6 AM pickup"],"map":"C.+Bohio,+Jaco,+61101,+Puntarenas,+Costa+Rica","rest":"Late · settle in, plan the 6 AM La Fortuna pickup"},
 ]},
 {"id":"jul23","tab":"Thu 23","kick":"Jul 23 · Thursday · Day 2","title":"La Fortuna: volcano, waterfall & hot springs","hero":I["hero_lafortuna"],
  "chips":["Full-day tour","6 AM pickup","Lunch + dinner included"],
  "secs":[
   {"tag":"Early","time":"6:00 AM","title":"Pickup at the Airbnb","img":I["shuttle"],"badge":"Be ready 5:45",
    "body":"Guided tour pickup at the main entrance of <a href=\"https://www.google.com/maps/search/?api=1&query=C.+Bohio,+Jaco,+61101,+Puntarenas,+Costa+Rica\" target=\"_blank\">Playa Hermosa Palms</a>. Scenic ride to the Arenal area, ~3 hrs.",
    "facts":["Round-trip transport","Bilingual guide","~3 hr drive"],"map":"Arenal+Volcano+Costa+Rica",
    "link":("View tour details","https://www.getyourguide.com/jaco-l667/jaco-arenal-volcano-fortuna-waterfall-hot-springs-tour-t413880/"),
    "bring":["Swimwear","Change of clothes","Towel","Sandals","Comfortable shoes","Sunscreen","Sunglasses","Insect repellent"],
    "hop":"Scenic drive through volcanoes, plantations and jungle to La Fortuna"},
   {"tag":"Late morning","time":"~10:00 AM","title":"La Fortuna Waterfall","img":I["falls"],
    "body":"Swim in the pool at the base of Costa Rica's most iconic waterfall. Rainforest all around; steps down and back up.",
    "facts":["Swim stop","Waterfall entry included","Bring sandals"],"map":"La+Fortuna+Waterfall","hop":"Short drive to La Fortuna town for lunch"},
   {"tag":"Midday","time":"~12:30 PM","title":"Costa Rican lunch","img":I["crlunch"],"badge":"Included",
    "body":"Authentic lunch at a restaurant near La Fortuna town. Included in the tour.",
    "facts":["Lunch included","La Fortuna town"],"map":"La+Fortuna+Costa+Rica+restaurants","hop":"To the 1968 lava trails"},
   {"tag":"Afternoon","time":"~2:00 PM","title":"Lava trails & Arenal viewpoint","img":I["arenal"],
    "body":"Hike the lava trails from the 1968 eruption and hit the main lookout for the best Arenal views on clear days.",
    "facts":["Lava trail hike","Volcano lookout","Trail entry included"],"map":"Arenal+Volcano+National+Park","hop":"To Paradise Hot Springs at the volcano base"},
   {"tag":"Late afternoon","time":"~4:00 PM","title":"Paradise Hot Springs","img":I["springs"],
    "body":"Soak a couple of hours in the hot spring pools set in tropical gardens at the base of Arenal.",
    "facts":["Hot springs included","~2 hrs","Volcano views"],"map":"Paradise+Hot+Springs+La+Fortuna","hop":"Dinner on the route back to Jaco"},
   {"tag":"Evening","time":"~7:00 PM","title":"Dinner on the way back","img":I["crdinner"],"badge":"Included",
    "body":"Dinner on the drive back to Jaco. Included in the tour. Back at the Airbnb around 10 PM.",
    "facts":["Dinner included","Back ~10 PM"],"map":"Jaco+Costa+Rica"},
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

def bring(items):
    if not items: return ""
    pills="".join(f'<span class="bpill">{x}</span>' for x in items)
    return f'<div class="bring"><span class="bhdr">&#127890; Pack a drawstring bag</span><div class="bwrap">{pills}</div></div>'

def card(i,s):
    b=f'<span class="badge">{s["badge"]}</span>' if s.get("badge") else ""
    lu='<div class="lunch">This is where you\'ll have lunch</div>' if s.get("lunch") else ""
    hop=f'<div class="hop"><span class="hi">&#128652;</span><span>{s["hop"]}</span></div>' if s.get("hop") else ""
    rt=s.get("rest")
    rest=(f'<div class="rest"><span class="ri">&#127796;</span><div><strong>Relax at the Airbnb</strong><span>{rt if isinstance(rt,str) else "Regroup at the house"}</span></div></div>') if rt else ""
    lk=s.get("link")
    lka=f'<a class="ml lkx" href="{lk[1]}" target="_blank">{lk[0]}</a>' if lk else ""
    return f'''{rest}<article class="card"><div class="dot">{i+1}</div><div class="photo"><img src="{s['img']}" loading="lazy"></div>
<div class="cb"><div class="ct"><span class="tg">{s['tag']}</span><span class="tm">{s['time']}</span></div><h3>{s['title']}{b}</h3><p>{s['body']}</p>{lu}{food(s.get('food'))}{supplies(s.get('supplies'))}{bring(s.get('bring'))}<div class="facts">{fct(s['facts'])}</div><a class="ml" href="https://www.google.com/maps/search/?api=1&query={s['map']}" target="_blank">Open in Maps</a>{lka}</div></article>{hop}'''

tabs="".join(f'<button class="tab" data-d="{d["id"]}" onclick="show(\'{d["id"]}\')">{d["tab"]}</button>' for d in days)
panels=""
for d in days:
    cards="".join(card(i,s) for i,s in enumerate(d["secs"]))
    hero=d.get("hero",I["hero"])
    panels+=f'''<section class="panel" id="{d['id']}"><header class="hero"><img src="{hero}"><div class="sc"></div><div class="ht"><div class="brand">Manish &amp; Sags De<span class="bx">BACH</span>ery</div><div class="kick">{d['kick']}</div><h1>{d['title']}</h1><div class="chips">{''.join(f'<span class="chip">{c}</span>' for c in d['chips'])}</div></div></header><main class="wrap">{cards}<div class="foot">Manish &amp; Sags DeBACHery · Costa Rica · Jul 22-26 · tap any spot for Maps</div></main></section>'''

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
.hero{{position:relative;height:330px;overflow:hidden}}.hero img{{width:100%;height:100%;object-fit:cover}}.sc{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.15),rgba(0,0,0,.62))}}.ht{{position:absolute;left:0;right:0;bottom:0;max-width:780px;margin:0 auto;padding:18px;color:#fff}}.kick{{display:inline-block;font-size:13px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;background:var(--ac);color:var(--af);padding:5px 12px;border-radius:999px}}.brand{{font-size:40px;font-weight:900;letter-spacing:-.5px;line-height:1.05;color:#fff;text-shadow:0 3px 16px rgba(0,0,0,.7);margin-bottom:10px}}.brand .bx{{color:#fff}}@media(max-width:560px){{.brand{{font-size:31px}}}}.hero h1{{font-size:22px;margin:8px 0;font-weight:700;text-shadow:0 2px 14px rgba(0,0,0,.55)}}.chips{{display:flex;gap:8px;flex-wrap:wrap}}.chip{{background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.35);padding:4px 10px;border-radius:999px;font-size:12.5px}}
.card{{position:relative;background:var(--sf);border:1px solid var(--bd);border-radius:16px;overflow:hidden;box-shadow:0 0 2px rgba(0,0,0,.12),0 1px 2px rgba(0,0,0,.14);margin-top:22px}}.dot{{position:absolute;top:14px;left:14px;z-index:2;width:30px;height:30px;border-radius:50%;background:var(--ac);color:var(--af);font-weight:700;display:flex;align-items:center;justify-content:center}}.photo{{height:200px}}.photo img{{width:100%;height:100%;object-fit:cover;display:block}}.cb{{padding:16px 18px}}.ct{{display:flex;gap:10px;margin-bottom:6px}}.tg{{font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--ac);font-weight:700}}.tm{{font-size:13px;color:var(--ts)}}h3{{font-size:19px;margin-bottom:7px}}.badge{{font-size:11px;font-weight:700;color:var(--af);background:var(--ac);padding:2px 8px;border-radius:999px;margin-left:8px}}p{{color:var(--tm);font-size:15px}}p a{{color:var(--lk);font-weight:600;text-decoration:underline}}.lunch{{margin-top:10px;padding:8px 12px;background:var(--as);border-left:3px solid var(--ac);border-radius:6px;font-size:13.5px;font-weight:600}}.food{{display:flex;flex-wrap:wrap;gap:7px;margin:12px 0 4px;align-items:center}}.foodhdr{{font-size:12.5px;font-weight:700;color:var(--ts)}}.foodlink{{font-size:12.5px;color:var(--ac);text-decoration:none;background:var(--as);border:1px solid var(--ac);padding:4px 10px;border-radius:999px}}.supp .foodlink{{color:var(--gr);background:var(--gs);border-color:var(--gr)}}.bring{{margin:12px 0 4px;padding:12px 14px;background:var(--gs);border:1px dashed var(--gr);border-radius:12px}}.bhdr{{display:block;font-size:12.5px;font-weight:700;color:var(--gr);margin-bottom:8px}}.bwrap{{display:flex;flex-wrap:wrap;gap:7px}}.bpill{{font-size:12.5px;background:var(--sf);border:1px solid var(--gr);color:var(--tm);padding:4px 10px;border-radius:999px}}.facts{{display:flex;flex-wrap:wrap;gap:7px;margin:13px 0 12px}}.fact{{font-size:12.5px;background:var(--ss);border:1px solid var(--bd);padding:4px 10px;border-radius:999px;color:var(--ts)}}.ml{{font-size:13px;font-weight:600;color:var(--lk);text-decoration:none}}.lkx{{margin-left:14px}}.hop{{display:flex;align-items:center;gap:10px;margin:14px 0;padding:11px 16px;background:var(--as);border:1px solid var(--ac);border-left:4px solid var(--ac);border-radius:10px;font-size:13.5px;font-weight:600}}.hi{{font-size:17px}}.rest{{display:flex;align-items:center;gap:14px;margin-top:14px;padding:14px 18px;background:var(--ev);border:1px dashed var(--bs);border-radius:14px}}.ri{{font-size:22px}}.rest div{{display:flex;flex-direction:column}}.rest span{{color:var(--ts);font-size:13px}}.foot{{text-align:center;margin-top:32px;color:var(--ts);font-size:12.5px}}@media(max-width:560px){{.hero{{height:300px}}.hero h1{{font-size:19px}}}}
</style></head><body>
<nav class="nav">{tabs}</nav>{panels}
<script>function show(id){{document.querySelectorAll('.panel').forEach(p=>p.classList.toggle('on',p.id===id));document.querySelectorAll('.tab').forEach(t=>t.classList.toggle('on',t.dataset.d===id));window.scrollTo(0,0);}}show('{days[0]["id"]}');</script>
</body></html>'''
open(os.path.join(base,"index.html"),"w",encoding="utf-8").write(html)
print("Wrote index.html",round(len(html)/1024),"KB, days:",len(days))
