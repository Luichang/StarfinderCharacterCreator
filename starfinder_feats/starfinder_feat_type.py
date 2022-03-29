from enum import Enum, auto

class FeatType(Enum):
    """Starfinder Class Feat Types. Inherits from Enum
    """
    WORDS = auto() # have no further effect
    REPLACABLE = auto() # only replaces the text has no other effect

    CHOOSE = auto() # choose from the class_choose_feats
    SELECTION = auto() # used to select type for mystic, operative, soldier

    WEAPON = auto()

    # condense these two
    ADD_EXPERTISE = auto() # envoy
    CLASS = auto() # solarian
    #

    # condense these four
    CHANNEL = auto() # mystic
    EDGE = auto() # operative
    INFLUENCE = auto() # solarian
    SKILLS = auto() # technomancer
    #

    # codense these three
    COMBAT = auto() # soldier
    CPOWER = auto() # mystic
    SPELL = auto() # mystic
    #


    TALENT = auto() # envoy


    ZENITH = auto() # solarian


    TECHNIQUE1 = auto() # soldier
    TECHNIQUE2 = auto() # soldier

    FEAT = auto() # technomancer
