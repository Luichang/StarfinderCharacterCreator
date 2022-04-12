from helpers.ability import Ability
from starfinder_themes.starfinder_theme import StarfinderTheme
from starfinder_feats.starfinder_feat_type import FeatType

@StarfinderTheme.register_subtheme('xenoseeker')
class Xenoseeker(StarfinderTheme):
    """The Xenoseeker Starfinder theme that inherits from the StarfinderTheme class
    """
    def __init__(self) -> None:
        super().__init__("Xenoseeker")
        self.attributes["charisma"] = 1
        self.abilities = self.all_theme_abilities()

    def all_theme_abilities(self):
        """creates the ability list for the theme

        Returns:
            list: List of abilities
        """

        abilities = [
            Ability("Theme knowledge", 1, FeatType.STATS, skills=["life science"]),
            Ability("Quick pidgin", 6, FeatType.WORDS),
            Ability("First contact", 12, FeatType.WORDS),
            Ability("Brilliant discovery", 18, FeatType.WORDS)
        ]
        return abilities
