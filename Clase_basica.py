class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
    def es_mayor_de_edad(self):
        """Indica en texto si la persona es mayor o menor de edad"""
        if self.edad >= 18:
            return "Sí, es mayor de edad."
        else:
            return "No, es menor de edad."
    
    def mostrar_datos(self):
        print(self.saludar())


# --- Prueba de la clase ---
p1 = Persona("Carlos", 20)   # mayor de edad
p2 = Persona("Ana", 15)      # menor de edad

p1.mostrar_datos()
print(p1.es_mayor_de_edad())

p2.mostrar_datos()
print(p2.es_mayor_de_edad())
