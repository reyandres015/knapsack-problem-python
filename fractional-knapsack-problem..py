class BagObject:
    def __init__(self, weight, value, index):
        self.index = index
        self.weight = weight
        self.value = value
        self.report = value // weight

    # Función para definir la comparación entre dos BagObjects, comparando el ratio calculado para ordenarlos
    def __lt__(self, other):
        return self.report < other.report


def fillBag(peso, valores, weight):
    arraySort = []
    for i in range(len(peso)):
        arraySort.append(BagObject(peso[i], valores[i], i))

    # Ordenar los elementos de la bolsa por su ratio
    arraySort.sort(reverse=True)
    
    #Seleccion de objetos para llevar en la maleta
    counterValue = 0 #Contador para indentificar el valor maximo de los objetos de la maleta.
    selectedObjects = []
    
    print('Objetos ordenados de mayor a menor de acuerdo a su ratio:')
    for obj in arraySort:
        print(f'Objeto {obj.index}; Tamaño: {obj.weight}; Valor: {obj.value}; Ratio: {obj.report}')
        currentWeight = int(obj.weight)
        currentValue = int(obj.value)
        if weight - currentWeight >= 0:
            selectedObjects.append(obj)
            # Restamos la weight
            weight -= currentWeight
            # Agregamos el valor en la bolsa
            counterValue += currentValue
        else:
            fraction = weight / currentWeight
            counterValue += currentValue * fraction
            weight = int(weight - (currentWeight * fraction))
            
            obj.value = currentValue * fraction
            obj.weight = currentWeight * fraction
            fractionalObject = BagObject(obj.weight, obj.value, (obj.index + 0.5))
            arraySort.append(fractionalObject)
            selectedObjects.append(fractionalObject)
            break  # Se agrega la palabra clave "break" para salir del bucle cuando la weight sea 0 o negativa
    
    print('Maleta Llena')
    for obj in selectedObjects:
        print(f'Objeto {obj.index}; Tamaño: {obj.weight}; Valor: {obj.value}; Ratio: {obj.report}')
    print(f'Valor Maximo: {counterValue}')
    print(f'Capacidad: {weight}')


peso = [1, 6, 3, 2, 4]
valores = [10, 50, 20, 30, 60]
weight = 11
fillBag(peso, valores, weight)
