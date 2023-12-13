from app.View import UploadPaperView

import sys, shutil

class UploadPaperController:
    def __init__(self):
        self.view=UploadPaperView(self)

    def run(self):
        self.view.ventana.mainloop()

    def on_close(self):
        sys.exit()

    def handle_file_selection(self, file_path):
        # Verificar si se seleccionó un archivo
        if not file_path:
            self.view.show_error("No se seleccionó ningún archivo.")
            return

        # Verificar si el archivo seleccionado es un PDF
        if not file_path.lower().endswith('.pdf'):
            self.view.show_error("El archivo seleccionado no es un PDF.")
            return

        # Copiar el archivo y actualizar la vista
        destino = "./assets/papers/input_paper/archivo.pdf"
        shutil.copy(file_path, destino)
        self.view.boton_subir.config(text=f"Archivo Seleccionado: {file_path.split('/')[-1]}")
        self.view.ventana.destroy()
    
    