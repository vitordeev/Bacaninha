# Retomada rápida — Bacaninha

Leia CONTEXTO_PROJETO.md antes de continuar.

## Estado em 12/10/2026
Site pronto localmente e preparado para hospedagem. Usuário pediu SOMENTE preparar; não publicar até nova instrução. Provedor ainda não escolhido. Não há domínio comprado, conta GitHub conectada ou site publicado.

Fonte principal: dist/. Pacote atualizado: bacaninha-publicar.zip. Pasta pronta: publicacao/.
Instruções: DEPLOY.md. Visão geral: README.md.

Para regenerar pacote e validar:
python scripts/preparar_deploy.py

Para abrir prévia local:
python -m http.server 8080 --bind 127.0.0.1 --directory dist
Acessar http://localhost:8080. O servidor pode parar ao fechar a sessão.

Sem pagamentos, cadastros ou banco. Logo real em dist/assets/bacaninha-logo.png. Foto da Ísis usa bolo-isis-tv.png, com TV adicionada a pedido. Dez fotos integradas; cinco capturas tratadas. Preservar originais.

Não confundir site/ (cópia para tentativa anterior de Sites) com dist/ (fonte atual). Tentativas de publicação falharam por restrição de conexão. Arquivos de contexto e referência não entram no pacote publicado.

Para retomar: “Leia CONTEXTO_PROJETO.md e RETOMAR.md e continue de onde paramos.”
