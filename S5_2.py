names = ['Саша', 'Маша', 'Паша']
rates = [1000, 1500, 2000]
bonuses = ['5%', '10.25%', '15.5%']

bonus_dict = {name: rate * (1 + float(bonus[:-1]) / 100) for name, rate, bonus in zip(names, rates, bonuses)}
print(bonus_dict)