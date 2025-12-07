from matplotlib import pyplot as plt


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

    def __call__(self, x):
        erg = 0
        for i in range(self.grad + 1):
            erg += self.koeffizenten[i] * x**i
        return erg

    def plot(self, x_1, x_2, aufloesung=200):
        x = [x_1 + (x_2 - x_1) * i / aufloesung for i in range(aufloesung + 1)] # Auf so eine Erklärung vorbereiten
        y = [self.__call__(xi) for xi in x] #ursprüngliche Klasse mit __call__ erweitert, erleichtert, das "aufrufen" der Funktion
        plt.plot(x, y)
        plt.xlabel("x")
        plt.ylabel("P(x)")
        plt.show()



f = Polynom([4,3,2])

f.plot(0,10, 200)