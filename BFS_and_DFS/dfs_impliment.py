graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = []
start = '5'
def dfs(visited, graph, start):
  if start not in visited:
    visited.append(start)
    print(start, end=' ')
    for n in graph[start]:
      dfs(visited, graph, n)
  return visited

print(dfs(visited, graph, start))