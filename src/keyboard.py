from src.item import Item


class MixinLog:
    def __init__(self):
        self._layout = "EN"

    def change_layout(self, new_lang):
        if new_lang in ["EN", "RU"]:
            self._layout = new_lang
            print(f"Раскладка изменена на {new_lang}")
            return self._layout
        else:
            print("Недопустимая раскладка.")


class KeyBoard(Item, MixinLog):
    def __init__(self, name, price, quantity, language="EN"):
        super().__init__(name, price, quantity)
        self._language = language

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"

        elif self._language == "RU":
            self._language = "EN"

        else:
            raise AttributeError

        return self
