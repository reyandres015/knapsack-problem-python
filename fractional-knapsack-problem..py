class BagObject:
    def __init__(self, weight, value, index):
        self.index = index
        self.weight = weight
        self.value = value
        self.report = value // weight

    # Función para definir la comparación entre dos BagObjects, comparando el ratio calculado para ordenarlos
    def __lt__(self, other):
        return self.report < other.report


def getMaxValue(peso, valores, capacidad):
    arraySort = []
    for i in range(len(peso)):
        arraySort.append(BagObject(peso[i], valores[i], i))

    # Ordena los elementos de la bolsa por su informe
    arraySort.sort(reverse=True)
    print('Objetos ordenados de mayor a menor de acuerdo a su ratio:')
    for object in arraySort:
        print(f'Objeto {object.index}; Tamaño: {object.weight}; Valor: {object.value}; Ratio: {object.report}')

    counterValue = 0
    for obj in arraySort:
        currentWeight = int(obj.weight)
        currentValue = int(obj.value)
        if capacidad - currentWeight >= 0:
            # Restamos la capacidad
            capacidad -= currentWeight
            # Agregamos el valor en la bolsa
            counterValue += currentValue
        else:
            fraccion = capacidad / currentWeight
            counterValue += currentValue * fraccion
            capacidad = int(capacidad - (currentWeight * fraccion))
            break  # Se agrega la palabra clave "break" para salir del bucle cuando la capacidad sea 0 o negativa
    return counterValue


peso = [1, 5, 3, 2, 4]
valores = [10, 50, 20, 30, 60]
capacidad = 11
maxValue = getMaxValue(peso, valores, capacidad)
print("Valor máximo en la mochila =", maxValue)
