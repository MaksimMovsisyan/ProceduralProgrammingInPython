salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
k = 1 + increase
money_capital = 0
for i in range(1, months + 1):
    Debt = salary - spend #Тот минус, который должна покрывать подушка, чтобы жить без долгов
    money_capital += abs(Debt)
    Debt = 0
    spend *= k
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
