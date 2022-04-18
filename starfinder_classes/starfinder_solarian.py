from helpers.ability import Ability
from starfinder_classes.starfinder_class import (StarfinderClass, advanced_melee_prof,
                                                 basic_melee_prof,
                                                 light_armor,
                                                 small_arm_proficiency)
from starfinder_feats.starfinder_feat_type import FeatType

@StarfinderClass.register_subclass('solarian')
class Solarian(StarfinderClass):
    """The Solarian Starfinder class that inherits from the StarfinderClass class
    """
    def __init__(self) -> None:
        super().__init__("Solarian")
        self.bab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.fort = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.reflex = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.will = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.skills = 4
        self.stamina_points = 7
        self.hit_points = 7
        self.key = "cha"
        self.proficiencies = [light_armor, basic_melee_prof, advanced_melee_prof,
                                small_arm_proficiency]

        self.bonuses = ["acrobatics", "athletics", "diplomacy", "intimidate", "mysticism",
                        "perception", "physical science", "profession", "profession2",
                        "sense motive", "stealth"]

        self.class_abilities = self.all_class_abilities()
        self.class_choose_feats = self.all_choosable_abilities()
        self.class_secondary_feats = self.all_secondary_abilities()

    def all_class_abilities(self) -> list[Ability]:
        """creates the ability list for character level up

        Returns:
            list: List of levlup abilities
        """

        levelups = [
            Ability("Skill adept", 1, FeatType.CLASS), # [["any"], ["any"]]
            Ability("Solar manifestation", 1, FeatType.WORDS),
            Ability("Stellar mode", 1, FeatType.WORDS),
            Ability("Stellar revelation (black hole, supernova)", 1, FeatType.CHOOSE), # TODO
            Ability("Stellar revelation", 2, FeatType.CHOOSE),
            Ability("Sidereal influence (2 skills)", 3, FeatType.INFLUENCE, short="Sidereal influence"),
            Ability("Weapon specialization", 3, FeatType.WEAPON),
            Ability("Stellar revelation", 4, FeatType.CHOOSE),
            Ability("Stellar revelation", 6, FeatType.CHOOSE),
            Ability("Flashing strikes", 7, FeatType.WORDS),
            Ability("Stellar revelation", 8, FeatType.CHOOSE),
            Ability("Zenith revelations", 9, FeatType.CHOOSE2),
            Ability("Stellar revelation", 10, FeatType.CHOOSE),
            Ability("Sidereal influence (4 skills)", 11, FeatType.INFLUENCE, short="Sidereal influence"),
            Ability("Stellar revelation", 12, FeatType.CHOOSE),
            Ability("Solarian's onslaught", 13, FeatType.WORDS),
            Ability("Stellar revelation", 14, FeatType.CHOOSE),
            Ability("Stellar revelation", 16, FeatType.CHOOSE),
            Ability("Zenith revelations", 17, FeatType.CHOOSE2),
            Ability("Stellar revelation", 18, FeatType.CHOOSE),
            Ability("Sidereal influence (6 skills)", 19, FeatType.INFLUENCE, short="Sidereal influence"),
            Ability("Stellar revelation", 20, FeatType.CHOOSE),
            Ability("Stellar paragon", 20, FeatType.WORDS)
        ]
        return levelups

    def all_choosable_abilities(self) -> list[Ability]:
        """creates the choosable ability list for the Mechanic class

        Returns:
            list[Ability]: list of choosable abilities
        """

        choosable = [
            Ability("Dark Matter", 2, FeatType.WORDS),
            Ability("Flare", 2, FeatType.WORDS),
            Ability("Gravity Anchor", 2, FeatType.WORDS),
            Ability("Gravity Boost", 2, FeatType.WORDS),
            Ability("Gravity Hold", 2, FeatType.WORDS),
            Ability("Plasma Sheath", 2, FeatType.WORDS),
            Ability("Radiation", 2, FeatType.WORDS),
            Ability("Stellar Rush", 2, FeatType.WORDS),
            Ability("Astrologic Sense", 6, FeatType.WORDS),
            Ability("Blazing Orbit", 6, FeatType.WORDS),
            Ability("Corona", 6, FeatType.WORDS),
            Ability("Crush", 6, FeatType.WORDS),
            Ability("Defy Gravity", 6, FeatType.WORDS),
            Ability("Glow of Life", 6, FeatType.WORDS),
            Ability("Gravity Surge", 6, FeatType.WORDS),
            Ability("Hypnotic Glow", 6, FeatType.WORDS),
            Ability("Reflection", 6, FeatType.WORDS),
            Ability("Soul Furnace", 10, FeatType.WORDS),
            Ability("Stealth Warp", 10, FeatType.WORDS),
            Ability("Gravity Shield", 14, FeatType.WORDS),
            Ability("Sunbolt", 14, FeatType.WORDS),
            Ability("Ultimate Graviton", 16, FeatType.WORDS),
            Ability("Ultimate Photon", 16, FeatType.WORDS)
        ]
        return choosable

    def all_secondary_abilities(self) -> list[Ability]:
        """creates the choosable ability list for the Mechanic class

        Returns:
            list[Ability]: list of choosable abilities
        """

        choosable = [
            Ability("Additional Skill Expertise", 1, FeatType.WORDS),
            Ability("Altered Bearing", 1, FeatType.WORDS),
            Ability("Analyst", 1, FeatType.WORDS),
            Ability("Cautious Expertise", 1, FeatType.WORDS),
            Ability("Convincing Liar", 1, FeatType.WORDS),
            Ability("Cultural Savant", 1, FeatType.WORDS),
            Ability("Cunning Disguise", 1, FeatType.WORDS),
            Ability("Engineering Adept", 1, FeatType.WORDS),
            Ability("Expert Forger", 1, FeatType.WORDS),
            Ability("Fast Hack", 1, FeatType.WORDS),
            Ability("Inspired Medic", 1, FeatType.WORDS),
            Ability("Keen Observer", 1, FeatType.WORDS),
            Ability("Menacing Gaze", 1, FeatType.WORDS),
            Ability("Rattling Presence", 1, FeatType.WORDS),
            Ability("Skilled Linguist", 1, FeatType.WORDS),
            Ability("Slick Customer", 1, FeatType.WORDS),
            Ability("Student of Technology", 1, FeatType.WORDS),
            Ability("Surgeon", 1, FeatType.WORDS),
            Ability("Well Informed", 1, FeatType.WORDS)
        ]
        return choosable

    def new_expertises(self, _ = None):
        """function to return the possible

        Args:
            _ (None): empty input so this can be used together with another class

        Returns:
            list: list of possible expertises.
        """

        possible_skill = ["acrobatics", "athletics", "bluff", "computers", "culture", "diplomacy",
                         "disguise", "engineering", "intimidate", "life science", "medicine",
                         "mysticism", "perception", "physical science", "profession1",
                         "profession2", "piloting", "sense motive", "sleight of hand", "stealth",
                         "survival"
        ]

        return possible_skill

    def list_of_secondaries(self, level) -> list[Ability]:
        """Function to return the secondary feats the player can choose from

        Args:
            level (int): current level of the character

        Returns:
            list[Ability]: list of feats the player can choose from
        """
        level_up_abilities = []
        for ability in self.class_choose_feats:
            if ability.level <= level:
                level_up_abilities.append(ability)
        return level_up_abilities
