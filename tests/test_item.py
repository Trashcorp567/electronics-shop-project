"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.apply_discount() == None
    assert item1.price == 10000.0

    assert item2.apply_discount() == None
    assert item2.price == 20000


def test_add_item():
    item1 = Item('Телефон', 10000, 5)
    item2 = Item('Ноутбук', 20000, 3)

    Item.add_item(item1)
    Item.add_item(item2)

    assert len(Item.all) == 2
    assert item1 in Item.all
    assert item2 in Item.all


def test_name_setter():
    item = Item('Телефон', 10000, 5)

    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    item.name = 'СуперСмартфон'
    assert item.name == 'Смартфон'  # Длинное имя не должно измениться

    item.name = 'Ноутбук'
    assert item.name == 'Ноутбук'


def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("iPhone X", 160_000, 3, 1)
    assert phone1.number_of_sim == 2
    assert phone2.number_of_sim == 1


def test_add_phone():
    phone1 = Phone("iPhone 14", 120_000, 90, 2)
    item1 = Item("Смартфон", 10000, 120)
    assert item1 + phone1 == 210
