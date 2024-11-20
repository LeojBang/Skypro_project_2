from src.product import Product


def test_product(products):
    assert products.name == "Samsung Galaxy C23 Ultra"
    assert products.description == "256GB, Серый цвет, 200MP камера"
    assert products.price == 180000.0
    assert products.quantity == 5


def test_sample_product(products):
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 185000.0,
            "quantity": 5,
        }
    )

    assert new_product.name == "Samsung Galaxy C23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 185000.0
    assert new_product.quantity == 10


def test_new_product():
    new_product_2 = Product.new_product(
        {"name": '55" QLED 5K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
    )

    assert new_product_2.name == '55" QLED 5K'
    assert new_product_2.description == "Фоновая подсветка"
    assert new_product_2.price == 123000
    assert new_product_2.quantity == 7


def test_invalid_price(products, capsys):
    products.price = 0
    captured = capsys.readouterr()

    assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
    assert products.price == 180000.0


def test_normal_price(products, capsys):
    products.price = 200000.0

    captured = capsys.readouterr()
    assert captured.out == ""
    assert products.price == 200000.0
