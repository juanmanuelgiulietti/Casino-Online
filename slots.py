import random
import time
from datetime import datetime

def registrar_historial(juego, resultado, dinero):
    """
    Registra en un archivo de texto el resultado de una partida en el casino.

    Parámetros:
    ----------
    juego : str
        Nombre del juego al que el usuario jugó (por ejemplo, "Blackjack", "Slots", "Ruleta").
    
    resultado : str
        Resultado de la partida en formato texto (por ejemplo, "Ganó $200", "Perdió $100", "Empate").
    
    saldo : float
        Saldo actual del jugador luego de la partida.

    Comportamiento:
    --------------
    - Abre (o crea si no existe) el archivo 'historial_casino.txt'.
    - Escribe una línea con la fecha y hora actual, el nombre del juego, el resultado y el saldo final.
    - Cada llamada a la función agrega una nueva línea al final del archivo, sin borrar las anteriores.

    Ejemplo de línea en el archivo:
    [04/07/2025 12:00] Juego: Slots | Resultado: Ganó $300.00 | Saldo: $1500.00
    """
    fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
    linea = f"[{fecha_hora}] Juego: {juego} | Resultado: {resultado} | Saldo: ${dinero:.2f}\n"
    
    with open("historial_casino.txt", "a", encoding="utf-8") as archivo:
        archivo.write(linea)

def continuarJuego():
    """
    Pregunta al usuario si desea continuar jugando otra ronda.

    Retorna:
        str: 's' si desea continuar, 'n' si desea finalizar.
    """
    continuar = input("\n🔁 ¿Querés jugar otra ronda? (s/n): ").strip().lower()
    while continuar not in ["s", "n"]:
        print("❌ Respuesta inválida. Ingresá 's' para sí o 'n' para no.")
        continuar = input("🔁 ¿Querés jugar otra ronda? (s/n): ").strip().lower()
    return continuar

def determinarResultado(pantalla, dinero, dineroApostado):
    """
    Evalúa la pantalla generada para determinar si hay combinaciones ganadoras 
    en filas, columnas o diagonales. Calcula la ganancia y la suma al dinero total.

    Parámetros:
        pantalla (list): Matriz 3x3 con los símbolos obtenidos.
        dinero (float): Dinero actual del jugador.
        dineroApostado (float): Monto apostado en la ronda.

    Retorna:
        float: Dinero actualizado del jugador después de aplicar la ganancia.
    """
    ganancia = 0

    for fila in pantalla:
        if fila[0] == fila[1] == fila[2]:
            if fila[0] == "🍒":
                ganancia += dineroApostado * 2
            elif fila[0] == "🍋":
                ganancia += dineroApostado * 3
            elif fila[0] == "🔔":
                ganancia += dineroApostado * 5
            elif fila[0] == "💎":
                ganancia += dineroApostado * 8
            else:
                ganancia += dineroApostado * 10

    for col in range(3):
        if pantalla[0][col] == pantalla[1][col] == pantalla[2][col]:
            if pantalla[0][col] == "🍒":
                ganancia += dineroApostado * 2
            elif pantalla[0][col] == "🍋":
                ganancia += dineroApostado * 3
            elif pantalla[0][col] == "🔔":
                ganancia += dineroApostado * 5
            elif pantalla[0][col] == "💎":
                ganancia += dineroApostado * 8
            else:
                ganancia += dineroApostado * 10

    if pantalla[0][0] == pantalla[1][1] == pantalla[2][2]:
        if pantalla[0][0] == "🍒":
            ganancia += dineroApostado * 2
        elif pantalla[0][0] == "🍋":
            ganancia += dineroApostado * 3
        elif pantalla[0][0] == "🔔":
            ganancia += dineroApostado * 5
        elif pantalla[0][0] == "💎":
            ganancia += dineroApostado * 8
        else:
            ganancia += dineroApostado * 10

    if pantalla[0][2] == pantalla[1][1] == pantalla[2][0]:
        if pantalla[0][2] == "🍒":
            ganancia += dineroApostado * 2
        elif pantalla[0][2] == "🍋":
            ganancia += dineroApostado * 3
        elif pantalla[0][2] == "🔔":
            ganancia += dineroApostado * 5
        elif pantalla[0][2] == "💎":
            ganancia += dineroApostado * 8
        else:
            ganancia += dineroApostado * 10

    if ganancia > 0:
        dinero += ganancia
        print("\n🎉 ¡Felicitaciones! Lograste una combinación ganadora.")
        print(f"💰 Ganancia obtenida: ${ganancia:.2f}")
        print(f"🪙 Tu nuevo saldo es: ${dinero:.2f}")
        resultado = f"+${ganancia:.2f}"
    else:
        print("\n💨 Los rodillos se detienen... y no hubo suerte esta vez.")
        print(f"💸 Perdiste tu apuesta de ${dineroApostado:.2f} 😞 ¡No te rindas! Probá otra vez.")
        resultado = f"-${ganancia:.2f}"
        
    registrar_historial("Slots", resultado, dinero)    
    return dinero, resultado


def girarRodillos():
    """
    Genera aleatoriamente una pantalla de 3x3 con símbolos de tragamonedas.

    Retorna:
        list: Matriz 3x3 representando los símbolos en la pantalla.
    """
    simbolos = ["🍒", "💎", "🔔", "🍋", "7️⃣"]
    pantalla = []

    for i in range(3):
        pantalla.append([])
        for j in range(3):
            simbolo = random.choice(simbolos)
            pantalla[i].append(simbolo)

    return pantalla


def dineroInicial():
    """
    Solicita al usuario que ingrese un monto válido con el que desea comenzar el juego.

    Retorna:
        float: Dinero inicial ingresado por el usuario (debe ser mayor a 0).
    """
    while True:
        dinero = input("💰 Ingresa la cantidad de dinero con la que deseas iniciar: ").strip()
        try:
            dinero = float(dinero)
            if dinero > 0:
                print(f"✅ Arrancás con ${dinero:.2f}. ¡Buena suerte! 🎯")
                return dinero
            else:
                print("❌ El monto debe ser mayor a cero. Probá de nuevo. 💸")
        except ValueError:
            print("❌ Valor inválido. Ingresá solo números, sin letras ni símbolos. 💸")


def apostarDinero(dinero):
    """
    Solicita al jugador un monto a apostar y valida que no supere su saldo.

    Parámetros:
        dinero (float): Dinero disponible del jugador.

    Retorna:
        tupla: Dinero restante luego de la apuesta, y el monto apostado.
    """
    while True:
        print(f"\n💵 Tienes ${dinero:.2f} disponibles.")
        dineroApostado = input("🎰 ¿Cuánto querés apostar esta ronda?: ").strip()
        try:
            dineroApostado = float(dineroApostado)
            if dineroApostado > 0 and dineroApostado <= dinero:
                print(f"💸 Apostaste ${dineroApostado:.2f}. ¡Suerte!")
                dinero = dinero - dineroApostado
                return dinero, dineroApostado
            else:
                print("❌ Apuesta inválida. Debe ser mayor a cero y no superar tu saldo. 💸")
        except ValueError:
            print("❌ Valor inválido. Ingresá solo números, sin letras ni símbolos. 💸")


def darBienvenida(nombre):
    """
    Muestra un mensaje de bienvenida al jugador al iniciar el juego.

    Parámetros:
        nombre (str): Nombre del jugador.
    """
    print(f"\n🎉 ¡Bienvenido/a a Slots, {nombre}! 🃏")
    print("🎰 Alineá los símbolos y ganá grandes premios 💰")
    print("-----------------------------------------------------------")


def ingresarDatos():
    """
    Solicita al jugador su nombre y valida que solo contenga letras.

    Retorna:
        str: Nombre del jugador con la primera letra en mayúscula.
    """
    nombre = input("👤 Ingresa tu nombre: ").strip()
    while not nombre or not nombre.isalpha():
        print("❌ El nombre no puede estar vacío y solo debe contener letras.")
        nombre = input("👤 Ingresa tu nombre: ").strip()
    return nombre.capitalize()


def main():
    """
    Función principal que orquesta el flujo del juego de tragamonedas:
    - Obtiene los datos del jugador
    - Inicia el saldo
    - Ejecuta las rondas con apuestas
    - Evalúa los resultados y controla el ciclo de juego
    - Finaliza cuando el jugador se queda sin dinero o decide no seguir jugando
    """
    nombre = ingresarDatos()
    darBienvenida(nombre)
    dinero = dineroInicial()

    while True:
        dinero, dineroApostado = apostarDinero(dinero)
        pantalla = girarRodillos()

        print()
        print("🎲 Girando los rodillos...")
        time.sleep(1.5) 
        print()
        for fila in pantalla:
            print('  '.join(fila))
            time.sleep(0.5)

        dinero, _ = determinarResultado(pantalla, dinero, dineroApostado)

        if dinero <= 0:
            print(f"\n💸 Te quedaste sin saldo, {nombre}. ¡Gracias por jugar a los Slots! 🎲")
            break

        if continuarJuego() == "n":
            print(f"\n🎩 Gracias por jugar, {nombre}. Terminaste con ${dinero:.2f}. ¡Hasta la próxima! 🍒")
            break

if __name__ == "__main__":
    main()