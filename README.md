# CobbleDex

Pequeno projeto para Hacktoberfest: um catálogo simples de **Cobblemons** (criaturas inspiradas em mods type "Cobblemon").  
Propósito: prática de open source — issues fáceis, documentação, e código claro.

## O que faz
- Mantém um arquivo `data/cobblemons.json` com cobblemons (nome, tipo, descrição, stats).
- CLI para gerar uma ficha `cobblemon` aleatória.
- Exporta página HTML estática com o catálogo.

## Começando (rápido)
```bash
git clone https://github.com/wenchyhui/cobbledex.git
cd cobbledex
python -m venv .venv
source .venv/bin/activate   # ou .venv\Scripts\activate no Windows
pip install -r requirements.txt
python -m cobbledex.cli list
python -m cobbledex.cli generate --name "Pedregulho" --export web/catalog.html
