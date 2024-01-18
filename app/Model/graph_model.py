import networkx as nx

class GraphModel:
    def __init__(self):
        self.graph = nx.DiGraph()
        id_current_node = None

    @property
    def get_current_id_node(self):
        return self.id_current_node
    
    def get_paper(self, paper_id=get_current_id_node):
        return self.graph.nodes[paper_id]['paper']
    
    def set_current_id_node(self, id):
        self.id_current_node = id

    def add_paper(self, paper):
        # Agregar el nodo paper al grafo
        self.graph.add_node(paper.id, paper=paper)

        # Si id_current_node está establecido y es diferente de None, agregar una arista desde id_current_node a paper.id
        if self.id_current_node is not None:
            self.graph.add_edge(self.id_current_node, paper.id)
        else:
            # Si id_current_node es None, establecer este paper como el nodo actual (raíz)
            self.id_current_node = paper.id

    def print_graph(self):
        for node in self.graph.nodes(data=True):
            if 'paper' in node[1]:
                paper = node[1]['paper']
                print(f"Paper ID: {node[0]}, Título: {paper.get_title}, Autor: {paper.get_author}, Fecha: {paper.get_date}")
            else:
                print(f"El nodo {node[0]} no tiene un objeto 'paper' asociado.")

    def get_first_paper(self):
        if self.graph.nodes:
            first_node_id = list(self.graph.nodes)[0]
            return self.get_paper(first_node_id)
        else:
            return None