import calendar

# print(calendar.calendar(2024))
nome_dia_semana_primero_mes, ultimo_dia_mes = calendar.monthrange(2024,10)

print(calendar.day_name[nome_dia_semana_primero_mes])
print(calendar.day_name[calendar.weekday(2022,12,ultimo_dia_mes)])

print(calendar.weekday(2022,12,ultimo_dia_mes))
print(ultimo_dia_mes)