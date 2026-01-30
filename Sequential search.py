import itertools
import sys
def travelling_salesman(graph, start):
 n = len(graph)
 vertices = [i for i in range(n) if i != start]
 min_cost = sys.maxsize
 for perm in itertools.permutations(vertices):
   cost = graph[start][perm[0]]
   for i in range(len(perm) - 1):
    cost += graph[perm[i]][perm[i + 1]]
    cost += graph[perm[-1]][start]
    min_cost = min(min_cost, cost)
    return min_cost
graph = [
 [0, 10, 15, 20],
 [10, 0, 35, 25],
 [15, 35, 0, 30],
 [20, 25, 30, 0]
]
print("Minimum cost:", travelling_salesman(graph, 0))