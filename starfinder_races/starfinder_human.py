from helpers.ability import Ability
from starfinder_races.starfinder_race import StarfinderRace
from starfinder_feats.starfinder_feat_type import FeatType

@StarfinderRace.register_subrace('human')
class Human(StarfinderRace):
    """The Human Starfinder race that inherits from the StarfinderRace class
    """
    def __init__(self, improvement : str = "str") -> None:
        super().__init__("Human")
        self.attributes[improvement] = 2
        self.improvement = improvement
        self.hit_points = 4
        self.abilities = self.all_race_abilities()

    def __str__(self) -> str:
        return f"{self.name} [{self.improvement}]"

    def all_race_abilities(self):
        """creates the ability list for the race

        Returns:
            list: List of abilities
        """
        abilities = [
            Ability("Bonus feat", 1, FeatType.FEAT),
            Ability("Skilled", 1, FeatType.WORDS)
        ]
        return abilities

    def select_improvement(self, attr : str) -> None:
        """Function to select new attribute for current human

        Args:
            attr (str): attribute, either str, dex, con, int, wis, cha
        """
        self.attributes[self.improvement] = 0
        self.improvement = attr
        self.attributes[attr] = 2
