money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0
a = money_capital+salary
while a > 0:
    a = a - spend
    spend = spend * 1.05
    month = month + 1
# TODO Оформить решение

print(month)
