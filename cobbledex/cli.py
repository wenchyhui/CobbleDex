import argparse
from .generator import CobbleGenerator
from .exporter import export_html

def main():
    parser = argparse.ArgumentParser(prog="cobbledex")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("list", help="listar cobblemons")
    gen = sub.add_parser("generate", help="gerar cobblemon aleatório")
    gen.add_argument("--name", type=str, help="nome (opcional)")
    gen.add_argument("--export", type=str, help="caminho para exportar HTML")

    args = parser.parse_args()
    g = CobbleGenerator("data/cobblemons.json")
    if args.cmd == "list":
        for c in g.list_all():
            print(f"{c['id']}: {c['name']} - {', '.join(c['types'])}")
    elif args.cmd == "generate":
        c = g.generate(name=args.name)
        print("Gerado:", c)
        if args.export:
            export_html([c], args.export)

if __name__ == "__main__":
    main()
