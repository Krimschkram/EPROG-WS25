def probability_list(n, k):
    # n = Anzahl der Würfel
    # k = Die zu erwürfl Summe
    sides = [i + 1 for i in range(1, n + 1)] # seiten der Würfel
    print(sides)


    max_sum = sum(sides)

    # dp[s] = Anzahl der Möglichkeiten Summe s zu erreichen
    dp = [0] * (max_sum + 1)
    dp[0] = 1

    for m in sides:
        new_dp = [0] * (max_sum + 1)

        for s in range(max_sum + 1):

            if dp[s] > 0:

                for face in range(1, m + 1):
                    new_dp[s + face] += dp[s]
        dp = new_dp

    print(dp)
    total = 1
    for m in sides:
        total *= m # Anzahl an verschiedenen Würfelsummen
    return dp[k] / total if k <= max_sum else 0.0
print (probability_list (3,3))