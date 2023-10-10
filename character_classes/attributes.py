from copy import deepcopy
from typing import Literal

ATTRIBUTE_NAMES = Literal[
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma"
]

MOD_NAMES = Literal[
    "str",
    "dex",
    "con",
    "int",
    "wis",
    "cha"
]

class Attributes:
    def __init__(self) -> None:
        self.attributes: dict[ATTRIBUTE_NAMES, int] = {
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10
        }

        self.mods: dict[MOD_NAMES, int] = {
            "str" : 0,
            "dex" : 0,
            "con" : 0,
            "int" : 0,
            "wis" : 0,
            "cha" : 0
        }

        self.spendable_point_buy = 10
        self.ability_point_buy: dict[ATTRIBUTE_NAMES, int] = {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0
        }

        self.spendable_ability_increase = 0
        self.ability_increases = deepcopy(self.ability_point_buy)

        self.race = deepcopy(self.ability_point_buy)

        self.theme = deepcopy(self.ability_point_buy)

    def update_spendable_ability_increase(self, level: int) -> None:
        self.spendable_ability_increase = (level // 5) * 4

    def update_race_bonus(self, race: dict[str, int]) -> None:
        self.race = race

    def update_theme_bonus(self, theme: dict[str, int]) -> None:
        self.theme = theme

    def point_buy(self, stat) -> None:
        if self.spendable_point_buy > 0:
            self.ability_point_buy[stat] += 1
            self.spendable_point_buy -= 1

    def increase_buy(self, stat) -> None:
        if self.spendable_ability_increase > 0:
            self.ability_increases[stat] += 1
            self.spendable_ability_increase -= 1

    def get_attribute_stats(self) -> dict[str, int]:
        """Calculate the attribute stats by adding the stat value of the self.attributes, self.ability_point_buy, self.race and self.theme.
        Finally for each point in the self.ability_increases if the combined total is less than 18 add 2, else add 1

        Returns:
            dict[str, int]: attribute total dict
        """
        attributes = {}
        for key, attribute in self.attributes.items():
            total = attribute + self.ability_point_buy[key] + self.race[key] + self.theme[key]
            for _ in range(self.ability_increases[key]):
                if total <= 17:
                    total += 2
                else:
                    total += 1
            attributes[key] = total
        return attributes

    def get_attribute_modifiers(self) -> dict[MOD_NAMES, int]:
        attributes = self.get_attribute_stats()
        mods: dict[MOD_NAMES, int] = {attribute_name: ((attribute_val // 2) - 5) for attribute_name, attribute_val in attributes}
        self.mods = mods
        return mods
