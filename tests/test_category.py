from src.category import Category


def test_category(categories):
    category_smart_phone, category_television = categories

    assert Category.product_count == 3
    assert Category.category_count == 2

    assert category_smart_phone.name == "Смартфоны"
    assert len(category_smart_phone.products) == 2

    assert category_television.name == "Телевизоры"
    assert len(category_television.products) == 1
