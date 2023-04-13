# DFS 메서드 정의
def dfs(graph, v, visited):
  visited[v] = True
  print(v, end = " ")
  for inner in graph[v]:
    for element in inner:
      if not visited[element]:
        dfs(graph, element, visited)
      
visited = [False] * 9
graph = [[] for _ in range(9)]
graph[1].append([2, 3, 8])
graph[2].append([1, 7])
graph[3].append([1, 4, 5])
graph[4].append([3, 5])
graph[5].append([3, 4])
graph[6].append([7])
graph[7].append([2, 6, 8])
graph[8].append([1, 7])

dfs(graph, 1, visited)