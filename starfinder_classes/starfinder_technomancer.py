from starfinder_classes.starfinder_class import StarfinderClass, Ability
from starfinder_feats.starfinder_feat_type import FeatType

@StarfinderClass.register_subclass('technomancer')
class Technomancer(StarfinderClass):
    """The Technomancer Starfinder class that inherits from the StarfinderClass class
    """
    def __init__(self) -> None:
        super().__init__("Technomancer")
        self.bab = [0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15]
        self.fort = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.reflex = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.will = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.skills = 4
        self.stamina_points = 5
        self.hit_points = 5
        self.key = "int"
        self.proficiencies = ["Light Armor Proficiency", "Basic Melee Weapon Proficiency",
                           "Small Arm Proficiency"]

        bonuses = ["computers", "engineering", "life science", "mysticism", "physical science", "piloting",
                   "profession", "profession2", "sleight of hand"]

        for bonus in bonuses:
            self.class_bonus[bonus] = 3

        self.class_abilities = self.all_class_abilities()
        #self.class_choose_feats = self.all_choosable_abilities()

    def all_class_abilities(self) -> list[Ability]:
        """creates the ability list for character level up

        Returns:
            list: List of levlup abilities
        """

        levelups = [
            Ability("Spell cache", 1, FeatType.WORDS),
            Ability("Magic hack", 2, FeatType.CHOOSE),
            Ability("Spell Focus", 3, FeatType.FEAT), # "Spell Focus"
            Ability("Techlore +1", 3, FeatType.SKILLS, short="Techlore"), # [["computers", 1], ["mysticism", 1]]
            Ability("Weapon specialization", 3, FeatType.WEAPON),
            Ability("Magic hack", 5, FeatType.CHOOSE),
            Ability("Cache capacitor 1", 6, FeatType.REPLACABLE, short="Cache capacitor"),
            Ability("Techlore +2", 6, FeatType.SKILLS, short="Techlore"), # [["computers", 1], ["mysticism", 1]]
            Ability("Magic hack", 8, FeatType.CHOOSE),
            Ability("Techlore +3", 9, FeatType.SKILLS, short="Techlore"), # [["computers", 1], ["mysticism", 1]]
            Ability("Magic hack", 11, FeatType.CHOOSE),
            Ability("Cache capacitor 2", 12, FeatType.REPLACABLE, short="Cache capacitor"),
            Ability("Techlore +4", 12, FeatType.SKILLS, short="Techlore"), # [["computers", 1], ["mysticism", 1]]
            Ability("Magic hack", 14, FeatType.CHOOSE),
            Ability("Techlore +5", 15, FeatType.SKILLS, short="Techlore"), # [["computers", 1], ["mysticism", 1]]
            Ability("Magic hack", 17, FeatType.CHOOSE),
            Ability("Cache capacitor 3", 18, FeatType.REPLACABLE, short="Cache capacitor"),
            Ability("Techlore +6", 18, FeatType.SKILLS, short="Techlore"), # [["computers", 1], ["mysticism", 1]]
            Ability("Resolve attunement", 19, FeatType.WORDS),
            Ability("Fuse spells", 20, FeatType.WORDS),
            Ability("Magic hack", 20, FeatType.CHOOSE)
        ]
        return levelups

    def all_choosable_abilities(self) -> list[Ability]:
        """creates the choosable ability list for the Mechanic class

        Returns:
            list[Ability]: list of choosable abilities
        """

        choosable = [
            Ability("Countertech", 2, FeatType.WORDS),
            Ability("Empowered Weapon", 2, FeatType.WORDS),
            Ability("Energize Spell", 2, FeatType.WORDS),
            Ability("Fabricate Tech", 2, FeatType.WORDS),
            Ability("Harmful Spells", 2, FeatType.WORDS),
            Ability("Quick Scan", 2, FeatType.WORDS),
            Ability("Robot Influence", 2, FeatType.WORDS),
            Ability("Selective Targeting", 2, FeatType.WORDS),
            Ability("Spell Countermeasures", 2, FeatType.WORDS),
            Ability("Technomantic Proficiency", 2, FeatType.WORDS),
            Ability("Charging Jolt", 5, FeatType.WORDS),
            Ability("Debug Spell", 5, FeatType.WORDS),
            Ability("Distant Spell", 5, FeatType.WORDS),
            Ability("Extended Spell", 5, FeatType.WORDS),
            Ability("Fabricate Arms", 5, FeatType.WORDS),
            Ability("Magic Negation", 5, FeatType.WORDS),
            Ability("Spell Grenade", 5, FeatType.WORDS),
            Ability("Diviner's Tap", 8, FeatType.WORDS),
            Ability("Flash Teleport", 8, FeatType.WORDS),
            Ability("Mental Mark", 8, FeatType.WORDS),
            Ability("Spellshot", 8, FeatType.WORDS),
            Ability("Tech Countermeasures", 8, FeatType.WORDS),
            Ability("Widened Spell", 8, FeatType.WORDS),
            Ability("Countertech Sentinel", 11, FeatType.WORDS),
            Ability("Eternal Spell", 11, FeatType.WORDS),
            Ability("Reboot Mind", 11, FeatType.WORDS),
            Ability("Seeking Shot", 11, FeatType.WORDS),
            Ability("Phase Shot", 14, FeatType.WORDS),
            Ability("Quickened Spell", 14, FeatType.WORDS),
            Ability("Rain of Fire", 14, FeatType.WORDS),
            Ability("Spell Library", 14, FeatType.WORDS)

        ]
        return choosable