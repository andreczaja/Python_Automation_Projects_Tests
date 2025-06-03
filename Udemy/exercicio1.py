from datetime import datetime
from dateutil.relativedelta import relativedelta

lista_datas_parcela = []

valor_emprestimo = 1_000_000
data_inicial = datetime(2020,12,20)
delta = relativedelta(years=5)
data_final = data_inicial + delta

data_parcelas = []
data_parcela = data_inicial
while data_parcela <= data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

num_parcelas = len(data_parcelas)

indice = 1
for data in data_parcelas:
    print(f'Data da Parcela {indice}: {data.strftime("%d/%m/%Y")}')
    print(f'Valor da Parcela: {valor_emprestimo/num_parcelas:.2f}')
    indice += 1
