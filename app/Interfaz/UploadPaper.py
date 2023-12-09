import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import shutil


class UploadPaper:
    def __init__(self):
        self.ventana = tk.Tk()
        self.configure_window()
        self.create_widgets()
        self.ventana.resizable(False, False)

    def run(self):
        self.ventana.mainloop()

    def configure_window(self):
        self.ventana.title("PaperGraph - Análisis de Artículo Académico")
        self.ventana.configure(bg="#263D42")
        self.ventana.geometry("600x500") 

        # Añadir logo a la ventana
        ruta_logo = "./assets/images/logo2.png"  # Asegúrate de que esta ruta sea correcta
        logo = Image.open(ruta_logo)
        logo_tk = ImageTk.PhotoImage(logo)
        self.ventana.iconphoto(True, logo_tk)

    def create_widgets(self):
        # Cargar y redimensionar la imagen
        ruta_imagen = "./assets/images/UploadPaper-interfaz.png"
        imagen_original = Image.open(ruta_imagen)
        imagen_redimensionada = imagen_original.resize((500, 300))  # Redimensionar a 500x300
        imagen = ImageTk.PhotoImage(imagen_redimensionada)

        label_imagen = tk.Label(self.ventana, image=imagen, bg="#263D42")
        label_imagen.image = imagen  # Mantener una referencia
        label_imagen.pack(pady=(20, 0))

        # Agregar título
        titulo = tk.Label(self.ventana, text="¡Dale sentido a los papers!", bg="#263D42", fg="#FFFFFF", font=("Helvetica", 24, "bold"))
        titulo.pack(pady=(10, 10))

        # Descripción
        descripcion = tk.Label(self.ventana, 
                                text="PaperGraph analiza automáticamente un artículo académico, inspeccionando sus referencias y contribuciones para generar un gráfico visual a partir de esta información.", 
                                bg="#263D42", 
                                fg="#A7BEBE", 
                                wraplength=500, 
                                justify="center")
        descripcion.pack(pady=(0, 20))

        # Botón para subir archivos
        self.boton_subir = tk.Button(self.ventana, text="Subir Paper", command=self.subir_archivo, bg="#4A6572", fg="#FFFFFF", font=("Helvetica", 16), borderwidth=0)
        self.boton_subir.pack(pady=(0, 20))

    def subir_archivo(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("PDF files", "*.pdf")]  # Esto limita el diálogo para mostrar solo archivos PDF.
        )

        # Verificar si el archivo no se seleccionó
        if not file_path:
            messagebox.showerror("Error", "No se seleccionó ningún archivo.")
            return  # Salir de la función si no hay archivo

        # Verificar si el archivo no es un PDF
        if not file_path.lower().endswith('.pdf'):
            messagebox.showerror("Error", "El archivo seleccionado no es un PDF.")
            return  # Salir de la función si no es PDF

        # Copiar el archivo a una nueva ubicación
        destino = "./assets/papers/input_paper/archivo.pdf"
        shutil.copy(file_path, destino)

        # Actualizar el botón y cerrar la ventana
        self.boton_subir.config(text=f"Archivo Seleccionado: {file_path.split('/')[-1]}")
        self.ventana.destroy()  # Cierra la ventana de Tkinter
