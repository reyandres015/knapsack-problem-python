class BagObject:
    def __init__(self, weight, value, index):
        self.index = index
        self.weight = weight
        self.value = value
        self.report = value // weight

    # Función para la comparación entre dos BagObjects
    # Comparamos el ratio calculado para ordenarlos
    def __lt__(self, other):
        return self.report < other.report


def fillBag(pesos, values, weight):
    arraySort = []
    for i in range(len(pesos)):
        arraySort.append(BagObject(pesos[i], values[i], i))

    # Ordenar los elementos de la bolsa por su informe
    arraySort.sort(reverse=True)

    selectedObjects = []  # Lista para almacenar los objetos seleccionados.
    counterValue = 0
    
    print('Objetos ordenados de mayor a menor de acuerdo a su ratio:')
    for obj in arraySort:
        print(f'Objeto {obj.index}; Tamaño: {obj.weight}; Valor: {obj.value}; Ratio: {obj.report}')
        currentWeight = int(obj.weight)
        currentValue = int(obj.value)
        if weight - currentWeight >= 0:
            selectedObjects.append(obj)  # Agregamos el objeto a la lista de objetos seleccionados.
            weight -= currentWeight # Restamos la weight
            counterValue += currentValue # Agregamos el valor en la bolsa
        else : 
            break

# Impresión de resultados
    print('Maleta Llena')
    for obj in selectedObjects:
        print(f'Objeto {obj.index}; Tamaño: {obj.weight}; Valor: {obj.value}; Ratio: {obj.report}')
    print(f'Valor Maximo: {counterValue}')
    print(f'Capacidad restante: {weight}')


pesos = [1, 5, 3, 2, 4]
values = [10, 50, 20, 30, 60]
weight = 11
fillBag(pesos, values, weight)

