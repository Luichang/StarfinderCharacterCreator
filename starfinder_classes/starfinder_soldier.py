from helpers.ability import Ability
from starfinder_classes.starfinder_class import (StarfinderClass, advanced_melee_prof,
                                                 basic_melee_prof,
                                                 grenade_proficiency,
                                                 heavy_armor, heavy_weapon,
                                                 light_armor,
                                                 longarm_proficiency,
                                                 small_arm_proficiency,
                                                 sniper_weapon)
from starfinder_feats.starfinder_feat_type import FeatType

@StarfinderClass.register_subclass('soldier')
class Soldier(StarfinderClass):
    """The Soldier Starfinder class that inherits from the StarfinderClass class
    """
    def __init__(self, key : str = "str") -> None:
        super().__init__("Soldier")
        self.selection = ["", ""]
        self.bab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.fort = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.reflex = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.will = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.skills = 4
        self.stamina_points = 7
        self.hit_points = 7
        self.key = key
        self.proficiencies = [light_armor, heavy_armor, basic_melee_prof, advanced_melee_prof,
                              small_arm_proficiency, longarm_proficiency, heavy_weapon,
                              sniper_weapon, grenade_proficiency]

        self.bonuses = ["acrobatics", "athletics", "engineering", "intimidate", "medicine",
                        "piloting", "profession", "profession2", "survival"]

        self.class_abilities = self.all_class_abilities()
        self.class_secondary_feats = self.all_choosable_abilities()

    def __str__(self) -> str:
        return f"{self.name} [{self.key}]"

    def select_key(self, key : str) -> None:
        """Function to select new Key attribute for current soldier

        Args:
            key (str): key, either str or dex
        """
        self.key = key

    def all_class_abilities(self) -> list[Ability]:
        """creates the ability list for character level up

        Returns:
            list: List of levlup abilities
        """
        all_abilities = [
            Ability("Primary Fighting style", 1, FeatType.SELECTION),
            Ability("Primary style technique", 1, FeatType.TECHNIQUE1),
            Ability("Combat feat", 2, FeatType.COMBAT),
            Ability("Gear boost", 3, FeatType.CHOOSE2),
            Ability("Weapon specialization", 3, FeatType.WEAPON),
            Ability("Combat feat", 4, FeatType.COMBAT),
            Ability("Primary style technique", 5, FeatType.TECHNIQUE1),
            Ability("Combat feat", 6, FeatType.COMBAT),
            Ability("Gear boost", 7, FeatType.CHOOSE2),
            Ability("Combat feat", 8, FeatType.COMBAT),
            Ability("Primary style technique", 9, FeatType.TECHNIQUE1),
            Ability("Secondary fighting style", 9, FeatType.SELECTION),
            Ability("Primary style technique", 9, FeatType.TECHNIQUE2),
            Ability("Combat feat", 10, FeatType.COMBAT),
            Ability("Gear boost", 11, FeatType.CHOOSE2),
            Ability("Soldier's onslaught", 11, FeatType.WORDS),
            Ability("Combat feat", 12, FeatType.COMBAT),
            Ability("Primary style technique", 13, FeatType.TECHNIQUE1),
            Ability("Secondary style technique", 13, FeatType.TECHNIQUE2),
            Ability("Combat feat", 14, FeatType.COMBAT),
            Ability("Gear boost", 15, FeatType.CHOOSE2),
            Ability("Combat feat", 16, FeatType.COMBAT),
            Ability("Primary style technique", 17, FeatType.TECHNIQUE1),
            Ability("Secondary style technique", 17, FeatType.TECHNIQUE2),
            Ability("Combat feat", 18, FeatType.COMBAT),
            Ability("Gear boost", 19, FeatType.CHOOSE2),
            Ability("Combat feat", 20, FeatType.COMBAT),
            Ability("Kill shot", 20, FeatType.WORDS)
        ]

        levelups = []

        for ability in all_abilities:
            if ability.level > self.level:
                break
            levelups.append(ability)

        return levelups

    def all_choosable_abilities(self) -> list[Ability]:
        """creates the choosable ability list for the Mechanic class

        Returns:
            list[Ability]: list of choosable abilities
        """

        all_choosable = [
            Ability("Armored Advantage", 1, FeatType.WORDS),
            Ability("Brutal Blast", 1, FeatType.WORDS),
            Ability("Bullet Barrage", 1, FeatType.WORDS),
            Ability("Laser Accuracy", 1, FeatType.WORDS),
            Ability("Melee Striker", 1, FeatType.WORDS),
            Ability("Anchoring Arcana", 7, FeatType.WORDS),
            Ability("Electric Arc", 7, FeatType.WORDS),
            Ability("Flash Freeze", 7, FeatType.WORDS),
            Ability("Plasma Immolation", 7, FeatType.WORDS),
            Ability("Powerful Explosive", 7, FeatType.WORDS),
            Ability("Sonic Resonance", 7, FeatType.WORDS),
            Ability("Heavy Onslaught", 11, FeatType.WORDS)
        ]

        choosable = []

        for ability in all_choosable:
            if ability.level > self.level:
                break
            choosable.append(ability)

        return choosable

    def select_selection(self, style : str, num : int):
        """function that sets the style

        Args:
            style (str): new style
            num (int): which style is to be changed, the first or the second
        """
        self.selection[num] = style

    def possible_selections(self) -> list:
        """function that gives every possible style

        Returns:
            list: list of possible styles
        """
        styles = [
            "Arcane Assailant", "Armor Storm", "Blitz", "Bombard", "Guard", "Hit-and-Run",
            "Sharpshoot"
        ]
        return styles

    def style_combat(self, style : int) -> dict:
        """function to return the dictionary of styles for each style

        Args:
            style (int): which style is to be returned, the first or the second

        Returns:
            dict: dictionary where the possible levels are the keys and the combat feats are the
                    items
        """

        styles = {
            "Arcane Assailant" : {
                1 : "Rune of the Eldritch Knight",
                5 : "Secret of the Magi",
                9 : "Power of Legend",
                13: "Secret of the Archmagi",
                17: "Arcane Attack"
            },
            "Armor Storm" : {
                1 : "Hammer Fist",
                5 : "Enhanced Tank",
                9 : "Smash Through",
                13: "Mobile Army",
                17: "On the Bounce"
            },
            "Blitz" : {
                1 : "Rapid Response",
                5 : "Charge Attack",
                9 : "Keep Fighting",
                13: "Perfect Opportunity",
                17: "Against the Odds"
            },
            "Bombard" : {
                1 : "Grenade Expert",
                5 : "Heavy Fire",
                9 : "Debilitating Attack",
                13: "Explosives Acumen",
                17: "Impactful Attack"
            },
            "Guard" : {
                1 : "Armor Training",
                5 : "Guard's Protection",
                9 : "Rapid Recovery",
                13: "Kinetic Resistance",
                17: "Impenetrable Defense"
            },
            "Hit-and-Run" : {
                1 : "Opening Volley",
                5 : "Nimble Fusillade",
                9 : "Duck and Weave",
                13: "Elusive Target",
                17: "Harrying Shot"
            },
            "Sharpshoot" : {
                1 : "Sniper's Aim",
                5 : "Focus Fire",
                9 : "Intense Focus",
                13: "Focused Damage",
                17: "Prepared Shot"
            }
        }
        return styles[self.selection[style]]
