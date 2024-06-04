#FIZBUZZ

X = 3
Y = 5
Z = X * Y

def FIZZBUZZ(i):
    if i % Z == 0:
        return '\nFIZZBUZZ'
    elif i % X == 0:
        return '\nFIZZ'
    elif i % Y == 0:
        return '\nBUZZ'
    else:
        return f'\n{i}'

for i in range(1, 101):
    print(FIZZBUZZ(i))