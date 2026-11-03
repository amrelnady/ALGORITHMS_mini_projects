from collections import deque

maze = [
    ['S', '.', '#', '.'],
    ['.', '.', '#', '.'],
    ['#', '.', '.', '.'],
    ['.', '#', '.', 'E']
]

start = (0, 0)
end = (3, 3)

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


# BFS
queue = deque([[start]])
visited = [start]
bfs_path = None

while queue:
    path = queue.popleft()
    x, y = path[-1]

    if (x, y) == end:
        bfs_path = path
        break

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if (0 <= nx < 4 and 0 <= ny < 4
                and maze[nx][ny] != '#'
                and (nx, ny) not in visited):

            visited.append((nx, ny))
            queue.append(path + [(nx, ny)])


# DFS
stack = [[start]]
visited = [start]
dfs_path = None

while stack:
    path = stack.pop()
    x, y = path[-1]

    if (x, y) == end:
        dfs_path = path
        break

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if (0 <= nx < 4 and 0 <= ny < 4
                and maze[nx][ny] != '#'
                and (nx, ny) not in visited):

            visited.append((nx, ny))
            stack.append(path + [(nx, ny)])


# Print Results
print("BFS Path:", bfs_path)
print("DFS Path:", dfs_path)

print("\nMaze:")
for row in maze:
    print(" ".join(row))