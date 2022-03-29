from starfinder_classes.starfinder_class import StarfinderClass, Ability
from starfinder_feats.starfinder_feat_type import FeatType

@StarfinderClass.register_subclass('soldier')
class Soldier(StarfinderClass):
    """The Soldier Starfinder class that inherits from the StarfinderClass class
    """
    def __init__(self, key : str = "str") -> None:
        super().__init__("Soldier")
        self.bab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.fort = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.reflex = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.will = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.skills = 4
        self.stamina_points = 7
        self.hit_points = 7
        self.key = key
        self.proficiencies = ["Light Armor Proficiency", "Heavy Armor Proficiency",
                              "Basic Melee Weapon Proficiency", "Advanced Melee Weapon Proficiency",
                              "Small Arm Proficiency", "Longarm Proficiency",
                              "Heavy Weapon Proficiency", "Sniper Weapon Proficiency",
                              "Grenade Proficiency"]

        bonuses = ["acrobatics", "athletics", "engineering", "intimidate", "medicine", "piloting",
                   "profession", "profession2", "survival"]

        for bonus in bonuses:
            self.class_bonus[bonus] = 3

        self.class_abilities = self.all_class_abilities()
        #self.class_choose_feats = self.all_choosable_abilities()

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
        levelups = [
            Ability("Primary Fighting style", 1, FeatType.SELECTION),
            Ability("Primary style technique", 1, FeatType.TECHNIQUE1),
            Ability("Combat feat", 2, FeatType.COMBAT),
            Ability("Gear boost", 3, FeatType.CHOOSE),
            Ability("Weapon specialization", 3, FeatType.WEAPON),
            Ability("Combat feat", 4, FeatType.COMBAT),
            Ability("Primary style technique", 5, FeatType.TECHNIQUE1),
            Ability("Combat feat", 6, FeatType.COMBAT),
            Ability("Gear boost", 7, FeatType.CHOOSE),
            Ability("Combat feat", 8, FeatType.COMBAT),
            Ability("Primary style technique", 9, FeatType.TECHNIQUE1),
            Ability("Secondary fighting style", 9, FeatType.SELECTION),
            Ability("Primary style technique", 9, FeatType.TECHNIQUE2),
            Ability("Combat feat", 10, FeatType.COMBAT),
            Ability("Gear boost", 11, FeatType.CHOOSE),
            Ability("Soldier's onslaught", 11, FeatType.WORDS),
            Ability("Combat feat", 12, FeatType.COMBAT),
            Ability("Primary style technique", 13, FeatType.TECHNIQUE1),
            Ability("Secondary style technique", 13, FeatType.TECHNIQUE2),
            Ability("Combat feat", 14, FeatType.COMBAT),
            Ability("Gear boost", 15, FeatType.CHOOSE),
            Ability("Combat feat", 16, FeatType.COMBAT),
            Ability("Primary style technique", 17, FeatType.TECHNIQUE1),
            Ability("Secondary style technique", 17, FeatType.TECHNIQUE2),
            Ability("Combat feat", 18, FeatType.COMBAT),
            Ability("Gear boost", 19, FeatType.CHOOSE),
            Ability("Combat feat", 20, FeatType.COMBAT),
            Ability("Kill shot", 20, FeatType.WORDS)
        ]
        return levelups

    def all_choosable_abilities(self) -> list[Ability]:
        """creates the choosable ability list for the Mechanic class

        Returns:
            list[Ability]: list of choosable abilities
        """

        choosable = [
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
        return choosable
