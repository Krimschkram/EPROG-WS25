import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return x**2 + y**2

# Punkte für die Tangentialebene
x0 = -4
y0 = 4
z0 = f(x0, y0)

# Gitter fürn Plot:
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
# Tangentialebene:
E = z0 + 2*x0*(X - x0) + 2*y0*(Y - y0)


fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")
ax.view_init(elev=5, azim=40)




# Funktion
ax.plot_surface(X, Y, Z, alpha=0.6)
# Tangentialebene
ax.plot_surface(X, Y, E, alpha=0.6, cmap= "plasma")

# Punkt markieren
ax.scatter(x0, y0, z0, color="navy", s=50)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Tangentialebene an f(x,y) = x² + y² im Punkt (1,1) #flying carpet")

plt.show()


# Die Tangentialebene berührt die Funktion exakt im Punkt (1,1)