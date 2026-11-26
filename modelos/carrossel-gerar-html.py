import json, os, datetime
OUT = "/home/claude/carrossel/project"
W, H, N = 1080, 1350, 9
DARK, CREAM, YEL = "#282829", "#F3F1EC", "#FFF212"
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap">'
HG = "font-family:'Space Grotesk',sans-serif"

def page(name, title, theme, body, swipe=True):
    bg, fg, muted = {"dark": (DARK, "#FFFFFF", "#A3A3A3"), "light": (CREAM, DARK, "#5E5E5E"), "yellow": (YEL, DARK, "#3A3A3A")}[theme]
    logo = "/_blob/98f37d2b07e27787cd157502c59b3a7f" if theme == "dark" else "/_blob/31aca16e65bf7934a8dba322b3280b11"
    n = int(name[1:3]) if name.startswith("S") else 1
    foot = f'<div style="display:flex;justify-content:space-between;align-items:center;font-size:24px;font-weight:600;color:{muted}"><div>@produlean_oficial</div>' + (f'<div>Arraste para o lado &#8594;</div>' if swipe else '<div></div>') + '</div>'
    html = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>
body{{margin:0}}
</style>
</helmet>
<div style="width:{W}px;height:{H}px;box-sizing:border-box;padding:88px 88px 80px;background:{bg};color:{fg};font-family:Inter,sans-serif;display:flex;flex-direction:column;justify-content:space-between;gap:40px;overflow:hidden">
<div style="display:flex;justify-content:space-between;align-items:center">
<img src="{logo}" alt="Produlean – Gestão em Manufatura" style="height:66px;width:auto;display:block">
<div style="font-size:26px;font-weight:600;color:{muted}">{n:02d}/{N:02d}</div>
</div>
{body}
{foot}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{W},"height":{H}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''
    with open(os.path.join(OUT, name), "w") as f:
        f.write(html)

def kicker(t, color=YEL, text=DARK):
    return f'<div style="align-self:flex-start;background:{color};color:{text};font-weight:700;font-size:22px;letter-spacing:2px;padding:10px 18px;border-radius:999px">{t}</div>'

def rows(items, fg=DARK, muted="#3F3F3F", line="#D6D2C8"):
    out = []
    for i, (t, d) in enumerate(items):
        border = f"border-top:2px solid {line};" if i else ""
        out.append(f'<div style="{border}padding:24px 0;display:flex;flex-direction:column;gap:8px"><div style="{HG};font-weight:700;font-size:32px;color:{fg}">{t}</div><div style="font-size:25px;line-height:1.4;color:{muted}">{d}</div></div>')
    return '<div style="display:flex;flex-direction:column">' + "".join(out) + '</div>'

# 1 cover
page("Main.dc.html", "Capa – Fim da escala 6x1", "dark", f'''
<div style="display:flex;flex-direction:column;gap:40px">
{kicker("GUIA PRÁTICO · NOVAS REGRAS DE JORNADA")}
<div style="display:flex;align-items:center;gap:36px;{HG};font-weight:700;font-size:150px;line-height:1">
<span style="color:#6E6E6E;text-decoration:line-through;text-decoration-thickness:10px">6x1</span>
<svg width="110" height="70" viewBox="0 0 110 70" aria-hidden="true"><path d="M4 35 H96 M66 6 L100 35 L66 64" fill="none" stroke="{YEL}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></svg>
<span style="color:{YEL}">5x2</span>
</div>
<h1 style="margin:0;{HG};font-weight:700;font-size:84px;line-height:1.05;letter-spacing:-1px">O que sua empresa precisa fazer <span style="color:{YEL}">até 16/12</span></h1>
<p style="margin:0;font-size:32px;line-height:1.4;color:#C9C9C9">As novas regras, o impacto na folha, os casos especiais e um checklist de adequação.</p>
</div>''')

# 2 o que muda
cards = [("42h", "Jornada máxima semanal (hoje são 44h). Cai para <b>40h em 16/12/2027</b>."),
         ("2 folgas", "Remuneradas por semana, uma delas preferencialmente no domingo. Podem ser em dias seguidos."),
         ("R$ =", "Salário mantido. A redução de jornada não permite reduzir salário."),
         ("≤ 40h", "Quem já trabalha 40h ou menos, mas em seis dias, também passa a ter as duas folgas.")]
cb = "".join(f'<div style="background:#FFFFFF;border-radius:20px;padding:30px 34px;display:flex;align-items:center;gap:32px"><div style="flex:0 0 200px;{HG};font-weight:700;font-size:60px;line-height:1;color:{DARK}">{a}</div><div style="font-size:27px;line-height:1.4;color:#3F3F3F">{b}</div></div>' for a, b in cards)
page("S02-o-que-muda.dc.html", "O que muda em 16/12", "light", f'''
<div style="display:flex;flex-direction:column;gap:28px">
{kicker("O QUE MUDA EM 16/12/2026", DARK, YEL)}
<h2 style="margin:0;{HG};font-weight:700;font-size:64px;line-height:1.05;letter-spacing:-1px">As novas regras</h2>
<div style="display:flex;flex-direction:column;gap:18px;margin-top:8px">{cb}</div>
</div>''')

# 3 jornada diária
page("S03-jornada-diaria.dc.html", "Jornada diária", "light", f'''
<div style="display:flex;flex-direction:column;gap:28px">
{kicker("E A JORNADA DIÁRIA?", DARK, YEL)}
<div style="{HG};font-weight:700;font-size:280px;line-height:0.9;letter-spacing:-6px;color:{DARK}">8h24</div>
<p style="margin:0;font-size:38px;line-height:1.35;color:{DARK}">por dia, em cinco dias, é o limite para empresas <b>sem acordo ou convenção coletiva</b> sobre o tema.</p>
<p style="margin:0;font-size:32px;line-height:1.4;color:#3F3F3F">Acima de 8h24, o excedente é hora extra.</p>
<div style="background:{DARK};color:#FFFFFF;border-radius:20px;padding:30px 34px;display:flex;gap:24px;align-items:flex-start">
<svg width="44" height="44" viewBox="0 0 24 24" aria-hidden="true" style="flex:0 0 44px"><path d="M12 3 L22 20 H2 Z M12 10 V14 M12 17 V17.5" fill="none" stroke="{YEL}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
<div style="font-size:26px;line-height:1.4">Essa regra vem de uma <b style="color:{YEL}">decisão liminar do STF</b>, ainda pendente de julgamento no Plenário. Vale acompanhar.</div>
</div>
</div>''')

# 4 folha
bl = [("Horas extras e adicional noturno", "também ficam mais caros, porque partem do novo valor da hora."),
      ("Não é reajuste salarial", "o salário mensal continua o mesmo; muda só o cálculo da hora."),
      ("DSR e faltas", "as duas folgas juntas continuam valendo um dia de salário."),
      ("Pisos salariais", "das categorias continuam preservados.")]
blh = "".join(f'<div style="display:flex;gap:20px;align-items:flex-start"><div style="flex:0 0 14px;height:14px;margin-top:12px;background:{YEL};border-radius:3px"></div><div style="font-size:27px;line-height:1.4;color:#D4D4D4"><b style="color:#FFFFFF">{a}:</b> {b}</div></div>' for a, b in bl)
page("S04-impacto-folha.dc.html", "Impacto na folha", "dark", f'''
<div style="display:flex;flex-direction:column;gap:30px">
{kicker("IMPACTO NA FOLHA")}
<h2 style="margin:0;{HG};font-weight:700;font-size:72px;line-height:1.05;letter-spacing:-1px">A hora trabalhada fica mais cara</h2>
<div style="display:flex;gap:20px">
<div style="flex:1;border:2px solid #3A3A3A;border-radius:20px;padding:28px 32px;display:flex;flex-direction:column;gap:10px"><div style="font-size:24px;color:#A3A3A3;font-weight:600">DIVISOR DOS MENSALISTAS</div><div style="{HG};font-weight:700;font-size:64px;line-height:1"><span style="color:#8A8A8A">220</span> <span style="color:{YEL}">&#8594; 210</span></div></div>
<div style="flex:1;border:2px solid #3A3A3A;border-radius:20px;padding:28px 32px;display:flex;flex-direction:column;gap:10px"><div style="font-size:24px;color:#A3A3A3;font-weight:600">EX.: SALÁRIO DE R$ 3.000</div><div style="{HG};font-weight:700;font-size:44px;line-height:1.15"><span style="color:#8A8A8A">R$ 13,64/h</span><br><span style="color:{YEL}">&#8594; R$ 14,29/h</span></div></div>
</div>
<div style="display:flex;flex-direction:column;gap:20px">{blh}</div>
</div>''')

# 5 casos 1
page("S05-casos-especiais-1.dc.html", "Casos especiais 1", "light", f'''
<div style="display:flex;flex-direction:column;gap:20px">
{kicker("CASOS ESPECIAIS · 1/2", DARK, YEL)}
<h2 style="margin:0;{HG};font-weight:700;font-size:64px;line-height:1.05;letter-spacing:-1px">Algum destes casos?</h2>
{rows([("Escala 12x36", "Continua permitida, mas a média mensal de horas semanais deve respeitar o novo limite. O excedente vira folga ou hora extra, conforme acordo ou convenção."),
       ("Turnos ininterruptos de revezamento", "Seguem com jornada de 6h, salvo negociação coletiva, respeitando a média semanal e as duas folgas."),
       ("Banco de horas", "O saldo acumulado até 15/12/2026 segue as regras do acordo que o criou."),
       ("Horistas, diaristas, tarefeiros e comissionistas", "O valor da hora (ou da unidade) é ajustado para manter a remuneração mensal, pela média dos 12 meses anteriores a 16/12/2026.")])}
</div>''')

# 6 casos 2
page("S06-casos-especiais-2.dc.html", "Casos especiais 2", "light", f'''
<div style="display:flex;flex-direction:column;gap:20px">
{kicker("CASOS ESPECIAIS · 2/2", DARK, YEL)}
<h2 style="margin:0;{HG};font-weight:700;font-size:64px;line-height:1.05;letter-spacing:-1px">Acordos e exceções</h2>
{rows([("Convenção ou acordo coletivo", "Cláusulas com jornada acima do novo limite ou com menos de duas folgas deixam de valer em 16/12. As demais seguem válidas e podem ser renegociadas."),
       ("Trabalho na segunda folga", "Só em situação excepcional, com outra folga no mesmo mês e pagamento como hora extra. Não autoriza manter a 6x1."),
       ("Compensação por acordo coletivo", "É possível, desde que garanta a média de duas folgas por semana no mês e pelo menos uma folga a cada seis dias de trabalho."),
       ("Jornadas especiais", "Saúde, jornalistas, petroleiros e outras: o Ministério do Trabalho ainda vai publicar normas específicas.")])}
</div>''')

# 7 checklist
steps = ["Revisar as escalas e eliminar a 6x1", "Definir a nova jornada diária", "Consultar o sindicato sobre convenção ou acordo coletivo",
         "Ajustar o controle de ponto", "Comunicar os empregados sobre os novos horários", "Enviar à contabilidade a nova jornada, horário e escala de cada um"]
sh = "".join(f'<div style="display:flex;gap:24px;align-items:center;background:#FFFFFF;border-radius:16px;padding:18px 28px"><svg width="40" height="40" viewBox="0 0 24 24" aria-hidden="true" style="flex:0 0 40px"><rect x="2" y="2" width="20" height="20" rx="5" fill="{YEL}"/><path d="M7 12.5 L10.5 16 L17 8.5" fill="none" stroke="{DARK}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg><div style="font-size:28px;line-height:1.35;color:{DARK}"><b>{i+1}.</b> {s}</div></div>' for i, s in enumerate(steps))
page("S07-checklist.dc.html", "Checklist até 16/12", "light", f'''
<div style="display:flex;flex-direction:column;gap:24px">
{kicker("CHECKLIST ATÉ 16/12", DARK, YEL)}
<h2 style="margin:0;{HG};font-weight:700;font-size:64px;line-height:1.05;letter-spacing:-1px">6 passos para se adequar</h2>
<div style="display:flex;flex-direction:column;gap:12px">{sh}</div>
<div style="border:2px solid {DARK};border-radius:16px;padding:22px 28px;font-size:25px;line-height:1.4;color:{DARK}"><b>Fiscalização:</b> nos primeiros 90 dias haverá dupla visita. Na primeira, orienta; na segunda, se a irregularidade continuar, pode multar.</div>
</div>''')

# 8 olhar produlean
lv = ["Redesenhar escalas e turnos a partir da demanda real", "Medir o OEE e atacar paradas, microparadas e perdas de velocidade",
      "Balancear linhas e padronizar o trabalho", "Kaizen para tirar do processo o que não agrega valor"]
lvh = "".join(f'<div style="display:flex;gap:20px;align-items:flex-start"><div style="flex:0 0 14px;height:14px;margin-top:12px;background:{YEL};border-radius:3px"></div><div style="font-size:28px;line-height:1.4;color:#E2E2E2">{s}</div></div>' for s in lv)
page("S08-olhar-produlean.dc.html", "O olhar da Produlean", "dark", f'''
<div style="display:flex;flex-direction:column;gap:30px">
{kicker("O OLHAR DA PRODULEAN")}
<h2 style="margin:0;{HG};font-weight:700;font-size:64px;line-height:1.05;letter-spacing:-1px">Menos horas não precisa significar <span style="color:{YEL}">menos produção</span></h2>
<div style="display:flex;gap:20px">
<div style="flex:1;background:#1E1E1E;border-radius:20px;padding:28px 32px"><div style="{HG};font-weight:700;font-size:76px;line-height:1;color:{YEL}">&#8722;4,5%</div><div style="font-size:24px;line-height:1.4;color:#C9C9C9;margin-top:10px">de horas por colaborador com a jornada de 42h</div></div>
<div style="flex:1;background:#1E1E1E;border-radius:20px;padding:28px 32px"><div style="{HG};font-weight:700;font-size:76px;line-height:1;color:{YEL}">&#8722;9,1%</div><div style="font-size:24px;line-height:1.4;color:#C9C9C9;margin-top:10px">quando a jornada chegar a 40h, em dez/2027</div></div>
</div>
<p style="margin:0;font-size:29px;line-height:1.4;color:#FFFFFF">Essa capacidade pode ser recuperada eliminando desperdícios, e não só com contratação ou hora extra:</p>
<div style="display:flex;flex-direction:column;gap:16px">{lvh}</div>
</div>''')

# 9 CTA
page("S09-cta.dc.html", "Chamada final", "yellow", f'''
<div style="display:flex;flex-direction:column;gap:36px">
<h2 style="margin:0;{HG};font-weight:700;font-size:88px;line-height:1.02;letter-spacing:-2px">Sua empresa já sabe como vai reorganizar as escalas?</h2>
<p style="margin:0;font-size:34px;line-height:1.4;color:{DARK}">A Produlean ajuda a redesenhar turnos e recuperar capacidade <b>sem perder produtividade</b>.</p>
<div style="align-self:flex-start;background:{DARK};color:#FFFFFF;border-radius:999px;padding:26px 44px;font-size:34px;font-weight:700;display:flex;gap:18px;align-items:center">Chame no direct <span style="color:{YEL}">&#8594;</span></div>
<div style="font-size:28px;font-weight:600;color:{DARK}">Salve este post para consultar até 16/12.</div>
</div>
<div style="border-top:2px solid rgba(18,18,18,0.25);padding-top:24px;font-size:20px;line-height:1.45;color:#2E2E2E">Conteúdo informativo. Para questões de folha e contratos, consulte sua contabilidade ou assessoria jurídica. Base: EC nº 141/2026; Decreto nº 13.173/2026; Portaria MTE nº 2.041/2026; liminar do STF nas ADIs 8041 e 8042 (pendente de referendo do Plenário). Informações atualizadas até 23/11/2026.</div>''', swipe=False)

files = ["Main.dc.html", "S02-o-que-muda.dc.html", "S03-jornada-diaria.dc.html", "S04-impacto-folha.dc.html",
         "S05-casos-especiais-1.dc.html", "S06-casos-especiais-2.dc.html", "S07-checklist.dc.html", "S08-olhar-produlean.dc.html", "S09-cta.dc.html"]
titles = ["01 Capa", "02 O que muda", "03 Jornada diária", "04 Impacto na folha", "05 Casos especiais 1", "06 Casos especiais 2", "07 Checklist", "08 Olhar Produlean", "09 Chamada final"]
boards = {}
for i, f in enumerate(files):
    boards[f] = {"x": (i % 5) * (W + 80), "y": (i // 5) * (H + 120), "w": W, "h": H, "title": titles[i]}
canvas = {"v": 3, "createdOnFiles": {"v": 1, "at": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")},
          "title": "Carrossel Instagram – Fim da escala 6x1 (Produlean)", "launch": {"view": "canvas"}, "pages": [],
          "boards": boards, "order": files, "notes": {}, "designSystems": []}
json.dump(canvas, open(os.path.join(OUT, "canvas.json"), "w"), ensure_ascii=False, indent=1)
print("ok")
