# Código do dev aqui
def list_comprehension_exercise_1():
    return [i for i in range(11)]

def list_comprehension_exercise_2():
    return [i for i in range(22) if i % 2 == 0 or i % 3 == 0]

def list_comprehension_exercise_3():
    return [i for i in range(-5, 32) if i % 2 != 0 and i % 5 != 0]

def list_comprehension_exercise_4():
    return [i * i for i in range(11)] 

def list_comprehension_exercise_5(sentence):
    return [letra for letra in sentence if letra == letra.upper() and letra != " "]

def list_comprehension_exercise_6(sentence):
    return [palavra for palavra in sentence.split() if palavra[0] == "r" and len(palavra) > 3]
