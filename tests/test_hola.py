import pytest
from hola import saludo


def test_saludo_returns_string():
    """La función saludo debe devolver una cadena."""
    s = saludo()
    assert isinstance(s, str)


def test_saludo_contenido():
    """La función saludo debe devolver exactamente '¡Hola, mundo!'"""
    assert saludo() == "¡Hola, mundo!"
