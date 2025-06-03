import calendar

ano = 2022
mes = 12

for week in calendar.monthcalendar(ano,mes):
    for day in week:
        if day == 0:
            continue
        else:
            dia_da_semana = calendar.weekday(ano,mes,day)
            print(day, ":", calendar.day_name[dia_da_semana])
