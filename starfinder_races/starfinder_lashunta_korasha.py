from helpers.ability import Ability
from starfinder_races.starfinder_race import StarfinderRace
from starfinder_feats.starfinder_feat_type import FeatType
from starfinder_feats.starfinder_spells import daze, pyschokinetic_hand, detect_thoughts

@StarfinderRace.register_subrace('lashunta(korasha)')
class LashuntaKorasha(StarfinderRace):
    """The Lashunta(Korasha) Starfinder race that inherits from the StarfinderRace class
    """
    def __init__(self) -> None:
        super().__init__("Lashunta_Korasha")
        self.attributes["strength"] = 2
        self.attributes["charisma"] = 2
        self.attributes["constitution"] = -2
        self.hit_points = 4
        self.abilities = self.all_race_abilities()
        self.spells = [[daze, pyschokinetic_hand], [detect_thoughts]]

    def all_race_abilities(self):
        """creates the ability list for the race

        Returns:
            list: List of abilities
        """

        abilities = [
            Ability("Dimorphic", 1, FeatType.WORDS),
            Ability("Lashunta magic", 1, FeatType.SPELL),
            Ability("Limited telepathy", 1, FeatType.WORDS),
            Ability("Student", 1, FeatType.STATS, skills=[["any", 2], ["any", 2]])
        ]
        return abilities
