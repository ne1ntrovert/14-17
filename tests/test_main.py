import pytest
from src.main import Product, Category
from src.main import Product, Category, Smartphone, LawnGrass

@pytest.fixture(autouse=True)
def reset_counters():
    @@ -13,21 +13,301
    @@


def test_product_initialization():
    assert product.price == 100.0
    assert product.quantity == 10

def test_smartphone_initialization():
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"

def test_lawn_grass_initialization():
    lawn_grass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
    )
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Элитная трава для газона"
    assert lawn_grass.price == 500.0
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7 дней"
    assert lawn_grass.color == "Зеленый"

def test_category_initialization():
    product1 = Product("Product 1", "Description 1", 100.0, 5)
    product2 = Product("Product 2", "Description 2", 200.0, 3)
    category = Category("Test Category", "Test Description", [product1, product2])
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )
    smartphone2 = Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "Gray space"
    )
    category = Category("Test Category", "Test Description", [smartphone1, smartphone2])
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert len(category.products) == 2
    assert len(category._Category__products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2

def test_add_product():
    category = Category("Test Category", "Test Description")
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )
    category.add_product(smartphone)
    assert len(category._Category__products) == 1
    assert Category.product_count == 1

def test_add_product_type_check():
    category = Category("Test Category", "Test Description")
    with pytest.raises(TypeError):
        category.add_product("Not a Product")

def test_products_getter():
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )
    smartphone2 = Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "Gray space"
    )
    category = Category("Test Category", "Test Description", [smartphone1, smartphone2])
    expected_output = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    )
    assert category.products == expected_output

def test_new_product():
    product_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
        "efficiency": 95.5,
        "model": "S23 Ultra",
        "memory": 256,
        "color": "Серый"
    }
    smartphone = Smartphone.new_product(product_data)
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"

def test_price_setter():
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )
    smartphone.price = 200000.0
    assert smartphone.price == 200000.0
    smartphone.price = -50.0
    assert smartphone.price == 200000.0
    smartphone.price = 0
    assert smartphone.price == 200000.0

def test_multiple_categories():
    product1 = Product("Product 1", "Description 1", 100.0, 5)
    product2 = Product("Product 2", "Description 2", 200.0, 3)
    product3 = Product("Product 3", "Description 3", 300.0, 2)
    category1 = Category("Category 1", "Description 1", [product1, product2])
    category2 = Category("Category 2", "Description 2", [product3])
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )
    smartphone2 = Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "Gray space"
    )
    lawn_grass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
    )
    category1 = Category("Category 1", "Description 1", [smartphone1, smartphone2])
    category2 = Category("Category 2", "Description 2", [lawn_grass])
    assert Category.category_count == 2
    assert Category.product_count == 3
    assert Category.product_count == 3

def test_product_str():
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )
    assert str(smartphone) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."

def test_category_str():
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )
    smartphone2 = Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "Gray space"
    )
    category = Category("Test Category", "Test Description", [smartphone1, smartphone2])
    assert str(category) == "Test Category, количество продуктов: 13 шт."

def test_product_add():
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )
    smartphone2 = Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "Gray space"
    )
    assert smartphone1 + smartphone2 == 2580000.0

def test_product_add_type_check():
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )
    lawn_grass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
    )
    with pytest.raises(TypeError):
        smartphone + lawn_grass

def test_mixin():
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )
    assert str(smartphone) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."

def test_product_initialization_with_zero_quantity():
    with pytest.raises(ValueError):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)

def test_middle_price():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Test Category", "Test Description", [product1, product2])
    assert category.middle_price() == (180000.0 + 210000.0) / 2

def test_middle_price_empty_category():
    category = Category("Empty Category", "Test Description", [])
    assert category.middle_price() == 0
