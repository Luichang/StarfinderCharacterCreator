from helpers.ability import Ability
from starfinder_classes.starfinder_class import StarfinderClass
from starfinder_feats.starfinder_feat_type import FeatType

@StarfinderClass.register_subclass('envoy')
class Envoy(StarfinderClass):
    """The Envoy Starfinder class that inherits from the StarfinderClass class
    """
    def __init__(self) -> None:
        super().__init__("Envoy")
        self.bab = [0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15]
        self.fort = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.reflex = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.will = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.skills = 8
        self.stamina_points = 6
        self.hit_points = 6
        self.key = "cha"
        self.proficiencies = ["Light Armor Proficiency", "Basic Melee Weapon Proficiency",
                           "Grenade Proficiency", "Small Arm Proficiency"]

        self.bonuses = ["acrobatics", "athletics", "bluff", "computers", "culture", "diplomacy",
                   "disguise", "engineering", "intimidate", "medicine", "perception", "piloting",
                   "profession", "profession2", "sense motive", "sleight of hand", "stealth"]


        self.class_abilities = self.all_class_abilities()
        self.class_choose_feats = self.all_choosable_abilities()
        self.class_secondary_feats = self.all_secondary_abilities()

    def all_class_abilities(self) -> list[Ability]:
        """creates the ability list for character level up

        Returns:
            list: List of levlup abilities
        """

        levelups = [
            Ability("Envoy improvisation", 1, FeatType.CHOOSE),
            Ability("Expertise (1d6)", 1, FeatType.ADD_EXPERTISE),
            Ability("Skill expertise (1)", 1, FeatType.ADD_EXPERTISE),
            Ability("Envoy improvisation", 2, FeatType.CHOOSE),
            Ability("Expertise talent", 3, FeatType.CHOOSE2),
            Ability("Weapon specialization", 3, FeatType.WEAPON),
            Ability("Envoy improvisation", 4, FeatType.CHOOSE),
            Ability("Expertise (1d6+1)", 5, FeatType.REPLACABLE, short="Expertise"),
            Ability("Skill expertise (2)", 5, FeatType.ADD_EXPERTISE),
            Ability("Envoy improvisation", 6, FeatType.CHOOSE),
            Ability("Expertise talent", 7, FeatType.CHOOSE2),
            Ability("Envoy improvisation", 8, FeatType.CHOOSE),
            Ability("Expertise (1d6+2)", 9, FeatType.REPLACABLE, short="Expertise"),
            Ability("Skill expertise (3)", 9, FeatType.ADD_EXPERTISE),
            Ability("Envoy improvisation", 10, FeatType.CHOOSE),
            Ability("Expertise talent", 11, FeatType.CHOOSE2),
            Ability("Envoy improvisation", 12, FeatType.CHOOSE),
            Ability("Expertise (1d8+2)", 13, FeatType.REPLACABLE, short="Expertise"),
            Ability("Skill expertise (4)", 13, FeatType.ADD_EXPERTISE),
            Ability("Envoy improvisation", 14, FeatType.CHOOSE),
            Ability("Expertise talent", 15, FeatType.CHOOSE2),
            Ability("Envoy improvisation", 16, FeatType.CHOOSE),
            Ability("Expertise (1d8+3)", 17, FeatType.REPLACABLE, short="Expertise"),
            Ability("Skill expertise (5)", 17, FeatType.ADD_EXPERTISE),
            Ability("Envoy improvisation", 18, FeatType.CHOOSE),
            Ability("Expertise talent", 19, FeatType.CHOOSE2),
            # gains the counter measures of lock out and wipe as a bonus
            Ability("Envoy improvisation", 20, FeatType.CHOOSE),
            Ability("Expertise (1d8+4)", 20, FeatType.REPLACABLE, short="Expertise"),
            Ability("True expertise", 20, FeatType.WORDS)
        ]
        return levelups

    def all_choosable_abilities(self) -> list[Ability]:
        """creates the choosable ability list for the Mechanic class

        Returns:
            list[Ability]: list of choosable abilities
        """

        choosable = [
            Ability("Clever Feint", 1, FeatType.WORDS),
            Ability("Dispiriting Taunt", 1, FeatType.WORDS),
            Ability("Don't Quit", 1, FeatType.WORDS),
            Ability("Expanded Attunement", 1, FeatType.WORDS),
            Ability("Get 'Em", 1, FeatType.WORDS),
            Ability("Inspiring Boost", 1, FeatType.WORDS),
            Ability("Not in the Face", 1, FeatType.WORDS),
            Ability("Universal Expression", 1, FeatType.WORDS),
            Ability("Watch Your Step", 1, FeatType.WORDS),
            Ability("Clever Attack", 4, FeatType.WORDS),
            Ability("Duck Under", 4, FeatType.WORDS),
            Ability("Focus", 4, FeatType.WORDS),
            Ability("Hurry", 4, FeatType.WORDS),
            Ability("Long-Range Improvisation", 4, FeatType.WORDS),
            Ability("Quick Dispiriting Taunt", 4, FeatType.WORDS),
            Ability("Quick Inspiring Boost", 4, FeatType.WORDS),
            Ability("Watch Out", 4, FeatType.WORDS),
            Ability("Clever Improvisations", 6, FeatType.WORDS),
            Ability("Draw Fire", 6, FeatType.WORDS),
            Ability("Heads Up", 6, FeatType.WORDS),
            Ability("Improved Get 'Em", 6, FeatType.WORDS),
            Ability("Desperate Defense", 8, FeatType.WORDS),
            Ability("Expert Attack", 8, FeatType.WORDS),
            Ability("Improved Hurry", 8, FeatType.WORDS),
            Ability("Situational Awareness", 8, FeatType.WORDS),
            Ability("Sustained Determination", 8, FeatType.WORDS)
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

    def new_expertises(self, current_expertises : list):
        """function to return the possible expertises. The first call should only return the first
        element. Every other should return the ones that have not been used yet.

        Args:
            current_expertises (list): list of current selected expertises

        Returns:
            list: list of possible expertises.
        """
        if not current_expertises:
            return ["sense motive"]

        expertises = [
            "bluff", "computers", "culture", "diplomacy", "disguise",
            "engineering", "intimidate", "medicine"
        ]

        for expertise in current_expertises:
            expertises.remove(expertise)
        return expertises

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
