import tkinter as tk
from tkinter import Frame, Scrollbar
import networkx as nx

class GraphFrame(Frame):
    def __init__(self, parent, controller, bg_color="#A7BEBE"):
        super().__init__(parent, bg=bg_color)
        self.controller = controller
        
        # Crear un Canvas con barras de desplazamiento
        self.canvas = tk.Canvas(self, bg="lightgray")
        self.v_scroll = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.h_scroll = Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set)

        # Posicionar los elementos en el Frame
        self.v_scroll.pack(side=tk.RIGHT, fill="y")
        self.h_scroll.pack(side=tk.BOTTOM, fill="x")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas.bind('<Configure>', self.on_canvas_configure)
        self.draw_graph()

    def on_canvas_configure(self, event=None):
        # Ajustar la región de desplazamiento al tamaño del Canvas
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def draw_graph(self):
        self.canvas.delete("all")  # Limpiar el canvas antes de dibujar
        
        graph = self.controller.model.graph
        pos = nx.spring_layout(graph)  # Posiciones de los nodos

        # Escalar y centrar el grafo (ajuste el factor de escala y la posición inicial aquí)
        scale_x, scale_y = 300, 300  # Factores de escala más bajos reducen la distancia
        offset_x, offset_y = 15000, 15000  # Posición inicial para centrar el grafo
        
        for node, (x, y) in pos.items():
            x = x * scale_x + offset_x  # Ajuste de escala y posición
            y = y * scale_y + offset_y
            # Dibujar el nodo como un círculo
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="white", outline="black")
            # Acceder al atributo 'label' del nodo para el texto
            label = graph.nodes[node].get('label', str(node))
            print(label)
            self.canvas.create_text(x, y, text=label)

        for edge in graph.edges():
            start_pos, end_pos = pos[edge[0]], pos[edge[1]]
            start_pos = (start_pos[0] * scale_x + offset_x, start_pos[1] * scale_y + offset_y)
            end_pos = (end_pos[0] * scale_x + offset_x, end_pos[1] * scale_y + offset_y)
            # Dibujar las aristas
            self.canvas.create_line(start_pos, end_pos, fill="black", width=1)

        self.on_canvas_configure()  # Ajustar la región de desplazamiento al contenido



