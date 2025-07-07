import random
from datetime import datetime

def registrar_historial(juego, resultado, saldoActualizado):
    """
    Registra en un archivo de texto el resultado de una partida en el casino.

    Parámetros:
    ----------
    juego : str
        Nombre del juego al que el usuario jugó (por ejemplo, "Blackjack", "Slots", "Ruleta").
    
    resultado : str
        Resultado de la partida en formato texto (por ejemplo, "+ $200", "- $100", "Empate").
    
    saldoActualizado : float
        Saldo actual del jugador luego de la partida.

    Comportamiento:
    --------------
    - Abre (o crea si no existe) el archivo 'historial_casino.txt'.
    - Escribe una línea con la fecha y hora actual, el nombre del juego, el resultado y el saldo final.
    - Cada llamada a la función agrega una nueva línea al final del archivo, sin borrar las anteriores.

    Ejemplo de línea en el archivo:
    [04/07/2025 12:00] Juego: Slots | Resultado: + $300.00 | Saldo: $1500.00
    """
    fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
    linea = f"[{fecha_hora}] Juego: {juego} | Resultado: {resultado} | Saldo: ${saldoActualizado:.2f}\n"
    
    with open("historial_casino.txt", "a", encoding="utf-8") as archivo:
        archivo.write(linea)

def continuarJuego():
    """
    Objetivo: Permitir al usuario continuar jugando o en su defecto terminar el juego y validar su respuesta.
    --------------------------------------
    Parametros: Sin parametros.
    --------------------------------------
    Retorno: Esta funcion retorna la respuesta del usuario, siendo esta si o no
    """
    
    seguirJugando = input("¿Deseas seguir jugando? 🧐: ").lower()
    while seguirJugando != "si" and seguirJugando != "no":
        print("Por favor ingrese una respuesta valida (si/no).")
        seguirJugando = input("¿Deseas seguir jugando? 🧐: ").lower()
    return seguirJugando

def determinarResultado(apuestaValidada, tirada, numero, dineroApostado, saldoActualizado):
    """
    Objetivo: Esta funcion tiene como objetivo comparar la apuesta del jugador con el resultado del giro de la ruleta. Haciendo asi que si el jugador gana se aumente su dinero disponible, como tambien si pierde disminuya si dinero disponible.
    --------------------------------------
    Parametros: Recibe como parametros la apuesta del jugador (apuestaValidada), la tirada de la ruleta (tirada), el numero elegido por el jugador si es que eligio jugar pleno (numero), el dinero apostado por el jugador (dineroApostado) y el saldo del jugador actualizado si se le resta o suma dependiendo del resultado (saldoActualizado).
    --------------------------------------
    Retorno: Esta funcion retorna el saldo del jugador actualizado dependiendo del resultado.
    """
    
    calcularGanancias = lambda dinero, multiplicador: dinero * multiplicador
    
    columnaUno = [i for i in range(1, 35, 3)]
    columnaDos = [i for i in range(2, 37, 3)]
    columnaTres = [i for i in range(3, 38, 3)]

    
    if apuestaValidada == "Pleno":
        if numero == tirada[0]:
            ganancia = calcularGanancias(dineroApostado, 36)
            resultado = f"+ ${ganancia:.2f}"
            print(f"Felicitaciones, ganaste $ {ganancia}!")
            saldoActualizado = saldoActualizado + ganancia
            print(f"Nuevo saldo: 💰 $ {saldoActualizado}")
        else:
            resultado = f"- ${dineroApostado:.2f}"
            print(f"😞 Perdiste, mala suerte! 😞")
            print(f"Saldo: 💸 $ {saldoActualizado}")
    elif (apuestaValidada == "Rojo") or (apuestaValidada == "Negro"):
        if apuestaValidada == tirada[1]:
            ganancia = calcularGanancias(dineroApostado, 2)
            resultado = f"+ ${ganancia:.2f}"
            print(f"🎉 ¡Felicitaciones, ganaste $ {ganancia}! 🎉")
            saldoActualizado = saldoActualizado + ganancia
            print(f"Nuevo saldo: 💰 $ {saldoActualizado}")
        else:
            resultado = f"- ${dineroApostado:.2f}"
            print(f"😞 Perdiste, mala suerte! 😞")
            print(f"Saldo: 💸 $ {saldoActualizado}")
    elif (apuestaValidada == "Par") or (apuestaValidada == "Impar"):
        if apuestaValidada == tirada[2]:
            ganancia = calcularGanancias(dineroApostado, 2)
            resultado = f"+ ${ganancia:.2f}"
            print(f"🎉 ¡Felicitaciones, ganaste $ {ganancia}! 🎉")
            saldoActualizado = saldoActualizado + ganancia
            print(f"Nuevo saldo: 💰 $ {saldoActualizado}")
        else:
            resultado = f"- ${dineroApostado:.2f}"
            print(f"😞 Perdiste, mala suerte! 😞")
            print(f"Saldo: 💸 $ {saldoActualizado}")
    elif (apuestaValidada == "1 a 18"):
        if 1 <= tirada[0] <= 18:
            ganancia = calcularGanancias(dineroApostado, 2)
            resultado = f"+ ${ganancia:.2f}"
            print(f"🎉 ¡Felicitaciones, ganaste $ {ganancia}! 🎉")
            saldoActualizado = saldoActualizado + ganancia
            print(f"Nuevo saldo: 💰 $ {saldoActualizado}")
        else:
            resultado = f"- ${dineroApostado:.2f}"
            print(f"😞 Perdiste, mala suerte! 😞")
            print(f"Saldo: 💸 $ {saldoActualizado}")
    elif (apuestaValidada == "19 a 36"):
        if 19 <= tirada[0] <= 36:
            ganancia = calcularGanancias(dineroApostado, 2)
            resultado = f"+ ${ganancia:.2f}"
            print(f"🎉 ¡Felicitaciones, ganaste $ {ganancia}! 🎉")
            saldoActualizado = saldoActualizado + ganancia
            print(f"Nuevo saldo: 💰 $ {saldoActualizado}")
        else:
            resultado = f"- ${dineroApostado:.2f}"
            print(f"😞 Perdiste, mala suerte! 😞")
            print(f"Saldo: 💸 $ {saldoActualizado}")
    elif apuestaValidada == "Columna 1":
        if tirada[0] in columnaUno:
            ganancia = calcularGanancias(dineroApostado, 2)
            resultado = f"+ ${ganancia:.2f}"
            print(f"🎉 ¡Felicitaciones, ganaste $ {ganancia}! 🎉")
            saldoActualizado = saldoActualizado + ganancia
            print(f"Nuevo saldo: 💰 $ {saldoActualizado}")
        else:
            resultado = f"- ${dineroApostado:.2f}"
            print(f"😞 Perdiste, mala suerte! 😞")
            print(f"Saldo: 💸 $ {saldoActualizado}")
    elif apuestaValidada == "Columna 2":
        if tirada[0] in columnaDos:
            ganancia = calcularGanancias(dineroApostado, 2)
            resultado = f"+ ${ganancia:.2f}"
            print(f"🎉 ¡Felicitaciones, ganaste $ {ganancia}! 🎉")
            saldoActualizado = saldoActualizado + ganancia
            print(f"Nuevo saldo: 💰 $ {saldoActualizado}")
        else:
            resultado = f"- ${dineroApostado:.2f}"
            print(f"😞 Perdiste, mala suerte! 😞")
            print(f"Saldo: 💸 $ {saldoActualizado}")
    elif apuestaValidada == "Columna 3":
        if tirada[0] in columnaTres:
            ganancia = calcularGanancias(dineroApostado, 2)
            resultado = f"+ ${ganancia:.2f}"
            print(f"🎉 ¡Felicitaciones, ganaste $ {ganancia}! 🎉")
            saldoActualizado = saldoActualizado + ganancia
            print(f"Nuevo saldo: 💰 $ {saldoActualizado}")
        else:
            resultado = f"- ${dineroApostado:.2f}"
            print(f"😞 Perdiste, mala suerte! 😞")
            print(f"Saldo: 💸 $ {saldoActualizado}")         
    elif (apuestaValidada == "Docena 1 (1-12)"):
        if 1 <= tirada[0] <= 12:
            ganancia = calcularGanancias(dineroApostado, 3)
            resultado = f"+ ${ganancia:.2f}"
            print(f"🎉 ¡Felicitaciones, ganaste $ {ganancia}! 🎉")
            saldoActualizado = saldoActualizado + ganancia
            print(f"Nuevo saldo: 💰 $ {saldoActualizado}")
        else:
            resultado = f"- ${dineroApostado:.2f}"
            print(f"😞 Perdiste, mala suerte! 😞")
            print(f"Saldo: 💸 $ {saldoActualizado}")
    elif (apuestaValidada == "Docena 2 (13-24)"):
        if 13 <= tirada[0] <= 24:
            ganancia = calcularGanancias(dineroApostado, 3)
            resultado = f"+ ${ganancia:.2f}"
            print(f"🎉 ¡Felicitaciones, ganaste $ {ganancia}! 🎉")
            saldoActualizado = saldoActualizado + ganancia
            print(f"Nuevo saldo: 💰 $ {saldoActualizado}")
        else:
            resultado = f"- ${dineroApostado:.2f}"
            print(f"😞 Perdiste, mala suerte! 😞")
            print(f"Saldo: 💸 $ {saldoActualizado}")
    elif (apuestaValidada == "Docena 3 (25-36)"):
        if 25 <= tirada[0] <= 36:
            ganancia = calcularGanancias(dineroApostado, 3)
            resultado = f"+ ${ganancia:.2f}"
            print(f"🎉 ¡Felicitaciones, ganaste $ {ganancia}! 🎉")
            saldoActualizado = saldoActualizado + ganancia
            print(f"Nuevo saldo: 💰 $ {saldoActualizado}")
        else:
            resultado = f"- ${dineroApostado:.2f}"
            print(f"😞 Perdiste, mala suerte! 😞")
            print(f"Saldo: 💸 $ {saldoActualizado}")
            
    registrar_historial("Ruleta", resultado, saldoActualizado)
    return saldoActualizado
            
def girarRuleta(numeros):
    """
    Objetivo: Esta funcion permite elegir un numero de la ruleta al azar gracias al random choice, lo que dara un resultado para comparar si el usuario gana o pierde.
    --------------------------------------
    Parametros: Recibe como parametro una lista de listas llamada numeros, que contiene todos los  numeros de la ruleta del 0 al 36, con su respectivo color y paridad.
    --------------------------------------
    Retorno:  Esta funcion retorna el numero elegido al azar por el random choice.
    """
    
    tirada = random.choice(numeros)
    resultadoAString = [str(num) for num in tirada]
    resultadoFinal = ", ".join(resultadoAString)
    print(f"Resultado de la ruleta: {resultadoFinal}")
    return tirada

def crearApuesta(dinero):
    """
    Objetivo: Esta funcion permite al usuario ingresar la cantidad de dinero que desea apostar, y tambien valida que esa cantidad de dinero que desea apostar el jugador este dentro del valor disponible.
    --------------------------------------
    Parametros: Recibe como parametro el dinero disponible al iniciar el juego.
    --------------------------------------
    Retorno: Esta funcion retorna el dinero apostado por el jugador y el saldo disponible actualizado.
    """
    
    dineroApostado = float(input("Ingrese la cantidad de dinero que desea apostar: "))
    
    while (dineroApostado > dinero) or (dineroApostado < 1):
        print(f"Saldo insuficiente.")
        dineroApostado = float(input("Ingrese la cantidad de dinero que desea apostar: "))
    saldoActualizado = dinero - dineroApostado
    return dineroApostado, saldoActualizado

def validarApuestaSeleccionada(apuestaSeleccionada):
    """
    Objetivo: Esta funcion tiene como objetivo validar la apuesta seleccionada por el usuario.
    --------------------------------------
    Parametros: Recibe como parametro el numero de opcion de apuesta elegido por el usuario.
    --------------------------------------
    Retorno: Esta funcion retorna la apuesta del jugador y tambien valida que si el jugador eligio la opcion pleno, eliga un numero entre 0 y 36.
    """
    
    numero = None
    
    if apuestaSeleccionada == 1:
        apuesta = "Pleno"
        numero = int(input("Ingrese el numero que desea apostar (0 - 36): "))
        while numero < 0 or numero > 36:
            print("Por favor ingrese una respuesta valida.")
            numero = int(input("Ingrese el numero que desea apostar (0 - 36): "))      
    elif apuestaSeleccionada == 2:
        apuesta = "Rojo"
    elif apuestaSeleccionada == 3:
        apuesta = "Negro"
    elif apuestaSeleccionada == 4:
        apuesta = "Par"
    elif apuestaSeleccionada == 5:
        apuesta = "Impar"
    elif apuestaSeleccionada == 6:
        apuesta = "1 a 18"
    elif apuestaSeleccionada == 7:
        apuesta = "19 a 36"
    elif apuestaSeleccionada == 8:
        apuesta = "Columna 1"
    elif apuestaSeleccionada == 9:
        apuesta = "Columna 2"
    elif apuestaSeleccionada == 10:
        apuesta = "Columna 3"
    elif apuestaSeleccionada == 11:
        apuesta = "Docena 1 (1-12)"
    elif apuestaSeleccionada == 12:
        apuesta = "Docena 2 (13-24)"
    else:
        apuesta = "Docena 3 (25-36)"
    return apuesta, numero
    
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
    Parámetros: Sin parámetros.
    --------------------------------------
    Retorno: Retorna el saldo inicial elegido por el usuario (float).
    """
    while True:
        dinero = input("Ingrese la cantidad de dinero con la que desea arrancar a jugar: ")
        try:
            dinero = float(dinero)
            if dinero > 0:
                return dinero
            else:
                print("Por favor ingrese un número mayor a 0.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número.")


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
    """
    Objetivo: Esta funcion permite llamar a todas las funciones utilizadas en este programa, chequear su funcionamiento y tambien utilizar datos como la lista de listas (numeros) o la variable (dinero)
    --------------------------------------
    Parametros: Sin parametros.
    --------------------------------------
    Retorno: Esta funcion retorna los resultados de todas las funciones del programa.
    """

    numeros = [
    (0, "Verde"),
    (1, "Rojo", "Impar"), (2, "Negro", "Par"), (3, "Rojo", "Impar"), (4, "Negro", "Par"),
    (5, "Rojo", "Impar"), (6, "Negro", "Par"), (7, "Rojo", "Impar"), (8, "Negro", "Par"),
    (9, "Rojo", "Impar"), (10, "Negro", "Par"), (11, "Negro", "Impar"), (12, "Rojo", "Par"),
    (13, "Negro", "Impar"), (14, "Rojo", "Par"), (15, "Negro", "Impar"), (16, "Rojo", "Par"),
    (17, "Negro", "Impar"), (18, "Rojo", "Par"), (19, "Rojo", "Impar"), (20, "Negro", "Par"),
    (21, "Rojo", "Impar"), (22, "Negro", "Par"), (23, "Rojo", "Impar"), (24, "Negro", "Par"),
    (25, "Rojo", "Impar"), (26, "Negro", "Par"), (27, "Rojo", "Impar"), (28, "Negro", "Par"),
    (29, "Negro", "Impar"), (30, "Rojo", "Par"), (31, "Negro", "Impar"), (32, "Rojo", "Par"),
    (33, "Negro", "Impar"), (34, "Rojo", "Par"), (35, "Negro", "Impar"), (36, "Rojo", "Par")
    ]
    
    # Llamadas a las funciones
    usuario = crearUsuario()
    print(f"¡Hola! 👋 {usuario} . Bienvenido al juego de la ruleta. Buena suerte 🍀")

    print()
    dinero = ingresarDinero()
    print()
    apuestaSeleccionada = elegirApuesta(dinero)
    print()
    apuestaValidada, numero = validarApuestaSeleccionada(apuestaSeleccionada)
    print()
    dineroApostado, saldoActualizado = crearApuesta(dinero)
    print(f"Usted aposto: $ {dineroApostado}")
    print()
    print(f"Saldo restante: $ {saldoActualizado}")
    tirada = girarRuleta(numeros)
    saldoActualizado = determinarResultado(apuestaValidada, tirada, numero, dineroApostado, saldoActualizado)
    continuar = continuarJuego()
    
    while continuar == "si" and saldoActualizado > 0:
        dinero = saldoActualizado
        apuestaSeleccionada = elegirApuesta(dinero)
        apuestaValidada, numero = validarApuestaSeleccionada(apuestaSeleccionada)
        dineroApostado, saldoActualizado = crearApuesta(dinero)
        print(f"Usted aposto: $ {dineroApostado}")
        print()
        print(f"Saldo restante: $ {saldoActualizado}")
        tirada = girarRuleta(numeros)
        saldoActualizado = determinarResultado(apuestaValidada, tirada, numero, dineroApostado, saldoActualizado)
        
        if saldoActualizado <= 0:
            print("😔 Te quedaste sin saldo. ¡Gracias por jugar! 🙌")
            print(f"Hasta la próxima, {usuario}! 👋")

        continuar = continuarJuego()
if __name__ == "__main__":
    main()