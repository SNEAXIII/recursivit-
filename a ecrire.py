from math import sqrt


class Point:
    def __init__(self, x=0, y=0):
        self.abs = x
        self.ord = y


class triangle:
    def __init__(self, p1, p2, p3):
        self.A = p1
        self.B = p2
        self.C = p3

    def perimetre(self, a, b, c):
        return a + b + c

    def surface(self):
        a, b, c = self.distance_point(self.B, self.C), self.distance_point(self.A, self.C), self.distance_point(self.B, self.A)
        P = self.perimetre(a, b, c) / 2
        return sqrt(P * (P - a) * (P - b) * (P - c))

    def distance_point(self,p_1, p_2):
        return sqrt((p_2.abs - p_1.abs) ** 2 + (p_2.ord - p_1.ord) ** 2)


p1 = Point(40, 10)
p2 = Point(0, 0)
p3 = Point(6, 5)


tritri = triangle(p1, p2, p3)

print(tritri.surface())
