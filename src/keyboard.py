from src.item import Item


class MixinLog:
    def __init__(self):
        self._language = "EN"

    @property
    def language(self):
        """
        Геттер для получения текущего значения языка
        """
        return self._language

    def change_lang(self):
        """
        Метод для изменения значения языка
        """
        if self._language == "EN":
            self._language = "RU"
        elif self._language == "RU":
            self._language = "EN"
        else:
            raise AttributeError("Недопустимый язык.")

        return self


class KeyBoard(Item, MixinLog):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
