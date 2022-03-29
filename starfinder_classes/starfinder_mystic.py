from starfinder_classes.starfinder_class import StarfinderClass, Ability
from starfinder_feats.starfinder_feat_type import FeatType

@StarfinderClass.register_subclass('mystic')
class Mystic(StarfinderClass):
    """The Mystic Starfinder class that inherits from the StarfinderClass class
    """
    def __init__(self) -> None:
        super().__init__("Mystic")
        self.connection = "Akashic"
        self.bab = [0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15]
        self.fort = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.reflex = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        self.will = [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        self.skills = 6
        self.stamina_points = 6
        self.hit_points = 6
        self.key = "wis"
        self.proficiencies = ["Light Armor Proficiency", "Basic Melee Weapon Proficiency",
                           "Small Arm Proficiency"]

        bonuses = ["bluff", "culture", "diplomacy", "disguise", "intimidate", "life science",
                   "medicine", "mysticism", "perception", "profession", "profession2",
                   "sense motive", "survival"]

        for bonus in bonuses:
            self.class_bonus[bonus] = 3

        self.class_abilities = self.all_class_abilities()
        #self.class_choose_feats = self.all_choosable_abilities()

    def all_class_abilities(self) -> list[Ability]:
        """creates the ability list for character level up

        Returns:
            list: List of levlup abilities
        """

        levelups = [
            Ability("Connection", 1, FeatType.SELECTION),
            Ability("Connection power", 1, FeatType.CPOWER), # argument of 0
            Ability("Connection spell", 1, FeatType.SPELL), # argument of 0
            Ability("Healing touch", 1, FeatType.WORDS),
            Ability("Channel skill +1", 2, FeatType.CHANNEL, short="Channel skill"),
            Ability("Mindlink", 2, FeatType.WORDS),
            Ability("Connection power", 3, FeatType.CPOWER), # argument of 1
            Ability("Weapon specialization", 3, FeatType.WEAPON),
            Ability("Connection spell", 4, FeatType.SPELL), # argument of 1
            Ability("Channel skill +2", 5, FeatType.CHANNEL, short="Channel skill"),
            Ability("Connection power", 6, FeatType.CPOWER), # argument of 2
            Ability("Connection spell", 7, FeatType.SPELL), # argument of 2
            Ability("Channel skill +3", 8, FeatType.CHANNEL, short="Channel skill"),
            Ability("Connection power", 9, FeatType.CPOWER), # argument of 3
            Ability("Connection spell", 10, FeatType.SPELL), # argument of 3
            Ability("Channel skill +4", 11, FeatType.CHANNEL, short="Channel skill"),
            Ability("Telepathic bond", 11, FeatType.WORDS),
            Ability("Connection power", 12, FeatType.CPOWER), # argument of 4
            Ability("Connection spell", 13, FeatType.SPELL), # argument of 4
            Ability("Channel skill +5", 14, FeatType.CHANNEL, short="Channel skill"),
            Ability("Connection power", 15, FeatType.CPOWER), # argument of 5
            Ability("Connection spell", 16, FeatType.SPELL), # argument of 5
            Ability("Channel skill +6", 17, FeatType.CHANNEL, short="Channel skill"),
            Ability("Connection power", 18, FeatType.CPOWER), # argument of 6
            Ability("Transcendence", 19, FeatType.WORDS),
            Ability("Channel skill +7", 20, FeatType.CHANNEL, short="Channel skill"),
            Ability("Enlightenment", 20, FeatType.WORDS)
        ]
        return levelups

    def select_connection(self, connection : str):
        """function that sets the connection

        Args:
            connection (str): new connection
        """
        self.connection = connection

    def possible_connections(self) -> list:
        """function that gives every possible connection

        Returns:
            list: list of possible connections
        """
        connections = [
            "Akashic", "Empath", "Healer", "Mindbreaker", "Overlord", "Star Shaman", "Xenodruid"
        ]
        return connections

    def connection_spell(self) -> list:
        """function to return the chosen connections spells

        Returns:
            list: list of connection spells
        """
        spell_dict = {
            "Akashic" : ["Identify", "Augury", "Tongues", "Divination", "Contact Other Plane",
                           "Vision"],

            "Empath" :  ["Detect Thoughts", "Zone of Truth", "Clairaudience/Clairvoyance",
                           "Mind Probe", "Telepathy", "True Seeing"],

            "Healer" : ["ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR"],

            "Mindbreaker" : ["ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR"],

            "Overlord" : ["Command", "Hold Person", "Suggestion", "Confusion", "Dominate Person",
                           "Mass Suggestion"],

            "Star Shaman" : ["Shooting Stars", "Darkvision", "Irradiate", "Remove Radioactivity",
                           "Telekinesis", "Control Gravity"],

            "Xenodruid" : ["Life Bubble", "Fog Cloud", "Entropic Grasp", "Reincarnate",
                           "Commune with Nature", "Terraform"]
        }

        return spell_dict[self.connection]

    def connection_skill(self) -> list:
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
        return skill_dict[self.connection]

    def connection_feat(self) -> list:
        """function to return the feats of the selected connection

        Returns:
            list: list of the feats from the connection
        """
        feat_dict = {
            "Akashic" : [["Akashic Knowledge"],
                         ["Access Akashic Record"],
                         ["Peer into the Future"],
                         ["Mind Probe"],
                         ["Telepathic Memories"],
                         ["Memory Palace"],
                         ["Glean Spell"]],

            "Empath" : [["Empathy"],
                        ["Greater Mindlink"],
                        ["Emotionsense"],
                        ["Discern Lies"],
                        ["Greater Emotionsense"],
                        ["Retrocognition"],
                        ["Empathic Mastery"]],

            "Healer" : [["Healing Channel"],
                        ["Lifelink"],
                        ["Healer's Bond"],
                        ["Steal Life"],
                        ["Channel Bond"],
                        ["Channel Life"],
                        ["Deny Death"]],

            "Mindbreaker" : [["Share Pain"],
                             ["Backlash"],
                             ["Sow Doubt"],
                             ["Mental Anguish"],
                             ["Mindbreaking Link"],
                             ["Mindkiller"],
                             ["Explode Head"]],

            "Overlord" :  [["Inexplicable Commands"],
                           ["Forced Amity"],
                           ["Echoes of Obedience"],
                           ["Greater Forced Amity"],
                           ["Jealous Overlord"],
                           ["Forceful Commands"],
                           ["Absolute Control"]],

            "Star Shaman" : [["Walk the Void"],
                             ["Starlight Form"],
                             ["Stargazer"],
                             ["Starflight"],
                             ["Starry Bond"],
                             ["Meteor Shower"],
                             ["Interplanetary Teleport"]],

            "Xenodruid" : [["Speak with Animals"],
                           ["Grasping Vines"],
                           ["Animal Adaptation"],
                           ["Reactive Resistance"],
                           ["Share Resistance"],
                           ["Plant Transport"],
                           ["Guided Rebirth"]]
        }
        return feat_dict[self.connection]
