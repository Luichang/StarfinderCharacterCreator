from helpers.ability import Ability
from starfinder_feats.feat_requirement import Requirements
from starfinder_feats.starfinder_feat import Feat
from starfinder_feats.starfinder_feat_type import FeatType

from starfinder_classes.starfinder_class import StarfinderClass
@StarfinderClass.register_subclass('operative')
class Operative(StarfinderClass):
    """The Operative Starfinder class that inherits from the StarfinderClass class
    """
    def __init__(self) -> None:
        super().__init__("Operative")
        self.selection = ""
        self.bab = [0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15]
        self.fort = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.reflex = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.will = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.skills = 8
        self.stamina_points = 6
        self.hit_points = 6
        self.key = "dex"
        self.proficiencies = ["Light Armor Proficiency", "Basic Melee Weapon Proficiency",
                           "Small Arm Proficiency", "Sniper Weapon Proficiency"]

        self.bonuses = ["acrobatics", "athletics", "bluff", "computers", "culture", "disguise",
                   "engineering", "intimidate", "medicine", "perception", "piloting", "profession",
                   "profession2", "sense motive", "sleight of hand", "stealth", "survival"]


        self.class_abilities = self.all_class_abilities()
        #self.class_choose_feats = self.all_choosable_abilities()

    def all_class_abilities(self) -> list[Ability]:
        """creates the ability list for character level up

        Returns:
            list: List of levlup abilities
        """

        levelups = [
            Ability("Operative's edge +1", 1, FeatType.MISC_INCREASE, short=""),
            Ability("Specialization", 1, FeatType.SELECTION), # ["feat", "Skill Focus"]
            Ability("Trick attack +1d4", 1, FeatType.REPLACABLE, short=""),
            Ability("Evasion", 2, FeatType.WORDS),
            Ability("Operative exploit", 2, FeatType.CHOOSE2),
            Ability("Operative's edge +2", 3, FeatType.MISC_INCREASE, short="Operative's edge"),
            Ability("Quick movement (+10 ft.)", 3, FeatType.REPLACABLE, short=""),
            Ability("Trick attack +1d8", 3, FeatType.REPLACABLE, short="Trick attack"),
            Ability("Weapon specialization", 3, FeatType.WEAPON),
            Ability("Debilitating trick", 4, FeatType.WORDS),
            Ability("Operative exploit", 4, FeatType.CHOOSE2),
            Ability("Specialization exploit", 5, FeatType.TECHNIQUE1), # ["exploit"]
            Ability("Trick attack +3d8", 5, FeatType.REPLACABLE, short="Trick attack"),
            Ability("Operative exploit", 6, FeatType.CHOOSE2),
            Ability("Operative's edge +3", 7, FeatType.MISC_INCREASE, short="Operative's edge"),
            Ability("Specialization skill mastery", 7, FeatType.WORDS),
            Ability("Trick attack +4d8", 7, FeatType.REPLACABLE, short="Trick attack"),
            Ability("Uncanny agility", 7, FeatType.WORDS),
            Ability("Operative exploit", 8, FeatType.CHOOSE2),
            Ability("Triple attack", 8, FeatType.WORDS),
            Ability("Quick movement (+20 ft.)", 9, FeatType.REPLACABLE, short="Quick movement"),
            Ability("Trick attack +5d8", 9, FeatType.REPLACABLE, short="Trick attack"),
            Ability("Operative exploit", 10, FeatType.CHOOSE2),
            Ability("Operative's edge +4", 11, FeatType.MISC_INCREASE, short="Operative's edge"),
            Ability("Specialization power", 11, FeatType.TECHNIQUE2), # ["power"]
            Ability("Trick attack +6d8", 11, FeatType.REPLACABLE, short="Trick attack"),
            Ability("Operative exploit", 12, FeatType.CHOOSE2),
            Ability("Quad attack", 13, FeatType.WORDS),
            Ability("Trick attack +7d8", 13, FeatType.REPLACABLE, short="Trick attack"),
            Ability("Operative exploit", 14, FeatType.CHOOSE2),
            Ability("Operative's edge +5", 15, FeatType.MISC_INCREASE, short="Operative's edge"),
            Ability("Quick movement (+30 ft.)", 15, FeatType.REPLACABLE, short="Quick movement"),
            Ability("Trick attack +8d8", 15, FeatType.REPLACABLE, short="Trick attack"),
            Ability("Operative exploit", 16, FeatType.CHOOSE2),
            Ability("Double debilitation", 17, FeatType.WORDS),
            Ability("Trick attack +9d8", 17, FeatType.REPLACABLE, short="Trick attack"),
            Ability("Operative exploit", 18, FeatType.CHOOSE2),
            Ability("Operative's edge +6", 19, FeatType.MISC_INCREASE, short="Operative's edge"),
            Ability("Trick attack +10d8", 19, FeatType.REPLACABLE, short="Trick attack"),
            Ability("Operative exploit", 20, FeatType.CHOOSE2),
            Ability("Supreme operative", 20, FeatType.WORDS)
        ]
        return levelups

    def all_choosable_abilities(self) -> list[Ability]:
        """creates the choosable ability list for the Mechanic class

        Returns:
            list[Ability]: list of choosable abilities
        """

        choosable = [
            Ability("Alien Archive", 2, FeatType.WORDS),
            Ability("Combat Trick", 2, FeatType.WORDS),
            Ability("Field Treatment", 2, FeatType.WORDS),
            Ability("Holographic Clone", 2, FeatType.WORDS),
            Ability("Inoculation", 2, FeatType.WORDS),
            Ability("Jack of All Trades", 2, FeatType.WORDS),
            Ability("Nightvision", 2, FeatType.WORDS),
            Ability("Quick Disguise", 2, FeatType.WORDS),
            Ability("Uncanny Mobility", 2, FeatType.WORDS),
            Ability("Uncanny Pilot", 2, FeatType.WORDS),
            Ability("Bleeding Shot", 6, FeatType.WORDS),
            Ability("Certainty", 6, FeatType.WORDS),
            Ability("Debilitating Sniper", 6, FeatType.WORDS),
            Ability("Enhanced Senses", 6, FeatType.WORDS),
            Ability("Hampering Shot", 6, FeatType.WORDS),
            Ability("Improved Quick Movement", 6, FeatType.WORDS),
            Ability("Interfering Shot", 6, FeatType.WORDS),
            Ability("Mentalist's Bane", 6, FeatType.WORDS),
            Ability("Speed Hacker", 6, FeatType.WORDS),
            Ability("Staggering Shot", 6, FeatType.WORDS),
            Ability("Stalwart", 6, FeatType.WORDS),
            Ability("Sure-Footed", 6, FeatType.WORDS),
            Ability("Uncanny Shooter", 6, FeatType.WORDS),
            Ability("Cloaking Field", 10, FeatType.WORDS),
            Ability("Deactivating Shot", 10, FeatType.WORDS),
            Ability("Elusive Hacker", 10, FeatType.WORDS),
            Ability("Ever Vigilant", 10, FeatType.WORDS),
            Ability("Glimpse the Truth", 10, FeatType.WORDS),
            Ability("Holographic Distraction", 10, FeatType.WORDS),
            Ability("Improved Evasion", 10, FeatType.WORDS),
            Ability("Improved Uncanny Mobility", 10, FeatType.WORDS),
            Ability("Master of Disguise", 10, FeatType.WORDS),
            Ability("Stunning Shot", 10, FeatType.WORDS),
            Ability("Versatile Movement", 10, FeatType.WORDS),
            Ability("Efficient Cloaking Field", 14, FeatType.WORDS),
            Ability("Knockout Shot", 14, FeatType.WORDS),
            Ability("Multiattack Mastery", 14, FeatType.WORDS),
            Ability("Uncanny Senses", 14, FeatType.WORDS)
        ]
        return choosable

    def select_selection(self, specialization : str, num : int = None):
        """function that sets the specialization

        Args:
            specialization (str): new specialization
            num (int): added so this function can be used with other classes that need the num
        """
        self.selection = specialization

    def possible_selections(self) -> list:
        """function that gives every possible specialization

        Returns:
            list: list of possible specializations
        """
        specializations = [
            "Daredevil", "Detective", "Explorer", "Ghost", "Hacker", "Spy", "Thief"
        ]
        return specializations

    def specialization_feat(self):
        """function to return the feat related stuff of the operative
        """
        specialization = {
            "Daredevil" : [["acrobatics", "athletics"], "Versatile movement", "Terrain Attack"],
            "Detective" : [["culture", "sense motive"], "Glimpse the truth","Detective's Insight"],
            "Explorer"  : [["culture", "survival"], "Ever vigilant", "Into the Unknown"],
            # Explorer: you gain a +4 bonus to Culture and Survival checks
            "Ghost"     : [["acrobatics", "stealth"], "Cloaking field", "Phase Shift Escape"],
            "Hacker"    : [["computers", "engineering"], "Elusive hacker", "Control Hack"],
            "Spy"       : [["bluff", "disguise"], "Master of disguise", "Fool Detection"],
            "Thief"     : [["perception", "sleight of hand"], "Holographic distraction",
                            "Contingency Plan"]
        }

    def specialization_exploit(self):
        """function to return the exploit related stuff of the operative
        """
        specialization = {
            "Daredevil" : [["acrobatics", "athletics"], "Versatile movement", "Terrain Attack"],
            "Detective" : [["culture", "sense motive"], "Glimpse the truth","Detective's Insight"],
            "Explorer"  : [["culture", "survival"], "Ever vigilant", "Into the Unknown"],
            # Explorer: you gain a +4 bonus to Culture and Survival checks
            "Ghost"     : [["acrobatics", "stealth"], "Cloaking field", "Phase Shift Escape"],
            "Hacker"    : [["computers", "engineering"], "Elusive hacker", "Control Hack"],
            "Spy"       : [["bluff", "disguise"], "Master of disguise", "Fool Detection"],
            "Thief"     : [["perception", "sleight of hand"], "Holographic distraction",
                            "Contingency Plan"]
        }

    def specialization_power(self):
        """function to return the power related stuff of the operative
        """
        specialization = {
            "Daredevil" : [["acrobatics", "athletics"], "Versatile movement", "Terrain Attack"],
            "Detective" : [["culture", "sense motive"], "Glimpse the truth","Detective's Insight"],
            "Explorer"  : [["culture", "survival"], "Ever vigilant", "Into the Unknown"],
            # Explorer: you gain a +4 bonus to Culture and Survival checks
            "Ghost"     : [["acrobatics", "stealth"], "Cloaking field", "Phase Shift Escape"],
            "Hacker"    : [["computers", "engineering"], "Elusive hacker", "Control Hack"],
            "Spy"       : [["bluff", "disguise"], "Master of disguise", "Fool Detection"],
            "Thief"     : [["perception", "sleight of hand"], "Holographic distraction",
                            "Contingency Plan"]
        }

    def misc_additions(self) -> list:
        """function to return the skills that are to be increased

        Returns:
            list: list of all the skills that are to be increased by 1
        """
        return ["acrobatics", "athletics", "bluff", "computers", "culture", "diplomacy",
                "disguise", "engineering", "intimidate", "life science", "medicine", "mysticism",
                "perception", "physical science", "piloting", "profession", "profession2",
                "sense motive", "sleight of hand", "stealth", "survival", "initiative"]

skill_focus = Feat("Skill Focus", False, None, FeatType.WORDS) # "choose", ["skill", ["any", 3]]
mobility = Feat("Mobility", True, Requirements(ability=[["dex", 13]]), FeatType.WORDS)
sidestep = Feat("Sidestep", True,
                Requirements(ability=[["dex", 15]], from_list=[["feat", [mobility]],
                                        ["class", Operative]]),
                FeatType.WORDS)
improved_sidestep = Feat("Improved Sidestep", True,
                        Requirements(ability=[["dex", 15]], feat=[sidestep],
                                    from_list=[["feat", [mobility]], ["class",  Operative]]),
                        FeatType.WORDS)
