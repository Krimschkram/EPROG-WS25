import numpy as np
import matplotlib.pyplot as plt

# Punkt-in-Polygon (Ray Casting)
def inside_poly(poly, point):
    x, y = point
    n = len(poly)
    counter = 0

    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]

        # schneidet die Kante die horizontale Halbgerade nach rechts?
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            counter += 1

    return counter % 2 == 1



vertices = np.load("vertices.npy")

# --- Bounding Box + Fläche der Box (in Koordinaten^2) ---
xmin, ymin = np.min(vertices[:, 0]), np.min(vertices[:, 1])
xmax, ymax = np.max(vertices[:, 0]), np.max(vertices[:, 1])

bounding_box = np.array([xmin, ymin, xmax, ymax])
box_area = (xmax - xmin) * (ymax - ymin)

# --- Monte Carlo Sampling ---
samples = 100_000  # gerne erhöhen für bessere Genauigkeit
random_points = np.random.rand(samples, 2)
random_points[:, 0] = random_points[:, 0] * (xmax - xmin) + xmin
random_points[:, 1] = random_points[:, 1] * (ymax - ymin) + ymin

points_inside = np.array([inside_poly(vertices, p) for p in random_points])

ratio = np.mean(points_inside)
area_est = ratio * box_area

print(f"Geschätzte Polygonfläche: {area_est:.6f} (in Einheiten^2 deiner Koordinaten)")

# --- Visualisierung ---
plt.figure(figsize=(7, 7))
plt.plot(vertices[:, 0], vertices[:, 1], "b-", marker="o", markersize=2)
plt.fill(vertices[:, 0], vertices[:, 1], alpha=0.2)

# Bounding Box
plt.plot([xmin, xmax, xmax, xmin, xmin],
         [ymin, ymin, ymax, ymax, ymin], "r--")

# Punkte
plt.scatter(random_points[points_inside, 0], random_points[points_inside, 1],
            s=1, alpha=0.4)
plt.scatter(random_points[~points_inside, 0], random_points[~points_inside, 1],
            s=1, alpha=0.1)

plt.axis("equal")
plt.xticks([])
plt.yticks([])
plt.show()
