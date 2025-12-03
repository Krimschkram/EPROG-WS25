class Polynom:

    def __init__(self, koeffizenten):
        self.koeffizenten = koeffizenten
        self.grad = len(koeffizenten) - 1

    def __mul__(self, other):
        ret = [0 for _  in range(self.grad * other.grad + 1)]

        for i in range(self.grad + 1):
            for j in range(other.grad + 1):
                ret[i + j] += self.koeffizenten[i] * other.koeffizenten[j]

        return Polynom(ret)





n = Polynom([5,3,1])
m = Polynom([5,3,1])


print(n * m)