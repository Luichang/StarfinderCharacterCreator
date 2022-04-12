from helpers.ability import Ability

class StarfinderTheme:
    """Parent class of various Starfinder themes
    """
    def __init__(self, name : str) -> None:
        self.name = name
        self.attributes = {
            "strength" : 0,
            "dexterity" : 0,
            "constitution" : 0,
            "intelligence" : 0,
            "wisdom" : 0,
            "charisma" : 0
        }
        self.abilities : list[Ability]

    def __str__(self) -> str:
        return self.name

    subthemes = {}
    @classmethod
    def register_subtheme(cls, starfinder_theme : str) -> callable:
        """Function to register all the Starfinder Themes in the Parent Theme

        Args:
            starfinder_theme (str): name of the starfinder theme

        Returns:
            callable: decorator function to be added in front of the child theme
        """
        def decorator(subtheme):
            cls.subthemes[starfinder_theme] = subtheme
            return subtheme

        return decorator

    @classmethod
    def create(cls, starfinder_theme : str):
        """Function to return the called starfinder theme

        Args:
            starfinder_theme (str): name of the starfinder theme

        Raises:
            ValueError: if the starfinder theme has not been implemented yet

        Returns:
            callable: the desired child theme
        """
        if starfinder_theme not in cls.subthemes:
            raise ValueError(f'{starfinder_theme} has not yet been implemented')

        return cls.subthemes[starfinder_theme]()

    def current_abilities(self, level : int) -> list[Ability]:
        """Function to handle feats from level up

        Args:
            level (int): the new Level

        Returns:
            list: List of the Abilities that come fix with the level up
        """
        abilities = []
        for ability in self.abilities:
            if ability.level <= level:
                abilities.append(ability)
        return abilities
