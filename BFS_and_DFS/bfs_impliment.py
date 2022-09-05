graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = [] # list of visited node
queue = [] # list of nodes to visit
start = '5'
def bfs(visited ,graph, start):
    visited.append(start)
    queue.append(start)

    while queue:
        m = queue.pop(0)
        print(m, end=' ')

        for n in graph[m]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
    return visited

bfs(visited, graph, start)
