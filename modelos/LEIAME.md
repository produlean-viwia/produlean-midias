# Modelo de carrossel Produlean

Modelo usado no primeiro carrossel (fim da escala 6x1, 26/11/2026).

- `carrossel-gerar-html.py`: gera um HTML por slide (1080×1350) com o visual da marca. Fundo grafite #282829, creme #F3F1EC ou amarelo #FFF212; títulos em Space Grotesk e texto em Inter; logo no topo, numeração 01/09, @produlean_oficial e "Arraste para o lado →" no rodapé.
- `carrossel-renderizar-png.py`: renderiza os HTMLs em PNG com Playwright e Chrome. As fontes vêm dos pacotes npm @fontsource/space-grotesk e @fontsource/inter.
- Logos em `../marca/`: `logo-produlean.png` para fundo claro ou amarelo, `logo-produlean-branco.png` (assinatura em branco) para fundo escuro e `logo-produlean-original-hd.png` como original.

Os caminhos dentro dos scripts eram do ambiente da primeira sessão: ajuste antes de reutilizar.
Para o LinkedIn, junte os PNGs num PDF e publique como documento.
