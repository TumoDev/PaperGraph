import tkinter as tk

class MenuFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#263D42")
        self.controller = controller
        self.content()
    
    def content(self):
        # Set dimensions
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1) 
        padding_x = 20 
        padding_y = 5
        
        title_p, author_p, date_p=self.controller.display_paper_data()

        # Name of the program
        titul_program = tk.Label(self, text="PaperGraph", bg="#263D42", fg="#FFFFFF", font=("Helvetica", 16, "bold"))
        titul_program.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=100, pady=(10, 5))

        # Title of the Paper
        title = tk.Label(self, text="Título: ", bg="#263D42", fg="#FFFFFF", font=("Helvetica", 10, "bold"))
        title.grid(row=1, column=0, sticky="w", padx=(padding_x, 3), pady=padding_y)
        
        title_paper = tk.Label(self, text=title_p, bg="#263D42", fg="#FFFFFF", font=("Helvetica", 8))
        title_paper.grid(row=1, column=1, sticky="e", padx=(0, padding_x), pady=padding_y)

        # Autor of the Paper
        title = tk.Label(self, text="Autor: ", bg="#263D42", fg="#FFFFFF", font=("Helvetica", 10, "bold"))
        title.grid(row=2, column=0, sticky="w", padx=(padding_x,3), pady=padding_y)

        titulo_author = tk.Label(self, text=author_p, bg="#263D42", fg="#FFFFFF", font=("Helvetica", 8))
        titulo_author.grid(row=2, column=1, sticky="e",padx=padding_x, pady=padding_y)
        
        # Date of the Paper
        title = tk.Label(self, text="Date: ", bg="#263D42", fg="#FFFFFF", font=("Helvetica", 10, "bold"))
        title.grid(row=3, column=0, sticky="w", padx=(padding_x,3), pady=padding_y)
        
        title_date = tk.Label(self, text=date_p, bg="#263D42", fg="#FFFFFF", font=("Helvetica", 10))
        title_date.grid(row=3, column=1, sticky="e",padx=padding_x, pady=padding_y)
        

        # Abstract
        title = tk.Label(self, text="Abstract", bg="#263D42", fg="#FFFFFF", font=("Helvetica", 10, "bold"))
        title.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=100, pady=(10, 5))
        
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam molestie malesuada ex, vitae accumsan mauris vestibulum vel. Duis at enim dignissim, consectetur sem sit amet, interdum ligula. Nunc iaculis odio ut mauris molestie, a fermentum nisi porttitor. Aenean ut finibus augue. Nunc sed augue sed nibh ultrices facilisis. Donec accumsan quam eu nisi cursus mattis. Nam odio est, tincidunt pretium velit ac, volutpat varius magna. Pellentesque rutrum rhoncus leo, vel elementum metus ultricies vel.Phasellus mattis laoreet lectus ut dignissim. Praesent rutrum dolor vitae dapibus laoreet. Aliquam vitae suscipit metus, sit amet vulputate tortor. Quisque sit amet rhoncus mauris, nec commodo nibh. Mauris sollicitudin in quam eget tempus. Quisque convallis nisl ac dolor posuere, vel rhoncus erat placerat. Phasellus semper quam ac eros pretium mattis. Nulla facilisi. Donec tincidunt hendrerit mauris quis elementum. Nullam a ornare libero. Nullam maximus erat a nunc condimentum convallis. Ut ornare malesuada ligula, vitae consectetur nulla pretium sed."
        self.text_box = tk.Label(self, text=text, bg="#FFFFFF", fg="#000000", wraplength=300, justify="left", font=("Helvetica", 8))
        self.text_box.grid(row=5, column=0, columnspan=2, padx=padding_x, pady=padding_y, sticky="nsew")

        # Contributions
        title = tk.Label(self, text="Contributions", bg="#263D42", fg="#FFFFFF", font=("Helvetica", 10, "bold"))
        title.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=100, pady=(10, 5))
        
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam molestie malesuada ex, vitae accumsan mauris vestibulum vel. Duis at enim dignissim, consectetur sem sit amet, interdum ligula. Nunc iaculis odio ut mauris molestie, a fermentum nisi porttitor. Aenean ut finibus augue. Nunc sed augue sed nibh ultrices facilisis. Donec accumsan quam eu nisi cursus mattis. Nam odio est, tincidunt pretium velit ac, volutpat varius magna. Pellentesque rutrum rhoncus leo, vel elementum metus ultricies vel.Phasellus mattis laoreet lectus ut dignissim. Praesent rutrum dolor vitae dapibus laoreet. Aliquam vitae suscipit metus, sit amet vulputate tortor. Quisque sit amet rhoncus mauris, nec commodo nibh. Mauris sollicitudin in quam eget tempus. Quisque convallis nisl ac dolor posuere, vel rhoncus erat placerat. Phasellus semper quam ac eros pretium mattis. Nulla facilisi. Donec tincidunt hendrerit mauris quis elementum. Nullam a ornare libero. Nullam maximus erat a nunc condimentum convallis. Ut ornare malesuada ligula, vitae consectetur nulla pretium sed."
        self.text_box = tk.Label(self, text=text, bg="#FFFFFF", fg="#000000", wraplength=300, justify="left", font=("Helvetica", 8))
        self.text_box.grid(row=7, column=0, columnspan=2, padx=padding_x, pady=padding_y, sticky="nsew")
        

        # Button download paper
        self.boton1 = tk.Button(self, text="Download", command=self.on_boton1_click, height=1, width=19)
        self.boton1.grid(row=8, column=0, padx=(padding_x,4), pady=padding_y, sticky="nsew")
        
        # Button Expand Graph
        self.boton2 = tk.Button(self, text="Expland", command=self.on_boton2_click,height=1, width=10)
        self.boton2.grid(row=8, column=1, padx=(4,padding_x), pady=padding_y, sticky="nsew")
        
    def on_boton1_click(self):
        pass

    def on_boton2_click(self):
        pass
