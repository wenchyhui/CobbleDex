from pathlib import Path
import json

TEMPLATE = Path("web/index_template.html").read_text(encoding="utf-8")

def export_html(cobblemons, out_path):
    html_items = ""
    for c in cobblemons:
        html_items += f"<div class='card'><h3>{c['name']}</h3><p>{c['description']}</p></div>\n"
    html = TEMPLATE.replace("{{ITEMS}}", html_items)
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    Path(out_path).write_text(html, encoding="utf-8")
