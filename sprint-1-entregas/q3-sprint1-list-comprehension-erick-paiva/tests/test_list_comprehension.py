from main import (
    list_comprehension_exercise_1,
    list_comprehension_exercise_2,
    list_comprehension_exercise_3,
    list_comprehension_exercise_4,
    list_comprehension_exercise_5,
    list_comprehension_exercise_6,
)


def test_exercise_1():

    expect = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = list_comprehension_exercise_1()

    assert type(result) is list, "Verificar se está retornando uma lista"

    assert (
        result == expect
    ), "Verificar se o intervalo está entre 0 e 10 (ambos inclusos)"


def test_exercise_2():

    expect = [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21]
    result = list_comprehension_exercise_2()

    assert type(result) is list, "Verificar se está retornando uma lista"

    assert (
        result == expect
    ), """Verificar se está sendo montado para 
        retornar apenas os divisíveis por 2 ou por 3"""


def test_exercise_3():

    expect = [-3, -1, 1, 3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31]
    result = list_comprehension_exercise_3()

    assert type(result) is list, "Verificar se está retornando uma lista"

    assert (
        result == expect
    ), """Verificar se está montado para retornar os valores,
        em um intervalo de -5 ~ 30 (tendo ambos incluso) que 
        não sejam divisíveis nem por 2 e nem por 5."""


def test_exercise_4():

    expect = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    result = list_comprehension_exercise_4()

    assert type(result) is list, "Verificar se está retornando uma lista"

    assert (
        result == expect
    ), """Verificar se está sendo montado para retornar a raiz 
        quadrada dos numeros de 0 ~ 10 (tendo ambos incluso)"""


def test_exercise_5():
    sentence = "O Rato Rui Gosta De QueiJo FresQuiNho"
    result = list_comprehension_exercise_5(sentence)
    expect = ["O", "R", "R", "G", "D", "Q", "J", "F", "Q", "N"]

    assert type(result) is list, "Verificar se está retonando uma lista."

    assert (
        result == expect
    ), """Verificar se está montado para retornar apenas as 
        letras que estão em uppercase."""


def test_exercise_6():
    sentence = "o rato rui roeu a roupa do rei de roma"
    result = list_comprehension_exercise_6(sentence)
    expect = ["rato", "roeu", "roupa", "roma"]

    assert type(result) is list, "Verificar se está retonando uma lista."

    assert (
        result == expect
    ), """Verificar se está montado para retornar palavras 
        que começam com 'r' e que tenham pelo menos 4 letras."""
