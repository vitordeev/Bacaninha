# Preparação e deploy

Estado: preparado localmente; NÃO publicado. Nenhuma conta, compra, domínio ou hospedagem foi configurada nesta etapa.

## Arquitetura

```text
Navegador → hospedagem estática com HTTPS
               ├── index.html
               ├── styles.css
               ├── app.js
               ├── catalogo.js
               └── assets/
Links de contato → WhatsApp e Instagram
Fontes → Google Fonts, com fallback local
```

Nenhum servidor de aplicação, banco, API, variável de ambiente ou segredo é necessário. Funciona em domínio próprio, subdomínio ou subpasta: os caminhos locais são relativos.

## Gerar os arquivos

Execute `python scripts/preparar_deploy.py` na raiz do projeto. Ele recria exclusivamente `publicacao/` e atualiza `bacaninha-publicar.zip`. Não use a pasta inteira do projeto como saída publicada: referências, contexto, repositórios e arquivos de trabalho não fazem parte do site.

## Configuração genérica de hospedagem

| Campo | Valor |
| --- | --- |
| Tipo | Site estático HTML/CSS/JS |
| Build, se necessário | `python scripts/preparar_deploy.py` |
| Diretório de saída após esse comando | `publicacao` |
| Alternativa sem Python/build | `dist` |
| Página inicial | `index.html` |
| Variáveis e segredos | Nenhum |
| Roteamento SPA | Desnecessário |

Para upload manual, envie o ZIP ou o CONTEÚDO da pasta `publicacao/`, mantendo `index.html` na raiz do endereço publicado. FTP/cPanel: envie esses arquivos para a pasta pública indicada pelo provedor. Não envie o ZIP fechado como se fosse uma página; o provedor deve extrair os arquivos.

## GitHub

O código pode ficar em um repositório e alimentar a hospedagem escolhida. Nenhum repositório remoto está conectado aqui. `.gitignore` exclui a cópia `site/`, pacotes, saída gerada e arquivos de ambiente. Revise os arquivos antes de enviar: para manter apenas o necessário, envie `dist/`, `scripts/`, `README.md`, `DEPLOY.md` e `.gitignore`. Não é preciso enviar contexto ou referências pessoais. A pasta `.git` da raiz teve restrições de escrita nesta sessão; não presumir que ela está pronta. Crie uma cópia limpa ou configure o Git na sua máquina se necessário.

GitHub armazena o código; a publicação pode ocorrer em outra plataforma. Não configurar GitHub Pages automaticamente: suas regras restringem sites destinados principalmente a facilitar transações comerciais.

## Cabeçalhos e segurança

`_headers` declara CSP, nosniff, antiframe, política de referência e bloqueio de câmera/microfone/geolocalização. Algumas hospedagens entendem esse arquivo, outras exigem configuração no painel ou servidor. Verifique os cabeçalhos realmente enviados. Não assuma que o arquivo é aplicado por qualquer provedor.

A CSP permite somente scripts locais e as origens de fontes usadas. Ao instalar recursos externos, atualizar a política de forma específica. Ative HTTPS no provedor. Não inserir chaves, senhas ou tokens nos arquivos públicos.

## Domínio

Um domínio não é obrigatório para testar a publicação: o provedor pode fornecer um endereço próprio. Para usar `.com`, registrar um nome disponível em sua conta e conectar conforme as instruções DNS do provedor. Não inventar registros DNS: copiar os valores fornecidos pela hospedagem. Não há domínio comprado ou reservado.

## Verificação depois de publicar

1. Abrir a URL com HTTPS no computador e celular.
2. Confirmar logo e fotos, especialmente a TV na foto da Ísis.
3. Testar as três categorias e navegação com teclado.
4. Testar os dois WhatsApps e o Instagram.
5. Conferir console, rede e cabeçalhos de segurança no navegador.
6. Confirmar contatos e disponibilidade dos produtos antes da divulgação.

## Atualizações e retorno

Editar em `dist/`, executar o script e enviar a nova saída. Guardar um ZIP anterior antes de substituí-lo se desejar rollback; ou usar o histórico de versões da hospedagem. Não foi configurado deploy automático, para preservar sua liberdade de escolher o provedor.
