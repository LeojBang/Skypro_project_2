from src.category_iter import CategoryIter


def test_category_iter(smartphone_products):
    iterator = CategoryIter(smartphone_products)
    assert len(list(iterator)) == 2
