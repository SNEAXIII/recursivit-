## Exercice 1


def factorielleA(n):
    rez = 1
    for a in range(1, n + 1):
        rez *= a
    return rez


def factorielleB(n):
    if n == 0: return 1
    return factorielleB(n - 1) * n


print(factorielleA(6))
print(factorielleB(6))

## Exercice 2

#u1 = 58 et u2 = 96.4


def suiteU(n):
    if n == 0: return 10
    return suiteU(n - 1) * 0.8 + 50


print(suiteU(10))

## Exercice 3


def puissance(x, n):
    assert type(n) == int and n >= 0, "n entier positif !"
    if n == 0: return 1
    return x * puissance(x, n - 1)


def syracuse(nb_pos, nrepet):
    if nrepet == 0:
        return nb_pos
    if nb_pos % 2 == 0: nb_pos /= 2
    elif nb_pos % 2 == 1: nb_pos = nb_pos * 3 + 1
    return syracuse(nb_pos, nrepet - 1)


print(syracuse(33, 20))

## Exercice 4


def fiborecur(n):
    if n <= 1: return n
    return fiborecur(n - 1) + fiborecur(n - 2)


print(fiborecur(10))
# le serveur de replit n'est pas assez puissant...


def fibo(n):
    liste = [1, 1]
    for a in range(n):
        liste.append(liste[0] + liste[1]), liste.pop(0)
    print(liste[0])


print(fibo(10))

## Exercice 5


def serie(n, a, b):
    if n == 0:
        return a
    if n == 1:
        return b
    return 3 * serie(n - 1, a, b) + 2 * serie(n - 2, a, b) + 5


print(serie(2, 1, 3))

## Exercice 6


def syracuse2(nb_pos):
    while int(nb_pos) != 1:
        if nb_pos % 2 == 0: nb_pos /= 2
        elif nb_pos % 2 == 1: nb_pos = nb_pos * 3 + 1
        print(nb_pos)
        return syracuse2(nb_pos)


## Exercice 7


def appartient(v, t, i):
   
    if t[i] == v:
        return True
    if i == len(t) - 1:
        return False

    return appartient(v, t, i + 1)


t = [1, 2, 3, 4, 5, 6]
print(appartient(7, t, 2))

## Exercice 8


def binom(n, p):
    if p > n:
        return 0
    if p == n:
        return 1
    if p == 0:
        return 1
    return binom(n - 1, p) + binom(n - 1, p - 1)


print(binom(4, 2))

## Exercice 9

from turtle import forward, left, right, hideturtle, goto


#goto(-200,0)
def koch(n, l):
    if n == 0:
        forward(l)
    else:
        koch(n - 1, l / 3)
        left(60)
        koch(n - 1, l / 3)
        left(-120)
        koch(n - 1, l / 3)
        left(60)
        koch(n - 1, l / 3)


goto(-200, 0)
koch(5, 400)
