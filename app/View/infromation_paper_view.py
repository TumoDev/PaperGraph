import tkinter as tk

class InformationPaperView():
    def __init__(self, controller):
        self.controller = controller
        self.ventana = tk.Tk()
        self.configure_window()
        self.content()

    def configure_window(self):
        self.ventana.title("Información del Paper")
        self.ventana.configure(bg="#263D42")
        self.ventana.geometry('300x100') 
        self.ventana.resizable(False, False)

    def content(self):
        boton_cerrar = tk.Button(self.ventana, text="Cerrar", command=self.ventana.destroy)
        boton_cerrar.pack()