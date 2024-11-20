import json

from src.utils import create_objects_from_json, read_json


def test_read_json(tmp_path):
    data = [{"key": "value"}]
    temp_file = tmp_path / "test.json"
    temp_file.write_text(json.dumps(data, indent=4))

    assert read_json(str(temp_file)) == data


def test_create_objects_from_json(data_of_products):
    result = create_objects_from_json(data_of_products)
    category_smart_phone, category_television = result

    assert len(result) == 2

    assert category_smart_phone.name == "Смартфоны"
    assert category_television.name == "Телевизоры"
