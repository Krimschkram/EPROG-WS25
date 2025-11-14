x = 4
def alpha(p):
    x = 6 # x = 4 wird ignoriert
    y = 0 + p # p = 10

    def beta(q):
        nonlocal y
        y += 1 # bezieht sich auf das in Alpha defineirte (wird 11, dann 25)
        y = y + q + p # erst 23, dann 37, p = 10, q = 2
        z = 1 # z bleibt 1

        def gamma():
            global x # nicht aus Alpha, x = 4, dann 7
            global z # existiert nicht
            nonlocal y #y aus beta
            y += 1 # erhöht, das y aus beta um 1, erst 24, dann 38
            z = 2 # wird nicht verwendet
            x += 3 # erst 7, dann 10
            w = 5 # wird nicht verwendet

        comp = [k*k for k in range(3)] # [0, 1, 4]
        gamma()
    for i in range(2): # zwei mal beta, mit 2 aufgerufen
        beta(2)
    for i in range(2):
        x+=i


alpha(10)