# Продуктовый каталог

Проект представляет собой систему для работы с категориями товаров и продуктами. Программа позволяет загружать данные о продуктах из JSON-файлов, создавать объекты для категорий и товаров, а также выводить информацию о категориях и их товарах.

## Структура проекта

Проект состоит из нескольких классов и функций, которые работают с категориями товаров и продуктами:
```
├── data/
│   └── products.json # Пример данных продуктов в формате JSON
│
├── htmlcov/ # Покрытие тестами
│
├── src/
│   ├── __init__.py
│   ├── category.py   # Модуль с классом Category
│   ├── product.py    # Модуль с классом Product
│   └── utils.py      # Утилиты для работы с JSON
│
├── tests/            # Папка с тестами
│   ├── __init__.py
│   ├── conftest.py       # Фикстуры для тестов
│   ├── test_category.py  # Тесты для класса Category
│   ├── test_utils.py     # Тесты утилиты работы с JSON
│   └── test_product.py   # Тесты для класса Product
│
├── main.py # Основной файл для запуска программы
├── .flake8
├── .gitignore
├── pyproject.toml
├── poetry.lock
├── requirements.txt  # Список зависимостей
└── README.md

```
- **Category** — класс, представляющий категорию товаров, который содержит имя, описание и список товаров в категории.
- **Product** — класс, представляющий товар, содержащий имя, описание, цену и количество.
- **read_json(path: str)** — функция для чтения данных из JSON-файла.
- **create_objects_from_json(data: dict)** — функция для создания объектов категорий и продуктов на основе данных из JSON.

### Классы-наследники

Проект включает два класса-наследника от `Product`:

#### Класс `Smartphone`
Класс представляет собой модель смартфона и расширяет функционал базового класса `Product`. Включает дополнительные атрибуты:
- **`efficiency`** — производительность.
- **`model`** — модель смартфона.
- **`memory`** — объем встроенной памяти (в гигабайтах).
- **`color`** — цвет устройства.

#### Класс `LawnGrass`
Класс описывает газонную траву и наследует базовые свойства от `Product`. Включает дополнительные атрибуты:
- **`country`** — страна-производитель.
- **`germination_period`** — срок прорастания (в днях).
- **`color`** — цвет газона.

---

### Ограничения сложения

Метод сложения (`__add__`) был доработан для обеспечения следующих условий:
- **Сложение возможно только для объектов одного типа.** Например:
  - `Smartphone` + `Smartphone` — допустимо.
  - `LawnGrass` + `LawnGrass` — допустимо.
  - `Smartphone` + `LawnGrass` — выброс исключения `TypeError`.

Для реализации используется проверка типа объектов через функцию `type()`.

---

### Ограничения добавления продукта

Метод добавления продукта в категорию (`add_product`) доработан для проверки типа добавляемых объектов:
- Добавить можно только объект класса `Product` или его наследников (`Smartphone`, `LawnGrass`).
- Попытка добавить объект другого типа вызовет исключение `TypeError`.

Для проверки используется функция `isinstance()` или `issubclass()`.

## Установка

1. Клонируйте репозиторий на свой локальный компьютер:

    ```bash
    git clone https://github.com/LeojBang/SkyPro_OOP_module.git
    ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
   poetry install
    ```

## Использование

### 1. Структура данных в JSON

Пример структуры данных в JSON:

```json
[
  {
    "name": "Смартфоны",
    "description": "Смартфоны, как средство коммуникации",
    "products": [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      },
      {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      },
      {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
      }
    ]
  },
  {
    "name": "Телевизоры",
    "description": "Современный телевизор, который позволяет наслаждаться просмотром",
    "products": [
      {
        "name": "55\" QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7
      }
    ]
  }
]
```
### 2. Тестирование

Проект включает тесты для проверки функциональности:

	•	Тесты для классов Category и Product.
	•	Тесты для функций read_json и create_objects_from_json.

Для запуска тестов используйте команду:
```bash
pytest
```

### 3. Запуск программы

Запустите программу, чтобы загрузить данные из файла и вывести информацию о категориях и продуктах:
```bash
python3 main.py
```

### Контакты

Для вопросов и предложений, пожалуйста, свяжитесь со мной по электронной почте: m.merkulovdodo@gmail.com

## Лицензия
Этот файл `README.md` описывает структуру проекта, его компоненты и инструкции по использованию и тестированию.
### Skypro