from slots import determinarResultado

def test_gana_slots():
    saldo, resultado = determinarResultado(["🍒", "🍒", "🍒"], 100, 500)
    assert saldo > 500

def test_pierde_slots():
    saldo, resultado = determinarResultado(["🍒", "💎", "7️⃣"], 100, 500)
    assert saldo == 500
    