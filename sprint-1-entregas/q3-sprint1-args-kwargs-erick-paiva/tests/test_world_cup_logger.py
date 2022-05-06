from main import world_cup_logger


def test_world_cup_logger():
    country = "Alemanha"
    year_list = [2014, 1990, 1974, 1954]

    result = world_cup_logger(country, *year_list)
    expected = "Alemanha - 1954, 1974, 1990 e 2014"

    assert (
        result == expected
    ), "Verifique se a montagem da string foi feita corretamente"


def test_world_cup_logger_2():
    country = "Ursal"
    year_list = [2030, 2034, 2026, 2022, 2038]

    result = world_cup_logger(country, *year_list)
    expected = "Ursal - 2022, 2026, 2030, 2034 e 2038"

    assert (
        result == expected
    ), "Verifique se a montagem da string foi feita corretamente"
