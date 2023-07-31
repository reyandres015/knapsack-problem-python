# knapsack-problem-python
# Problema de la Mochila

Este repositorio contiene soluciones en Python para el problema de la mochila (Knapsack Problem) en sus versiones no fraccionada y fraccionada.

## Descripción del Código

### Versión No Fraccionada

El archivo `no-fractional-knapsack-problem..py` contiene una implementación del problema de la mochila no fraccionada. Se define una clase `BagObject` para representar los objetos que pueden ir en la mochila, y se implementa el método `__lt__` para permitir la comparación de objetos basada en su ratio valor/peso.

La función `fillBag` recibe tres listas: `peso`, `valores` y `weight`, que representan el peso de cada objeto, el valor de cada objeto y la capacidad de la mochila, respectivamente. La función selecciona los objetos de mayor valor que puedan caber en la mochila y muestra los objetos seleccionados y el valor máximo alcanzado.

### Versión Fraccionada

El archivo `fractional-knapsack-problem..py` contiene una implementación del problema de la mochila fraccionada. Al igual que en la versión no fraccionada, se define la clase `BagObject` para representar los objetos que pueden ir en la mochila.

La función `fillBag` recibe tres listas: `peso`, `valores` y `weight`, que representan el peso de cada objeto, el valor de cada objeto y la capacidad de la mochila, respectivamente. La función selecciona los objetos de mayor valor que puedan caber en la mochila, ajustando fraccionalmente el peso si es necesario, y muestra los objetos seleccionados y el valor máximo alcanzado.

## Ejemplo de Uso

Para utilizar los códigos, simplemente ejecuta los archivos `no-fractional-knapsack-problem..py` y `fractional-knapsack-problem..py`. Puedes modificar las listas `peso`, `valores` y `weight` con los valores deseados para realizar pruebas con diferentes conjuntos de objetos y capacidades de la mochila.

```python
# Ejemplo para la versión no fraccionada
peso = [1, 6, 3, 2, 4]
valores = [10, 50, 20, 30, 60]
weight = 11
fillBag(peso, valores, weight)

# Ejemplo para la versión fraccionada
peso = [1, 5, 3, 2, 4]
valores = [10, 50, 20, 30, 60]
weight = 11
fillBag(peso, valores, weight)
```

## Contribuciones

Siéntete libre de realizar mejoras, corregir errores o agregar nuevas funcionalidades al código. Las contribuciones son bienvenidas y te agradeceremos si deseas enviar un pull request. Esperamos que estos códigos te sean útiles para resolver el problema de la mochila en ambas versiones. Si tienes alguna pregunta o sugerencia, no dudes en comunicarte.
¡Gracias por visitar este repositorio!

