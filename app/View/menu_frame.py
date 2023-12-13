import tkinter as tk

class MenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#263D42")
        self.controller = controller
        self.content()
    
    def content(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)  # Ajustamos el weight para dar más espacio al título del paper

        padding_x = 10  # Este padding se aplicará a los extremos de la fila
        padding_y = 5
        
        # Nombre del Programa
        titulo_programa = tk.Label(self, text="PaperGraph", bg="#263D42", fg="#FFFFFF", font=("Helvetica", 16, "bold"))
        titulo_programa.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=100, pady=(10, 5))

        # Título
        titulo = tk.Label(self, text="Título: ", bg="#263D42", fg="#FFFFFF", font=("Helvetica", 11, "bold"))
        titulo.grid(row=1, column=0, sticky="w", padx=(padding_x, 0), pady=padding_y)

        # Título del Paper
        titulo_paper = tk.Label(self, text="Aquí va el título del paper", bg="#263D42", fg="#FFFFFF", font=("Helvetica", 10))
        titulo_paper.grid(row=1, column=1, padx=(0, padding_x), pady=padding_y)
        
        
        # Autor
        autor = tk.Label(self, text="Autor: ", bg="#263D42", fg="#FFFFFF", font=("Helvetica", 11, "bold"))
        autor.grid(row=2, column=0, sticky="w", padx=padding_x, pady=padding_y)

        # Nombre Autor
        titulo_paper = tk.Label(self, text="Aquí va el Nombre del Autor", bg="#263D42", fg="#FFFFFF", font=("Helvetica", 10))
        titulo_paper.grid(row=2, column=1, padx=(0, padding_x), pady=padding_y)
        
        # Fecha de Publicación
        fecha_publicacion = tk.Label(self, text="Fecha de Publicación: ", bg="#263D42", fg="#FFFFFF", font=("Helvetica", 11, "bold"))
        fecha_publicacion.grid(row=3, column=0, sticky="w", padx=padding_x, pady=padding_y)
        
        # Fecha de Publicacion
        titulo_paper = tk.Label(self, text="23/03/12", bg="#263D42", fg="#FFFFFF", font=("Helvetica", 10))
        titulo_paper.grid(row=3, column=1, padx=(0, padding_x), pady=padding_y)
        
        # Abstract
        titulo = tk.Label(self, text="Contribuciones", bg="#263D42", fg="#FFFFFF", font=("Helvetica", 12, "bold"))
        titulo.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=100, pady=(10, 5))
        
        # Cuadro de Texto (Label con texto fijo)
        texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam molestie malesuada ex, vitae accumsan mauris vestibulum vel. Duis at enim dignissim, consectetur sem sit amet, interdum ligula. Nunc iaculis odio ut mauris molestie, a fermentum nisi porttitor. Aenean ut finibus augue. Nunc sed augue sed nibh ultrices facilisis. Donec accumsan quam eu nisi cursus mattis. Nam odio est, tincidunt pretium velit ac, volutpat varius magna. Pellentesque rutrum rhoncus leo, vel elementum metus ultricies vel.Phasellus mattis laoreet lectus ut dignissim. Praesent rutrum dolor vitae dapibus laoreet. Aliquam vitae suscipit metus, sit amet vulputate tortor. Quisque sit amet rhoncus mauris, nec commodo nibh. Mauris sollicitudin in quam eget tempus. Quisque convallis nisl ac dolor posuere, vel rhoncus erat placerat. Phasellus semper quam ac eros pretium mattis. Nulla facilisi. Donec tincidunt hendrerit mauris quis elementum. Nullam a ornare libero. Nullam maximus erat a nunc condimentum convallis. Ut ornare malesuada ligula, vitae consectetur nulla pretium sed."
        self.cuadro_texto = tk.Label(self, text=texto, bg="#FFFFFF", fg="#000000", wraplength=400, justify="left")
        self.cuadro_texto.grid(row=5, column=0, columnspan=2, padx=padding_x, pady=padding_y, sticky="nsew")

        # Contribuciones
        titulo = tk.Label(self, text="Contribuciones", bg="#263D42", fg="#FFFFFF", font=("Helvetica", 12, "bold"))
        titulo.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=100, pady=(10, 5))

        # Cuadro de Texto (Label con texto fijo)
        texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam molestie malesuada ex, vitae accumsan mauris vestibulum vel. Duis at enim dignissim, consectetur sem sit amet, interdum ligula. Nunc iaculis odio ut mauris molestie, a fermentum nisi porttitor. Aenean ut finibus augue. Nunc sed augue sed nibh ultrices facilisis. Donec accumsan quam eu nisi cursus mattis. Nam odio est, tincidunt pretium velit ac, volutpat varius magna. Pellentesque rutrum rhoncus leo, vel elementum metus ultricies vel.Phasellus mattis laoreet lectus ut dignissim. Praesent rutrum dolor vitae dapibus laoreet. Aliquam vitae suscipit metus, sit amet vulputate tortor. Quisque sit amet rhoncus mauris, nec commodo nibh. Mauris sollicitudin in quam eget tempus. Quisque convallis nisl ac dolor posuere, vel rhoncus erat placerat. Phasellus semper quam ac eros pretium mattis. Nulla facilisi. Donec tincidunt hendrerit mauris quis elementum. Nullam a ornare libero. Nullam maximus erat a nunc condimentum convallis. Ut ornare malesuada ligula, vitae consectetur nulla pretium sed."
        self.cuadro_texto = tk.Label(self, text=texto, bg="#FFFFFF", fg="#000000", wraplength=400, justify="left")
        self.cuadro_texto.grid(row=7, column=0, columnspan=2, padx=padding_x, pady=padding_y, sticky="nsew")


        # Botón 1
        self.boton1 = tk.Button(self, text="Botón 1", command=self.on_boton1_click)
        self.boton1.grid(row=8, column=0, padx=(padding_x, 5), pady=padding_y, sticky="nsew")

        # Botón 2
        self.boton2 = tk.Button(self, text="Botón 2", command=self.on_boton2_click)
        self.boton2.grid(row=8, column=1, padx=(5,padding_x), pady=padding_y, sticky="nsew")

    def on_boton1_click(self):
        pass

    def on_boton2_click(self):
        pass
