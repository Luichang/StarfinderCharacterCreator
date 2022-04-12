from helpers.ability import Ability
from starfinder_classes.starfinder_class import StarfinderClass
from starfinder_feats.starfinder_feat_type import FeatType

@StarfinderClass.register_subclass('mechanic')
class Mechanic(StarfinderClass):
    """The Mechanic Starfinder class that inherits from the StarfinderClass class
    """
    def __init__(self) -> None:
        super().__init__("Mechanic")
        self.bab = [0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15]
        self.fort = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.reflex = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.will = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.skills = 4
        self.stamina_points = 6
        self.hit_points = 6
        self.key = "int"
        self.proficiencies = ["Light Armor Proficiency", "Basic Melee Weapon Proficiency",
                           "Grenade Proficiency", "Small Arm Proficiency"]

        self.bonuses = ["athletics", "computers", "engineering", "medicine", "perception",
                   "physical science", "piloting", "profession", "profession2"]


        self.class_abilities = self.all_class_abilities()
        self.class_choose_feats = self.all_choosable_abilities()

    def all_class_abilities(self) -> list[Ability]:
        """creates the ability list for character level up

        Returns:
            list: List of levlup abilities
        """

        levelups = [
            Ability("Artificial intelligence", 1, FeatType.WORDS),
            # might want a selector between Drone and Exocortex
            Ability("Bypass +1", 1, FeatType.REPLACABLE, short="Bypass"),
            Ability("Custom rig", 1, FeatType.WORDS),
            Ability("Mechanic trick", 2, FeatType.CHOOSE), # TODO
            Ability("Overload", 3, FeatType.WORDS),
            Ability("Weapon specialization", 3, FeatType.WEAPON),
            Ability("Mechanic trick", 4, FeatType.CHOOSE),
            Ability("Bypass +2", 5, FeatType.REPLACABLE, short="Bypass"),
            Ability("Remote hack", 5, FeatType.WORDS),
            Ability("Mechanic trick", 6, FeatType.CHOOSE),
            Ability("Expert rig", 7, FeatType.WORDS),
            Ability("Miracle worker 1/day", 7, FeatType.WORDS),
            Ability("Mechanic trick", 8, FeatType.CHOOSE),
            Ability("Bypass +3", 9, FeatType.REPLACABLE, short="Bypass"),
            Ability("Override", 9, FeatType.WORDS),
            Ability("Mechanic trick", 10, FeatType.CHOOSE),
            Ability("Coordinated assault +1", 11, FeatType.WORDS),
            Ability("Miracle worker 2/day", 11, FeatType.WORDS),
            Ability("Mechanic trick", 12, FeatType.CHOOSE),
            Ability("Advanced rig", 13, FeatType.WORDS),
            # gains a counter measure of firewall as a bonus
            Ability("Bypass +4", 13, FeatType.REPLACABLE, short="Bypass"),
            Ability("Mechanic trick", 14, FeatType.CHOOSE),
            Ability("Miracle worker 3/day", 15, FeatType.WORDS),
            Ability("Mechanic trick", 16, FeatType.CHOOSE),
            Ability("Bypass +5", 17, FeatType.REPLACABLE, short="Bypass"),
            Ability("Control net", 17, FeatType.WORDS),
            Ability("Coordinated assault +2", 17, FeatType.WORDS),
            Ability("Mechanic trick", 18, FeatType.CHOOSE),
            Ability("Ghost in the machine", 19, FeatType.WORDS),
            Ability("Miracle worker 4/day", 19, FeatType.WORDS),
            Ability("Superior rig", 19, FeatType.WORDS),
            # gains the counter measures of lock out and wipe as a bonus
            Ability("Bypass +6", 20, FeatType.REPLACABLE, short="Bypass"),
            Ability("Mechanic trick", 20, FeatType.CHOOSE),
            Ability("Tech master", 20, FeatType.WORDS)
        ]
        return levelups

    def all_choosable_abilities(self) -> list[Ability]:
        """creates the choosable ability list for the Mechanic class

        Returns:
            list[Ability]: list of choosable abilities
        """
        choosable = [
            Ability("Distracting Hack", 2, FeatType.WORDS),
            Ability("Energy Shield", 2, FeatType.WORDS),
            Ability("Hack Directory", 2, FeatType.WORDS),
            Ability("Neural Shunt", 2, FeatType.WORDS),
            Ability("Nightvision Processor", 2, FeatType.WORDS),
            Ability("Overcharge", 2, FeatType.WORDS),
            Ability("Overclocking", 2, FeatType.WORDS),
            Ability("Overload Weapon", 2, FeatType.WORDS),
            Ability("Portable Power", 2, FeatType.WORDS),
            Ability("Quick Patch", 2, FeatType.WORDS),
            Ability("Quick Repair", 2, FeatType.WORDS),
            Ability("Repair Drone", 2, FeatType.WORDS),
            Ability("Visual Data Processor", 2, FeatType.WORDS),
            Ability("Boost Shield", 8, FeatType.WORDS),
            Ability("Drone Meld", 8, FeatType.WORDS),
            Ability("Engineer's Eye", 8, FeatType.WORDS),
            Ability("Ghost Intrusion", 8, FeatType.WORDS),
            Ability("Holographic Projector", 8, FeatType.WORDS),
            Ability("Hyperclocking", 8, FeatType.WORDS),
            Ability("Improved Overcharge", 8, FeatType.WORDS),
            Ability("Invisibility Bypass Processor", 8, FeatType.WORDS),
            Ability("Resistant Energy", 8, FeatType.WORDS),
            Ability("Scoutbot", 8, FeatType.WORDS),
            Ability("Extra Mod", 14, FeatType.WORDS),
            Ability("Improved Resistant Energy", 14, FeatType.WORDS),
            Ability("Invisibility-Hampering Projector", 14, FeatType.WORDS),
            Ability("Mod Tinkerer", 14, FeatType.WORDS),
            Ability("Saboteur", 14, FeatType.WORDS),
            Ability("Superior Overcharge", 14, FeatType.WORDS),
            Ability("Ultraclocking", 14, FeatType.WORDS)
        ]
        return choosable
