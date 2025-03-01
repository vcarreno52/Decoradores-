import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time of {func.__name__}: {end - start:.6f} seconds")
        return result
    return wrapper

class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def CalcularDistancia(self, punto):
        return ((self.x - punto.x) ** 2 + (self.y - punto.y) ** 0.5)

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

class Shape:
    def __init__(self, vertices: list[Punto], edges: list[Linea], angulos_internos: list[float]):
        self._vertices = vertices
        self._edges = edges
        self._angulos_internos = angulos_internos
        self._es_poligono_regular = self._verificar_poligono_regular()
    
    @property
    def vertices(self):
        return self._vertices
    
    @property
    def edges(self):
        return self._edges
    
    @property
    def angulos_internos(self):
        return self._angulos_internos
    
    @property
    def es_poligono_regular(self):
        return self._es_poligono_regular
    
    def _verificar_poligono_regular(self):
        lados = [edge.largo for edge in self._edges]
        angulos = self._angulos_internos
        return all(lado == lados[0] for lado in lados) and all(angulo == angulos[0] for angulo in angulos)
    
    @time_it
    def calcular_area(self):
        pass
    
    def calcular_perimetro(self):
        return sum(edge.largo for edge in self._edges)
    
    @classmethod
    def set_tipo(cls, nuevo_tipo):
        cls.tipo = nuevo_tipo

class Triangulo(Shape):
    @time_it
    def calcular_area(self):
        a, b, c = [edge.largo for edge in self._edges]
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

class TrianguloIsosceles(Triangulo):
    @time_it
    def calcular_area(self):
        a, b, c = [edge.largo for edge in self._edges]
        if a == b or b == c or a == c:
            s = (a + b + c) / 2
            return (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return "No es isósceles"

class TrianguloEscaleno(Triangulo):
    @time_it
    def calcular_area(self):
        a, b, c = [edge.largo for edge in self._edges]
        if a != b and b != c and a != c:
            s = (a + b + c) / 2
            return (s * (s - a) * (s - b) * (s - c)) ** 0.5

class TrianguloRectangulo(Triangulo):
    @time_it
    def calcular_area(self):
        a, b, c = sorted([edge.largo for edge in self._edges])
        return (a * b) / 2

class TrianguloEquilatero(Triangulo):
    @time_it
    def calcular_area(self):
        a = self._edges[0].largo
        return ((3) ** 0.5 / 4) * (a ** 2)

class Rectangulo(Shape):
    @time_it
    def calcular_area(self):
        a, b = [self._edges[0].largo, self._edges[1].largo]
        return a * b

class Cuadrado(Rectangulo):
    @time_it
    def calcular_area(self):
        lado = self._edges[0].largo
        return lado ** 2
    
    def calcular_perimetro(self):
        lado = self._edges[0].largo
        return 4 * lado
