# Bacaninha

<img src="src/assets/bacaninha-logo.png" alt="Logo da Bacaninha" width="220">

Site: [bacaninha.netlify.app](https://bacaninha.netlify.app)

Landing page responsiva para bolos, doces, salgados e buffets. Desenvolvida com HTML, CSS e JavaScript, sem framework, build obrigatório, cadastro, pagamento ou banco de dados. Os pedidos são encaminhados para WhatsApp.

## Visualizar

Na pasta do projeto, inicie o servidor:

```powershell
python -m http.server 8080 --bind 127.0.0.1 --directory src
```

Abra http://localhost:8080. Use Ctrl + F5 para renovar o cache.

## Estrutura

- `src/index.html`: página, conteúdo e contatos.
- `src/styles.css`: identidade visual, responsividade e enquadramento da logo.
- `src/catalogo.js`: categorias e sabores.
- `src/app.js`: interação por abas e ano automático.
- `src/assets/`: logo, fotografias e registros de tratamento.
- `src/_headers`: cabeçalhos para hospedagem compatível.

Logo real: `bacaninha-logo.png`. Foto da Ísis: `bolo-isis-tv.png`, com a TV adicionada a pedido. Cinco capturas foram tratadas com IA; originais preservados. Fontes usam Google Fonts com alternativas locais.

## Conteúdo e privacidade

Sem backend, credenciais, formulários ou ferramentas de rastreamento. Contatos: (11) 98762-1083, (11) 96833-0334 e Instagram @bacaniinhaa. Confirme contatos e sabores antes de divulgar. Não há preços, depoimentos ou condições comerciais inventadas.

Os testes de estrutura não substituem a revisão em navegador. Antes de divulgar, conferir desktop/celular, cabeçalhos, imagens e WhatsApp na hospedagem escolhida.
