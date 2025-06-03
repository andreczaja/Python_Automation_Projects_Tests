from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

data = '2024-10-19'
fmt = '%Y-%m-%d'


data_convertida = datetime.strptime(data,fmt)
# é necessário antes transformar em data a string especificando o formato que ela está para
# depois passar para o formato requerido, no caso, '%d/%m/%Y'
print(data_convertida)


delta = timedelta(days=10)
print(data_convertida + delta)

relative = relativedelta(days=15)
print(data_convertida + relative)

# print(datetime.strftime(data_formatada + delta,'%d/%m/%Y'))
data_formatada = datetime.strftime(data_convertida,'%d/%m/%Y')
print(data_formatada)
