class Product:
from abc import ABC, abstractmethod

class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: dict):
        pass

class ProductMixin:
    def __init__(self, *args, **kwargs):
        print(f"{self.__class__.__name__}({', '.join(map(str, args))})")
        super().__init__(*args, **kwargs)

class Product(ProductMixin, BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.price = price
        self.__price = price
        self.quantity = quantity
        super().__init__(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Цена не должна быть нулевой или отрицательной")

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, type(self)):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Операнд должен быть экземпляром того же класса")

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"]
        )

class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
            efficiency=product_data["efficiency"],
            model=product_data["model"],
            memory=product_data["memory"],
            color=product_data["color"]
        )

class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
            country=product_data["country"],
            germination_period=product_data["germination_period"],
            color=product_data["color"]
        )

class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.products = products
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(products)

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
        Category.product_count += len(self.__products)

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Добавляемый объект должен быть экземпляром класса Product или его наследника")

    @property
    def products(self):
        return "\n".join(str(product) for product in self.__products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def middle_price(self):
        try:
            return sum(product.price for product in self.__products) / len(self.__products)
        except ZeroDivisionError:
            return 0

    if __name__ == "__main__":
        try:
            product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
        except ValueError as e:
            print(
                "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
        else:
            print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

        print(category1.middle_price())

        category_empty = Category("Пустая категория", "Категория без продуктов", [])
        print(category_empty.middle_price())
