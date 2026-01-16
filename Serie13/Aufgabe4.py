import sympy as sp

a, b, x = sp.symbols('a b x', real=True)
c0, c1, c2, c3 = sp.symbols('c0 c1 c2 c3')

p = c0 + c1*x + c2*x**2 + c3*x**3

eqs = []
for k in range(4):  # q(x)=x^k
    eqs.append(sp.Eq(sp.integrate(p*x**k, (x, a, b)), b**k))

sol = sp.solve(eqs, [c0, c1, c2, c3], simplify=True)
p_sol = sp.simplify(p.subs(sol))

print(p_sol)
