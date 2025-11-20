import math
import matplotlib.pyplot as plt

n=10
maze = [[0]*n for _ in range(n)]
walls = [(2,8),(0,9),(1,7),(2,2),(2,3),(2,4),(2,5),
         (2,6),(2,7),(3,2),(4,2),(7,2),(6,2),(8,2),
         (4,7),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),
         (5,7),(6,2),(6,6),(7,6),(3,5),(7,4),(8,4),
         (9,4),(8,6),(8,7),(8,8)]
for (x,y) in walls:
    maze[x][y]=1

start = (9,1)
goal = (3,4)

def print_maze(maze, path=None, start=None, goal=None, dist = None):
    plt.scatter([x for (x,y) in walls],[y for (x,y) in walls], color='lightblue', marker='s', s=600)
    plt.plot([-0.5,n-0.5,n-0.5,-0.5,-0.5],[-0.5,-0.5,n-0.5,n-0.5,-0.5],
             color='lightblue', linewidth=3)
    if path:
        plt.plot([x for (x,y) in path], [y for (x,y) in path],
                 color='orange', linewidth=3)
    if goal:
        plt.scatter(goal[0],goal[1], color='red', marker='*', s=200)
    if start:
        plt.scatter(start[0], start[1], color='orange', marker='o', s=200)
    if dist:
        for i in range(n):
            for j in range(n):
                if maze[i][j]==0 and dist[i][j]<float('inf'):
                    plt.text(i,j,str(round(dist[i][j],1)), color='black',
                             fontsize=10, ha='center', va='center')
    plt.xlim(-1,n)
    plt.ylim(-1,n)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.gca().invert_yaxis()  # optional, damit es „mathematischer“ aussieht
    plt.show()


# Distanzmatrix initialisieren
dist = [[float('inf')]*n for _ in range(n)]
dist[goal[0]][goal[1]] = 0

# --- NEU: Update mit 8 Nachbarn (4 orthogonal, 4 diagonal) ---
def update(dist, maze, pos):
    x, y = pos
    n = len(maze)

    # (dx, dy, kosten)
    moves = [
        (-1, 0, 1.0),  # links
        ( 1, 0, 1.0),  # rechts
        ( 0,-1, 1.0),  # unten
        ( 0, 1, 1.0),  # oben
        (-1,-1, math.sqrt(2)),  # diagonal
        (-1, 1, math.sqrt(2)),
        ( 1,-1, math.sqrt(2)),
        ( 1, 1, math.sqrt(2)),
    ]

    for dx, dy, cost in moves:
        xp, yp = x + dx, y + dy
        tmp = dist[x][y] + cost
        if 0 <= xp < n and 0 <= yp < n and maze[xp][yp] == 0 and tmp < dist[xp][yp]:
            dist[xp][yp] = tmp
            update(dist, maze, (xp, yp))

# --- NEU: Pfadfindung mit 8 Nachbarn ---
def find_shortest_path(dist, path):
    x, y = path[-1]
    if dist[x][y] != 0:  # noch nicht am Ziel
        moves = [
            (-1, 0), (1, 0), (0,-1), (0, 1),
            (-1,-1), (-1, 1), (1,-1), (1, 1)
        ]
        # Nachbar mit kleinerer Distanz suchen
        for dx, dy in moves:
            xp, yp = x + dx, y + dy
            if 0 <= xp < n and 0 <= yp < n and dist[xp][yp] < dist[x][y]:
                path.append((xp, yp))
                return find_shortest_path(dist, path)
    return path


# ausführen
dist = [[float('inf')]*n for _ in range(n)]
dist[goal[0]][goal[1]] = 0
update(dist, maze, goal)

path = [start]
path = find_shortest_path(dist, path)

print_maze(maze, path, start, goal, dist)
