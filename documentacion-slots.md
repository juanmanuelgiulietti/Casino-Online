# 🎰 Slots - Casino Online 🎰

Este juego de **Slots** (tragamonedas) forma parte del proyecto de **Casino Online**, desarrollado en Python. El objetivo es brindar una experiencia divertida y sencilla al jugador, permitiéndole apostar, girar rodillos, ganar combinaciones y llevar un historial de sus partidas.

---

## 📌 ¿Cómo funciona?

- El jugador ingresa su **nombre** y elige un **saldo inicial**.
- En cada ronda:
  - Apuesta una cantidad.
  - Gira los rodillos.
  - Aparecen símbolos aleatorios en una **pantalla de 3x3**.
  - Se evalúan combinaciones ganadoras:
    - Filas, columnas o diagonales con símbolos iguales generan ganancias.
- Las ganancias se suman al saldo actual.
- Se registra un historial de partidas en un archivo de texto.

---

## 🛠️ Tecnologías utilizadas

- **Python 3**
- Librerías estándar: `random`, `time`, `datetime`

---

## 🧩 Reglas del juego

### 🎲 Símbolos posibles:

- 🍒 Cereza
- 💎 Diamante
- 🔔 Campana
- 🍋 Limón
- 7️⃣ Siete

### 💰 Pagos por combinación:

| Símbolo | Multiplicador de ganancia |
| ------- | ------------------------- |
| 🍒      | 2x                        |
| 🍋      | 3x                        |
| 🔔      | 5x                        |
| 💎      | 8x                        |
| 7️⃣      | 10x                       |

✅ Se paga por **cada línea ganadora**:

- Filas horizontales
- Columnas verticales
- Diagonales principales

---

## 🧪 Pruebas unitarias

Se encuentra un archivo `test_slots.py` con varias pruebas utilizando `pytest`, que validan:

- Ganancias en combinaciones de filas, columnas y diagonales.
- Escenarios sin combinaciones ganadoras.
- Actualización correcta del saldo.
- Registro correcto de historial.

Para ejecutarlas:

```bash
pytest test_slots.py

🧠 Consideraciones
Si el jugador pierde todo su dinero, el juego termina.

Se puede jugar indefinidamente mientras haya saldo.

El historial guarda fecha, juego, resultado y saldo actual.