import os

def mostrarMenu():
    while True:
        print(f"Opciones de juegos: ")
        print(f"1. Ruleta")
        print(f"2. Black Jack")
    
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
            else:
                print("\n🎩 Gracias por visitar el Casino Online de Juan 🎰")
                print("¡Esperamos verte pronto de nuevo! 🃏🎲")
                print("👋 Cerrando sesión... ¡Buena suerte en la próxima! 🍀")
                break
        except ValueError as e:
            print(f"Error en la respuesta: {e}")

def main():
    mostrarMenu()
main()