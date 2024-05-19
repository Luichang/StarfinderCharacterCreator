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

name_to_mod: dict[ATTRIBUTE_NAMES, MOD_NAMES] = {
    "strength": "str",
    "dexterity": "dex",
    "constitution": "con",
    "intelligence": "int",
    "wisdom": "wis",
    "charisma": "cha"
}

class Attributes:
    def __init__(self) -> None:

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

    def update_point_buy(self, stat: ATTRIBUTE_NAMES, new_amount: int):
        amount_before = self.ability_point_buy[stat]
        self.ability_point_buy[stat] = new_amount
        self.spendable_point_buy -= new_amount - amount_before

    def increase_buy(self, stat) -> None:
        if self.spendable_ability_increase > 0:
            self.ability_increases[stat] += 1
            self.spendable_ability_increase -= 1

    def update_increase_buy(self, stat: ATTRIBUTE_NAMES, new_amount: int):
        amount_before = self.ability_increases[stat]
        self.ability_increases[stat] = new_amount
        self.spendable_ability_increase -= new_amount - amount_before


    def get_attribute_stats(self) -> dict[str, int]:
        """Calculate the attribute stats by adding 10 (as the base attribute number), self.ability_point_buy, self.race and self.theme.
        Finally for each point in the self.ability_increases if the combined total is less than 18 add 2, else add 1

        Returns:
            dict[str, int]: attribute total dict
        """
        attributes = {}
        for attribute_name, point_buy_value in self.ability_point_buy.items():
            total = 10 + point_buy_value + self.race[attribute_name] + self.theme[attribute_name]
            for _ in range(self.ability_increases[attribute_name]):
                if total <= 17:
                    total += 2
                else:
                    total += 1
            attributes[attribute_name] = total
        return attributes

    def get_attribute_modifiers(self) -> dict[MOD_NAMES, int]:
        attributes = self.get_attribute_stats()
        mods: dict[MOD_NAMES, int] = {name_to_mod[attribute_name]: ((attribute_val // 2) - 5) for attribute_name, attribute_val in attributes.items()}
        return mods
