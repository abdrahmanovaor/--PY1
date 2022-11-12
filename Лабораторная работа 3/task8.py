money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0

while True:
    delta = salary - spend
    for current_cap in range (1, month + 1):
        current_cap = (spend - salary)
        spend = spend * (increase + 1)
        month += current_cap



print(month)
