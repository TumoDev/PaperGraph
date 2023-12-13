import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk


class UploadPaperView:
    def __init__(self, controller):
        self.controller = controller
        self.ventana = tk.Tk()
        self.configure_window()
        self.content()

    def show_error(self, error_message):
        messagebox.showerror("Error", error_message)

    def configure_window(self):
        self.ventana.title("PaperGraph")
        self.ventana.configure(bg="#263D42")
        self.ventana.geometry("600x500") 
        self.ventana.resizable(False, False)
        
        # Add logo to window        
        ruta_logo = "./assets/images/logo2.png"  
        logo = Image.open(ruta_logo)
        logo_tk = ImageTk.PhotoImage(logo)
        self.ventana.iconphoto(True, logo_tk)

        # Kill window 
        self.ventana.protocol("WM_DELETE_WINDOW", self.controller.on_close)


    def content(self):
        # Image
        ruta_imagen = "./assets/images/UploadPaper-interfaz.png"
        imagen_original = Image.open(ruta_imagen)
        imagen_redimensionada = imagen_original.resize((500, 300))  # Redimensionar a 500x300
        imagen = ImageTk.PhotoImage(imagen_redimensionada)

        label_imagen = tk.Label(self.ventana, image=imagen, bg="#263D42")
        label_imagen.image = imagen  
        label_imagen.pack(pady=(20, 0))

        # Header Text
        titulo = tk.Label(self.ventana, text="¡Dale sentido a los papers!", bg="#263D42", fg="#FFFFFF", font=("Helvetica", 24, "bold"))
        titulo.pack(pady=(10, 10))

        # Text
        descripcion = tk.Label(self.ventana, 
                                text="PaperGraph analiza automáticamente un artículo académico, inspeccionando sus referencias y contribuciones para generar un gráfico visual a partir de esta información.", 
                                bg="#263D42", 
                                fg="#A7BEBE", 
                                wraplength=500, 
                                justify="center")
        descripcion.pack(pady=(0, 20))

        # Button to upload PDF
        self.boton_subir = tk.Button(self.ventana, text="Subir Paper", command=self.subir_archivo, bg="#4A6572", fg="#FFFFFF", font=("Helvetica", 16), borderwidth=0)
        self.boton_subir.pack(pady=(0, 20))

    def subir_archivo(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("PDF files", "*.pdf")]
        )
        self.controller.handle_file_selection(file_path)