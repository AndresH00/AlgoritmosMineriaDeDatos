import pandas as pd

class OneR(object):
    
    def __init__(self):
        self.ideal_variable = None
        self.max_accuracy = 0
    
    def fit(self, X, y):
        response = list()
        result = dict()
        
        dfx = pd.DataFrame(X)
        
        for i in dfx:
            result[str(i)] = dict()
            options_values = set(dfx[i])
            join_data = pd.DataFrame({"variable":dfx[i], "label":y})
            cross_table = pd.crosstab(join_data.variable, join_data.label)
            summary = cross_table.idxmax(axis=1)
            result[str(i)] = dict(summary)
            
            counts = 0
            
            for idx, row in join_data.iterrows():
                if row['label'] == result[str(i)][row['variable']]:
                    counts += 1

            accuracy = (counts/len(y))
            
            if accuracy > self.max_accuracy:
                self.max_accuracy = accuracy
                self.ideal_variable = i

            result_feature = {"variable": str(i), "exactitud":accuracy, "regla": result[str(i)] }  
            response.append(result_feature)
            
        return response

    
    def predict(self, X=None):
        #cambiar si se necesita
        self.ideal_variable = self.ideal_variable + 1
        
    def __repr__(self):
        if self.ideal_variable != None:
            txt = "La mejor variable para tus datos es: " + str(self.ideal_variable)
        else:
            txt = "La mejor variable aun no se ha encontrado, intente ejecutar el metodo fit previamente"
        return txt