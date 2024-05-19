from typing import Literal
from items.item import Armor


class ArmorClasses:
    def __init__(self) -> None:
        self.eac = 0
        self.kac = 0
        self.ac_vs = 0
        self.armor = Armor("Skin", 0, 0, "Light", 0, 0, "+0", None, None, 0)

    def update_ac(self, character_dex_mod: int):
        """update ac tab related boxes
        """
        self.eac = 10 + self.armor.eac + character_dex_mod + 0
        self.kac = 10 + self.armor.kac + character_dex_mod + 0
        self.ac_vs = 8 + self.kac

    def update_armor(self, new_armor: Armor) -> None:
        self.armor = new_armor

    def get_armor_stats(self) -> dict[Literal["eac", "kac", "ac_vs", "armor_eac", "armor_kac"], int]:
        return {
            "eac": self.eac,
            "kac": self.kac,
            "ac_vs": self.ac_vs,
            "armor_eac": self.armor.eac,
            "armor_kac": self.armor.kac
        }
