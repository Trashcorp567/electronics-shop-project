from src.item import Item
from src.keyboard import KeyBoard
from src.keyboard import MixinLog


def class_test_keyboard():
    """
    Проверка на наследование атрибутов класса Item
    """
    kb = KeyBoard('Dark Project KD87A', 27600, 3)
    assert kb.name == 'Dark Project KD87A'
    assert kb.price == 27600
    assert kb.quantity == 3


def test_change_lang():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert kb.language == "EN"  # Проверяет установленное значение по умолчанию
    kb.change_lang()  # Изменяет язык на RU
    assert kb.language == "RU"  # Проверяет измененное значение на RU
