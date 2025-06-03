# O que é JSON - JavaScript Object Notation
# JSON - JavaScript Object Notation (extensão .json)
# É uma estrutura de dados que permite a serialização
# de objetos em texto simples para facilitar a transmissão de
# dados através da rede, APIs web ou outros meios de comunicação.
# O JSON suporta os seguintes tipos de dados:
# Números: podem ser inteiros ou com ponto flutuante, como 42 ou 3.14
# Strings: são cadeias de caracteres, como "Olá, mundo!" ou "12345"
#   As strings devem ser envolvidas por aspas duplas
# Booleanos: são os valores verdadeiro (true) ou falso (false)
# Arrays: são listas ordenadas de valores, como [1, 2, 3] ou
#   ["Oi", "Olá", "Bom dia"]
# Objetos: são conjuntos de pares chave/valor -> {"nome": "João", "idade": 30}
# null: é um valor especial que representa ausência de valor
#
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null

import json
import os

os.system('cls')


teste = os.path.basename(__file__)
arquivo_json = os.path.abspath(__file__).replace(os.path.basename(__file__),'aula12.json')

# print('oi')
with open(arquivo_json,'r') as arquivo:
    arquivo = json.load(arquivo)
    # print(arquivo)
    for chave, valor in arquivo.items():
        print(chave, valor, sep='\n\t')


# print(filme['year'] + 10)

# print(json.dumps(filme,ensure_ascii=False, indent=2))

