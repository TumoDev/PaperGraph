import sys
from app.View import LoadingView
from app.Utils import GPT as gpt
from app.Utils import Paper
import tkinter as tk
import json

class LoadingController:
    def __init__(self, model):
        self.model= model
        self.view=LoadingView(self)
        self.tasks=[
            #(25, "Conectando con GPT...", lambda: self.connect_GPT()),
            (50, "Recopilando Informacion del Paper...", lambda: self.search_information_paper()),
            (75, "Buscando Referencias y contribuciones...", lambda: self.search_references_and_contributions()),
            (100, "Cerrando Ventana...", lambda: self.destroy_view())
        ]
        self.current_task_index = 0

    def run(self):
        self.execute_next_task()
        self.view.window.mainloop()
        
    def update_progress(self, value, text):
        self.view.update_progress(value, text)

    def execute_next_task(self):
        if self.current_task_index < len(self.tasks):
            progress, text, task = self.tasks[self.current_task_index]
            self.update_progress(progress, text)
            task()

    def complete_task(self):
        self.current_task_index += 1
        self.view.window.after(20, self.execute_next_task)

    def on_close(self):
        sys.exit()

    def destroy_view(self):
        self.view.window.destroy()
        

    def connect_GPT(self):
        print("Connecting with GPT...")
        # Here goes the logic to connect with GPT
        self.complete_task()

    def search_information_paper(self):
        from app.Controller import InformationPaperController
        print("Searching for information...")
        #paper=GPT_funcion():
        #if paper:
        #    self.paper=paper
        #else:
        secondary_window = tk.Toplevel(self.view.window)
        InformationPaperController(self.model,secondary_window, self.complete_task).run()
        self.complete_task()

    def search_references_and_contributions(self):
        print("Searching references and contributions...")
        #print(self.model.get_paper(self.model.get_current_id_node))
        # Fragmento inicial con tokens
        introduct_fragment = gpt.extract_fragment_with_tokens('assets/papers/input_paper/archivo.pdf')

        # Analizar referencias y crear JSON de contribuciones e indices
        contributions = gpt.analyze_references(introduct_fragment)

        # Crear lista con índices de referencias
        array_indices = gpt.list_index_references(contributions)

        # Almacenar parte de referencias del PDF
        text_references = gpt.text_references_pdf('assets/papers/input_paper/archivo.pdf')

        # Extraer información de las referencias basado en los índices
        diccionario = gpt.info_references(text_references, array_indices)

        # Extraer detalles de las referencias y crear JSON final
        references = gpt.reference_details(diccionario)
        dict_references = json.loads(references)
        print(dict_references)
        print("_________________________________________")
        print(references)

        for ref in dict_references["references"]:
            paper = Paper(title=ref["title"], author=ref["author"], date=str(ref["year"]))
            self.model.add_paper(paper)
        
        self.complete_task()