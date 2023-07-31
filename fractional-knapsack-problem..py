# Definición de la clase BagObject para representar los objetos que pueden ir en la mochila.
class BagObject:
    def __init__(self, weight, value, index):
        self.index = index
        self.weight = weight
        self.value = value
        self.report = value // weight  # Ratio valor/peso del objeto

    # Función para definir la comparación entre dos BagObjects, comparando el ratio calculado para ordenarlos
    def __lt__(self, other):
        return self.report < other.report

# Función para llenar la mochila seleccionando objetos de mayor valor y ajustando su peso fraccionalmente si es necesario.
def fillBag(peso, valores, weight):
    arraySort = []
    for i in range(len(peso)):
        arraySort.append(BagObject(peso[i], valores[i], i))

    # Ordenar los elementos de la bolsa por su ratio de mayor a menor
    arraySort.sort(reverse=True)
    
    counterValue = 0  # Contador para identificar el valor máximo de los objetos en la mochila.
    selectedObjects = []  # Lista para almacenar los objetos seleccionados.

    print('Objetos ordenados de mayor a menor de acuerdo a su ratio:')
    for obj in arraySort:
        print(f'Objeto {obj.index}; Tamaño: {obj.weight}; Valor: {obj.value}; Ratio: {obj.report}')
        currentWeight = int(obj.weight)
        currentValue = int(obj.value)
        if weight - currentWeight >= 0:  # Si el peso del objeto cabe en la mochila
            selectedObjects.append(obj)  # Agregamos el objeto a la lista de objetos seleccionados.
            weight -= currentWeight  # Identificamos la nueva capacidad de la mochila.
            counterValue += currentValue  # Sumamos el valor del objeto al contador de valor total de la mochila.
        else: #En caso que un objeto completo no quepa en la mochila:
            fraction = weight / currentWeight  # Calculamos la fracción del objeto que podemos llevar.
            counterValue += currentValue * fraction  # Agregamos el valor fraccional del objeto al contador de valor total.
            weight = int(weight - (currentWeight * fraction))  # Reducimos la capacidad de la mochila según el peso fraccional del objeto.

            # Actualizamos el peso y valor del objeto para reflejar el peso fraccional y lo agregamos como un nuevo objeto fraccional.
            obj.value = currentValue * fraction
            obj.weight = currentWeight * fraction
            fractionalObject = BagObject(obj.weight, obj.value, (obj.index + 0.5))
            arraySort.append(fractionalObject)  # Agregamos el nuevo objeto fraccional a la lista de objetos ordenados.
            selectedObjects.append(fractionalObject)  # Agregamos el nuevo objeto fraccional a la lista de objetos seleccionados.
            break

    # Impresión de resultados
    print('Maleta Llena')
    for obj in selectedObjects:
        print(f'Objeto {obj.index}; Tamaño: {obj.weight}; Valor: {obj.value}; Ratio: {obj.report}')
    print(f'Valor Maximo: {counterValue}')
    print(f'Capacidad restante: {weight}')

#Ejecución
peso = [1, 6, 3, 2, 4]
valores = [10, 50, 20, 30, 60]
weight = 11
fillBag(peso, valores, weight)
