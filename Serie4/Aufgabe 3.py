# ein Teil der Menge M
M = {7*a + 11*b + 13*c for a in range(0,100) for b in range(0,100) for c in range(0,100)}
# alle Zahlen in M', für die n, n+1, ..., n+5 auch in M' sind
consecutive_six = {n for n in M if all((n + i) in M for i in range(7))}
n = min(consecutive_six)
print("", n-1)

# Kopiert aus dem Skript