def elegirApuesta(dinero):
    """
    Objetivo: Esta funcion permite imprimir al usuario las opciones de apuestas disponibles y a su vez permitir al usuario elegir una.
    --------------------------------------
    Parametros: Recibe como parametro el dinero inicial que tiene disponible el jugador para iniciar el juego. Tambien valida que la opcion elegida por el usuario sea valida.
    --------------------------------------
    Retorno: Esta funcion retorna el dinero disponible del jugador, junto con la opcion elegida por el usuario.
    """

    opcionesApuesta = [
    "Pleno",
    "Rojo",
    "Negro",
    "Par",
    "Impar",
    "1 a 18",
    "19 a 36",
    "Columna 1",
    "Columna 2",
    "Columna 3",
    "Docena 1 (1-12)",
    "Docena 2 (13-24)",
    "Docena 3 (25-36)"
    ]

    print("Opciones de apuesta:")
    i = 1
    for opcion in opcionesApuesta:
        print(f"{i} - {opcion}")
        i += 1
    print()
    print(f"💰 Dinero disponible: $ {dinero}")
    print()
    apuestaSeleccionada = int(input(f"Ingrese el tipo de apuesta que desea realizar: "))
    while apuestaSeleccionada < 1 or apuestaSeleccionada > 13:
        print(f"Por favor ingrese una respuesta valida (1 al 10).")
        apuestaSeleccionada = int(input(f"Ingrese el tipo de apuesta que desea realizar: "))
    return apuestaSeleccionada

def ingresarDinero():
    """
    Objetivo: Permite al usuario definir con cuánto dinero desea comenzar el juego.
    --------------------------------------
    Parametros: Sin parametros.
    --------------------------------------
    Retorno: Retorna el saldo inicial elegido por el usuario (float).
    """
    dinero = float(input("Ingrese la cantidad de dinero con la que desea arrancar a jugar: "))
    while dinero <= 0:
        print("Por favor ingrese una respuesta valida (mayor a 0).")
        dinero = float(input("Ingrese la cantidad de dinero con la que desea arrancar a jugar: "))
    return dinero

def crearUsuario():
    """
    Objetivo: Esta funcion permite al usuario ingresar su nombre e iniciar el juego y a su vez verifica que la respuesta sea correcta. 
    --------------------------------------
    Parametros: Sin parametros.
    --------------------------------------
    Retorno: Esta funcion retorna un saludo hacia el usuario, completando la frase con el nombre ingresado.
    """

    usuario = input("Ingrese su nombre para iniciar el juego: ")
    
    while not usuario.isalpha():
        print("Por favor ingrese un nombre valido (sin espacios o caracteres especiales): ")
        usuario = input("Hola!, por favor ingrese su nombre para iniciar el juego: ")
    return usuario

def main():
    numeros = [
        [0, "Verde"],
        [1, "Rojo", "Impar"], [2, "Negro", "Par"], [3, "Rojo", "Impar"], [4, "Negro", "Par"],
        [5, "Rojo", "Impar"], [6, "Negro", "Par"], [7, "Rojo", "Impar"], [8, "Negro", "Par"],
        [9, "Rojo", "Impar"], [10, "Negro", "Par"], [11, "Negro", "Impar"], [12, "Rojo", "Par"],
        [13, "Negro", "Impar"], [14, "Rojo", "Par"], [15, "Negro", "Impar"], [16, "Rojo", "Par"],
        [17, "Negro", "Impar"], [18, "Rojo", "Par"], [19, "Rojo", "Impar"], [20, "Negro", "Par"],
        [21, "Rojo", "Impar"], [22, "Negro", "Par"], [23, "Rojo", "Impar"], [24, "Negro", "Par"],
        [25, "Rojo", "Impar"], [26, "Negro", "Par"], [27, "Rojo", "Impar"], [28, "Negro", "Par"],
        [29, "Negro", "Impar"], [30, "Rojo", "Par"], [31, "Negro", "Impar"], [32, "Rojo", "Par"],
        [33, "Negro", "Impar"], [34, "Rojo", "Par"], [35, "Negro", "Impar"], [36, "Rojo", "Par"]
    ]
    
    usuario = crearUsuario()
    print(f"¡Hola! 👋 {usuario} . Bienvenido al juego de la ruleta. Buena suerte 🍀")
    
    print()
    dinero = ingresarDinero()
    print()
    apuestaSeleccionada = elegirApuesta(dinero)
main()