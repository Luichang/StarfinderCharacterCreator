from helpers.ability import Ability
from starfinder_themes.starfinder_theme import StarfinderTheme
from starfinder_feats.starfinder_feat_type import FeatType

@StarfinderTheme.register_subtheme('themeless')
class Themeless(StarfinderTheme):
    """The Themeless Starfinder theme that inherits from the StarfinderTheme class
    """
    def __init__(self, improvement : str = "str") -> None:
        super().__init__("Themeless")
        self.improvement = improvement
        self.attributes[improvement] = 1
        self.abilities = self.all_theme_abilities()

    def __str__(self) -> str:
        return f"{self.name} [{self.improvement}]"

    def all_theme_abilities(self):
        """creates the ability list for the theme

        Returns:
            list: List of abilities
        """

        abilities = [
            Ability("Theme knowledge", 1, FeatType.STATS, skills=["any"]),
            Ability("Certainty", 6, FeatType.WORDS),
            Ability("Extensive studies", 12, FeatType.WORDS),
            Ability("Steely determination", 18, FeatType.WORDS)
        ]
        return abilities

    def select_improvement(self, attr : str) -> None:
        """Function to select new attribute for current themeless

        Args:
            attr (str): attribute, either str, dex, con, int, wis, cha
        """
        self.attributes[self.improvement] = 0
        self.improvement = attr
        self.attributes[self.improvement] = 1
