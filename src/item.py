import csv
import os
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __repr__(self):
        return self._name

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
            pass

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
        with open('C:/Users/Админ/PycharmProjects/electronics-shop-project/src/items.csv', 'r',
                  encoding='cp1251') as csvfile:
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
        new_value = round(float(value) / 5) * 5
        return round(new_value)
