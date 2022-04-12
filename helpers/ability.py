from starfinder_feats.starfinder_feat_type import FeatType

class Ability:
    """The ability class for Starfinder Classes
    """
    def __init__(self, name : str, level : int, _type : FeatType, *, short : str = None, 
                 skills : list[(str, int)] = None, spells : list = None) -> None:
        self.name = name
        self.level = level
        self.type = _type
        self.short = short
        self.skills = skills # an option can be any, needs to be remembered (at least in races)
        self.spells = spells
    def __str__(self) -> str:
        return self.name

    def get_type(self) -> FeatType:
        """returns the type of the Ability

        Returns:
            FeatType: Ability Type
        """
        return self.type
