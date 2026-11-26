import re, glob, os
from playwright.sync_api import sync_playwright
SRC="/home/claude/carrossel/project"; OUT="/home/claude/render/png"; os.makedirs(OUT,exist_ok=True)
F="/home/claude/render/node_modules/@fontsource"
ff=""
for w in (500,700): ff+=f"@font-face{{font-family:'Space Grotesk';font-weight:{w};src:url(file://{F}/space-grotesk/files/space-grotesk-latin-{w}-normal.woff2)}}"
for w in (400,500,600,700): ff+=f"@font-face{{font-family:Inter;font-weight:{w};src:url(file://{F}/inter/files/inter-latin-{w}-normal.woff2)}}"
logos={"/_blob/31aca16e65bf7934a8dba322b3280b11":"file:///home/claude/assets/logo-produlean.png","/_blob/98f37d2b07e27787cd157502c59b3a7f":"file:///home/claude/assets/logo-produlean-branco.png"}
order=["Main","S02-o-que-muda","S03-jornada-diaria","S04-impacto-folha","S05-casos-especiais-1","S06-casos-especiais-2","S07-checklist","S08-olhar-produlean","S09-cta"]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--allow-file-access-from-files"])
    pg=b.new_page(viewport={"width":1080,"height":1350})
    for i,n in enumerate(order,1):
        h=open(f"{SRC}/{n}.dc.html").read()
        m=re.search(r"</helmet>\s*(.*?)\s*</x-dc>",h,re.S); body=m.group(1)
        for k,v in logos.items(): body=body.replace(k,v)
        html=f"<!doctype html><html><head><meta charset='utf-8'><style>{ff}body{{margin:0}}</style></head><body>{body}</body></html>"
        path=f"/home/claude/render/tmp{i}.html"; open(path,"w").write(html)
        pg.goto("file://"+path); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        # overflow check
        ov=pg.evaluate("(()=>{const r=document.body.firstElementChild;return r.scrollHeight})()")
        pg.screenshot(path=f"{OUT}/produlean-6x1-{i:02d}.png",clip={"x":0,"y":0,"width":1080,"height":1350})
        print(i,n,ov)
    b.close()
