"""Valida e empacota a landing page; não faz deploy nem acessa a rede."""
from pathlib import Path
from html.parser import HTMLParser
import re
import shutil
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "dist"
OUTPUT = ROOT / "publicacao"
ZIP = ROOT / "bacaninha-publicar.zip"

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.anchors = []
        self.assets = set()
    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if "id" in values:
            identifier = values["id"]
            if identifier in self.ids:
                raise ValueError(f"ID duplicado: {identifier}")
            self.ids.add(identifier)
        href = values.get("href", "")
        if href.startswith("#"):
            self.anchors.append(href[1:])
        if values.get("target") == "_blank":
            if not {"noopener", "noreferrer"}.issubset(set(values.get("rel", "").split())):
                raise ValueError("Link externo sem proteção de abertura")
        if tag == "img" and not values.get("alt"):
            raise ValueError("Imagem sem texto alternativo")
        if tag in ("img", "script", "link"):
            asset = values.get("src") or values.get("href")
            if asset and not asset.startswith(("http:", "https:", "//", "data:")):
                self.assets.add(asset.split("?")[0].split("#")[0])

def prepare():
    page = Page()
    page.feed((SOURCE / "index.html").read_text(encoding="utf-8-sig"))
    missing = set(page.anchors) - page.ids
    if missing:
        raise ValueError(f"Âncoras inexistentes: {missing}")
    assets = {"index.html", "_headers"} | page.assets
    # Dependências locais declaradas pelas folhas de estilo.
    for name in list(assets):
        if name.endswith(".css"):
            css = (SOURCE / name).read_text(encoding="utf-8-sig")
            for url in re.findall(r"url\(['\"]?([^)'\"]+)['\"]?\)", css):
                if not url.startswith(("https:", "http:", "data:")):
                    assets.add((Path(name).parent / url).as_posix())
    for asset in assets:
        path = (SOURCE / asset).resolve()
        if not path.is_relative_to(SOURCE.resolve()) or not path.is_file():
            raise ValueError(f"Arquivo local inválido: {asset}")
        if path.stat().st_size > 25 * 1024 * 1024:
            raise ValueError(f"Arquivo acima de 25 MiB: {asset}")
    node = shutil.which("node")
    if node:
        for asset in sorted(assets):
            if asset.endswith(".js"):
                subprocess.run([node, "--check", str(SOURCE / asset)], check=True)
    else:
        print("Node não encontrado: verificação de sintaxe JS não executada.")
    # Nunca apagar uma pasta calculada sem confirmar seu destino.
    if OUTPUT.resolve() != ROOT.resolve() / "publicacao":
        raise ValueError("Destino inesperado")
    OUTPUT.mkdir(exist_ok=True)
    # Preservar diretórios sincronizados pelo OneDrive e remover só arquivos obsoletos.
    for existing in OUTPUT.rglob("*"):
        if existing.is_file() and existing.relative_to(OUTPUT).as_posix() not in assets:
            existing.unlink()
    for asset in sorted(assets):
        target = OUTPUT / asset
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(SOURCE / asset, target)
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as archive:
        for asset in sorted(assets):
            archive.write(OUTPUT / asset, asset)
    print(f"Pronto: {len(assets)} arquivos, {ZIP.stat().st_size / 1024**2:.1f} MiB")
    print("Pasta de publicação: publicacao/")
    print("Pacote: bacaninha-publicar.zip")
    print("Nenhum arquivo enviado; nenhuma publicação realizada.")

if __name__ == "__main__":
    prepare()
