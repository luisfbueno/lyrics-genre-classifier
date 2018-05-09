Este projeto contém os seguintes repositórios:

Modelo: contém um arquivo do Jupyter Notebook explicando o desenvolvimento do modelo, assim como os datasets utilizados
Form: contém o formulário web para envio da letra da música ao servidor
Servidor: contém o servidor web feito em Flask, assim como o arquivo do modelo utilizado por ele

Para executar:
- Na pasta Servidor, executar: python3.x main.py
- Abrir o arquivo index.html na pasta Form e enviar as letras de música

Observação: o form envia as requisições para o endereço 'http://127.0.0.1:5000/'. Caso o endereço do servidor seja diferente,
alterar a variável url_destino na linha 6 do arquivo Form/js/main.js
