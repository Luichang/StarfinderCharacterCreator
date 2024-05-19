from helpers.ability import Ability
from starfinder_themes.starfinder_theme import StarfinderTheme
from starfinder_feats.starfinder_feat_type import FeatType

@StarfinderTheme.register_subtheme('priest')
class Priest(StarfinderTheme):
    """The Priest Starfinder theme that inherits from the StarfinderTheme class
    """
    def __init__(self) -> None:
        super().__init__("Priest")
        self.attributes["wisdom"] = 1
        self.abilities = self.all_theme_abilities()

    def all_theme_abilities(self):
        """creates the ability list for the theme

        Returns:
            list: List of abilities
        """

        abilities = [
            Ability("Theme knowledge", 1, FeatType.STATS, skills=["mysticism"]),
            Ability("Mantle of the clergy", 6, FeatType.WORDS),
            Ability("Divine Boon", 12, FeatType.SPELL),
            Ability("True communion", 18, FeatType.WORDS)
        ]
        return abilities
