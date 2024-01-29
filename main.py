from app.Model import GraphModel
from app.View import UploadPaperView, LoadingView, AplicationView
from app.Controller import UploadPaperController, LoadingController, AplicationController



def main():
    UploadPaperController().run()
    
    model=GraphModel()

    LoadingController(model).run()
    model.print_graph()
    AplicationController(model).run()
    
   
if __name__ == "__main__":
   main()


