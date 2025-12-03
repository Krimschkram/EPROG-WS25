class mySet:
    def __init__(self, list):
        self.items = []
        for i in list:
            if self.items.__contains__(i):
                continue
            self.items.append(i)

    def __add__(self, other):
        return mySet(self.items + other.items)

    def __sub__(self, other):
        subtract = []
        for i in self.items:
            if i not in other.items:
                subtract.append(i)

        for i in other.items:
            if i not in self.items:
                subtract.append(i)

        return mySet(subtract)

    def __str__(self):
        return str(self.items)

    def add(self, a):
        if a not in self.items:
            self.items.append(a)


i = mySet([1,2,3,3,3,3,3])
i2 = mySet([3,5,6])
print(i)
print(i + i2)
print(i - i2)


