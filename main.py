import os

def validarEdad():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad <= 0:
                print("❌ Edad inválida. La edad debe ser mayor a 0. 🎰")
            elif edad < 18:
                print("🚫 Lo sentimos. Debés tener al menos 18 años para ingresar al casino. 🎰")
            else:
                return edad
        except ValueError:
            print("❌ Entrada inválida. Ingresá un número válido para la edad. 🔢")

def mostrarMenu():
    while True:
        print(f"Opciones de juegos: ")
        print(f"1. Ruleta")
        print(f"2. Black Jack")
        print(f"3. Slots")
    
        print(f"0. Salir")
        
        try:
            respuesta = int(input("Indica a que juego desea jugar: "))

            while respuesta not in [1, 2, 0]:
                 print("❌ Opción inválida. Por favor ingresá 1, 2 o 0 según el juego que quieras jugar o si querés salir. 🎲")
                 respuesta = int(input("Indica a que juego desea jugar: "))
            if respuesta == 1:
                os.system("python ruleta.py")
            elif respuesta == 2:
                os.system("python black_jack.py")
            elif respuesta == 3:
                os.system("python slots.py")
            else:
                print("\n🎩 Gracias por visitar el Casino Online de Juan 🎰")
                print("¡Esperamos verte pronto de nuevo! 🃏🎲")
                print("👋 Cerrando sesión... ¡Buena suerte en la próxima! 🍀")
                break
        except ValueError as e:
            print(f"Error en la respuesta: {e}")

def main():
    validarEdad()
    mostrarMenu()
main()