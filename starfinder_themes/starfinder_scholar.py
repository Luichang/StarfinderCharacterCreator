from helpers.ability import Ability
from starfinder_themes.starfinder_theme import StarfinderTheme
from starfinder_feats.starfinder_feat_type import FeatType

@StarfinderTheme.register_subtheme('scholar')
class Scholar(StarfinderTheme):
    """The Scholar Starfinder theme that inherits from the StarfinderTheme class
    """
    def __init__(self) -> None:
        super().__init__("Scholar")
        self.attributes["intelligence"] = 1
        self.abilities = self.all_theme_abilities()

    def all_theme_abilities(self):
        """creates the ability list for the theme

        Returns:
            list: List of abilities
        """

        abilities = [
            Ability("Theme knowledge", 1, FeatType.STATS, skills=["life science", "physical science"]),
            Ability("Tip of the tongue", 6, FeatType.WORDS),
            Ability("Research maven", 12, FeatType.WORDS),
            Ability("Master scholar", 18, FeatType.WORDS)
        ]
        return abilities
