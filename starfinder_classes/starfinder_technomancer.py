from helpers.ability import Ability
from starfinder_feats.feat_requirement import Requirements
from starfinder_feats.starfinder_feat import Feat
from starfinder_feats.starfinder_feat_type import FeatType

from starfinder_classes.starfinder_class import (StarfinderClass,
                                                 basic_melee_prof,
                                                 light_armor,
                                                 small_arm_proficiency)
from starfinder_classes.starfinder_mystic import Mystic
from starfinder_classes.starfinder_operative import mobility

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
        self.proficiencies = [light_armor, basic_melee_prof, small_arm_proficiency]

        self.bonuses = ["computers", "engineering", "life science", "mysticism", "physical science", "piloting",
                   "profession", "profession2", "sleight of hand"]

        self.class_abilities = self.all_class_abilities()
        self.class_choose_feats = self.all_choosable_abilities()

    def all_class_abilities(self) -> list[Ability]:
        """creates the ability list for character level up

        Returns:
            list: List of levlup abilities
        """

        all_abilities = [
            Ability("Spell cache", 1, FeatType.WORDS),
            Ability("Magic hack", 2, FeatType.CHOOSE),
            Ability("Spell Focus", 3, FeatType.FEAT, feat=spell_focus),
            Ability("Techlore +1", 3, FeatType.MISC_INCREASE, short="Techlore"),
            Ability("Weapon specialization", 3, FeatType.WEAPON),
            Ability("Magic hack", 5, FeatType.CHOOSE),
            Ability("Cache capacitor 1", 6, FeatType.REPLACABLE, short="Cache capacitor"),
            Ability("Techlore +2", 6, FeatType.MISC_INCREASE, short="Techlore"),
            Ability("Magic hack", 8, FeatType.CHOOSE),
            Ability("Techlore +3", 9, FeatType.MISC_INCREASE, short="Techlore"),
            Ability("Magic hack", 11, FeatType.CHOOSE),
            Ability("Cache capacitor 2", 12, FeatType.REPLACABLE, short="Cache capacitor"),
            Ability("Techlore +4", 12, FeatType.MISC_INCREASE, short="Techlore"),
            Ability("Magic hack", 14, FeatType.CHOOSE),
            Ability("Techlore +5", 15, FeatType.MISC_INCREASE, short="Techlore"),
            Ability("Magic hack", 17, FeatType.CHOOSE),
            Ability("Cache capacitor 3", 18, FeatType.REPLACABLE, short="Cache capacitor"),
            Ability("Techlore +6", 18, FeatType.MISC_INCREASE, short="Techlore"),
            Ability("Resolve attunement", 19, FeatType.WORDS),
            Ability("Fuse spells", 20, FeatType.WORDS),
            Ability("Magic hack", 20, FeatType.CHOOSE)
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

        choosable = []

        for ability in all_choosable:
            if ability.level > self.level:
                break
            choosable.append(ability)

        return choosable

    def misc_additions(self) -> list:
        """function to return the skills that are to be increased

        Returns:
            list: list of all the skills that are to be increased by 1
        """
        return ["computers", "mysticism"]

spell_focus = Feat("Spell Focus", False, Requirements(spell_level=1, level=3), FeatType.WORDS)
agile_casting = Feat("Agile Casting", False,
                    Requirements(ability=[["key", 15], ["dex", 15]], feat=[mobility],
                                class_name=[Mystic, Technomancer], level=4),
                    FeatType.WORDS)
techno_dabbler = Feat("Technomantic Dabbler", False, Requirements(ability=[["int", 15]], level=5),
                        FeatType.WORDS) # TODO need to check that the character is NOT technomancer
