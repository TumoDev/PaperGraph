import networkx as nx

class GraphModel:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_paper(self, paper):
        self.graph.add_node(paper.id, paper=paper)

    def add_relation(self, parent_id, child_id):
        self.graph.add_edge(parent_id, child_id)

    def get_paper_info(self, paper_id):
        return self.graph.nodes[paper_id]['paper']

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
            return self.get_paper_info(first_node_id)
        else:
            return None