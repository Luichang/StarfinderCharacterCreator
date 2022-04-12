from enum import Enum, auto

class FeatType(Enum):
    """Starfinder Class Feat Types. Inherits from Enum
    """
    WORDS = auto() # have no further effect
    REPLACABLE = auto() # only replaces the text has no other effect
    WEAPON = auto()

    CHOOSE = auto() # choose from the class_choose_feats
    CHOOSE2 = auto() # envoy Talent, solarian Zenith
    SELECTION = auto() # used to select type for mystic, operative, soldier
    MISC_INCREASE = auto() # mystic Channel, operative Edge, technomancer Skills


    # condense these two maybe? one has a rename, the other does not
    ADD_EXPERTISE = auto() # envoy
    INFLUENCE = auto() # solarian
    #

    # codense these two
    CPOWER = auto() # mystic
    SPELL = auto() # mystic
    #

    COMBAT = auto() # soldier
    CLASS = auto() # solarian
    FEAT = auto() # technomancer


    TECHNIQUE1 = auto() # soldier
    TECHNIQUE2 = auto() # soldier

    STATS = auto() # race related

    DABBLER = auto() # theme related
