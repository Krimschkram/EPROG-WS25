from fractions import Fraction

def _round_fraction_to_int(fr: Fraction) -> int:
    """
    Runden von Fraction auf die nächste ganze Zahl (ties-to-even),
    rein mit Integer-Arithmetik.
    """
    n, d = fr.numerator, fr.denominator
    q, r = divmod(n, d)          # fr = q + r/d, 0 <= r < d
    twice_r = 2 * r

    if twice_r < d:
        return q
    if twice_r > d:
        return q + 1
    # exact tie: r/d = 0.5 -> round to even
    return q if (q % 2 == 0) else (q + 1)

def float_to_floating_point(x, beta=2, t=4, L=-4, U=4):
    """
    Liefert die nächste Zahl x~ in F(2,4,-4,4) zu x.
    Intern nur Integer-Arithmetik via Fraction.
    Rückgabe: Fraction (exakter Wert der Gleitkommazahl).
    """
    x = Fraction(x)  # falls x float ist: exakt als rationale Zahl des float-Werts

    if x == 0:
        return Fraction(0)

    sign = -1 if x < 0 else 1
    x = abs(x)

    two_t = 1 << t  # 2^t

    # --- Normalisierungs-Exponenten e finden: mant in [1/2, 1) ---
    e = 0
    mant = x
    while mant >= 1:
        mant /= 2
        e += 1
    while mant < Fraction(1, 2):
        mant *= 2
        e -= 1

    # --- Falls Exponent zu groß -> clamp auf Maximum ---
    if e > U:
        k_max = two_t - 1  # 0.1111_2 => 15
        return sign * Fraction(k_max, two_t) * (2 ** U)

    # --- Falls Exponent zu klein -> subnormal behandeln (Exponent = L) ---
    if e < L:
        # x~ = (k/2^t)*2^L  =>  k ≈ x * 2^(t-L)
        scaled = x * (2 ** (t - L))
        k = _round_fraction_to_int(scaled)

        # subnormal: k in [0, 2^t - 1]
        if k < 0:
            k = 0
        if k > two_t - 1:
            k = two_t - 1

        return sign * Fraction(k, two_t) * (2 ** L)

    # --- Normalfall: k ≈ mant * 2^t ---
    scaled = mant * two_t
    k = _round_fraction_to_int(scaled)

    # Überlauf in der Mantisse (z.B. 0.1111.. rundet auf 1.0000)
    if k == two_t:
        k = two_t // 2   # 0.1000...
        e += 1
        if e > U:
            k_max = two_t - 1
            return sign * Fraction(k_max, two_t) * (2 ** U)

    # normalisiert bedeutet d1=1 -> k mindestens 2^(t-1)
    if k < (two_t // 2):
        # kann durch Rundung passieren, dann zur kleinsten normalisierten Mantisse
        k = two_t // 2

    return sign * Fraction(k, two_t) * (2 ** e)
