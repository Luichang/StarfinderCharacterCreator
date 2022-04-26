from helpers.ability import Ability
from starfinder_feats.feat_requirement import Requirements
from starfinder_feats.starfinder_feat import Feat
from starfinder_feats.starfinder_feat_type import FeatType
from starfinder_feats.starfinder_spells import (augury, clairaudience, command,
                                                commune_nature, confusion,
                                                contact_plane, control_gravity,
                                                darkvision, divination,
                                                dominate_person, detect_thoughts,
                                                entropic_grasp, feeblemind,
                                                fog_cloud,
                                                greater_remove_condition,
                                                hold_person, identify,
                                                inflict_pain, irridate,
                                                lesser_confusion,
                                                lesser_remove_condition,
                                                life_bubble, magic_missile,
                                                mass_suggestion, mind_probe,
                                                mind_thrust_1, mind_thrust_2,
                                                mind_thrust_3, mind_thrust_4,
                                                mind_thrust_5, mind_thrust_6,
                                                mystic_cure_1, mystic_cure_2,
                                                mystic_cure_3, mystic_cure_4,
                                                mystic_cure_5, mystic_cure_6,
                                                reincarnate, remove_affliction,
                                                remove_condition,
                                                remove_radioactivity,
                                                restoration, suggestion,
                                                synaptic_pulse, telekinesis,
                                                telepathy, terraform, tongues,
                                                true_seeing, vision,
                                                zone_truth)

from starfinder_classes.starfinder_class import (StarfinderClass,
                                                 basic_melee_prof, light_armor,
                                                 small_arm_proficiency)


@StarfinderClass.register_subclass('mystic')
class Mystic(StarfinderClass):
    """The Mystic Starfinder class that inherits from the StarfinderClass class
    """
    def __init__(self) -> None:
        super().__init__("Mystic")
        self.selection = ""
        self.bab = [0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15]
        self.fort = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.reflex = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.will = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.skills = 6
        self.stamina_points = 6
        self.hit_points = 6
        self.key = "wis"
        self.proficiencies = [light_armor, basic_melee_prof, small_arm_proficiency]

        self.bonuses = ["bluff", "culture", "diplomacy", "disguise", "intimidate", "life science",
                   "medicine", "mysticism", "perception", "profession", "profession2",
                   "sense motive", "survival"]


        self.class_abilities = self.all_class_abilities()
        #self.class_choose_feats = self.all_choosable_abilities()

    def all_class_abilities(self) -> list[Ability]:
        """creates the ability list for character level up

        Returns:
            list: List of levlup abilities
        """

        levelups = [
            Ability("Connection", 1, FeatType.SELECTION),
            Ability("Connection power", 1, FeatType.TECHNIQUE1), # argument of 0
            Ability("Connection spell", 1, FeatType.TECHNIQUE2), # argument of 0 -> 1 - 8 = -7
            Ability("Healing touch", 1, FeatType.WORDS),
            Ability("Channel skill +1", 2, FeatType.MISC_INCREASE, short="Channel skill"),
            Ability("Mindlink", 2, FeatType.WORDS),
            Ability("Connection power", 3, FeatType.TECHNIQUE1), # argument of 1
            Ability("Weapon specialization", 3, FeatType.WEAPON),
            Ability("Connection spell", 4, FeatType.TECHNIQUE2), # argument of 1 -> 4 - 8 = -4
            Ability("Channel skill +2", 5, FeatType.MISC_INCREASE, short="Channel skill"),
            Ability("Connection power", 6, FeatType.TECHNIQUE1), # argument of 2
            Ability("Connection spell", 7, FeatType.TECHNIQUE2), # argument of 2 -> 7 - 8 = -1
            Ability("Channel skill +3", 8, FeatType.MISC_INCREASE, short="Channel skill"),
            Ability("Connection power", 9, FeatType.TECHNIQUE1), # argument of 3
            Ability("Connection spell", 10, FeatType.TECHNIQUE2), # argument of 3 -> 10 - 8 = 2
            Ability("Channel skill +4", 11, FeatType.MISC_INCREASE, short="Channel skill"),
            Ability("Telepathic bond", 11, FeatType.WORDS),
            Ability("Connection power", 12, FeatType.TECHNIQUE1), # argument of 4
            Ability("Connection spell", 13, FeatType.TECHNIQUE2), # argument of 4 -> 13 - 8 = 5
            Ability("Channel skill +5", 14, FeatType.MISC_INCREASE, short="Channel skill"),
            Ability("Connection power", 15, FeatType.TECHNIQUE1), # argument of 5
            Ability("Connection spell", 16, FeatType.TECHNIQUE2), # argument of 5 -> 16 - 8 = 8
            Ability("Channel skill +6", 17, FeatType.MISC_INCREASE, short="Channel skill"),
            Ability("Connection power", 18, FeatType.TECHNIQUE1), # argument of 6
            Ability("Transcendence", 19, FeatType.WORDS),
            Ability("Channel skill +7", 20, FeatType.MISC_INCREASE, short="Channel skill"),
            Ability("Enlightenment", 20, FeatType.WORDS)
        ]
        return levelups

    def select_selection(self, connection : str, _ : int = None):
        """function that sets the connection

        Args:
            connection (str): new connection
            num (int): added so this function can be used with other classes that need the num
        """
        connections = [
            "Akashic", "Empath", "Healer", "Mindbreaker", "Overlord", "Star Shaman", "Xenodruid"
        ]
        if connection in connections:
            self.selection = connection
        else:
            raise ValueError(f"Entered Value {connection} is not a valid Connection")

    def possible_selections(self) -> list:
        """function that gives every possible connection

        Returns:
            list: list of possible connections
        """
        connections = [
            "Akashic", "Empath", "Healer", "Mindbreaker", "Overlord", "Star Shaman", "Xenodruid"
        ]
        return connections

    def style_combat(self, _ : int = None) -> dict:
        """function to return the dictionary of specializations for each specialization
        The way the dictionary is setup is: the keys are level equivalent so this function
        can work in tandem with the soldier class. For the soldier in technique2 the character
        level is taken and 8 is subtracted. So since the operative gains Specialization exploit
        at level 5 and Specialization power at level 11, the dictionary has the keys of 5 and 3.
        Yes it is dumb. Whoever is reading this, feel free to make a pull request with a better
        solution.

        Args:
            _ (int): comes from the soldier class. can be ignored here

        Returns:
            dict: dictionary where the possible levels are the keys and the combat feats are the
                    items
        """

        specialization = {
            "Akashic" : {
                1  : "Akashic Knowledge",
                3  : "Access Akashic Record",
                6  : "Peer into the Future",
                9  : "Mind Probe",
                12 : "Telepathic Memories",
                15 : "Memory Palace",
                18 : "Glean Spell",
                -7 : identify,
                -4 : augury,
                -1 : tongues,
                2  : divination,
                5  : contact_plane,
                8  : vision
            },
            "Empath" : {
                1  : "Empathy",
                3  : "Greater Mindlink",
                6  : "Emotionsense",
                9  : "Discern Lies",
                12 : "Greater Emotionsense",
                15 : "Retrocognition",
                18 : "Empathic Mastery",
                -7 : detect_thoughts,
                -4 : zone_truth,
                -1 : clairaudience,
                2  : mind_probe,
                5  : telepathy,
                8  : true_seeing
            },
            "Healer" : {
                1  : "Healing Channel",
                3  : "Lifelink",
                6  : "Healer's Bond",
                9  : "Steal Life",
                12 : "Channel Bond",
                15 : "Channel Life",
                18 : "Deny Death",
                -7 : [lesser_remove_condition, mind_thrust_1],
                -4 : [remove_condition, mind_thrust_2],
                -1 : [remove_affliction, mind_thrust_3],
                2  : [restoration, mind_thrust_4],
                5  : [greater_remove_condition, mind_thrust_5],
                8  : mind_thrust_6
            },
            "Mindbreaker" : {
                1  : "Share Pain",
                3  : "Backlash",
                6  : "Sow Doubt",
                9  : "Mental Anguish",
                12 : "Mindbreaking Link",
                15 : "Mindkiller",
                18 : "Explode Head",
                -7 : [lesser_confusion, mind_thrust_1],
                -4 : [inflict_pain, mind_thrust_2],
                -1 : [synaptic_pulse, mind_thrust_3],
                2  : [confusion, mind_thrust_4],
                5  : [feeblemind, mind_thrust_5],
                8  : mind_thrust_6
            },
            "Overlord" : {
                1  : "Inexplicable Commands",
                3  : "Forced Amity",
                6  : "Echoes of Obedience",
                9  : "Greater Forced Amity",
                12 : "Jealous Overlord",
                15 : "Forceful Commands",
                18 : "Absolute Control",
                -7 : command,
                -4 : hold_person,
                -1 : suggestion,
                2  : confusion,
                5  : dominate_person,
                8  : mass_suggestion
            },
            "Star Shaman" : {
                1  : "Walk the Void",
                3  : "Starlight Form",
                6  : "Stargazer",
                9  : "Starflight",
                12 : "Starry Bond",
                15 : "Meteor Shower",
                18 : "Interplanetary Teleport",
                -7 : magic_missile,
                -4 : darkvision,
                -1 : irridate,
                2  : remove_radioactivity,
                5  : telekinesis,
                8  : control_gravity
            },
            "Xenodruid" : {
                1  : "Speak with Animals",
                3  : "Grasping Vines",
                6  : "Animal Adaptation",
                9  : "Reactive Resistance",
                12 : "Share Resistance",
                15 : "Plant Transport",
                18 : "Guided Rebirth",
                -7 : life_bubble,
                -4 : fog_cloud,
                -1 : entropic_grasp,
                2  : reincarnate,
                5  : commune_nature,
                8  : terraform
            }
        }
        return specialization[self.selection]

    def connection_spell(self) -> list:
        """function to return the chosen connections spells

        Returns:
            list: list of connection spells
        """
        spell_dict = {
            "Akashic" : [identify, augury, tongues, divination, contact_plane, vision],

            "Empath" :  [detect_thoughts, zone_truth, clairaudience, mind_probe, telepathy,
                         true_seeing],

            "Healer" : [lesser_remove_condition, remove_condition, remove_affliction, restoration,
                        greater_remove_condition, mind_thrust_1, mind_thrust_2, mind_thrust_3,
                        mind_thrust_4, mind_thrust_5, mind_thrust_6],

            "Mindbreaker" : [lesser_confusion, inflict_pain, synaptic_pulse, confusion, feeblemind,
                             mind_thrust_1, mind_thrust_2, mind_thrust_3, mind_thrust_4,
                             mind_thrust_5, mind_thrust_6],

            "Overlord" : [command, hold_person, suggestion, confusion, dominate_person,
                           mass_suggestion],

            "Star Shaman" : [magic_missile, darkvision, irridate, remove_radioactivity,
                             telekinesis, control_gravity],

            "Xenodruid" : [life_bubble, fog_cloud, entropic_grasp, reincarnate, commune_nature,
                           terraform]
        }

        return spell_dict[self.selection]

    def connection_feat(self) -> list:
        """function to return the feats of the selected connection

        Returns:
            list: list of the feats from the connection
        """
        feat_dict = {
            "Akashic" : ["Akashic Knowledge",
                         "Access Akashic Record",
                         "Peer into the Future",
                         "Mind Probe",
                         "Telepathic Memories",
                         "Memory Palace",
                         "Glean Spell"],

            "Empath" : ["Empathy",
                        "Greater Mindlink",
                        "Emotionsense",
                        "Discern Lies",
                        "Greater Emotionsense",
                        "Retrocognition",
                        "Empathic Mastery"],

            "Healer" : ["Healing Channel",
                        "Lifelink",
                        "Healer's Bond",
                        "Steal Life",
                        "Channel Bond",
                        "Channel Life",
                        "Deny Death"],

            "Mindbreaker" : ["Share Pain",
                             "Backlash",
                             "Sow Doubt",
                             "Mental Anguish",
                             "Mindbreaking Link",
                             "Mindkiller",
                             "Explode Head"],

            "Overlord" :  ["Inexplicable Commands",
                           "Forced Amity",
                           "Echoes of Obedience",
                           "Greater Forced Amity",
                           "Jealous Overlord",
                           "Forceful Commands",
                           "Absolute Control"],

            "Star Shaman" : ["Walk the Void",
                             "Starlight Form",
                             "Stargazer",
                             "Starflight",
                             "Starry Bond",
                             "Meteor Shower",
                             "Interplanetary Teleport"],

            "Xenodruid" : ["Speak with Animals",
                           "Grasping Vines",
                           "Animal Adaptation",
                           "Reactive Resistance",
                           "Share Resistance",
                           "Plant Transport",
                           "Guided Rebirth"]
        }
        return feat_dict[self.selection]

    def misc_additions(self) -> list:
        """function to return the two skills that get improved by the selected connection

        Returns:
            list: list containing the two skills that are to be improved
        """
        skill_dict = {
            "Akashic" : ["culture", "mysticism"],

            "Empath" : ["perception", "sense motive"],

            "Healer" : ["medicine", "mysticism"],

            "Mindbreaker" : ["bluff", "intimidate"],

            "Overlord" : ["diplomacy", "intimidate"],

            "Star Shaman" : ["perception", "piloting"],

            "Xenodruid" : ["life science", "survival"]
        }
        return skill_dict[self.selection]

connection_inkling = Feat("Connection Inkling", False, Requirements(ability=[["wis", 15]], level=5),
                            FeatType.WORDS) # TODO need to check that the character is NOT mystic
tmp_class_name = Mystic()
tmp_class_name.select_selection("Healer")
harm_undead = Feat("Harm Undead", False, Requirements(class_name=tmp_class_name), FeatType.WORDS)
