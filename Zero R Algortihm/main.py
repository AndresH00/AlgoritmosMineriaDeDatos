import pandas as pd
from naives import ejecutarNaives
from sklearn.model_selection import train_test_split
from zeroR import ZeroR
from oneR import OneR

menu = True
while(menu):
    opcion = 0
    opcion = int(input(
        """
        Elije una de las siguientes opciones:
        1.- Zero R
        2.- One R
        3.- Naives
        4.- Salir
        """
    ))
    if opcion == 4:
        menu = False
    elif opcion < 4 and opcion > 0:
        file_name = str(input('Dame el nombre del archivo: '))
        numero_testeo = int(input('Dame el numero de datos que seran para testeo: '))
        try:
            arc = pd.read_csv(file_name)
        except:
            print("Nombre de archivo o el archivo no es valido")
            opcion = 100
        if opcion == 1:
            ZeroR.ejecutarZeroR(file_name)
        elif opcion == 2:
            nombre_clase = str(input('Dame el nombre de la columna de la clase: '))
            clf = OneR()
            y_class =  exec('arc[\''+nombre_clase+'\']')
            clf_mush = OneR()
            results = clf_mush.fit(arc, y_class)

            print(clf_mush)
            exec('arc.pop(\''+nombre_clase+'\')')
            X_train, X_test, y_train, y_test = train_test_split(arc,y_class, test_size=numero_testeo,random_state=42)
            results = clf.fit(X_train, X_test)
            print(results)
            print(clf)
        elif opcion == 3:
            X_train, X_test = train_test_split(arc, test_size=numero_testeo)
            ejecutarNaives(X_train,X_test)
    else:
        print(opcion + "no es valida")



    