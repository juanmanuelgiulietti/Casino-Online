# 🃏 Blackjack en Python

Bienvenido/a a este juego de **Blackjack** desarrollado en Python. Una versión simplificada pero fiel a las reglas clásicas del casino, jugada desde la consola. ¡Desafía al crupier, administra tus apuestas y probá tu suerte y estrategia!

---

## 🎯 Objetivo del Juego

Acercarte lo más posible a 21 sin pasarte y vencer al crupier. Si lográs sumar exactamente 21 con tus dos primeras cartas, ¡Blackjack automático!

---

## 🚀 ¿Cómo jugar?

1. Ingresás tu nombre.
2. Definís con cuánto dinero inicial querés jugar.
3. En cada ronda:
   - Apostás una cantidad.
   - Recibís 2 cartas.
   - Podés:
     - **1️⃣ Plantarte**.
     - **2️⃣ Pedir otra carta**.
     - **3️⃣ Duplicar la apuesta** *(solo con saldo suficiente)*.

4. El crupier jugará su turno y se determinará el ganador.
5. El juego continúa hasta que:
   - Te quedás sin dinero.
   - Decidís no jugar más.

---

## 🧠 Reglas clave implementadas

- Los As valen 11 u 1, según convenga al jugador.
- El crupier se planta con 17 o más.
- El jugador puede duplicar su apuesta, recibiendo una única carta extra y plantándose automáticamente.
- El empate devuelve el dinero apostado.
- La victoria paga 2x la apuesta.

---

## 🛠️ Tecnologías utilizadas

- **Python 3**
- Librerías estándar:
  - `random` – para mezclar el mazo
  - `time` – para animar acciones con pausas leves

---

## 🖥️ Cómo ejecutar

1. Cloná o descargá el repositorio.
2. Ejecutá el script en consola:

```bash
python blackjack.py
