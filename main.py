from app.Controller import UploadPaperController, AplicationController

def main():
    app=UploadPaperController()
    app.run()
    
    app=AplicationController()
    app.run()
   

    #view = AplicationView()  # Crear la vista
    #controller = UploadPaperController(view)  # Crear el controlador y pasarle la vista
    #view.set_controller(controller)  # Establecer el controlador en la vista

    #view.run()
    #app = AplicationController()
    #app.run()


    """
    #iniciar el objeto paper-+-+
    #ruta_paper = ".\\assets\\input_paper\\paper_main.pdf"
    paper_main=Paper(name="Interval Branch-and-Bound algorithms for optimization and constraint satisfaction: a survey and prospects",
                     author="Ignacio Araya1 y Victor Reyes",
                     date="6 December 2015",
                     id_name_location="input_paper/paper_main") 
    
    
    #extraer referencias
    paper_main.set_content()
    paper_main.extract_references()
    
    """
    #descargar papers
    #list_papers=paper_main.references
    #for paper in list_papers:
    #    if not paper.download_paper():
    #        paper_main.references.remove(paper)
    """

    #buscar contribuciones y graficar
    
    contributions=GPT.extract_contributions(paper_main.content,paper_main.references)

    if not contributions:
        return
    
    names=[]
    authors=[]
    rate=[]

    """
    #for i in range(0,len(contributions),3):
    #    names.append(contributions[i])
    #    authors.append(contributions[i+1])
    #    rate.append(contributions[i+2])
    """
    nodes=[]
    node1 = Node("1", paper_main.name)
    nodes.append(node1)
    num_paper=1
    for i in range(0,len(contributions),3):
        num_paper+=1
        nodes.append(Node(num_paper,contributions[i] + contributions[i+1] ,[nodes[0]],[contributions[i+2]]))
    
    
    #graficar resultados
    # Creación de nodos del gráfico
    root = tk.Tk()
    root.title("Visualizador de Gráficos")

    # Creación del visualizador
    visualizer = GraphVisualizer(root)

    # Calcular posiciones de los nodos
    positions = visualizer.generate_positions_by_level(nodes[0], 800, 500)

    # Dibujar el gráfico
    visualizer.draw_graph(nodes, positions)

    root.mainloop()
    """

if __name__ == "__main__":
   main()


