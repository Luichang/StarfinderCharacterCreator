from copy import deepcopy
from typing import Literal

SKILL_NAMES = Literal[
    "acrobatics",
    "athletics",
    "bluff",
    "computers",
    "culture",
    "diplomacy",
    "disguise",
    "engineering",
    "intimidate",
    "life science",
    "medicine",
    "mysticism",
    "perception",
    "physical science",
    "piloting",
    "profession",
    "profession2",
    "sense motive",
    "sleight of hand",
    "stealth",
    "survival"
]

class Skills:
    def __init__(self) -> None:
        self.skills: dict[SKILL_NAMES, int] = {
            "acrobatics"       : 0,
            "athletics"        : 0,
            "bluff"            : 0,
            "computers"        : 0,
            "culture"          : 0,
            "diplomacy"        : 0,
            "disguise"         : 0,
            "engineering"      : 0,
            "intimidate"       : 0,
            "life science"     : 0,
            "medicine"         : 0,
            "mysticism"        : 0,
            "perception"       : 0,
            "physical science" : 0,
            "piloting"         : 0,
            "profession"       : 0,
            "profession2"      : 0,
            "sense motive"     : 0,
            "sleight of hand"  : 0,
            "stealth"          : 0,
            "survival"         : 0,
        }

        self.skill_ranks = deepcopy(self.skills)

        self.skill_misc = deepcopy(self.skills)

        self.skill_dabbler = deepcopy(self.skills)

        self.skill_class = deepcopy(self.skills)

        self.skill_race = deepcopy(self.skills)

        self.skill_theme = deepcopy(self.skills)

        self.max_skillpoints = 0
        self.skillpoints = 0

        self.profession_ability = 'wis'
        self.profession2_ability = 'wis'

    def update_skillpoints(self, class_skill_count, int_mod, level):
        new_max = (class_skill_count + int_mod) * level
        if new_max > self.max_skillpoints:
            self.skillpoints += new_max - self.max_skillpoints
        elif new_max < self.max_skillpoints:
            # remove all spent skillpoints
            for skill in self.skill_ranks:
                self.skills[skill] = 0
                self.skill_ranks[skill] = 0
            self.skillpoints = new_max
        self.max_skillpoints = new_max

    def calc_skills(self, mods, bonuses: list[SKILL_NAMES]) -> None:
        """calculate the total of every skill
        """
        self.skills = {
            "acrobatics"       : mods['dex'],
            "athletics"        : mods['str'],
            "bluff"            : mods['cha'],
            "computers"        : mods['int'],
            "culture"          : mods['int'],
            "diplomacy"        : mods['cha'],
            "disguise"         : mods['cha'],
            "engineering"      : mods['int'],
            "intimidate"       : mods['cha'],
            "life science"     : mods['int'],
            "medicine"         : mods['int'],
            "mysticism"        : mods['wis'],
            "perception"       : mods['wis'],
            "physical science" : mods['int'],
            "piloting"         : mods['dex'],
            "profession"       : mods[self.profession_ability],
            "profession2"      : mods[self.profession2_ability],
            "sense motive"     : mods['wis'],
            "sleight of hand"  : mods['dex'],
            "stealth"          : mods['dex'],
            "survival"         : mods['wis'],
        }

        for skill in self.skills:
            if self.skill_ranks[skill] > 0 or self.skill_dabbler[skill] > 0:
                self.skills[skill] +=   self.skill_ranks[skill] +\
                                        self.skill_misc[skill] + self.skill_dabbler[skill] +\
                                          self.skill_race[skill] + self.skill_theme[skill]
                self.skills[skill] += self.calc_skill_class(skill, bonuses)
            else:
                self.skills[skill] = 0

    def calc_skill_class(self, skill : str, bonuses: list[SKILL_NAMES]) -> int:
        """function to calculate the resulting skill class value

        Args:
            skill (str): name of the skill that is to be checked

        Returns:
            int: 0 if not a class skill. 3 if only once a class skill, anything above 3 is the
                 amount of duplicates the class skill
        """
        skill_count = bonuses.count(skill)
        if skill_count == 0:
            return 0
        if skill_count == 1:
            return 3
        return 3 + skill_count - 1

    def get_misc_mods(self) -> dict[SKILL_NAMES, int]:
        misc_mods = {}
        for skill, misc_value in self.skill_misc.items():
            misc_mods[skill] = misc_value + self.skill_race[skill] + self.skill_theme[skill]
        return misc_mods

    def point_buy_skill(self, level: int, skill_name: SKILL_NAMES):
        if self.skill_ranks[skill_name] >= level:
            return False #?

        if self.skillpoints == 0:
            return False #?

        self.skill_ranks[skill_name] += 1
        self.skillpoints -= 1

    def update_point_buy_skill(self, skill_name: SKILL_NAMES, skill_value: int):
        if self.skillpoints < skill_value:
            return False #?

        skill_diff = skill_value - self.skill_ranks[skill_name]
        self.skill_ranks[skill_name] = skill_value
        self.skillpoints -= skill_diff

    def update_class_stats(self, new_class_stats: dict[SKILL_NAMES, int]):
        self.skill_class = new_class_stats

    def update_race_stats(self, new_race_stats: dict[SKILL_NAMES, int]):
        self.skill_race = new_race_stats

    def update_theme_stats(self, new_theme_stats: dict[SKILL_NAMES, int]):
        self.skill_theme = new_theme_stats

    def update_professions(self, profession1 : str=None, profession2 : str = None) -> None:
        """function to update the profession ability modifiers

        Args:
            profession1 (str, optional): ability modifier for profession1.
                                         Options are 'wis, int, and cha'. Defaults to None.
            profession2 (str, optional): ability modifier for profession2.
                                         Options are 'wis, int, and cha'. Defaults to None.
        """
        if profession1:
            self.profession_ability = profession1
        if profession2:
            self.profession2_ability = profession2
