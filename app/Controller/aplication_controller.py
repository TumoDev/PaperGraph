from app.View import AplicationView

import sys

class AplicationController:
    def __init__(self):
        self.view=AplicationView(self)
    
    def run(self):
        self.view.ventana.mainloop()

    def on_close(self):
        sys.exit()