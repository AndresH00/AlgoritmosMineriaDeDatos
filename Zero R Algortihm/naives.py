from csv import reader
from math import sqrt
from math import exp
from math import pi
 
# Carga de csv
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset
 
# Convertir columnas a string que no sirvio
# def str_column_to_float(dataset, column):
#     for row in dataset:
#         row[column] = float(row[column].strip())
 
# Conversor de string a int
def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
		print('[%s] => %d' % (value, i))
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup
 
# Separar el dataset por clase y valores, regresa un diccionario
def separate_by_class(dataset):
	separated = dict()
	for i in range(len(dataset)):
		vector = dataset[i]
		class_value = vector[-1]
		if (class_value not in separated):
			separated[class_value] = list()
		separated[class_value].append(vector)
	return separated
 
# Calcular el promedio de una lista de numeros
def mean(numbers):
	return sum(numbers)/float(len(numbers))
 
# calcular la desviacion estandar de una lista de numeros
def stdev(numbers):
	avg = mean(numbers)
	variance = sum([(x-avg)**2 for x in numbers]) / float(len(numbers)-1)
	return sqrt(variance)
 
# Calcula el promedio , desviacion estandar por cada columna en el dataset
def summarize_dataset(dataset):
	summaries = [(mean(column), stdev(column), len(column)) for column in zip(*dataset)]
	del(summaries[-1])
	return summaries
 
# Divide el dataset por clase y calcula las estadisticas por cada fila
def summarize_by_class(dataset):
	separated = separate_by_class(dataset)
	summaries = dict()
	for class_value, rows in separated.items():
		summaries[class_value] = summarize_dataset(rows)
	return summaries
 
# Calcula la funcion de la probabilidad de distribucion gaussiana para x
def calculate_probability(x, mean, stdev):
	exponent = exp(-((x-mean)**2 / (2 * stdev**2 )))
	return (1 / (sqrt(2 * pi) * stdev)) * exponent

# Calcula las probabilidadees de predecir cada clase por una fila seleccionada 
def calculate_class_probabilities(summaries, row):
	total_rows = sum([summaries[label][0][2] for label in summaries])
	probabilities = dict()
	for class_value, class_summaries in summaries.items():
		probabilities[class_value] = summaries[class_value][0][2]/float(total_rows)
		for i in range(len(class_summaries)):
			mean, stdev, _ = class_summaries[i]
			probabilities[class_value] *= calculate_probability(row[i], mean, stdev)
	return probabilities

# Predice la clase de una fila en especifico 
def predict(summaries, row):
	probabilities = calculate_class_probabilities(summaries, row)
	best_label, best_prob = None, -1
	for class_value, probability in probabilities.items():
		if best_label is None or probability > best_prob:
			best_prob = probability
			best_label = class_value
	return best_label
 

# Funcion para predecir con Naive Bayes en el dataset de Iris
def ejecutarNaives(dataTrain, dataTest):
    # filename = str(input("Dame el nombre del archivo csv para entrenar: "))
    # nameAtt = str(input('Tiene el nombre de los atributos en la primera linea (si, no): '))
    # dataset = load_csv(filename)
    count_row = dataTrain.shape[0]  # Gives number of rows
    count_col = dataTrain.shape[1]  # Gives number of columns
    dataset = []
    for x in range(count_row):
        lista_row = []
        for y in range(count_col):
            lista_row.append(dataTrain.iloc[x][y])
        dataset.append(lista_row)
    print(dataset)
    # if nameAtt.lower() == "si":
    #     nameAtt = dataset[0]
    #     dataset.pop(0)
    # for i in range(len(dataset[0])-1):
    #     str_column_to_float(dataset, i)
    # convert class column to integers
    str_column_to_int(dataset, len(dataset[0])-1)
    # fit model
    model = summarize_by_class(dataset)
    # define a new record
    # filename = str(input("Dame el nombre del archivo csv para practicar: "))
    # nameAtt = str(input('Tiene el nombre de los atributos en la primera linea (si, no): '))
    # dataset = load_csv(filename)

    # if nameAtt.lower() == "si":
    #     nameAtt = dataset[0]
    #     dataset.pop(0)
    count_row = dataTest.shape[0]  # Gives number of rows
    count_col = dataTest.shape[1]  # Gives number of columns
    dataset = []
    for x in range(count_row):
        lista_row = []
        for y in range(count_col):
            lista_row.append(dataTest.iloc[x][y])
        dataset.append(lista_row)
    # for i in range(len(dataset[0])-1):
    #     str_column_to_float(dataset, i)
    str_column_to_int(dataset, len(dataset[0])-1)
    total = 0
    errores = 0
    for row in dataset:
        linea = []
        resultadoEsperado = row[-1]
        for i in range(len(dataset[0])-1):
            linea.append(row[i])
        # predict the label
        label = predict(model, linea)
        total += 1
        if label != resultadoEsperado:
            errores +=1
        print('Data=%s, Predicted: %s Expected: %s' % (linea, label, resultadoEsperado))
    print('Total datos de prueba: {} | Errores: {} | Porcentaje de error: {}% | Porcentaje de acierto: {}%'.format(total,errores,round((errores/total*100),2),round((100-(errores/total*100)),2)))

