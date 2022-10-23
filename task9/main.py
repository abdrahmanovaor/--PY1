salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
month = 0
need_money = 0  # количество денег, чтобы прожить 10 ме
for month in range (0, 10):
    a = spend - salary
    spend = spend * 1.03
    need_money = need_money + a
    month += 1

print(round(need_money))
