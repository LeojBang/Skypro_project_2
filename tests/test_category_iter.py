import pytest

from src.category_iter import CategoryIter


def test_category_iter(category_iter):
    assert iter(category_iter) is category_iter
    assert category_iter.index == 0
    assert next(category_iter).name == 'Samsung Galaxy C23 Ultra'
    assert next(category_iter).name == 'Iphone 15'
    with pytest.raises(StopIteration):
        next(category_iter)
