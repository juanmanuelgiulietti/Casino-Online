import pytest
from ruleta import determinarResultado

def test_ruleta_gana_pleno():
    saldo = determinarResultado("Pleno", (17, "Rojo", "Impar"), 17, 100, 500)
    assert saldo == 500 + (100 * 36)
    
def test_ruleta_pierde_pleno():
    saldo = determinarResultado("Pleno", (18, "Rojo", "Par"), 17, 100, 500)
    assert saldo == 500

def test_ruleta_gana_color():
    saldo = determinarResultado("Rojo", (5, "Rojo", "Impar"), None, 100, 500)
    assert saldo == 500 + (100 * 2)

def test_ruleta_pierde_color():
    saldo = determinarResultado("Rojo", (4, "Negro", "Par"), None, 100, 500)
    assert saldo == 500