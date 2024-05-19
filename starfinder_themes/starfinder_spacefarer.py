from helpers.ability import Ability
from starfinder_themes.starfinder_theme import StarfinderTheme
from starfinder_feats.starfinder_feat_type import FeatType

@StarfinderTheme.register_subtheme('spacefarer')
class Spacefarer(StarfinderTheme):
    """The Spacefarer Starfinder theme that inherits from the StarfinderTheme class
    """
    def __init__(self) -> None:
        super().__init__("Spacefarer")
        self.attributes["constitution"] = 1
        self.abilities = self.all_theme_abilities()

    def all_theme_abilities(self):
        """creates the ability list for the theme

        Returns:
            list: List of abilities
        """

        abilities = [
            Ability("Theme knowledge", 1, FeatType.STATS, skills=["physical science"]),
            Ability("Eager dabbler", 6, FeatType.DABBLER),
            Ability("Jack of all trades", 12, FeatType.WORDS),
            Ability("Master explorer", 18, FeatType.WORDS)
        ]
        return abilities
