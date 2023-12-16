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
        self.execute_next_task()

    def execute_next_task(self):
        if self.tasks:
            progress, text, task = self.tasks.pop(0)
            self.update_progress(progress, text)
            threading.Thread(target=lambda: self.run_task(task)).start()
        else:
            # Todas las tareas han terminado, cierra la ventana
            self.destroy_view()

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
        # Implement the logic for searching information of the paper here
        print("Searching for paper information...")
        # Ensure that this function does not block, perform operations in a thread if necessary

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
