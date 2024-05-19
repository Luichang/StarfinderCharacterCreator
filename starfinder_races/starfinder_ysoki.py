from helpers.ability import Ability
from starfinder_races.starfinder_race import StarfinderRace
from starfinder_feats.starfinder_feat_type import FeatType

@StarfinderRace.register_subrace('ysoki')
class Ysoki(StarfinderRace):
    """The Ysoki Starfinder race that inherits from the StarfinderRace class
    """
    def __init__(self) -> None:
        super().__init__("Ysoki")
        self.attributes["dexterity"] = 2
        self.attributes["intelligence"] = 2
        self.attributes["strength"] = -2
        self.hit_points = 2

    def all_race_abilities(self):
        """creates the ability list for the race

        Returns:
            list: List of abilities
        """

        abilities = [
            Ability("Cheek Pouches", 1, FeatType.WORDS),
            Ability("Darkvision", 1, FeatType.WORDS),
            Ability("Moxie", 1, FeatType.WORDS),
            Ability("Scrounger", 1, FeatType.STATS, skills=[["engineering", 2], ["stealth", 2], ["survival", 2]])
        ]
        return abilities
