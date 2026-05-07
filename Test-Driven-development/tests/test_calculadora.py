import pytest
from calculadora import Calculadora


def test_suma_positiva():
    calc = Calculadora()
    assert calc.sumar(2, 3) == 5


def test_suma_negativa():
    calc = Calculadora()
    assert calc.sumar(-2, -3) == -5


def test_suma_con_cero():
    calc = Calculadora()
    assert calc.sumar(5, 0) == 5


def test_resta_positiva():
    calc = Calculadora()
    assert calc.restar(5, 3) == 2


def test_resta_negativa():
    calc = Calculadora()
    assert calc.restar(3, 5) == -2


def test_multiplicacion_positiva():
    calc = Calculadora()
    assert calc.multiplicar(4, 5) == 20


def test_multiplicacion_por_cero():
    calc = Calculadora()
    assert calc.multiplicar(4, 0) == 0


def test_multiplicacion_negativa():
    calc = Calculadora()
    assert calc.multiplicar(-2, 3) == -6


def test_division_exacta():
    calc = Calculadora()
    assert calc.dividir(10, 2) == 5


def test_division_decimal():
    calc = Calculadora()
    assert calc.dividir(7, 2) == 3.5


def test_division_por_cero():
    calc = Calculadora()

    with pytest.raises(ValueError):
        calc.dividir(5, 0)