from helpers.ability import Ability
from starfinder_races.starfinder_race import StarfinderRace
from starfinder_feats.starfinder_feat_type import FeatType

@StarfinderRace.register_subrace('kasatha')
class Kasatha(StarfinderRace):
    """The Kasatha Starfinder race that inherits from the StarfinderRace class
    """
    def __init__(self) -> None:
        super().__init__("Kasatha")
        self.attributes["strength"] = 2
        self.attributes["wisdom"] = 2
        self.attributes["intelligence"] = -2
        self.hit_points = 4
        self.abilities = self.all_race_abilities()

    def all_race_abilities(self):
        """creates the ability list for the race

        Returns:
            list: List of abilities
        """

        abilities = [
            Ability("Desert Stride", 1, FeatType.WORDS),
            Ability("Four-Armed", 1, FeatType.WORDS),
            Ability("Historian", 1, FeatType.STATS, skills=[["culture", 2]]),
            Ability("Natural Grace", 1, FeatType.STATS, skills=[["acrobatics", 2], ["athletics", 2]])
        ]
        return abilities
