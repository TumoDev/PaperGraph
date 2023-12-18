from app.View import InformationPaperView

class InformationPaperController:
    def __init__(self):
        self.view = InformationPaperView(self)

    def run(self):
        self.view.ventana.mainloop()