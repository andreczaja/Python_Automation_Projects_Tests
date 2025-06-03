from datetime import datetime
from dateutil.relativedelta import relativedelta

emprestimo = 1_000_000
data_inicio = '2024.10.19'

data_inicio_convert =  datetime.strptime(data_inicio, '%Y.%m.%d')
data_final_convert = data_inicio_convert + relativedelta(years=5)

print(data_inicio_convert)
print(data_final_convert)

data_parcelas = []
numero_parcela = 1
while data_inicio_convert < data_final_convert:
    data_parcelas.append(f'{numero_parcela},{data_inicio_convert}')
    numero_parcela += 1
    data_inicio_convert +=  relativedelta(months=1)

valor_parcelas = emprestimo/len(data_parcelas)

for parcela in data_parcelas:
    x, y = parcela.split(',')
    y_date_convert = datetime.strptime(y,'%Y-%m-%d %H:%M:%S')
    y_date_format = datetime.strftime(y_date_convert,'%d/%m/%Y')
    print(f'A parcela nº {x} será paga no dia {y_date_format}')
    print(f'No valor de {valor_parcelas:.0f}')


