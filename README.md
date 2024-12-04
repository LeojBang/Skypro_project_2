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
│   ├── base_entity.py # Базовый класс для Category и Order
│   ├── base_product.py # Базовый класс для Product
│   ├── category.py   # Модуль с классом Category
│   ├── category_iter.py # Модуль с классом CategoryIter
│   ├── order.py    # Модуль с классом Order
│   ├── print_mixin.py # Модуль с классом Mixin
│   ├── product.py    # Модуль с классом Product
│   └── utils.py      # Утилиты для работы с JSON
│
├── tests/            # Папка с тестами
│   ├── __init__.py
│   ├── conftest.py       # Фикстуры для тестов
│   ├── test_category.py  # Тесты для класса Category
│   ├── test_category_iter.py  # Тесты для класса CategoryIter
│   ├── test_utils.py     # Тесты утилиты работы с JSON
│   ├── test_order.py     # Тесты для класса Order
│   ├── test_print_mixin.py # Тесты для класса Mixin
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
- **Order** - класс, представляющий ссылку на то, какой товар был куплен, количество купленного товара, а также итоговая стоимость.
- **read_json(path: str)** — функция для чтения данных из JSON-файла.
- **create_objects_from_json(data: dict)** — функция для создания объектов категорий и продуктов на основе данных из JSON.

### Классы:
1. **`Product`** — представляет отдельный товар.  
   Атрибуты:
   - `name` — название продукта.
   - `description` — описание продукта.
   - `price` — цена продукта.
   - `quantity` — количество доступного товара.

2. **`Category`** — представляет категорию товаров.  
   Атрибуты:
   - `name` — название категории.
   - `description` — описание категории.
   - `products` — список товаров в категории.

3. **`Order`** — представляет заказ.  
   Атрибуты:
   - `product` — товар, указанный в заказе.
   - `quantity` — количество товара в заказе.
   - `total_price` — итоговая стоимость заказа.

4. **`Smartphone`** и **`LawnGrass`** — расширения класса `Product`, представляющие смартфоны и газонную траву соответственно.

5. **Абстрактные классы**:
   - `BaseEntity` — общий интерфейс для классов с методом `__str__`.

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
### 2. Пример работы с проектом

```python
from src.category import Category
from src.product import Product
from src.order import Order

# Создание продуктов
product1 = Product("Iphone 15", "512GB, Gray Space", 210000.0, 8)
product2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

# Создание категории
category = Category("Смартфоны", "Категория смартфонов", [product1, product2])

# Вывод информации о категории
print(category)

# Создание заказа
order = Order(product1, 2, product1.price * 2)
print(order)
```

### 3. Тестирование

Проект включает тесты для проверки функциональности:

	•	Тесты для классов Category, Product, CategoryIter, Order, PrintMixin.
	•	Тесты для функций read_json и create_objects_from_json.

Для запуска тестов используйте команду:
```bash
pytest
```

### 4. Запуск программы

Запустите программу, чтобы загрузить данные из файла и вывести информацию о категориях и продуктах:
```bash
python3 main.py
```

### Контакты

Для вопросов и предложений, пожалуйста, свяжитесь со мной по электронной почте: m.merkulovdodo@gmail.com

## Лицензия
Этот файл `README.md` описывает структуру проекта, его компоненты и инструкции по использованию и тестированию.
### Skypro