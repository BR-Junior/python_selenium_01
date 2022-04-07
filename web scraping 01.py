#metodo de requisição (requests)
# Respostas de Satus (informação (1xx): Resposta sem conteudo, contem apenas informação sebre a comunicação.
# Seucesso (2xx): A mensagem chegou ao servidor e era válida.
# Redirecionamento (3xx): O recurso buscado está em outro servidor).
# Erro do cliente (4xx): A requisição possui algum erro.
# Erro de servidor (5xx): O servidor não pode atender á requisição.

# Como fazer requisição.
# passo 01: instalar e importa o modulo (requests)
# passo 02: usar o metodo (requests.get("url do site")).

import requests

response = requests.get('https://www.walissonsilva.com/')

print('Status code: ', response.status_code)
print('Header: ')
print(response.headers)

print('\n Content') 
print(response.content) # .content traz todo o conteudo html da pagina

