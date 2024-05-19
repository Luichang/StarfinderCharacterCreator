from helpers.ability import Ability
from starfinder_races.starfinder_race import StarfinderRace
from starfinder_feats.starfinder_feat_type import FeatType

@StarfinderRace.register_subrace('shirren')
class Shirren(StarfinderRace):
    """The Shirren Starfinder race that inherits from the StarfinderRace class
    """
    def __init__(self) -> None:
        super().__init__("Shirren")
        self.attributes["constitution"] = 2
        self.attributes["wisdom"] = 2
        self.attributes["charisma"] = -2
        self.hit_points = 6

    def all_race_abilities(self):
        """creates the ability list for the race

        Returns:
            list: List of abilities
        """

        abilities = [
            Ability("Blindsense", 1, FeatType.WORDS),
            Ability("Communalism", 1, FeatType.WORDS),
            Ability("Cultural Fascination", 1, FeatType.STATS, skills=[["culture", 2], ["diplomacy", 2]]),
            Ability("Limited telepathy", 1, FeatType.WORDS)
        ]
        return abilities
