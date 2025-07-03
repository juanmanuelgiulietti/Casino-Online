import random
import time

def mezclarMazo(mazo):
    print("\U0001f500 Mezclando el mazo…")
    random.shuffle(mazo)
    time.sleep(1)
    print("\u2705 El mazo está listo para repartir")
    return mazo

def ingresarDatos():
    nombre = input("Ingresa tu nombre: ").strip()
    while not nombre or not nombre.isalpha():
        print("❌ El nombre no puede estar vacío y solo debe contener letras.")
        nombre = input("Ingresa tu nombre: ").strip()
    return nombre.capitalize()

def darBienvenida(nombre):
    print(f"🎉 ¡Bienvenido/a al Blackjack, {nombre}! 🃏")
    print("Prepárate para desafiar al crupier y acercarte lo más posible a 21 sin pasarte.")
    print("💵 ¡Si lográs vencer a la casa, te llevás la gloria (y las fichas)! 🪙")
    print("-----------------------------------------------------------")

def dineroInicial():
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
        print("\n" + "-" * 60)
        print(f"🃏 NUEVA RONDA - SALDO: ${dinero:.2f}")
        print("-" * 60 + "\n")

        dinero, dineroApostado = apostarDinero(dinero)
        print(f"Dinero restante: $ {dinero:.2f}")
        mazo = mezclarMazo(mazo)
<<<<<<< HEAD
main()
=======
main()
>>>>>>> 4eb7d1937e407b10c343d9f1bbb3d7a91aa2d43a
