import pytest
from black_jack import determinarGanador, calcularSuma, mezclarMazo, repartirCartas

# --- determinarGanador ---
def test_gana_jugador_crupier_se_pasa():
    resultado = determinarGanador(20, 22, 100, 10, "Juan")
    assert resultado == 120

def test_empate():
    resultado = determinarGanador(19, 19, 100, 10, "Ana")
    assert resultado == 110

# --- calcularSuma ---
def test_suma_simple():
    mano = [(10, "10 de Corazones"), (5, "5 de Tréboles")]
    assert calcularSuma(mano) == 15

def test_suma_con_ases():
    mano = [(11, "A de Corazones"), (8, "8 de Tréboles"), (5, "5 de Diamantes")]
    assert calcularSuma(mano) == 14

# --- mezclarMazo ---
def test_mazo_se_mezcla():
    mazo_original = [(i, f"{i} de Prueba") for i in range(1, 53)]
    mazo_mezclado = mezclarMazo(mazo_original[:])
    assert sorted(mazo_mezclado) == sorted(mazo_original)
    assert mazo_mezclado != mazo_original

# --- repartirCartas ---
def test_repartir_cartas_crea_dos_manos():
    mazo = [(i, f"{i}") for i in range(1, 53)]
    manos = repartirCartas(mazo, "Jugador")
    assert "Jugador" in manos
    assert "Computadora" in manos

def test_cada_mano_tiene_dos_cartas():
    mazo = [(i, f"{i}") for i in range(1, 53)]
    manos = repartirCartas(mazo, "Jugador")
    assert len(manos["Jugador"]) == 2
    assert len(manos["Computadora"]) == 2
