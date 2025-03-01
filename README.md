# Shape Decorators Challenge

Descripción

Este proyecto implementa una jerarquía de clases para representar figuras geométricas en Python, incorporando decoradores para mejorar la encapsulación, la gestión de atributos y la medición del tiempo de ejecución de ciertos métodos.

Objetivos del Reto

# Encapsulación con @property: 
Se usó el decorador @property en la clase Shape y otras clases para permitir el acceso a atributos protegidos sin exponerlos directamente.
        class Linea:
    def __init__(self, punto_inicial: Punto, punto_final: Punto):
        self.punto_inicial = punto_inicial    
        self.punto_final = punto_final
        self._largo = self.Calcular_largo()
    
    def Calcular_largo(self):
        return self.punto_inicial.CalcularDistancia(self.punto_final)
    
    @property
    def largo(self):
        return self._largo

# Método de clase con @classmethod: 
Se agregó @classmethod en la clase Shape para definir y cambiar el tipo de figura.
        

# Decorador personalizado para medir tiempo de ejecución: 
Se creó un decorador time_it que mide el tiempo de ejecución de los métodos que calculan el área.

        class TrianguloEquilatero(Triangulo):
          @time_it
          def calcular_area(self):
          a = self._edges[0].largo
          return ((3) ** 0.5 / 4) * (a ** 2)
