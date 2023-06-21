import csv
import os
import math


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

    def __repr__(self):
        return f'{self.__class__.__name__}{self.name, self.price, self.quantity}'

    def __add__(self, other):
        if isinstance(other, Item) or isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            raise TypeError(f"Объект {other} не является экземпляром класса Item или Phone")

    def __str__(self):
        return self._name

    @classmethod
    def add_item(cls, item):
        cls.all.append(item)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self._name = name
        else:
            raise Exception("Длина наименования товара превышает 10 символов.")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        file_path = os.path.join(os.path.dirname(__file__), 'items.csv')
        with open(file_path, 'r', encoding='cp1251') as csvfile:
            reader = csv.DictReader(csvfile)
            items = []
            for row in reader:
                name = row["name"]
                price = float(row['price'])
                quantity = int(row['quantity'])
                item = cls(name, price, quantity)
                cls.add_item(item)  # Добавить экземпляр в список all
                items.append(item)
            return items

    @staticmethod
    def string_to_number(value):
        new_value = math.floor(float(value))
        return new_value
