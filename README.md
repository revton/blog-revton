# Blog

## Escrever Conteúdo

Escreva o artigo usando Markdown. Salve o arquivo na pasta `content`.

## Publicar no Github Pages

Usando o Pelican para transformar o conteúdo em páginas estáticas.

```bash
pelican content -o output -s pelicanconf.py
```

Este comando irá processar os arquivos em content, gerando o site estático em output.

Utilize o `ghp-import` para preparar a branch `gh-pages` com seu conteúdo estático.

```bash
ghp-import output -b gh-pages
```

Isso irá importar o conteúdo da pasta `output` para a branch `gh-pages`.

Envie as alterações para o GitHub, atualizando a branch gh-pages.

```bash
git push origin gh-pages
```