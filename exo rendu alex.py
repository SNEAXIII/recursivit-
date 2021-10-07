## Ex 8

def binom(n, p):
    if p > n: return 0
    if p == n: return 1
    if p == 0: return 1
    return binom(n - 1, p) + binom(n - 1, p - 1)

## Ex 9

from turtle import forward, left, hideturtle, speed, exitonclick

def koch(n, l):
    if n == 0: forward(l)
    else: koch(n - 1, l / 3), left(60), koch(n - 1, l / 3), left(-120), koch(n - 1, l / 3), left(60), koch(n - 1, l / 3)

speed(0), hideturtle(), koch(4, 400), exitonclick()
