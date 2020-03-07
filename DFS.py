from _collections import defaultdict

vis_nodes = []


class DepthFirstAlgo:

    def __init__(self):
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def new_vertex(self, a, b):
        self.graph[a].append(b)

    def dfs(self, visited, graph, node):
        if node not in visited:
            print(node)
            visited.append(node)
            for next_node in graph[node]:
                self.dfs(visited, graph, next_node)


if __name__ == '__main__':
    algo = DepthFirstAlgo()
    algo.new_vertex('A', 'B')
    algo.new_vertex('A', 'C')
    algo.new_vertex('B', 'D')
    algo.new_vertex('B', 'E')
    algo.new_vertex('C', 'F')
    algo.new_vertex('E', 'F')
    algo.new_vertex('F', 'C')
    algo.dfs(vis_nodes, algo.graph, 'A')
