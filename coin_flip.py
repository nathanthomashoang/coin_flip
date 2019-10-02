import random

def coin_flip(num):
    options = {'heads':0, 'tails':0}
    coin_sides = ('heads', 'tails')
    print('Random coin-flip results:\n')

    for n in range(num):
        result = random.choice(coin_sides)
        options[result] += 1
        print(result)

    print(f'\n# of Heads: {options["heads"]}')
    print(f'# of Tails: {options["tails"]}')
