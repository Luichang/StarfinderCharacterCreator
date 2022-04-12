from dataclasses import dataclass

@dataclass(repr=False, eq=False)
class Spell:
    """class to hold the information for a starfinder spell
    """
    name : str
    level : int
    mystic : bool
    technomancer : bool

    def __str__(self):
        return self.name
