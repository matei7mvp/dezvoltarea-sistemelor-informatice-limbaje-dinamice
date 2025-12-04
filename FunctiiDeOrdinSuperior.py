def inmultire2(x):
    return x * 2

def impartire2(x):
    return x / 2

def rezultat(operatie, numar):
    print(operatie(numar))

rezultat(inmultire2, 100)
rezultat(impartire2, 200)


def numar(baza):
    def putere(exponent):
        return baza ** exponent
    return putere

print(numar(2)(10))

x = numar(2)
print(x(10))


def valori():
    return 1,2,3

print(valori()[1])
