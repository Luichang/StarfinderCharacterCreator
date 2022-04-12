from helpers.ability import Ability
from starfinder_races.starfinder_race import StarfinderRace
from starfinder_feats.starfinder_feat_type import FeatType

@StarfinderRace.register_subrace('vesk')
class Vesk(StarfinderRace):
    """The Vesk Starfinder race that inherits from the StarfinderRace class
    """
    def __init__(self) -> None:
        super().__init__("Vesk")
        self.attributes["strength"] = 2
        self.attributes["constitution"] = 2
        self.attributes["intelligence"] = -2
        self.hit_points = 6
        self.abilities = self.all_race_abilities()

    def all_race_abilities(self):
        """creates the ability list for the race

        Returns:
            list: List of abilities
        """

        abilities = [
            Ability("Armor Savant", 1, FeatType.WORDS),
            Ability("Fearless", 1, FeatType.WORDS),
            Ability("Low-Light Vision", 1, FeatType.WORDS),
            Ability("Natural Weapons", 1, FeatType.WORDS)
        ]
        return abilities
