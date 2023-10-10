from helpers.ability import Ability
from starfinder_races.starfinder_race import StarfinderRace
from starfinder_feats.starfinder_feat_type import FeatType

@StarfinderRace.register_subrace('android')
class Android(StarfinderRace):
    """The Android Starfinder race that inherits from the StarfinderRace class
    """
    def __init__(self) -> None:
        super().__init__("Android")
        self.attributes["dexterity"] = 2
        self.attributes["intelligence"] = 2
        self.attributes["charisma"] = -2
        self.hit_points = 4
        self.abilities = self.all_race_abilities()

    def all_race_abilities(self) -> list[Ability]:
        """creates the ability list for the race

        Returns:
            list: List of abilities
        """
        abilities = [
            Ability("Constructed", 1, FeatType.WORDS),
            Ability("Exceptional Vision", 1, FeatType.WORDS),
            Ability("Flat Affect", 1, FeatType.STATS, skills=[["sense motive", -2]]),
            Ability("Upgrade Slot", 1, FeatType.WORDS)
        ]
        return abilities
