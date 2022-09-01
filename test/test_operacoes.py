import pytest
from matematica.Calculadora import soma, sub, multiplicacao, divisao, media_lista_valores
import numpy as np

def test_soma_dois_valores_positivos():
    assert soma(1.0, 2.0) == 3.0

def test_soma_valor_positivo_e_negativo():
    assert soma(3.0, -5.2) == -2.2

def test_soma_negativo_com_negativo():
    assert soma(-7, -13) == -20

def test_subtracao_positivo_com_positivo():
    assert sub(8.0, 5.0) == 3.0

def test_subtracao_negativo_com_positivo():
    assert sub(-3, 7) == -10

def test_subtracao_negativo_com_negativo():
    assert sub(-8, -9) == 1

def test_multiplicacao_positivo_negativo():
    assert multiplicacao(-4, 5) == -20

def test_multiplicacao_positivo_positivo():
    assert multiplicacao(4,3) == 12

def test_multiplicacao_negativo_negativo():
    assert multiplicacao(-7, -2) == 14

def test_divisao_por_zero():
    assert divisao(2, 0) == np.inf

def test_divisao_com_zero():
    assert divisao(0, 8) == np.inf

def test_divisao_por_positivo():
    assert divisao(5, 5) == 1

def test_divisao_negativo_negativo():
    assert divisao(-14, -7) == 2

def test_media_lista_vazia():
    assert media_lista_valores([]) == 0

def test_media_lista_so_numeros():
    assert media_lista_valores([2, 8, 7, 6]) == 5.7

def test_media_lista_num_e_letra():
    assert media_lista_valores([2, 2, 3, 'a', 2]) == 2.3



