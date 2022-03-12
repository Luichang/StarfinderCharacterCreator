from starfinder_feat_type import Type
class Ability:
    """The ability class for Starfinder Classes
    """
    def __init__(self, name : str, level : int, _type : Type) -> None:
        self.name = name
        self.level = level
        self.type = _type


class StarfinderClass:
    """Parent class of various Starfinder classes
    """
    def __init__(self) -> None:
        self.bab = [0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15]
        self.fort = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.reflex = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.will = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.skills = 0
        self.stamina_points = 0
        self.hit_points = 0
        self.key = "int"
        self.proficiencies = []
        self.class_bonus = {
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
                "survival"         : 0
        }
        self.class_abilities = []
        self.class_choose_feats = []

    def level_up(self, level : int) -> list[Ability]:
        """Function to handle feats from level up

        Args:
            level (int): the new Level

        Returns:
            list: List of the Abilities that come fix with the level up
        """
        level_up_abilities = []
        for ability in self.class_abilities:
            if ability.level == level:
                level_up_abilities.append(ability)
        return level_up_abilities

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
