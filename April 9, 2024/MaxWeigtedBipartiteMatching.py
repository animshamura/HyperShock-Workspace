def AugmentedPath(graph, u, visited, match):
    for v, weight in enumerate(graph[u]):
        if not visited[v] and weight > 0:
            visited[v] = True
            if match[v] == -1 or AugmentedPath(graph, match[v], visited, match):
                match[v] = u
                return True
    return False

def BipartiteMatch(graph):
    num_left = len(graph)
    num_right = len(graph[0])
    match = [-1] * num_right
    result = 0

    for u in range(num_left):
        visited = [False] * num_right
        if AugmentedPath(graph, u, visited, match):
            result += 1

    return result, match

if __name__ == "__main__":
   
    graph = []
    for i in range(int(input("Enter number of nodes : "))): 
        graph.append(list(map(int,input("Enter capacity and flow : ").split())))

    max_matching, matching = BipartiteMatch(graph)
    print("Maximum weighted bipartite matching :", max_matching)
    print("Matching pairs :", matching)
