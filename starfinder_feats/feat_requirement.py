from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from starfinder_races.starfinder_race import StarfinderRace

if TYPE_CHECKING:
    from starfinder_classes.starfinder_class import StarfinderClass
    from starfinder_feats.starfinder_feat import Feat

@dataclass(repr=False, eq=False)
class Requirements:
    """Requirements Class to offer an easier time checking if the character fulfills the
        requirements needed by any given feat
    """
    level : int = None
    spell_level : int = None
    skills : list = None
    ability : list = None
    class_name : StarfinderClass = None
    bab : int = None
    reflex : int = None
    will : int = None
    fort : int = None
    race : StarfinderRace = None
    feat : list[Feat] = None
    from_list : list = None
        