import math


class myFunction:
    def __init__(self, a,b,func):
        self.a = a
        self.b = b
        self.func = func

    def __call__(self, x):
        if self.a <= x <= self.b:
            return self.func(x)
        raise ValueError("Außerhalb vom Definitionbereich")


funct = myFunction(1,100, math.sqrt)
print(funct(101))