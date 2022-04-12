from helpers.ability import Ability
from starfinder_themes.starfinder_theme import StarfinderTheme
from starfinder_feats.starfinder_feat_type import FeatType

@StarfinderTheme.register_subtheme('icon')
class Icon(StarfinderTheme):
    """The Icon Starfinder theme that inherits from the StarfinderTheme class
    """
    def __init__(self) -> None:
        super().__init__("Icon")
        self.attributes["charisma"] = 1
        self.abilities = self.all_theme_abilities()

    def all_theme_abilities(self):
        """creates the ability list for the theme

        Returns:
            list: List of abilities
        """

        abilities = [
            Ability("Theme knowledge", 1, FeatType.STATS, skills=["profession", "profession2"]),
            Ability("Celebrity", 6, FeatType.WORDS),
            Ability("Megacelebrity", 12, FeatType.WORDS),
            Ability("Master icon", 18, FeatType.WORDS)
        ]
        return abilities
