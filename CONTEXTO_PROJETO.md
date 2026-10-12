# Contexto do projeto Bacaninha

Atualizado em 11/10/2026. Conversa em português brasileiro.

## Objetivo e escopo confirmado
Landing page para a Bacaninha, loja de bolos, doces, salgados e buffets. NÃO haverá pagamentos, cadastro de clientes, login, banco de dados ou checkout. Catálogo público e contato pelo WhatsApp. Usuário quer execução direta, prévia local e publicação gratuita; perguntou por endereço .com e por GitHub.

## Estado atual
Página implementada em `dist/`, com HTML/CSS/JavaScript sem build. Catálogo por abas, galeria de seis bolos, galeria de quatro mesas/buffets, contatos e Instagram. Abas funcionam com mouse e teclado. Todas as dez fotos fornecidas foram integradas. Layout responsivo. A prévia foi servida em http://localhost:8080 e http://127.0.0.1:8080 com Python; o processo pode não persistir ao retomar.

## Preferências visuais e mudanças aprovadas
Usuário rejeitou os primeiros designs. Pediu algo tradicional, original, com cara de pequena confeitaria. Depois solicitou a logo real, redução de tamanho e ajuste de enquadramento. Paleta atual: laranja #ed6228, marrom #603523, texto escuro #301a0e, destaque #9e411f, fundo creme #fffaf3. Títulos Georgia, corpo DM Sans. Fotos inteiras com object-fit: contain. Não inventar depoimentos, preços, prazos, história, endereço ou condições do buffet. Não mudar a identidade sem necessidade. Usuário ainda pode querer refinamentos de design.

## Arquivos principais
- `dist/index.html`: estrutura, textos, imagens e contatos. CSS com query v=9 para invalidar cache.
- `dist/styles.css`: folha principal consolidada, seguida de ajuste de logo/cabeçalho. Evitar acumular muitas sobreposições; consolidar se editar novamente.
- `dist/catalogo.js`: 21 sabores de bolos, 13 docinhos e 8 salgados, transcritos das capturas. Ninho foi deduplicado.
- `dist/app.js`: abas acessíveis e ano automático; usa textContent.
- `dist/_headers`: cabeçalhos CSP, permissões, referrer, antiframe e nosniff para hospedagem compatível. A aplicação real desses cabeçalhos ainda deve ser verificada online.
- `dist/assets/`: imagens originais e tratadas.
- `dist/assets/TRATAMENTO.md`: registros da edição por IA e prompt das cinco capturas.
- `dist/assets/fotos.json`: mapeamento dos arquivos de referência para os originais copiados; não é a lista final de imagens usadas no HTML.
- `README.md`: instruções iniciais. Tem descrições antigas de logo e imagens que precisam atualizar se usado como documentação final.
- `Imagens de Referencia/`: arquivos fornecidos pelo usuário; preservar.
- `site/`: cópia para o fluxo de publicação Sites, com seu próprio Git e `.openai/hosting.json`. O usuário visualiza `dist/` da raiz. Toda alteração deve ser sincronizada para `site/dist/` antes de tentar publicar pelo Sites.
- `.openai/hosting.json`: identidade Sites também persistida na raiz.
- `bacaninha-publicar.zip`: pacote para upload direto em hospedagem. Criado antes da última conversa sobre GitHub; contém 16 arquivos e cerca de 14,7 MB. Regenerar após alterações.

## Logo
Arquivo do usuário: `Imagens de Referencia/Bacaninha_Logo.png`; cópia usada: `dist/assets/bacaninha-logo.png`. PNG RGBA 1254x1254, desenho branco com espaços transparentes. Usar arquivo real, sem recriar a marca. HTML usa `.brand-image` contendo img; CSS enquadra áreas transparentes com overflow hidden, proporção 1254/690, imagem top -46.38%. Largura final: 164 px desktop, 150 intermediário, 125 celular, 112 muito pequeno; rodapé 130/115 px. Conferir visualmente o recorte em futura QA. Não há logo tipográfica substituta no HTML atual.

## Fotografias
Cinco originais usadas sem tratamento: bolo infantil Ísis, bolo futebol, bolo Minha mãe é uma peça, buffet em evento lilás e mesa de café/frutas.
Cinco capturas Instagram tratadas com image_gen integrada: bolo-princesa-melhorada.png, bolo-salgados-melhorada.png, bolo-amarelo-melhorada.png, bolo-borboletas-melhorada.png e mesa-doces-salgados-melhorada.png. Interface removida e nitidez melhorada; resultados inspecionados visualmente. IA pode reconstruir pequenas texturas. Originais preservados.
Usuário pediu TV de volta na foto da Ísis. Foi criada `dist/assets/bolo-isis-tv.png`, adicionando TV desligada ao painel de madeira no fundo. Resultado inspecionado e usado tanto no destaque quanto na galeria. Original `bolo-infantil.jpeg` permanece intacto. Não voltar ao original sem esse pedido. Prompt registrado em TRATAMENTO.md.
Hero tem bolo da Ísis e foto de buffet, ambas img reais.

## Contatos e informação a confirmar
WhatsApps transcritos de captura antiga: (11) 98762-1083 e (11) 96833-0334. Links wa.me respectivos 5511987621083 e 5511968330334.
Instagram enviado pelo usuário: https://www.instagram.com/bacaniinhaa/ (usar esse). Uma captura antiga cita @bacaninha09; divergência não confirmada. Site usa link enviado.
Disponibilidade de sabores, contatos, cidade, valores e condições comerciais não foram confirmados diretamente. Não inventar.

## Publicação: estado e bloqueios reais
Site NÃO está publicado. Apenas localhost verificado com HTTP 200. Criação no Sites ocorreu numa primeira tentativa interrompida, mas foi recuperada e identidade persistida. Não criar outro Site.
ID existente: appgprj_6acb015445088191b871e2ed9f33f6e2
Slug: bacaninha-doces
URL esperada, NÃO publicada: https://bacaninha-doces.earthycorgi.chatgpt.site
Última consulta get_site: access_mode custom (owner-private), modos disponíveis custom/public, current_live_url null. Não mudar audiência só para deploy; acesso público precisa ser explicitamente pedido.
Tentativas de helper site-workflow com novas credenciais falharam no Git remoto por rede: Failed to connect to git.chatgpt-team.site:443. Não houve commit/push confirmado, archive validado nem versão salva/deploy. As credenciais são temporárias: obter novamente pelo conector no futuro; NUNCA guardar tokens em arquivos ou exibí-los.
Git da raiz tem restrição de escrita. `git init` na raiz falhou por Permission denied em .git/config. O subdiretório `site/.git` foi inicializado com sucesso e é usado pelo helper. Site source está untracked conforme última consulta. Não alterar políticas de segurança para contornar restrições.
`gh` não está instalado e não há ferramenta/conector GitHub disponível na sessão atual. Nenhuma conta GitHub autenticada, nenhum repositório GitHub criado ou enviado. Não afirmar que GitHub já está configurado.

## Conversa sobre domínio e hospedagem
Usuário quer grátis e perguntou por final .com. Explicado que registro/renovação .com tem custo; ofertas de primeiro ano grátis normalmente exigem hospedagem paga antecipadamente. Hostinger foi verificada: planos elegíveis a partir de Premium, 12 meses ou mais. Não afirmar que existe promoção grátis sem custo inicial sem verificar.
Cloudflare Pages tem hospedagem gratuita de assets estáticos, endereço pages.dev e upload direto ZIP. Usuário ainda não criou conta nem comprou domínio.
Última pergunta: dá para colocar no GitHub? Resposta: guardar código no GitHub e conectar ao Cloudflare Pages. GitHub Pages tem restrição para sites principalmente destinados a facilitar transações comerciais; não tratar ausência de checkout como prova de elegibilidade. Pergunta pendente: usuário já tem conta GitHub? Sem resposta até agora.
Fontes verificadas:
https://developers.cloudflare.com/pages/functions/pricing/
https://developers.cloudflare.com/pages/get-started/direct-upload/
https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
https://support.hostinger.com/pt/articles/1583407-como-eu-consigo-um-registro-de-dominio-gratis
Consultar regras e preços novamente se necessário.

## Verificação realizada e limitações
Sintaxe JS verificada com node --check. HTML analisado para IDs duplicados, arquivos locais e âncoras. HTTP 200 em prévia e imagens. Contrastes de pares centrais testados: texto claro/destaque 6,26; escuro/laranja 4,98; texto secundário/creme 5,70.
Não há browser-control ou preview tool disponível; visual do site não foi conferido em navegador automatizado. Fotos individuais foram vistas via view_image. Não dizer que houve teste visual completo ou auditoria de segurança.

## Próximos passos
1. Ler este contexto e inspecionar estado real dos arquivos, sem refazer a página.
2. Atender às mudanças pedidas mantendo logo, fotos e TV da Ísis.
3. Reabrir localhost se necessário: python -m http.server 8080 --bind 127.0.0.1 --directory dist.
4. Definir conta/hospedagem com o usuário; última opção discutida GitHub + Cloudflare Pages. Não pedir senhas/tokens em chat.
5. Sincronizar site/dist e regenerar ZIP antes de publicar a versão mais recente.
6. Confirmar resultado online real antes de entregar URL como publicada. Link esperado não comprova publicação.

## Atualização 12/10/2026 — preparação de deploy
Usuário pediu SOMENTE preparar, sem publicar. Criados DEPLOY.md, .gitignore e scripts/preparar_deploy.py; README atualizado. O script valida e gera publicacao/ e bacaninha-publicar.zip sem rede. Provedor ainda não escolhido. dist/ continua fonte principal. Nenhum deploy ou conta configurado.

## Encerramento salvo — 12/10/2026
Usuário vai fechar a sessão e pediu salvar tudo. Arquivos persistidos, RETOMAR.md atualizado, pacote regenerado e validado. Última entrega: preparação de deploy SEM publicação. Conteúdo de dist/ sincronizado com site/dist/. A prévia pode precisar ser reiniciada ao retomar.
