import numpy as np
import matplotlib.pyplot as plt
A=np.random.rand(1000,1000)
# Funktion, die überprüft, ob ein Punkt innerhalb eines Polygons liegt
def inside_poly(poly, point):
    x, y = point
    n = len(poly)
    counter = 0

    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            counter += 1

    return counter % 2 == 1

austria_vertices = np.load("vertices.npy")

bounding_box = np.array([np.min(austria_vertices[:,0]), np.min(austria_vertices[:,1]),
                         np.max(austria_vertices[:,0]), np.max(austria_vertices[:,1])])
box_area = 562 * 287  # ca. Fläche der Bounding Box in km²

# Generiere zufällige Punkte innerhalb der Bounding Box
samples = 10000
random_points = np.random.rand(samples, 2)
random_points[:, 0] = random_points[:, 0] * (bounding_box[2] - bounding_box[0]) + bounding_box[0]
random_points[:, 1] = random_points[:, 1] * (bounding_box[3] - bounding_box[1]) + bounding_box[1]

# Überprüfe, ob die Punkte innerhalb oder außerhalb des Polygons liegen
points_inside = np.array([inside_poly(austria_vertices, point) for point in random_points])
print(f"Anteil der Punkte: {np.sum(points_inside==True)/samples:.2%}")


# Visualisierung der Berechnung
plt.figure(figsize=(8, 8))
plt.plot(austria_vertices[:, 0], austria_vertices[:, 1], 'b-', marker='o')
plt.fill(austria_vertices[:, 0], austria_vertices[:, 1], alpha=0.2, color='blue')
plt.plot([bounding_box[0], bounding_box[2], bounding_box[2], bounding_box[0], bounding_box[0]],
         [bounding_box[1], bounding_box[1], bounding_box[3], bounding_box[3], bounding_box[1]], 'r--')
plt.scatter(random_points[points_inside,0], random_points[points_inside,1], color='red', s=1, alpha=0.5)
plt.scatter(random_points[~points_inside,0], random_points[~points_inside,1], color='green', s=1, alpha=0.5)
plt.xticks([])
plt.yticks([])
plt.axis('equal')
plt.show()