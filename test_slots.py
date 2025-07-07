from slots import determinarResultado

def test_gana_slots():
    pantalla = [
        ["🍒", "🍒", "🍒"],
        ["💎", "7️⃣", "🍋"],
        ["🔔", "🍋", "💎"]
    ]
    saldo, resultado = determinarResultado(pantalla, 1000, 500)
    assert saldo > 1000

def test_pierde_slots():
    pantalla = [
        ["🍒", "💎", "7️⃣"],
        ["💎", "🍋", "🔔"],
        ["7️⃣", "🍋", "💎"]
    ]
    saldo, resultado = determinarResultado(pantalla, 1000, 500)
    assert saldo == 1000