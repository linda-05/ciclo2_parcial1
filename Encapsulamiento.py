class TarjetaPrepago:
    def __init__(self, numero, saldo_inicial=0):
        self.numero = numero
        self.__saldo = saldo_inicial  # Atributo privado
    
    def recargar(self, monto):
        """Aumenta el saldo validando que el monto sea positivo"""
        if monto > 0:
            self.__saldo += monto
            return True, f" Recarga exitosa: ${monto:.2f}"
        else:
            return False, " Error: El monto de recarga debe ser positivo"
    
    def consumir(self, monto):
        """Resta del saldo validando que no quede negativo"""
        if monto <= 0:
            return False, " Error: El monto de consumo debe ser positivo"
        
        if self.__saldo >= monto:
            self.__saldo -= monto
            return True, f" Consumo exitoso: ${monto:.2f}"
        else:
            return False, f" Error: Saldo insuficiente. Saldo actual: ${self.__saldo:.2f}"
    
    def consultarSaldo(self):
        """Muestra el saldo actual"""
        return f" Saldo actual: ${self.__saldo:.2f}"

# Función para mostrar el menú
def mostrar_menu():
    print("\n" + "="*40)
    print("       SISTEMA DE TARJETA PREPAGO")
    print("="*40)
    print("1. Consultar saldo")
    print("2. Recargar tarjeta")
    print("3. Realizar consumo")
    print("4. Salir")
    print("="*40)

# Función principal
def main():
    # Crear tarjeta con saldo inicial de 200
    tarjeta = TarjetaPrepago("1234-5678-9012-3456", 200)
    
    print("¡Bienvenido al Sistema de Tarjeta Prepago!")
    print(f"Se ha creado una tarjeta con saldo inicial de $200.00")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSeleccione una opción (1-4): ").strip()
            
            if opcion == "1":
                # Consultar saldo
                print("\n" + "-"*30)
                print(tarjeta.consultarSaldo())
                
            elif opcion == "2":
                # Recargar tarjeta
                print("\n" + "-"*30)
                print("RECARGAR TARJETA")
                try:
                    monto = float(input("Ingrese el monto a recargar: $"))
                    exito, mensaje = tarjeta.recargar(monto)
                    print(mensaje)
                    if exito:
                        print(tarjeta.consultarSaldo())
                except ValueError:
                    print(" Error: Por favor ingrese un número válido")
                    
            elif opcion == "3":
                # Realizar consumo
                print("\n" + "-"*30)
                print("REALIZAR CONSUMO")
                try:
                    monto = float(input("Ingrese el monto a consumir: $"))
                    exito, mensaje = tarjeta.consumir(monto)
                    print(mensaje)
                    if exito:
                        print(tarjeta.consultarSaldo())
                except ValueError:
                    print(" Error: Por favor ingrese un número válido")
                    
            elif opcion == "4":
                # Salir
                print("\n" + "-"*30)
                print("¡Gracias por usar el sistema!")
                print("Saldo final:", tarjeta.consultarSaldo())
                break
                
            else:
                print(" Opción no válida. Por favor seleccione 1-4")
                
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario")
            break
        except Exception as e:
            print(f" Error inesperado: {e}")

if __name__ == "__main__":
    main()