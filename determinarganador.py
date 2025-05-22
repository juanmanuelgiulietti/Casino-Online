def calcularSuma(mano):
    total = 0
    ases = 0
    for valor, _ in mano:
        total += valor
        if valor == 11:
            ases += 1
    while total > 21 and ases:
        total -= 10
        ases -= 1
    return total

def determinarGanador(sumaJugador, sumaComputadora, dinero, dineroApostado, nombre):
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


def main():
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
        print("
" + "-" * 60)
        print(f"🃏 NUEVA RONDA - SALDO: ${dinero:.2f}")
        print("-" * 60 + "
")

        dinero, dineroApostado = apostarDinero(dinero)
        print(f"Dinero restante: $ {dinero:.2f}")
        mazo = mezclarMazo(mazo)

        manos = repartirCartas(mazo, nombre)
        cartasJugador = ', '.join([carta[1] for carta in manos[nombre]])
        print(f"🃏 {nombre} recibe: {cartasJugador}")
        print(f"🃏 Crupier muestra: {manos['Computadora'][0][1]}")

        sumaJugador = turnoDeJugador(mazo, manos, nombre)
        sumaComputadora = turnoDeComputadora(mazo, manos, nombre)

        sumaJugador = calcularSuma(manos[nombre])
        sumaComputadora = calcularSuma(manos["Computadora"])

        print("
🧾 RESUMEN DE LA RONDA")
        print(f"{nombre}: {cartasJugador} (Total: {sumaJugador})")
        cartasCrupier = ', '.join([carta[1] for carta in manos["Computadora"]])
        print(f"Crupier: {cartasCrupier} (Total: {sumaComputadora})")

        dinero = determinarGanador(sumaJugador, sumaComputadora, dinero, dineroApostado, nombre)