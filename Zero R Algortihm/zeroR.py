import csv

class ZeroR:
    def __init__(self):
        self.datasetName    = ""
        self.dataset        = []
        self.attClass       = -1
        self.attNames       = []
        self.allClasses     = []
        self.dictClasses    = {}
        self.model          = {}

    #Abre el csv
    def loadData(self,nameDataset):
        with open(nameDataset, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            self.dataset = list(reader)
            self.attNames = reader.fieldnames
        return
    #Set de clases
    def setClasses(self):  
        for linha in self.dataset:
            self.allClasses.append(linha[self.attNames[self.attClass]])

            if (linha[self.attNames[self.attClass]]) not in self.dictClasses:
                self.dictClasses.update({ linha[self.attNames[self.attClass]]:1} )

            else:
                self.dictClasses[linha[self.attNames[self.attClass]]] += 1
        return
    
    #Se genera el modelo
    def generateModel(self):
        # Usando la clase mas frecuente para generar el modelo
        maxi = max(self.dictClasses, key=self.dictClasses.get)
        print("Modelo: \n ",self.attNames[self.attClass],"=>",maxi)


    #funcion de ejecucion
    def ejecutarZeroR(name_csv):
        zz= ZeroR()
        zz.loadData(name_csv)
        zz.setClasses()
        zz.generateModel()
        print(zz.dictClasses)




