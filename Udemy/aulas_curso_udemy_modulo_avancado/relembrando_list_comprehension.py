produtos = [
    {'nome':'café', 'preco':7.50},
    {'nome':'agua', 'preco':3.00},
    {'nome':'sanduíche', 'preco':5.50},
    {'nome':'queijo', 'preco':8.00},
    ]

novos_produtos = [
    {**p,'preco':p['preco'] * 1.50}
    if p['preco'] < 6.00 else {**p}
    for p in produtos
]


for p in novos_produtos:
    print(p)