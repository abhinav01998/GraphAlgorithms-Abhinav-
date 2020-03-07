from _collections import defaultdict

vis_nodes = []
stack = []


class BreadthFirstAlgo:

    def __init__(self):
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def new_vertex(self, a, b):
        self.graph[a].append(b)

    def dfs(self, visited, graph, node):
        vis_nodes.append(node)
        stack.insert(0, node)
        while stack:
            s = stack.pop()
            print(s)
            for next_node in graph[s]:
                if next_node not in visited:
                    visited.append(next_node)
                    stack.insert(0, next_node)


if __name__ == '__main__':
    algo = BreadthFirstAlgo()
    algo.new_vertex('A', 'B')
    algo.new_vertex('A', 'C')
    algo.new_vertex('B', 'D')
    algo.new_vertex('B', 'E')
    algo.new_vertex('C', 'F')
    algo.new_vertex('E', 'F')
    algo.new_vertex('F', 'C')
    algo.dfs(vis_nodes, algo.graph, 'A')
