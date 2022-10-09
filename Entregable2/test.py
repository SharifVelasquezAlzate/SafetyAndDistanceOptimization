from Graph import Graph

graphy = Graph()

graphy.add_edge("A", "B", 4, directed=True)
graphy.add_edge("A", "C", 2, directed=True)
graphy.add_edge("B", "D", 2, directed=True)
graphy.add_edge("B", "E", 3, directed=True)
graphy.add_edge("B", "C", 3, directed=True)
graphy.add_edge("C", "B", 1, directed=True)
graphy.add_edge("C", "D", 4, directed=True)
graphy.add_edge("C", "E", 5, directed=True)
graphy.add_edge("E", "D", 1, directed=True)

graphy.print_graph()
print(graphy.dijkstra("A", "E", pretty=True))
