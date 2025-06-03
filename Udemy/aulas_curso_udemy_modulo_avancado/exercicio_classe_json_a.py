import json

CAMINHO_ARQUIVO = 'exercicio_classe_json.json'
with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    lista_json = json.load(arquivo)

# for indice in lista_json:
#     nome = indice.get('nome')
#     complexidade = indice.get('complexidade')
#     print(f'A linguagem {nome} é {complexidade}')
    
for indice in lista_json:
    print(indice.get('nome'))
    print(indice.get('complexidade'))
    


