money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
k = 1 + increase #коэффициент на который надо умножать расходы
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
Budget = money_capital
months = 0
while True:
    Budget = Budget + salary - spend
    spend *= k
    if Budget >= 0:
        months += 1
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", months)
