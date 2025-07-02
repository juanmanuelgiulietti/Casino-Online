import random

def girarRodillos():
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
    dinero = dineroInicial()
    dinero, dineroApostado = apostarDinero(dinero)
    pantalla = girarRodillos()
    for sim in pantalla:
        print(sim)
main()