from helpers.ability import Ability
from starfinder_feats.starfinder_feat import Feat
from starfinder_feats.starfinder_feat_type import FeatType
from starfinder_feats.feat_requirement import Requirements

class StarfinderClass:
    """Parent class of various Starfinder classes
    """
    def __init__(self, name : str) -> None:
        self.name = name
        self.bab : list[int]
        self.fort : list[int]
        self.reflex : list[int]
        self.will : list[int]
        self.skills : int
        self.stamina_points : int
        self.hit_points : int
        self.key : str
        self.proficiencies : list[str]
        self.class_bonus : list[str]
        self.class_abilities : list[Ability]
        self.class_choose_feats : list[Ability]
        self.class_secondary_feats : list[Ability]
        self.bonuses : list[str]

    def __str__(self) -> str:
        return self.name

    subclasses = {}
    @classmethod
    def register_subclass(cls, starfinder_class : str) -> callable:
        """Function to register all the Starfinder Classes in the Parent Class

        Args:
            starfinder_class (str): name of the starfinder class

        Returns:
            callable: decorator function to be added in front of the child class
        """
        def decorator(subclass):
            cls.subclasses[starfinder_class] = subclass
            return subclass

        return decorator

    @classmethod
    def create(cls, starfinder_class : str, key : str = None):
        """Function to return the called starfinder class

        Args:
            starfinder_class (str): name of the starfinder class
            key (str): key attribute should it be needed. Defaults to None

        Raises:
            ValueError: if the starfinder class has not been implemented yet

        Returns:
            callable: the desired child class
        """
        if starfinder_class not in cls.subclasses:
            raise ValueError(f'{starfinder_class} has not yet been implemented')

        if key: # only to be called on the soldier class
            return cls.subclasses[starfinder_class](key)
        return cls.subclasses[starfinder_class]()

    def current_abilities(self, level : int) -> list[Ability]:
        """Function to handle feats from level up

        Args:
            level (int): the new Level

        Returns:
            list: List of the Abilities that come fix with the level up
        """
        abilities = []
        for ability in self.class_abilities:
            if ability.level <= level:
                abilities.append(ability)
        return abilities

    def list_of_choosables(self, level : int) -> list[Ability]:
        """Function to return the feats the player can choose from

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
    
    def list_of_secondaries(self, level) -> list[Ability]:
        """Function to return the secondary feats the player can choose from

        Args:
            level (int): current level of the character

        Returns:
            list[Ability]: list of feats the player can choose from
        """
        level_up_abilities = []
        for ability in self.class_secondary_feats:
            if ability.level <= level:
                level_up_abilities.append(ability)
        return level_up_abilities

light_armor = Feat("Light Armor Proficiency", True, None, FeatType.WORDS)
basic_melee_prof = Feat("Basic Melee Weapon Proficiency", True, None, FeatType.WORDS)
advanced_melee_prof = Feat("Advanced Melee Weapon Proficiency", True,
                            Requirements(feat=[basic_melee_prof]), FeatType.WORDS)
small_arm_proficiency = Feat("Small Arm Proficiency", True, None, FeatType.WORDS)
longarm_proficiency = Feat("Longarm Proficiency", True, Requirements(feat=[small_arm_proficiency]),
                            FeatType.WORDS)
heavy_weapon = Feat("Heavy Weapon Proficiency", True,
                    Requirements(ability=[["str", 13]],
                                feat=[longarm_proficiency, small_arm_proficiency]),
                    FeatType.WORDS)
sniper_weapon = Feat("Sniper Weapon Proficiency", True, None, FeatType.WORDS)
special_weapon = Feat("Special Weapon Proficiency", True,
                        Requirements(from_list=[["feat", [small_arm_proficiency,
                                                            basic_melee_prof]]]),
                        FeatType.WORDS)
suppressive_fire = Feat("Suppressive Fire", True, Requirements(feat=[heavy_weapon], bab=1),
                        FeatType.WORDS)
grenade_proficiency = Feat("Grenade Proficiency", True, None, FeatType.WORDS)
heavy_armor = Feat("Heavy Armor Proficiency", True,
                    Requirements(ability=[["str", 13]], feat=[light_armor]), FeatType.WORDS)
