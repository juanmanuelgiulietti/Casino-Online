import random
import time

def determinarGanador(sumaJugador, sumaComputadora, dinero, dineroApostado, nombre):
    """
    Determina el ganador de la ronda y ajusta el dinero del jugador según el resultado.

    Parametros:
        sumaJugador (int): Puntos del jugador.
        sumaComputadora (int): Puntos del crupier.
        dinero (float): Dinero actual del jugador.
        dineroApostado (float): Dinero apostado en la ronda.
        nombre (str): Nombre del jugador.

    Retorna:
        float: Dinero actualizado del jugador.
    """ 
    if sumaJugador <= 21 and sumaComputadora > 21:
        print("💥 Crupier se pasó de 21. ¡Victoria automática!")
        dinero += dineroApostado * 2
        print(f"🎉 ¡{nombre} gana la ronda! Te llevás ${dinero:.2f} 🪙")
    elif sumaJugador > 21 and sumaComputadora <= 21:
        print("❌ Crupier gana esta vez.")
    elif sumaJugador <= 21 and sumaComputadora <= 21:
        if sumaJugador == sumaComputadora:
            print("🤝 ¡Empate! Recuperás tu apuesta.")
            dinero += dineroApostado
        elif sumaJugador > sumaComputadora:
            dinero += dineroApostado * 2
            print(f"🎉 ¡{nombre} gana la ronda! Te llevás ${dinero:.2f} 🪙")
        else:
            print("❌ Crupier gana esta vez.")
    else:
        print("🤝 ¡Empate! Recuperás tu apuesta.")
    return dinero

def calcularSuma(manos):
    """
    Calcula la suma total de una mano considerando el valor flexible de los Ases.

    Parametros:
        manos (list): Lista de cartas (tuplas de valor y nombre).

    Retorna:
        int: Suma total ajustada de la mano.
    """
    total = 0
    ases = 0
    for valor, nombre in manos:
        total += valor
        if valor == 11:
            ases += 1
    while total > 21 and ases:
        total -= 10
        ases -= 1
    return total

def turnoDeJugador(mazo, manos, nombre, dinero, dineroApostado):
    """
    Gestiona el turno del jugador: pedir, plantarse, duplicar o dividir mano.

    Parametros:
        mazo (list): Mazo de cartas.
        manos (dict): Manos de jugador y crupier.
        nombre (str): Nombre del jugador.
        dinero (float): Dinero actual del jugador.
        dineroApostado (float): Apuesta actual.

    Retorna:
        tuple: Suma final del jugador, dinero actualizado, apuesta actual, manos actualizadas.
    """
    jugadorSePlanto = False
    sumaJugador = sum(carta[0] for carta in manos[nombre])
    while not jugadorSePlanto:
        print("\n-------------------------------------")
        print(f"📍 Cartas de {nombre}:")
        cartas = ', '.join([carta[1] for carta in manos[nombre]])
        print(f"🃏 {cartas}")
        print(f"🧮 Total actual: {sumaJugador}")

        if sumaJugador == 21:
            print("🎉 ¡Blackjack! ¡21 exacto! 🥳")
            break
        elif sumaJugador > 21:
            print("💥 Te pasaste de 21... ¡perdiste esta ronda! 😞")
            break
        else:
            print("👉 ¿Querés pedir otra carta o plantarte?")
            print("1⃣  Plantarse")
            print("2⃣  Pedir carta")
            print("3⃣  Duplicar apuesta (recibís solo una carta más)")
            print("4⃣  Dividir mano (Split)")
            
            try:
                respuesta = int(input("Ingrese su elección: "))
                while respuesta not in [1, 2, 3]:
                    print("❌ Opción inválida. Escribí 1, 2 o 3.")
                    respuesta = int(input("Ingrese su elección: "))
            except ValueError:
                print("❌ Eso no es un número. Probá de nuevo.")
                continue

            if respuesta == 1:
                jugadorSePlanto = True
                print(f"🧙‍♂️  Te plantaste con un total de {sumaJugador}. Ahora juega la computadora...")
            elif respuesta == 2:
                nuevaCarta = mazo.pop()
                manos[nombre].append(nuevaCarta)
                print(f"🃏 Nueva carta: {nuevaCarta[1]}")
                sumaJugador = calcularSuma(manos[nombre])
            elif respuesta == 3:
                if dinero >= dineroApostado:
                    dinero -= dineroApostado
                    dineroApostado *= 2
                    nuevaCarta = mazo.pop()
                    manos[nombre].append(nuevaCarta)
                    print(f"🃏 Nueva carta: {nuevaCarta[1]}")
                    sumaJugador = calcularSuma(manos[nombre])
                    print("📍 Te plantaste automáticamente tras duplicar.")
                    jugadorSePlanto = True   
                else:
                    print("❌ No tenés suficiente dinero para duplicar la apuesta. Elegí otra opción.")
            else:
                if dinero >= dineroApostado and manos[nombre][0][0] == manos[nombre][1][0]:
                    carta1 = manos[nombre][0]
                    carta2 = manos[nombre][1]

                    dinero -= dineroApostado
                    mano1 = [carta1, mazo.pop()]
                    mano2 = [carta2, mazo.pop()]

                    print("✂️ ¡Dividiste tu mano! Ahora jugás dos manos independientes.")

                    for i, mano in enumerate([mano1, mano2], start=1):
                        print(f"\n🎮 Jugando mano {i}:")
                        suma = calcularSuma(mano)
                        sePlanto = False
                        while not sePlanto:
                            print(f"🃏 Cartas: {', '.join([c[1] for c in mano])}")
                            print(f"🧮 Total: {suma}")
                            if suma >= 21:
                                break
                            opcion = input("¿Querés otra carta en esta mano? (s/n): ").strip().lower()
                            if opcion == 's':
                                nueva = mazo.pop()
                                mano.append(nueva)
                                print(f"🃏 Nueva carta: {nueva[1]}")
                                suma = calcularSuma(mano)
                            else:
                                sePlanto = True
                        manos[f"{nombre}_split_{i}"] = mano

                    jugadorSePlanto = True
                    sumaJugador = -1
                else:
                    print("❌ No tenés suficiente dinero para realizar un Split. Elegí otra opción.")
    return sumaJugador, dinero, dineroApostado, manos

def turnoDeComputadora(mazo, manos, nombre):
    """
    Ejecuta el turno de la computadora (crupier) según reglas del Blackjack.

    Parametros:
        mazo (list): Mazo de cartas.
        manos (dict): Manos de ambos jugadores.
        nombre (str): Nombre del jugador humano (solo para mensajes).

    Retorna:
        int: Suma final de la computadora.
    """
    computadoraSePlanto = False
    print(f"Segunda carta: {manos['Computadora'][1]}")
    sumaComputadora = sum(carta[0] for carta in manos["Computadora"])
    while not computadoraSePlanto:
        if sumaComputadora > 21:
            print("💥 Crupier se pasó de 21... ¡Ganaste la ronda!")
            break
        elif sumaComputadora < 17:
            nuevaCarta = mazo.pop()
            manos["Computadora"].append(nuevaCarta)
            print(f"🃏 Nueva carta: {nuevaCarta[1]}")
        else:
            computadoraSePlanto = True
            print(f"🧙‍♂️ Crupier se planta con un total de {sumaComputadora}. Ahora juega {nombre}...")
        sumaComputadora = sum(carta[0] for carta in manos["Computadora"])
    return sumaComputadora

def repartirCartas(mazo, nombre):
    """
    Reparte dos cartas al jugador y dos al crupier.

    Parametros:
        mazo (list): Mazo de cartas.
        nombre (str): Nombre del jugador.

    Retorna:
        dict: Diccionario con las manos iniciales.
    """
    jugadores = [nombre, "Computadora"]
    manos = {
        nombre: [],
        "Computadora": []
    }
    print("🃏 Repartiendo cartas...")
    time.sleep(1)
    for i in range(2):
        manos[nombre].append(mazo.pop())
        manos["Computadora"].append(mazo.pop())
    return manos

def mezclarMazo(mazo):
    """
    Mezcla aleatoriamente el mazo de cartas.

    Parametros:
        mazo (list): Lista de cartas del mazo.

    Retorna:
        list: Mazo mezclado.
    """
    print("\U0001f500 Mezclando el mazo…")
    random.shuffle(mazo)
    time.sleep(1)
    print("\u2705 El mazo está listo para repartir")
    return mazo

def ingresarDatos():
    """
    Pide y valida el nombre del jugador.

    Retorna:
        str: Nombre validado.
    """
    nombre = input("Ingresa tu nombre: ").strip()
    while not nombre or not nombre.isalpha():
        print("❌ El nombre no puede estar vacío y solo debe contener letras.")
        nombre = input("Ingresa tu nombre: ").strip()
    return nombre.capitalize()

def darBienvenida(nombre):
    """
    Muestra un mensaje de bienvenida al jugador.

    Parametros:
        nombre (str): Nombre del jugador.
    """
    print(f"🎉 ¡Bienvenido/a al Blackjack, {nombre}! 🃏")
    print("Prepárate para desafiar al crupier y acercarte lo más posible a 21 sin pasarte.")
    print("💵 ¡Si lográs vencer a la casa, te llevás la gloria (y las fichas)! 🪙")
    print("-----------------------------------------------------------")

def dineroInicial():
    """
    Pide y valida el dinero inicial con el que desea jugar el jugador.

    Retorna:
        float: Dinero inicial válido.
    """
    while True:
        dinero = input("💰 Ingresa la cantidad de dinero con la que deseas iniciar: ").strip()
        try:
            dinero = float(dinero)
            if dinero > 0:
                print(f"✅ Arrancás con ${dinero:.2f} en la mesa. ¡Buena suerte! 🎯")
                return dinero
            else:
                print("❌ El monto debe ser mayor a cero. Probá de nuevo. 💸")
        except ValueError:
            print("❌ Valor inválido. Ingresá solo números, sin letras ni símbolos. 💸")

def apostarDinero(dinero):
    """
    Pide al jugador cuánto desea apostar en la ronda.

    Parametros:
        dinero (float): Dinero disponible del jugador.

    Retorna:
        tupla: Dinero restante y dinero apostado.
    """
    while True:
        print(f"Tienes $ {dinero} disponibles.")
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

def main():
    """
    Función principal que ejecuta el juego completo de Blackjack.
    """
    mazo = [
        (2, "2 de Corazones"), (3, "3 de Corazones"), (4, "4 de Corazones"), (5, "5 de Corazones"),
        (6, "6 de Corazones"), (7, "7 de Corazones"), (8, "8 de Corazones"), (9, "9 de Corazones"),
        (10, "10 de Corazones"), (10, "J de Corazones"), (10, "Q de Corazones"), (10, "K de Corazones"), (11, "A de Corazones"),
        (2, "2 de Diamantes"), (3, "3 de Diamantes"), (4, "4 de Diamantes"), (5, "5 de Diamantes"),
        (6, "6 de Diamantes"), (7, "7 de Diamantes"), (8, "8 de Diamantes"), (9, "9 de Diamantes"),
        (10, "10 de Diamantes"), (10, "J de Diamantes"), (10, "Q de Diamantes"), (10, "K de Diamantes"), (11, "A de Diamantes"),
        (2, "2 de Tréboles"), (3, "3 de Tréboles"), (4, "4 de Tréboles"), (5, "5 de Tréboles"),
        (6, "6 de Tréboles"), (7, "7 de Tréboles"), (8, "8 de Tréboles"), (9, "9 de Tréboles"),
        (10, "10 de Tréboles"), (10, "J de Tréboles"), (10, "Q de Tréboles"), (10, "K de Tréboles"), (11, "A de Tréboles"),
        (2, "2 de Picas"), (3, "3 de Picas"), (4, "4 de Picas"), (5, "5 de Picas"),
        (6, "6 de Picas"), (7, "7 de Picas"), (8, "8 de Picas"), (9, "9 de Picas"),
        (10, "10 de Picas"), (10, "J de Picas"), (10, "Q de Picas"), (10, "K de Picas"), (11, "A de Picas")
    ]
        
    nombre = ingresarDatos()
    darBienvenida(nombre)
    dinero = dineroInicial()

    while dinero > 0:
        print("" + "-" * 60)
        print(f"🃏 NUEVA RONDA - SALDO: ${dinero:.2f}")
        print("-" * 60 + "")

        dinero, dineroApostado = apostarDinero(dinero)
        print(f"Dinero restante: $ {dinero:.2f}")
        mazo = mezclarMazo(mazo)

        manos = repartirCartas(mazo, nombre)
        cartasJugador = ', '.join([carta[1] for carta in manos[nombre]])
        print(f"🃏 {nombre} recibe: {cartasJugador}")
        print(f"🃏 Crupier muestra: {manos['Computadora'][0][1]}")

        sumaJugador, dinero, dineroApostado, manos = turnoDeJugador(mazo, manos, nombre, dinero, dineroApostado)
        sumaComputadora = turnoDeComputadora(mazo, manos, nombre)

        print("🧾 RESUMEN DE LA RONDA")
        print(f"{nombre}: {cartasJugador} (Total: {sumaJugador})")
        cartasCrupier = ', '.join([carta[1] for carta in manos["Computadora"]])
        print(f"Crupier: {cartasCrupier} (Total: {sumaComputadora})")

        dinero = determinarGanador(sumaJugador, sumaComputadora, dinero, dineroApostado, nombre)
        print()

        print("\n" + "=" * 50 + "\n")

        if dinero > 0:
            continuar = input("¿Querés jugar otra ronda? (S/N): ").strip().lower()
            if continuar != "s":
                print(f"\nGracias por jugar, {nombre}. Terminaste con ${dinero:.2f} ¡Hasta la próxima!")
                break
        else:
            print(f"\nTe quedaste sin dinero, {nombre}. ¡Gracias por jugar! 💸")
if __name__ == "__main__":
    main()