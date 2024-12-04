from src.product import Product, Smartphone, LawnGrass


def test_print_mixin(capsys):
    Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    messages = capsys.readouterr()
    assert messages.out.strip() == 'Product(Samsung Galaxy C23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0. 5)'

    Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
               "S23 Ultra", 256, "Серый")
    messages = capsys.readouterr()
    assert messages.out.strip() == 'Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0. 5)'

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    messages = capsys.readouterr()
    assert messages.out.strip() == 'LawnGrass(Газонная трава, Элитная трава для газона, 500.0. 20)'





