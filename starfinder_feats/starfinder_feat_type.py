from enum import Enum, auto

class FeatType(Enum):
    """Starfinder Class Feat Types. Inherits from Enum
    """
    WORDS = auto() # have no further effect
    REPLACABLE = auto() # only replaces the text has no other effect

    CHOOSE = auto() # choose from the class_choose_feats
    SELECTION = auto() # used to select type for mystic, operative, soldier

    WEAPON = auto()


    ADD_EXPERTISE = auto() # envoy
    CLASS = auto() # solarian



    TALENT = auto() # envoy


    CPOWER = auto() # mystic
    SPELL = auto() # mystic
    CHANNEL = auto() # mystic

    EDGE = auto() # operative


    
    INFLUENCE = auto() # solarian
    ZENITH = auto() # solarian


    TECHNIQUE1 = auto() # soldier
    COMBAT = auto() # soldier
    TECHNIQUE2 = auto() # soldier

    FEAT = auto() # technomancer
    SKILLS = auto() # technomancer
