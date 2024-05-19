from __future__ import annotations

from helpers.ability import Ability
from starfinder_feats.starfinder_feat_type import FeatType
from starfinder_feats.starfinder_spell import Spell

class StarfinderRace:
    """Parent class of various Starfinder races
    """
    def __init__(self, name : str) -> None:
        self.name = name
        self.attributes = {
            "strength" : 0,
            "dexterity" : 0,
            "constitution" : 0,
            "intelligence" : 0,
            "wisdom" : 0,
            "charisma" : 0
        }
        self.hit_points : int
        self.abilities : list[Ability] = self.all_race_abilities()
        self.spells: list[Spell] = []

    def __str__(self) -> str:
        return self.name

    subraces = {}
    @classmethod
    def register_subrace(cls, starfinder_race : str) -> callable:
        """Function to register all the Starfinder Races in the Parent Race

        Args:
            starfinder_race (str): name of the starfinder race

        Returns:
            callable: decorator function to be added in front of the child race
        """
        def decorator(subrace):
            cls.subraces[starfinder_race] = subrace
            return subrace

        return decorator

    @classmethod
    def create(cls, starfinder_race : str, key : str=None) -> StarfinderRace:
        """Function to return the called starfinder race

        Args:
            starfinder_race (str): name of the starfinder race
            key (str): key attribute should it be needed. Defaults to None

        Raises:
            ValueError: if the starfinder race has not been implemented yet

        Returns:
            callable: the desired child race
        """
        if starfinder_race not in cls.subraces:
            raise ValueError(f'{starfinder_race} has not yet been implemented')

        if key: # only to be called on the human race
            return cls.subraces[starfinder_race](key)
        return cls.subraces[starfinder_race]()

    def all_race_abilities(self):
        raise NotImplementedError(f"This function needs to be implemented for race {self.name}")

    def resolve_abilities(self) -> tuple[list[dict], int]:
        skills = []
        number_of_feats_to_add = 0
        for ability in self.abilities:
            if ability.get_type == FeatType.STATS:
                for skill in ability.skills:
                    skills.append(skill)
            elif ability.get_type == FeatType.FEAT:
                number_of_feats_to_add += 1
        return (skills, number_of_feats_to_add)
