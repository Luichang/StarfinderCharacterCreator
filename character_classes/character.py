from typing import Optional
from character_classes.attributes import Attributes
from character_classes.armor import ArmorClasses
from character_classes.attacks import Attacks
from character_classes.health import Health
from character_classes.initiative import Initiative
from character_classes.saves import Saves
from character_classes.skills import Skills
from character_classes.spells import Spells
from starfinder_classes.starfinder_class import StarfinderClass
from starfinder_races.starfinder_race import StarfinderRace
from starfinder_themes.starfinder_theme import StarfinderTheme

class Character:
    def __init__(self, name: str=None) -> None:
        self.name = name
        self.level = 0
        self.exp = 0
        self.health = Health()
        self.attributes = Attributes()
        self.armor = ArmorClasses()
        self.saves = Saves()
        self.attacks = Attacks()
        self.initiaitve = Initiative()
        self.skills = Skills()
        self.spells = Spells()
        self.feats = None
        self.starfinder_class: Optional[StarfinderClass] = None
        self.race: Optional[StarfinderRace] = None
        self.theme: Optional[StarfinderTheme] = None

    def update_name(self, new_name: str) -> None:
        self.name = new_name

    def choose_class(self, class_name: str, soldier_style: Optional[str]):
        if class_name == "Soldier":
            self.starfinder_class = StarfinderClass.create(class_name.lower(), soldier_style.lower())
        else:
            self.starfinder_class = StarfinderClass.create(class_name.lower())

        self.update_class_stats()
        self.update_saves()
        self.update_attack()

    def update_professions(self, prof1: str, prof2: str) -> None:
        self.skills.update_professions(prof1.lower(), prof2.lower())
        self.attributes.get_attribute_stats()

    def update_class_stats(self):
        character_skills = {}
        for skill_name in self.skills.skills.keys():
            val = 0
            if skill_name in self.starfinder_class.bonuses:
                val = 3
            character_skills[skill_name] = val
        self.skills.update_class_stats(character_skills)
        self.skills.calc_skills(self.attributes.get_attribute_modifiers(), self.starfinder_class.bonuses)
        self.update_skillpoints()
        self.update_health()

    def choose_race(self, race_name: str, human_style: Optional[str]) -> None:
        if race_name == "Human":
            self.race = StarfinderRace.create(race_name.lower(), human_style.lower())
        else:
            self.race = StarfinderRace.create(race_name.lower())

        self.attributes.update_race_bonus(self.race.attributes)
        self.update_abilities()

    def resolve_race_feats(self):
        skills, spells, number_of_feats_to_add = self.race.resolve_abilities()
        race_skills = {
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
        for skill, value in skills:
            if skill == "any":
                continue # TODO
            race_skills[skill] = value
        self.skills.update_race_stats(race_skills)


    def choose_theme(self, theme_name: str, themeless_style: Optional[str]):
        if theme_name == "Themeless":
            self.theme = StarfinderTheme.create(theme_name.lower(), themeless_style.lower())
        else:
            self.theme = StarfinderTheme.create(theme_name.lower())

        skills, theme_spell = self.theme.resolve_abilities(self.level)

        self.attributes.update_theme_bonus(self.theme.attributes)
        self.update_abilities()

    def update_abilities(self):
        self.update_health()
        self.update_initiative()
        self.update_saves()
        self.update_ac()
        self.update_attack()
        self.update_dabbler()

    def update_dabbler(self) -> None:
        """function to update the dabbler stats
        """
        dabble = 0
        if self.theme == "spacefarer" and self.level >= 6:
            dabble = 2
        # +2 bonus to skill checks for skills with 0 ranks in skill
        for skill in self.skills.skills:
            if self.skills.skill_ranks[skill] == 0:
                self.skills.skill_dabbler[skill] = dabble
            else:
                self.skills.skill_dabbler[skill] = 0

    def update_health(self):
        if not all((self.starfinder_class, self.race)):
            return
        mods = self.attributes.get_attribute_modifiers()
        self.health.update_hit_points(
            class_hp=self.starfinder_class.hit_points,
            race_hp=self.race.hit_points,
            class_stamina=self.starfinder_class.stamina_points,
            class_mod=mods[self.starfinder_class.key],
            con_mod=mods['con'],
            character_level=self.level
        )

    def update_ac(self):
        mods = self.attributes.get_attribute_modifiers()
        self.armor.update_ac(mods['dex'])

    def update_saves(self):
        if self.starfinder_class is None:
            return
        mods = self.attributes.get_attribute_modifiers()
        self.saves.update_saves(
            self.starfinder_class.fort[self.level - 1],
            self.starfinder_class.reflex[self.level - 1],
            self.starfinder_class.will[self.level - 1],
            mods['con'],
            mods['dex'],
            mods['wis']
        )

    def update_attack(self):
        if self.starfinder_class is None or self.level == 0:
            return
        mods = self.attributes.get_attribute_modifiers()
        self.attacks.update_attack(
            self.starfinder_class.bab[self.level - 1],
            mods['str'],
            mods['dex']
        )

    def update_initiative(self):
        mods = self.attributes.get_attribute_modifiers()
        self.initiaitve.update_initiative(mods['dex'])

    def update_skillpoints(self):
        mods = self.attributes.get_attribute_modifiers()
        self.skills.update_skillpoints(self.starfinder_class.skills, mods['int'], self.level)

    def update_spendable_ability_increase(self):
        self.attributes.update_spendable_ability_increase(self.level)

    def update_level(self, new_level: int):
        self.level = new_level
        self.starfinder_class.level_up(new_level)
        self.update_skillpoints()

    def gain_exp(self, gained_exp: int):
        self.exp += gained_exp
        levels = [1300, 3300, 6000, 10000, 15000, 23000, 34000, 50000, 71000, 105000,
                  14500, 210000, 295000, 425000, 600000, 850000, 1200000, 1700000, 2400000]
        currLevel = 1
        for level in levels:
            if self.exp >= level:
                currLevel += 1
            else:
                break

        self.update_level(currLevel)

    def select_new_class_feat(self, secondary : bool = False) -> list:
        """Adds a new feature based on the entered featType and level. Should verbose be set to
           False the list of options is returned

        Args:
            secondary (bool, optional): If the secondary list is the one to be considered.
                                        Defaults to True.

        Returns:
            list : list of class feats that can be selected
        """
        if secondary:
            possible_class_feats = self.starfinder_class.list_of_secondaries(self.level)
        else:
            possible_class_feats = self.starfinder_class.list_of_choosables(self.level)

        for feat in self.other_abilities:
            if feat in possible_class_feats:
                possible_class_feats.remove(feat)

        return possible_class_feats
