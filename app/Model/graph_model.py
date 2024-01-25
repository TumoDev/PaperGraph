import tkinter as tk
import networkx as nx

class GraphModel:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.id_current_node = None  # Asegúrate de inicializar correctamente las variables de instancia

    @property
    def get_graph(self):
        return self.graph

    @property
    def get_current_id_node(self):
        return self.id_current_node
    
    def get_paper(self, paper_id=None):
        if paper_id is None:
            paper_id = self.id_current_node
        return self.graph.nodes[paper_id]['paper'] if paper_id in self.graph.nodes else None
    
    def set_current_id_node(self, id):
        self.id_current_node = id

    def add_paper(self, paper):
        # Usar el título del paper como clave del nodo
        paper_title = paper.get_title
        self.graph.add_node(paper_title, paper=paper)

        # Si el nodo actual está establecido, agregar una arista
        if self.id_current_node is not None:
            self.graph.add_edge(self.id_current_node, paper_title)
        else:
            self.id_current_node = paper_title  # Establecer el título del paper como el nodo actual

    def print_graph(self):
        for node in self.graph.nodes(data=True):
            if 'paper' in node[1]:
                paper = node[1]['paper']
                print(f"Título: {paper.get_title}, Autor: {paper.get_author}, Fecha: {paper.get_date}")
            else:
                print(f"El nodo {node[0]} no tiene un objeto 'paper' asociado.")

    def get_first_paper(self):
        if self.graph.nodes:
            first_node_id = next(iter(self.graph.nodes))  # Obtener el primer nodo
            return self.get_paper(first_node_id)
        else:
            return None
