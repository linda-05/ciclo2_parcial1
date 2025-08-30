from abc import ABC, abstractmethod
import math

# Clase abstracta
class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

# Subclase Rectángulo
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

# Subclase Círculo
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

# Programa de prueba
rectangulo = Rectangulo(5, 3)
circulo = Circulo(4)

print(f"Área del rectángulo: {rectangulo.area()}")
print(f"Área del círculo: {circulo.area():.2f}")  # con dos decimales