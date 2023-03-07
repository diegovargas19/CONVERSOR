#App para convertir pies a metros usando tkinter
#Vargas Gonzalez Diego Alejandro
#23 de febrero 2023

from tkinter import*
from tkinter import ttk


class Conversor:
    #init es el tipo constructor de la clase
    def __init__(self, raiz):#raiz = root
        raiz.title("Pies a metros")

        self.pies = StringVar()
        self.metros = StringVar()

        mainFrame = ttk.Frame(raiz, padding="3 3 12 12")#izquierda arriba derecha abajo
        mainFrame.grid(column=0, row=0)
        
        piesEntry = ttk.Entry(mainFrame, textvariable=self.pies, width=7)
        piesEntry.grid(column=1, row=0, sticky=(W, E))

        ttk.Label(mainFrame, text="pies").grid(column=2, row=0)
        
        ttk.Label(mainFrame, text="Son equivalentes a:").grid(column=0, row=1)

        ttk.Label(mainFrame, textvariable=self.metros).grid(column=1, row=1)

        ttk.Label(mainFrame, text="metros").grid(column=2, row=1)

        ttk.Button(mainFrame, text="Calcular", command=self.calcular).grid(column=2, row=2)
        piesEntry.focus()
        #Hacer la operacion presionando <enter>
        raiz.bind("<Return>", self.calcular)

    def calcular(self, *args):
         print("Boton presionado")  
         piesUsuario = self.pies.get() #siempre devuelve una cadena.
         print("Pies ingresados: ", piesUsuario)   

         try:
            piesFlotante =float(piesUsuario)#con el float convierte la cadena a flotante.  
            metros = piesFlotante / 3.281 
            print("Metros: ", metros)
            self.metros.set(metros)
         except ValueError: 
            print("No es un dato valido.")
            self.pies.set("")
        


if __name__=="__main__":
    print("Este es el archivo principal.")
    print("Nada mas se mostrara este mensaje si es el principal")
