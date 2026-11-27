import os
from playwright.sync_api import sync_playwright

BASE = "/home/claude/case"
IMG = f"file://{BASE}/img"
OUT = f"{BASE}/png"
os.makedirs(OUT, exist_ok=True)
W, H, N = 1080, 1350, 9
DARK, CREAM, YEL = "#282829", "#F3F1EC", "#FFF212"
HG = "font-family:'Space Grotesk',sans-serif"
F = "/home/claude/render/node_modules/@fontsource"
FF = ""
for w in (500, 700):
    FF += f"@font-face{{font-family:'Space Grotesk';font-weight:{w};src:url(file://{F}/space-grotesk/files/space-grotesk-latin-{w}-normal.woff2)}}"
for w in (400, 500, 600, 700):
    FF += f"@font-face{{font-family:Inter;font-weight:{w};src:url(file://{F}/inter/files/inter-latin-{w}-normal.woff2)}}"

slides = []


def page(n, theme, body, swipe=True, bgimg=None):
    bg, fg, muted = {"dark": (DARK, "#FFFFFF", "#A3A3A3"), "light": (CREAM, DARK, "#5E5E5E"), "yellow": (YEL, DARK, "#3A3A3A")}[theme]
    logo = f"{IMG}/logo-produlean-branco.png" if theme == "dark" else f"{IMG}/logo-produlean.png"
    back = ""
    if bgimg:
        back = (f'<div style="position:absolute;inset:0;background:url({bgimg}) center/cover"></div>'
                f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(40,40,41,.35) 0%,rgba(40,40,41,.10) 25%,rgba(40,40,41,.75) 52%,rgba(40,40,41,.98) 68%)"></div>')
    foot = (f'<div style="display:flex;justify-content:space-between;align-items:center;font-size:24px;font-weight:600;color:{muted}">'
            f'<div>@produlean_oficial</div><div>{"Arraste para o lado &#8594;" if swipe else ""}</div></div>')
    html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{FF}body{{margin:0}}b{{font-weight:700}}</style></head><body>
<div style="position:relative;width:{W}px;height:{H}px;background:{bg};overflow:hidden">{back}
<div style="position:relative;width:{W}px;height:{H}px;box-sizing:border-box;padding:88px 88px 80px;color:{fg};font-family:Inter,sans-serif;display:flex;flex-direction:column;justify-content:space-between;gap:36px">
<div style="display:flex;justify-content:space-between;align-items:center">
<img src="{logo}" style="height:66px;width:auto;display:block">
<div style="font-size:26px;font-weight:600;color:{muted}">{n:02d}/{N:02d}</div></div>
{body}
{foot}
</div></div></body></html>'''
    slides.append(html)


def kicker(t, color=YEL, text=DARK):
    return f'<div style="align-self:flex-start;background:{color};color:{text};font-weight:700;font-size:22px;letter-spacing:2px;padding:10px 18px;border-radius:999px">{t}</div>'


def photo(src, h, label=None, lab_bg=DARK, lab_fg="#FFFFFF", pos="center"):
    lab = f'<div style="position:absolute;left:16px;top:16px;background:{lab_bg};color:{lab_fg};font-weight:700;font-size:20px;letter-spacing:2px;padding:8px 14px;border-radius:999px">{label}</div>' if label else ""
    return f'<div style="position:relative;flex:1;height:{h}px;border-radius:18px;background:url({IMG}/{src}) {pos}/cover">{lab}</div>'


def bullets(items, color="#3F3F3F", size=27, dot=DARK):
    return '<div style="display:flex;flex-direction:column;gap:14px">' + "".join(
        f'<div style="display:flex;gap:18px;align-items:flex-start"><div style="flex:0 0 12px;height:12px;margin-top:13px;background:{dot};border-radius:3px"></div><div style="font-size:{size}px;line-height:1.4;color:{color}">{t}</div></div>'
        for t in items) + '</div>'


def compare(rows, dark=False):
    line = "#3A3A3A" if dark else "#D6D2C8"
    head = "#A3A3A3" if dark else "#5E5E5E"
    fg = "#FFFFFF" if dark else DARK
    old = "#8A8A8A"
    out = (f'<div style="display:grid;grid-template-columns:1.25fr 1fr 1fr 0.9fr;font-size:20px;font-weight:700;letter-spacing:1.5px;color:{head};padding-bottom:12px;border-bottom:2px solid {line}">'
           f'<div>INDICADOR</div><div>ANTES</div><div>AGORA</div><div style="text-align:right">RESULTADO</div></div>')
    for k, a, b, r in rows:
        out += (f'<div style="display:grid;grid-template-columns:1.25fr 1fr 1fr 0.9fr;align-items:center;padding:20px 0;border-bottom:2px solid {line}">'
                f'<div style="font-size:25px;font-weight:600;color:{fg}">{k}</div>'
                f'<div style="font-size:27px;color:{old}">{a}</div>'
                f'<div style="{HG};font-size:32px;font-weight:700;color:{fg}">{b}</div>'
                f'<div style="text-align:right"><span style="display:inline-block;background:{YEL};color:{DARK};{HG};font-weight:700;font-size:30px;padding:6px 14px;border-radius:10px">{r}</span></div></div>')
    return f'<div style="display:flex;flex-direction:column">{out}</div>'


# 01 capa
page(1, "dark", f'''
<div style="flex:1;display:flex;flex-direction:column;justify-content:flex-end;gap:30px">
<div style="display:flex;align-items:center;gap:22px">{kicker("CASE DE CLIENTE")}<img src="{IMG}/logo-moldemaq.png" style="height:70px;mix-blend-mode:screen"></div>
<h1 style="margin:0;{HG};font-weight:700;font-size:92px;line-height:1.02;letter-spacing:-2px">1 ano de Lean na montagem: <span style="color:{YEL}">+52% de capacidade</span></h1>
<p style="margin:0;font-size:33px;line-height:1.4;color:#D8D8D8">Como a Moldemaq reorganizou o fluxo, padronizou as linhas e implantou o sistema puxado.</p>
</div>''', bgimg=f"{IMG}/equipe.jpg")

# 02 ponto de partida
page(2, "light", f'''
<div style="display:flex;flex-direction:column;gap:30px">
{kicker("DE ONDE PARTIMOS", DARK, YEL)}
<h2 style="margin:0;{HG};font-weight:700;font-size:66px;line-height:1.05;letter-spacing:-1px">A montagem funcionava, mas sem fluxo</h2>
<div style="display:flex">{photo("motor-antes.png", 400, "ANTES · MONTAGEM DE MOTOR")}</div>
{bullets(["Sem previsão de quantidade a montar por dia",
          "Sem padronização do trabalho",
          "Movimentações desnecessárias de pessoas e peças",
          "Separação de um carrinho com todos os componentes de cada máquina"])}
</div>''')

# 03 MFV
page(3, "dark", f'''
<div style="display:flex;flex-direction:column;gap:30px">
{kicker("PRIMEIRO PASSO · MFV")}
<h2 style="margin:0;{HG};font-weight:700;font-size:66px;line-height:1.05;letter-spacing:-1px">Enxergar o fluxo antes de mexer nele</h2>
<div style="display:flex;gap:18px">{photo("mfv2.jpg", 430)}{photo("mfv.png", 430, pos="center 30%")}</div>
<p style="margin:0;font-size:29px;line-height:1.45;color:#E2E2E2">O mapa do fluxo de valor da família de transportadores foi feito <b style="color:#FFFFFF">com quem executa o processo</b>, no papel e na parede.</p>
<p style="margin:0;font-size:29px;line-height:1.45;color:#E2E2E2">As perdas viraram evidência, e o mapa virou uma carteira de projetos em sequência.</p>
</div>''')

# 04 linha de motor
page(4, "light", f'''
<div style="display:flex;flex-direction:column;gap:28px">
{kicker("PROJETO 1 · LINHA DE MOTOR", DARK, YEL)}
<h2 style="margin:0;{HG};font-weight:700;font-size:62px;line-height:1.05;letter-spacing:-1px">De área de montagem a linha padronizada</h2>
<div style="display:flex;gap:18px">{photo("motor-antes.png", 330, "ANTES")}{photo("motor-agora.png", 330, "AGORA", YEL, DARK)}</div>
{compare([("Tempo de montagem", "130 min", "90 min", "&#8722;30,8%"),
          ("Área utilizada", "47 m²", "28 m²", "&#8722;40,4%"),
          ("Produção por dia", "sem plano", "4/dia", "planejada")])}
</div>''')

# 05 linha TM
page(5, "light", f'''
<div style="display:flex;flex-direction:column;gap:28px">
{kicker("PROJETO 2 · MONTAGEM FINAL TM", DARK, YEL)}
<h2 style="margin:0;{HG};font-weight:700;font-size:62px;line-height:1.05;letter-spacing:-1px">A montagem final virou linha</h2>
<div style="display:flex;gap:18px">{photo("tm-antes.png", 330, "ANTES")}{photo("tm-agora.png", 330, "AGORA", YEL, DARK)}</div>
{compare([("Tempo de montagem", "1.201 min", "1.056 min", "&#8722;12,1%"),
          ("Área utilizada", "208 m²", "143 m²", "&#8722;31,3%"),
          ("Produção por dia", "sem plano", "3/dia", "planejada")])}
</div>''')

# 06 sistema puxado
cols3 = "".join(
    f'<div style="flex:1;display:flex;flex-direction:column;gap:14px"><div style="height:330px;border-radius:18px;background:url({IMG}/{s}) center/cover"></div>'
    f'<div style="{HG};font-weight:700;font-size:30px;color:#FFFFFF">{t}</div><div style="font-size:22px;line-height:1.4;color:#C9C9C9">{d}</div></div>'
    for s, t, d in [("kanban.jpg", "Kanban", "Cartões dizem o que produzir e quando."),
                    ("supermercado.jpg", "Supermercado", "Itens identificados e posicionados para o consumo."),
                    ("abast1.png", "Rotas", "Duas rotas por dia abastecem as linhas de TM e de motor.")])
page(6, "dark", f'''
<div style="display:flex;flex-direction:column;gap:30px">
{kicker("SISTEMA PUXADO")}
<h2 style="margin:0;{HG};font-weight:700;font-size:62px;line-height:1.05;letter-spacing:-1px">Repor só o que <span style="color:{YEL}">foi consumido</span></h2>
<div style="display:flex;gap:18px">{cols3}</div>
<div style="border:2px solid #3A3A3A;border-radius:18px;padding:22px 26px;font-size:24px;line-height:1.45;color:#E2E2E2"><b style="color:{YEL}">Antes:</b> 2 a 3 separações por dia, com um carrinho por máquina. <b style="color:{YEL}">Agora:</b> o carrinho leva só os Kanbans que acabaram.</div>
</div>''')

# 07 resultado
big = "".join(
    f'<div style="background:#FFFFFF;border-radius:20px;padding:30px 34px;display:flex;align-items:center;gap:30px">'
    f'<div style="flex:0 0 330px;{HG};font-weight:700;font-size:84px;line-height:1;letter-spacing:-2px;color:{DARK}">{a}</div>'
    f'<div style="display:flex;flex-direction:column;gap:6px"><div style="{HG};font-weight:700;font-size:30px;color:{DARK}">{b}</div><div style="font-size:24px;line-height:1.4;color:#3F3F3F">{c}</div></div></div>'
    for a, b, c in [("+52,3%", "Capacidade produtiva", "de 520 para 792 máquinas por ano"),
                    ("+39,5%", "Produtividade", "de 47,3 para 66 máquinas por operador por ano"),
                    ("+1", "Posto de montagem", "a equipe da linha passou de 11 para 12 pessoas")])
page(7, "yellow", f'''
<div style="display:flex;flex-direction:column;gap:24px">
{kicker("O RESULTADO", DARK, YEL)}
<h2 style="margin:0;{HG};font-weight:700;font-size:66px;line-height:1.05;letter-spacing:-1px">Mais máquinas com praticamente a mesma equipe</h2>
<div style="display:flex;flex-direction:column;gap:14px">{big}</div>
<div style="font-size:21px;line-height:1.45;color:#2E2E2E">Base: ritmo de produção realizado em julho/2026 (3,3 máquinas/dia, antes 2,17), anualizado.</div>
</div>''')

# 08 olhar Produlean
page(8, "dark", f'''
<div style="display:flex;flex-direction:column;gap:28px">
{kicker("O OLHAR DA PRODULEAN")}
<h2 style="margin:0;{HG};font-weight:700;font-size:60px;line-height:1.05;letter-spacing:-1px">Lean não é ferramenta isolada. <span style="color:{YEL}">É sistema e é gente.</span></h2>
<div style="display:flex;gap:18px">{photo("treinamento.jpg", 300, pos="center 60%")}{photo("gd.jpg", 300)}</div>
{bullets(["Treinamento Lean Thinking para toda a equipe e prática no gemba",
          "5S, programa Kaizen, gerenciamento diário e A3 conectados",
          "<b style='color:#FFFFFF'>18 projetos na carteira:</b> 10 realizados, 5 em andamento e 3 próximos",
          "Próximo ciclo: formar lideranças e dar autonomia à equipe"], color="#E2E2E2", size=26, dot=YEL)}
</div>''')

# 09 CTA
page(9, "yellow", f'''
<div style="display:flex;flex-direction:column;gap:36px">
<h2 style="margin:0;{HG};font-weight:700;font-size:86px;line-height:1.02;letter-spacing:-2px">Quanto da sua fábrica cabe em um mapa de fluxo?</h2>
<p style="margin:0;font-size:34px;line-height:1.4;color:{DARK}">A Produlean conduz a jornada Lean junto com a sua equipe: do mapeamento ao resultado <b>medido</b>.</p>
<div style="align-self:flex-start;background:{DARK};color:#FFFFFF;border-radius:999px;padding:26px 44px;font-size:34px;font-weight:700;display:flex;gap:18px;align-items:center">Chame no direct <span style="color:{YEL}">&#8594;</span></div>
<div style="font-size:26px;font-weight:600;color:{DARK}">Obrigado, equipe Moldemaq, pela parceria.</div>
</div>''', swipe=False)

with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
    pg = b.new_page(viewport={"width": W, "height": H})
    for i, html in enumerate(slides, 1):
        path = f"{BASE}/tmp{i}.html"
        open(path, "w").write(html)
        pg.goto("file://" + path)
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(400)
        ov = pg.evaluate("(()=>{const r=document.body.firstElementChild.lastElementChild;return r.scrollHeight})()")
        pg.screenshot(path=f"{OUT}/produlean-case-moldemaq-{i:02d}.png", clip={"x": 0, "y": 0, "width": W, "height": H})
        print(i, "altura", ov, "OVERFLOW" if ov > H else "")
    b.close()
