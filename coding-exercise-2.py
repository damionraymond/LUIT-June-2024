income = 250_000
lowtaxland_rate = 0.05
ripoffland_rate = 0.43

lowtaxland_amount = (income * lowtaxland_rate)
ripoffland_amount = (income * ripoffland_rate)

print('Your income is',income, 'and you would pay',income * lowtaxland_rate, 'income tax in Lowtaxland or',income * ripoffland_rate, 'income tax in Ripoffland. You would save', ripoffland_amount-lowtaxland_amount, 'by paying taxes in Lowtaxland!')