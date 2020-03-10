from _collections import defaultdict


class DijkstraAlgo:

    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distance = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distance[(from_node, to_node)] = distance
        self.distance[(to_node, from_node)] = distance

    def dijsktra(self, graph, start_node):
        visited = {start_node: 0}

        nodes = set(graph.nodes)

        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in graph.edges[min_node]:
                weight = current_weight + graph.distance[(min_node, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight

        return visited


if __name__ == '__main__':
    graph = DijkstraAlgo()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_node('D')
    graph.add_node('E')
    graph.add_node('F')
    graph.add_edge('A', 'B', 5)
    graph.add_edge('A', 'C', 7)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 4)
    graph.add_edge('C', 'D', 4)
    graph.add_edge('C', 'E', 8)
    graph.add_edge('D', 'E', 5)
    graph.add_edge('D', 'F', 1)
    graph.add_edge('E', 'F', 3)
    print(graph.dijsktra(graph, 'A'))
