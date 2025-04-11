import os
import time
import datetime
import calendar

print("Diretório atual:", os.getcwd())
print("Data e hora atuais:", datetime.datetime.now())

hoje = datetime.date.today()
print("Calendário do mês atual:")
print(calendar.month(hoje.year, hoje.month))

print("Pausando por 3 segundos...")
time.sleep(3)
print("Fim da pausa.")