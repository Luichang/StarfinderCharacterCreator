from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from starfinder_feats.starfinder_feat_type import FeatType

if TYPE_CHECKING:
    from starfinder_feats.feat_requirement import Requirements


@dataclass(repr=False, eq=False)
class Feat:
    """The Feat Class for Starfinder Feats
    """
    name : str
    combat : bool
    requirements : Requirements
    result : FeatType

    def __str__(self) -> str:
        return self.name

    def copy(self) -> Feat:
        """function that returns a copy of the Feat

        Returns:
            Feat: a copy of the current Feat
        """
        return Feat(self.name, self.combat, self.requirements, self.result)
