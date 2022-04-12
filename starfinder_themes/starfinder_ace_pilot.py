from helpers.ability import Ability
from starfinder_themes.starfinder_theme import StarfinderTheme
from starfinder_feats.starfinder_feat_type import FeatType

@StarfinderTheme.register_subtheme('ace pilot')
class AcePilot(StarfinderTheme):
    """The Ace Pilot Starfinder theme that inherits from the StarfinderTheme class
    """
    def __init__(self) -> None:
        super().__init__("Ace Pilot")
        self.attributes["dexterity"] = 1
        self.abilities = self.all_theme_abilities()

    def all_theme_abilities(self):
        """creates the ability list for the theme

        Returns:
            list: List of abilities
        """

        abilities = [
            Ability("Theme knowledge", 1, FeatType.STATS, skills=["piloting"]),
            Ability("Lone Wolf", 6, FeatType.WORDS),
            Ability("Need for Speed", 12, FeatType.WORDS),
            Ability("Master Pilot", 18, FeatType.WORDS)
        ]
        return abilities
