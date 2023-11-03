from collections import defaultdict, deque


def min_depth(root, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    queue = deque([(root, 1)])
    visited = set([root])

    while queue:
        node, depth = queue.popleft()
        if node not in graph or not graph[node]:
            return depth
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, depth + 1))


def main():
    with open('src/input.txt', 'r') as file:
        root = int(file.readline())
        edges = [tuple(map(int, line.split(','))) for line in file]

    depth = min_depth(root, edges)

    with open('src/output.txt', 'w') as file:
        file.write(str(depth))


if __name__ == "__main__":
    main()
