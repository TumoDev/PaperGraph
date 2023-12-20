import tkinter as tk

class InformationPaperView():
    def __init__(self, controller, window):
        self.controller = controller
        self.window = window
        self.configure_window()
        self.content()
        
    def configure_window(self):
        self.window.title("Información del Paper")
        self.window.configure(bg="#263D42")
        self.window.geometry('300x100') 
        self.window.resizable(False, False)
        

    def content(self):
        boton_cerrar = tk.Button(self.window, text="Cerrar", command=self.controller.destroy_view)
        boton_cerrar.pack()