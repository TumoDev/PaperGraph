import sys
import threading
from app.View import LoadingView 

class LoadingController:
    def __init__(self):
        self.view = LoadingView(self)
        self.tasks = [
            (15, "Conectando con GPT...", self.connect_gpt),
            (30, "Recopilando Informacion del Paper...", self.search_information_paper),
            (45, "Buscando Referencias...", self.search_references),  
            (60, "Buscando Contribuciones...", self.search_contributions),  
            (99, "Armando Grafo...", self.arming_graph)
        ]
        
    def run(self):
        self.start_loading_process()
        self.view.ventana.mainloop()
        
    def update_progress(self, value, text):
        self.view.update_progress(value, text)

    def start_loading_process(self):
        # Inicia todas las tareas en un único hilo
        threading.Thread(target=self.execute_all_tasks).start()

    def execute_all_tasks(self):
        for progress, text, task in self.tasks:
            self.update_progress(progress, text)
            task()
        # Todas las tareas han terminado, cierra la ventana
        self.view.ventana.after(0, self.destroy_view)

    def run_task(self, task):
        task()
        self.view.ventana.after(0, self.execute_next_task)

    def on_close(self):
        sys.exit()

    def destroy_view(self):
        self.view.ventana.destroy()

    def connect_gpt(self): #deivit
        # Implement the logic for connecting to GPT here
        print("Connecting with GPT...")
        # Ensure that this function does not block, perform operations in a thread if necessary

    def search_information_paper(self):
        from app.Controller import InformationPaperController

        self.view.ventana.withdraw()
        print("Searching for information...")
        InformationPaperController().run()
        self.view.ventana.deiconify()

    def search_references(self): #deivit
        # Implement the logic for searching references here
        print("Searching for references...")
        # Ensure that this function does not block, perform operations in a thread if necessary
        

    def search_contributions(self): #deivit
        # Implement the logic for searching contributions here
        print("Searching for contributions...")
        # Ensure that this function does not block, perform operations in a thread if necessary

    def arming_graph(self):
        # Implement the logic for graph construction here
        print("Constructing graph...")
        # Ensure that this function does not block, perform operations in a thread if necessary
