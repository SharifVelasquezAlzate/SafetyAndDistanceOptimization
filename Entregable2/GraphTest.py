class Graph:
    def __init__(self):
        self.graph = {}
        self.algorithm_nodes = {}
        self.vertices = {}

    def set_graph(self, dictionary):
        self.graph = dictionary

    def print_graph(self):
        print(self.graph)

    def add_vertex(self, v, heuristic=0):
        self.graph[v] = []
        self.vertices[v] = heuristic
        # Ponemos que todos los nodos tienen una distancia infinita desde la fuente, y que todavía no sabemos qué nodo llega a ellos.
        self.algorithm_nodes[v] = [float('inf'), None]  # [dist. inicio, como llegar]

    def add_edge(self, v1, v2, weight=0, directed=False, enabled=True):
        self.add_vertex(v1)
        self.add_vertex(v2)

        self.graph[v1].append([v2, weight, enabled])
        if not directed:
            self.graph[v2].append([v1, weight, enabled])

    def a_star(self, s, f, pretty=False):
        # En unvisited guardaremos los nodos que no hemos visitado (así no entraremos en "bucles infinitos" entre nodos)
        unvisited = list(self.graph.keys())
        # nodes será el diccionario que guarde toda la información de los nodos, específicamente tiene esta estructura:
        # {
        #   nodo: [distancia más corta desde la fuente hasta ese nodo, el nodo por medio del cual llegamos, la variable "heurística"]
        #   "A": [12, "E", 16]
        # }

        # El nodo fuente siempre tendrá una distancia de cero (pues es donde iniciamos)
        self.algorithm_nodes[s][0] = 0

        # Mientras nos falten nodos por visitar...
        while unvisited:
            print(len(unvisited))
            # Escogemos el nodo que tiene la distancia más corta hasta el momento
            min_node_index, min_node = self.optimized_min_nodes(unvisited)  # min_node = min(unvisited, key=lambda node: self.algorithm_nodes[node][0])
            # Iteramos por cada uno de sus vecinos
            for neighbour in self.graph[min_node]:
                # Si ya visitamos a ese vecino, no hacemos nada (para evitar bucles infinitos)
                if not neighbour[2]:  # If not enabled
                    pass

                # Si al llegar a ese vecino por medio del nodo actual es más corto que llegar por el camino que en
                # iteraciones pasadas habíamos descubierto, pues modificamos la distancia del vecino a la que hallamos
                if self.algorithm_nodes[min_node][0] + neighbour[1] < self.algorithm_nodes[neighbour[0]][0]:
                    # Modificamos la distancia
                    self.algorithm_nodes[neighbour[0]][0] = self.algorithm_nodes[min_node][0] + neighbour[1]
                    # Decimos que llegamos al vecino (neighbour) por medio del nodo actual (min_node)
                    self.algorithm_nodes[neighbour[0]][1] = min_node

                # Desabilitamos el camino entre ambos nodos para indicar que ya analizamos este nodo
                neighbour[2] = False

            # Una vez revisemos todos los vecinos de ese nodo, lo eliminaremos de la lista de "nodos por visitar"
            del unvisited[min_node_index]

        # Después de que hayamos recorrido todos los nodos, simplemente construimos el patrón
        path = []
        node = f
        # Recorremos desde el último nodo hasta el nodo fuente
        while node is not None:
            path.append((node, self.algorithm_nodes[node]))
            node = self.algorithm_nodes[node][1]

        if pretty:
            path_simplified = []
            for i in range(len(path) - 1, -1, -1):
                path_simplified.append(path[i][0])
            path = ' ===> '.join(path_simplified)
        return path

    def optimized_min_nodes(self, array):
        min_index = 0
        minim = array[min_index]
        for index, value in enumerate(array):
            if self.algorithm_nodes[value][0] < self.algorithm_nodes[minim][0]:
                min_index = index
                minim = value
        return min_index, minim
