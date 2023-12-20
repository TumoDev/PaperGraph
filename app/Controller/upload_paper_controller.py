from app.View import UploadPaperView

import sys, shutil

class UploadPaperController:
    def __init__(self):
        self.view=UploadPaperView(self)

    def run(self):
        self.view.window.mainloop()

    def on_close(self):
        sys.exit()

    def file_selection(self, file_path):
        # Check if a file was selected
        if not file_path:
            self.view.show_error("No se seleccionó ningún archivo.")
            return

        # Check if the selected file is a PDF
        if not file_path.lower().endswith('.pdf'):
            self.view.show_error("El archivo seleccionado no es un PDF.")
            return

        # Copy the file and update the view
        file_destination = "./assets/papers/input_paper/archivo.pdf"
        shutil.copy(file_path, file_destination)
        self.view.upload_button.config(text=f"Archivo Seleccionado: {file_path.split('/')[-1]}")
        self.view.window.destroy()
    
    