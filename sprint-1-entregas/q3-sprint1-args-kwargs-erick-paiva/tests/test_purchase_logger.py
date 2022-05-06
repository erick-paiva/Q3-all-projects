from main import purchase_logger


def test_purchase_logger():
    purchase = {"name": "washing powder", "price": 6.7, "quantity": 4}

    result = purchase_logger(**purchase)
    expected = "Product washing powder costs 6.7 and was bought 4"

    assert result == expected, "Verifique se a string está sendo formatada corretamente"
