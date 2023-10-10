from items.item import Armor


class ArmorClasses:
    def __init__(self) -> None:
        self.eac = 0
        self.kac = 0
        self.ac_vs = 0
        self.armor = Armor("Skin", 0, 0, "Light", 0, 0, "+0", None, None, 0)

    def update_ac(self, character_dex_mod):
        """update ac tab related boxes
        """
        self.eac = 10 + self.armor.eac + character_dex_mod + 0
        self.kac = 10 + self.armor.kac + character_dex_mod + 0
        self.ac_vs = 8 + self.kac

    def update_armor(self, new_armor: Armor) -> None:
        self.armor = new_armor
