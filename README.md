# Lyrics Genre Classifier

Projeto de uma página web que faz uma requisição para um servidor Python feito com o framework Flask, para classificar uma letra de música em quatro gêneros possíveis: Sertanejo, Bossa Nova, Funk e Gospel. O modelo 

## Estrutura 

Este projeto contém os seguintes diretórios:

- Modelo: contém um arquivo do Jupyter Notebook explicando o desenvolvimento do modelo, assim como os datasets utilizados;
- Form: contém o formulário web para envio da letra da música ao servidor;
- Servidor: contém o servidor web feito em Flask, assim como o arquivo do modelo utilizado por ele.

## Executando

- Na pasta Servidor, executar: ```python3.x main.py```
- Abrir o arquivo index.html na pasta Form e enviar as letras de música

Obs: o form envia as requisições para o endereço 'http://127.0.0.1:5000/'. Caso o endereço do servidor seja diferente,
alterar a variável url_destino na linha 6 do arquivo Form/js/main.js
