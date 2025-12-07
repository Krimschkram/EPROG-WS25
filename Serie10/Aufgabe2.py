# ihr müsst natürlich das Data.txt in eure Entwicklungsumgebung einbinden
from matplotlib import pyplot as plt

stats = {}
sum = 0

with open("data.txt") as file:
    for line in file:
        sum+=len(line)
        for char in line:

            if char not in stats:
                stats[char] = 1
                continue
            stats[char] += 1


list1 = list(stats.keys())
list2 = list(stats.values())

check = 0 # sind es 100%
for i in range(len(list2)):
    list2[i] = list2[i]/sum * 100
    check += list2[i]
print(check) # fast

print(len(list1))




labels = [] # für alle nicht sichtbaren elemente (Leerzeichen, zeilenumpruch, tab) ein Label hinzugefügt
for c in list1:
    if c == " ":
        labels.append("SPACE")
    elif c == "\n":
        labels.append("\\n")
    elif c == "\t":
        labels.append("\\t")
    else:
        labels.append(c)

# Plot

x_pos = range(len(labels))

plt.figure(figsize=(35, 8))   # viel breiter machen
plt.bar(x_pos, list2)
plt.xticks(x_pos, labels)   # an welcher pos welcher wert steht
plt.title("Häufigkeit der Zeichen in data.txt")
plt.xlabel("Zeichen")
plt.ylabel("Prozent")
plt.show()