from main import text_merge


def test_text_merge_blank_spaces():
    text_a = "Na Londres do pós-guerra, a escritora     Juliet tenta encontrar."
    text_b = "um vinho intenso    e    delicado."

    result = text_merge(text_a, text_b)
    expected = "Na Londres do pós-guerra, a escritora Juliet tenta encontrar um vinho intenso e delicado."

    assert (
        result == expected
    ), "Verifique se há mais de um espaço em branco entre palavras"


def test_text_merge_pos_dot_letter_capitalize():
    text_a = "Uma trama para seu novo livro. ela recebe ajuda desconhecida."
    text_b = "e se sente enfeitiçada pelo mistério. de quem será ?"

    result = text_merge(text_a, text_b)
    expected = "Uma trama para seu novo livro. Ela recebe ajuda desconhecida e se sente enfeitiçada pelo mistério. De quem será ?"

    assert result == expected, "Verifique se a primeira letra após um ponto é maiuscula"


def test_text_merge_upper_lower_first_letter():
    text_a = "na Londres do pós-guerra"
    text_b = 'O romance "Cinco Quartos de Laranja"'

    result = text_merge(text_a, text_b)
    expected = 'Na Londres do pós-guerra o romance "Cinco Quartos de Laranja"'

    assert (
        result == expected
    ), "Verifique se a primeira letra do texto a e do b sao maiuscula e minuscula respectivamente quanto juntados"


def test_merge_remove_period():
    text_a = "Na Londres pós-guerra."
    text_b = "fazia muito frio"

    result = text_merge(text_a, text_b)
    expected = "Na Londres pós-guerra fazia muito frio"

    assert result == expected, "Verifique se retirou o ponto final do text_of_blog_a"


def test_merge_join_texts():
    text_a = "Na Londres pós-guerra "
    text_b = "fazia muito frio"

    result = text_merge(text_a, text_b)
    expected = "Na Londres pós-guerra fazia muito frio"

    assert result == expected, "Verifique se os textos estão sendo unidos corretamente"
