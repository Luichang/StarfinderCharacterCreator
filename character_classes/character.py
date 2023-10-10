from typing import Optional
from character_classes.attributes import Attributes
from character_classes.armor import ArmorClasses
from character_classes.attacks import Attacks
from character_classes.health import Health
from character_classes.initiative import Initiative
from character_classes.saves import Saves
from character_classes.skills import Skills
from starfinder_classes.starfinder_class import StarfinderClass
from starfinder_races.starfinder_race import StarfinderRace
from starfinder_themes.starfinder_theme import StarfinderTheme

class Character:
    def __init__(self, name: str=None) -> None:
        self.name = name
        self.level = 0
        self.health = Health()
        self.attributes = Attributes()
        self.armor = ArmorClasses()
        self.saves = Saves()
        self.attacks = Attacks()
        self.initiaitve = Initiative()
        self.skills = Skills()
        self.spells = None
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
        self.skills.calc_skills(self.attributes.mods, self.starfinder_class.bonuses)
        self.update_skillpoints()
        self.update_health()

    def choose_race(self, race_name: str, human_style: Optional[str]) -> None:
        if race_name == "Human":
            self.race = StarfinderRace.create(race_name.lower(), human_style.lower())
        else:
            self.race = StarfinderRace.create(race_name.lower())

    def choose_theme(self, theme_name: str, themeless_style: Optional[str]):
        if theme_name == "Themeless":
            self.theme = StarfinderTheme.create(theme_name.lower(), themeless_style.lower())
        else:
            self.theme = StarfinderTheme.create(theme_name.lower())

    def update_health(self):
        if not all((self.starfinder_class, self.race)):
            return
        self.health.update_hit_points(class_hp=self.starfinder_class.hit_points,
                                      race_hp=self.race.hit_points,
                                      class_stamina=self.starfinder_class.stamina_points,
                                      class_mod=self.attributes.mods[self.starfinder_class.key],
                                      con_mod=self.attributes.mods['con'],
                                      character_level=self.level)

    def update_ac(self):
        self.armor.update_ac(self.attributes.mods['dex'])

    def update_saves(self):
        self.saves.update_saves(
            self.starfinder_class.fort[self.level - 1],
            self.starfinder_class.reflex[self.level - 1],
            self.starfinder_class.will[self.level - 1],
            self.attributes.mods['con'],
            self.attributes.mods['dex'],
            self.attributes.mods['wis']
        )

    def update_attack(self):
        self.attacks.update_attack(self.starfinder_class.bab[self.level], self.attributes.mods['str'], self.attributes.mods['dex'])

    def update_initiative(self):
        self.initiaitve.update_initiative(self.attributes.mods['dex'])

    def update_skillpoints(self):
        self.skills.update_skillpoints(self.starfinder_class.skills, self.attributes.mods['int'])

    def update_spendable_ability_increase(self):
        self.attributes.update_spendable_ability_increase(self.level)

    def update_level(self, new_level: int):
        self.level = new_level
