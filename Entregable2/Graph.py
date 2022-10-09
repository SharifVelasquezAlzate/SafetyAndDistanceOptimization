class Graph:
    def __init__(self):
        self.graph = {}
        self.vertices = {}

    def set_graph(self, dictionary):
        self.graph = dictionary

    def print_graph(self):
        print(self.graph)

    def add_vertex(self, v, heuristic=0):
        if v not in self.graph.keys():
            self.graph[v] = []
            self.vertices[v] = heuristic

    def add_edge(self, v1, v2, weight=0, directed=False):
        self.add_vertex(v1)
        self.add_vertex(v2)

        self.graph[v1].append([v2, weight])
        if not directed:
            self.graph[v2].append([v1, weight])

    def dijkstra(self, s, f, pretty=False) -> None:
        unvisited = list(self.graph.keys())

        nodes = {}
        for node in self.graph.keys():
            nodes[node] = [float('inf'), None]
        # El nodo fuente siempre tendrá una distancia de cero (pues es la distancia que recorre para llegar de él a él)
        nodes[s][0] = 0

        while unvisited:
            min_node = min(unvisited, key=lambda node: nodes[node][0])
            for neighbour in self.graph[min_node]:
                if neighbour[0] not in unvisited:
                    pass

                if nodes[min_node][0] + self.vertices[neighbour[0]] + neighbour[1] < nodes[neighbour[0]][0]:
                    nodes[neighbour[0]][0] = nodes[min_node][0] + self.vertices[neighbour[0]] + neighbour[1]
                    nodes[neighbour[0]][1] = min_node
            unvisited.remove(min_node)

        path = []
        node = f
        while node is not None:
            path.append((node, nodes[node]))
            node = nodes[node][1]

        if pretty:
            path_simplified = []
            for i in range(len(path)-1, -1, -1):
                path_simplified.append(path[i][0])
            path = ' ===> '.join(path_simplified)
        return path

    def a_star(self, s, f):
        # En unvisited guardaremos los nodos que no hemos visitado (así no entraremos en "bucles infinitos" entre nodos)
        unvisited = list(self.graph.keys())
        # nodes será el diccionario que guarde toda la información de los nodos, específicamente tiene esta estructura:
        # {
        #   nodo: [distancia más corta desde la fuente hasta ese nodo, el nodo por medio del cual llegamos, la variable "heurística"]
        #   "A": [12, "E", 16]
        # }
        nodes = {}

        # Ponemos que todos los nodos tienen una distancia infinita desde la fuente, y que todavía no sabemos qué nodo llega a ellos.
        for node in self.graph.keys():

            nodes[node] = [float('inf'), None, self.graph[node][2]]  # [dist. inicio, como llegar, heuristica]
        # El nodo fuente siempre tendrá una distancia de cero (pues es donde iniciamos)
        nodes[s][0] = 0

        # Mientras nos falten nodos por visitar...
        while unvisited:
            # Escogemos el nodo que tiene la distancia más corta hasta el momento
            min_node = min(unvisited, key=lambda node: nodes[node][0] + nodes[node][2])
            # Iteramos por cada uno de sus vecinos
            for neighbour in self.graph[min_node]:
                # Si ya visitamos a ese vecino, no hacemos nada (para evitar bucles infinitos)
                if neighbour[0] not in unvisited:
                    pass

                # Si al llegar a ese vecino por medio del nodo actual es más corto que llegar por el camino que en
                # iteraciones pasadas habíamos descubierto, pues modificamos la distancia del vecino a la que hallamos
                if nodes[min_node][0] + neighbour[1] < nodes[neighbour[0]][0]:
                    # Modificamos la distancia
                    nodes[neighbour[0]][0] = nodes[min_node][0] + neighbour[1]
                    # Decimos que llegamos al vecino (neighbour) por medio del nodo actual (min_node)
                    nodes[neighbour[0]][1] = min_node

            # Una vez revisemos todos los vecinos de ese nodo, lo remos de la lista de "nodos por visitar"
            unvisited.remove(min_node)

        # Después de que hayamos recorrido todos los nodos, simplemente construimos el patrón
        path = []
        node = f
        # Recorremos desde el último nodo hasta el nodo fuente
        while node is not None:
            path.append((node, nodes[node]))
            node = nodes[node][1]

        path.reverse()
        return path
