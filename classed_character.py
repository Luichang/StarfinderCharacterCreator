from copy import deepcopy

from helpers.feats import feats
from helpers.helper import get_user_response, write_to_file
from helpers.spells import spells
from helpers.starfinder_class_dicts import (classAbilities, classChoseFeats,
                                            classesStatBonus, classesStatFocus)
from helpers.starfinder_dicts import (attribute_shortener, attribute_shorthand,
                                      possible_attributes, skills,
                                      spells_bonus, spells_day, spells_known)
from helpers.starfinder_html_dict import htmlTags
from helpers.starfinder_race_dicts import raceAbilities, raceStatList
from helpers.starfinder_theme_dicts import themeAbilities, themes
from starfinder_classes.starfinder_class import StarfinderClass
from starfinder_feats.starfinder_feat_type import FeatType



class Character:
    """This class is to create a starfinder character
    """
    def __init__(self, file_name="", gui=False):

        self.name = ""
        self.spell_level = -1

        self.list_class_abilities = []
        self.chosen_feats = []
        self.class_feats = []
        self.styles = [] # this is soldier, mystic, and operative exclusive
        self.spells = [[], [], [], [], [], [], []]
        self.additional_spells = [[], [], [], [], [], [], []]
        # for spells provided outside of class level up
        self.expertise = []

        self.mods = {
            "str" : 0,
            "dex" : 0,
            "con" : 0,
            "int" : 0,
            "wis" : 0,
            "cha" : 0
        }

        self.attributes = {
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10
        }

        self.ability_increases = {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0
        }

        self.skills = deepcopy(skills)

        self.skill_ranks = deepcopy(skills)

        self.skill_class = deepcopy(skills)

        self.skill_misc = deepcopy(skills)

        self.skill_dabbler = deepcopy(skills)

        self.spent_points = {"strength" : 0, "dexterity" : 0, "constitution" : 0,
                            "intelligence" : 0, "wisdom": 0, "charisma" : 0}
        self.theme_attributes = themes["themeless"]
        self.race_attributes = raceStatList["human"]

        self.class_level = 5

        self.theme = ""
        self.race_name = ""
        self.class_name = ""

        self.stamina_points = 0
        self.hit_points = 0
        self.resolve_points = 0

        self.fort_save_misc = 0
        self.reflex_save_misc = 0
        self.will_save_misc = 0

        self.melee_misc = 0
        self.range_misc = 0
        self.throw_misc = 0

        self.profession_ability = "wis"
        self.profession2_ability = "wis"

        self.key = "Str"
        self.eac = 0
        self.kac = 0
        self.vs_combat = 0

        self.initiative = 0

        self.fort_save = 0
        self.reflex_save = 0
        self.will_save = 0

        self.melee = 0
        self.range = 0
        self.throw = 0

        self.initiative_misc = 0

        if not gui:
            if file_name == "":
                self.create_new()

    def create_new(self):
        """create a new character
        """
        # entered = get_user_response([""], "Enter a Character Name", False)
        # self.set_name(entered)

        # response_text = "Please chose a race, options are: android, human, kasatha, " +\
        #                 "lashunta(korasha), lashunta(damaya), shirren, vesk, ysoki"
        # entered = get_user_response(["android", "human", "kasatha", "lashunta(korasha)",
        #                                  "lashunta(damaya)", "shirren", "vesk", "ysoki"],
        #                                  response_text
        #                                 )
        # self.set_race(entered)

        # response_text = 'Chose a theme. Possible themes are: "ace pilot, bounty hunter, icon, ' +\
        #                 'mercenary, outlaw, priest, scholar, spacefarer, xenoseeker, themeless'
        # entered = get_user_response(["ace pilot", "bounty hunter", "icon", "mercenary",
        #                                 "outlaw", "priest", "scholar", "spacefarer",
        #                                 "xenoseeker", "themeless"], response_text
        #                               )

        # self.set_theme(entered)

        response_text = "Chose a Class. Possible Classes are: envoy, mechanic, mystic, " +\
                        "operative, solarian, soldier, technomancer"
        entered = get_user_response(["envoy", "mechanic", "mystic", "operative", "solarian",
                                        "soldier", "technomancer"], response_text
                                      )
        self.class_name = StarfinderClass.create(entered)
        if str(self.class_name) in ["Soldier [str]", "Soldier [dex]"]:
            response_text = "Soldier has to chose the key ability. Possible are str and dex"
            key = get_user_response(["str", "dex"], response_text)
            self.class_name.select_key(key)

        # self.calc_spell_level()

        # self.point_buy()

        # self.calc_attribut_mod()

        # self.calc_init()

        # self.calc_armor_class()

        # self.calc_hit_points()

        # self.calc_save()

        # self.calc_attack()

        # self.add_skill_points()

        self.feats_and_abilities()

        # self.add_spells()

    def add_spells(self, gui : bool=False) -> None:
        """add spells to the character
        """
        if self.class_name in ["mystic", "technomancer"]:
            list_of_pickable_spells = [[], [], [], [], [], [], []]
            for i in range(7):
                if spells_known[self.class_level - 1][i] > 0:
                    list_of_pickable_spells[i] += spells[self.class_name][i]

            for i in range(7):
                for spell in self.spells[i]:
                    if spell in list_of_pickable_spells[i]:
                        list_of_pickable_spells[i].remove(spell)
                for spell in self.additional_spells[i]:
                    if spell in list_of_pickable_spells[i]:
                        list_of_pickable_spells[i].remove(spell)

            if gui:
                return list_of_pickable_spells

            if self.class_level > 1:
                for i in range(7):
                    if spells_known[self.class_level - 1][i] - \
                        spells_known[self.class_level - 2][i] == 0:
                        list_of_pickable_spells[i] = []

            for i in range(7):
                if list_of_pickable_spells[i] != []:
                    num_to_add = spells_known[self.class_level - 1][i]
                    if self.class_level > 1:
                        num_to_add -= spells_known[self.class_level - 2][i]
                    for _ in range(num_to_add):
                        print_text = f"please enter spell name of level {i} to add. "+\
                                      "Possible spells are: " +\
                                      ", ".join(list_of_pickable_spells[i])
                        entered = get_user_response([x.lower() for x in \
                                                        list_of_pickable_spells[i]], print_text)
                        entered = entered.title()
                        list_of_pickable_spells[i].remove(entered)
                        self.spells[i].append(entered)
        return None

    def feats_and_abilities(self) -> None:
        """do something with the feats and abilities
        """

        # TODO copy from character the race and theme feats

        for ability in self.class_name.current_abilities(self.class_level):
            # add ability to list_class_abilities
            if ability.get_type() in [FeatType.REPLACABLE, FeatType.CHANNEL, FeatType.EDGE, FeatType.INFLUENCE, FeatType.SKILLS]:
                result = [oldAbility for oldAbility in self.list_class_abilities \
                            if ability.short in oldAbility]
                if len(result) != 0:
                    result = result[0]
                    result = self.list_class_abilities.index(result)
                    self.list_class_abilities[result] = str(ability)
                else:
                    self.list_class_abilities.append(str(ability))
            else:
                self.list_class_abilities.append(str(ability))

            # perform ability logic
            if ability.get_type() == FeatType.CHOOSE:
                self.select_new_class_feat()

        print(self.list_class_abilities)
        self.calc_skills()

    def select_new_class_feat(self, verbose : bool=True) -> list:
        """Adds a new feature based on the entered featType and level. Should verbose be set to
           False the list of options is returned

        Args:
            verbose (bool, optional): If this function is called in terminal it prompts the user
                                      to enter a response, otherwise it returns all possibilities.
                                      Defaults to True.

        Returns:
            list : list of class feats that can be selected
        """
        possible_class_feats = self.class_name.list_of_choosables(self.class_level)
                
        for feat in self.class_feats:
            if feat in possible_class_feats:
                possible_class_feats.remove(feat)
        if verbose:
            print_text = "please enter class feat name you would like to add. " +\
                         "Possible feats are: " + ", ".join(possible_class_feats)
            lower_class_feats = [x.lower() for x in possible_class_feats]
            entered = get_user_response(lower_class_feats, print_text)
            entered_feat_index = lower_class_feats.index(entered)
            self.class_feats.append(possible_class_feats[entered_feat_index])
        return possible_class_feats

    def calc_skills(self) -> list:
        """calculate the total of every skill

        Returns:
            list: list of objects to be printed to the HTML file
        """
        self.skills = {
            "acrobatics"       : self.mods["dex"],
            "athletics"        : self.mods["str"],
            "bluff"            : self.mods["cha"],
            "computers"        : self.mods["int"],
            "culture"          : self.mods["int"],
            "diplomacy"        : self.mods["cha"],
            "disguise"         : self.mods["cha"],
            "engineering"      : self.mods["int"],
            "intimidate"       : self.mods["cha"],
            "life science"     : self.mods["int"],
            "medicine"         : self.mods["int"],
            "mysticism"        : self.mods["wis"],
            "perception"       : self.mods["wis"],
            "physical science" : self.mods["int"],
            "piloting"         : self.mods["dex"],
            "profession"       : self.mods[self.profession_ability],
            "profession2"      : self.mods[self.profession2_ability],
            "sense motive"     : self.mods["wis"],
            "sleight of hand"  : self.mods["dex"],
            "stealth"          : self.mods["dex"],
            "survival"         : self.mods["wis"],
        }
        for skill in self.skills:
            if self.skill_ranks[skill] > 0 or self.skill_dabbler[skill] > 0:
                self.skills[skill] += self.skill_ranks[skill] + self.skill_class[skill] +\
                                    self.skill_misc[skill] + self.skill_dabbler[skill]
            else:
                self.skills[skill] = 0

    def add_skill_points(self) -> None:
        """add points to skills, only used in terminal use
        """
        skillpoints = classesStatBonus[self.class_name]["skills"] + self.mods["int"]
        possible_skill = ["acrobatics", "athletics", "bluff", "computers", "culture", "diplomacy",
                         "disguise", "engineering", "intimidate", "life science", "medicine",
                         "mysticism", "perception", "physical science", "profession1",
                         "profession2", "piloting", "sense motive", "sleight of hand", "stealth",
                         "survival"]

        while skillpoints > 0:
            response_text = "please enter skill name to add a point to. Possible skills are: " +\
                            ", ".join(possible_skill)
            entered = get_user_response(possible_skill, response_text)
            possible_skill.remove(entered)
            self.skill_ranks[entered] += 1
            skillpoints -= 1

    def calc_attack(self) -> None:
        """calculates the base attack values
        """
        self.melee = self.class_name.bab[self.class_level - 1] +\
                     self.mods["str"] + self.melee_misc
        self.range = self.class_name.bab[self.class_level - 1] +\
                     self.mods["dex"] + self.range_misc
        self.throw = self.class_name.bab[self.class_level - 1] +\
                     self.mods["str"] + self.throw_misc

    def calc_save(self) -> None:
        """calculate the values of the saving throw bases
        """
        self.fort_save = self.class_name.fort[self.class_level - 1] +\
                         self.mods["con"] + self.fort_save_misc
        self.reflex_save = self.class_name.reflex[self.class_level - 1] +\
                          self.mods["dex"] + self.reflex_save_misc
        self.will_save = self.class_name.will[self.class_level - 1] +\
                          self.mods["wis"] + self.will_save_misc

    def calc_hit_points(self) -> None:
        """calculates the current HP, SP, and RP
        """
        self.stamina_points = max(1, (max(0, self.class_name.sp +\
                                             self.mods["con"])) * self.class_level)
        self.hit_points = max(1, (self.class_name.hp * self.class_level) +\
                             raceStatList[self.race_name.split()[0]]["hp"])
        self.resolve_points = max(1, max(1, self.class_level // 2) + self.mods[self.key])

    def calc_armor_class(self) -> None:
        """calculate the armor classes
        """
        self.eac = 10 + 0 + self.mods["dex"] + 0
        self.kac = 10 + 0 + self.mods["dex"] + 0
        self.vs_combat = 8 + self.kac

    def calc_init(self) -> None:
        """calculate the initiative values
        """
        self.initiative = self.mods["dex"] + self.initiative_misc

    def calc_attribut_mod(self) -> None:
        """calculate the attribute modifiers
        """
        self.mods["str"] = ((self.attributes["strength"] // 2) - 5)
        self.mods["dex"] = ((self.attributes["dexterity"] // 2) - 5)
        self.mods["con"] = ((self.attributes["constitution"] // 2) - 5)
        self.mods["int"] = ((self.attributes["intelligence"] // 2) - 5)
        self.mods["wis"] = ((self.attributes["wisdom"] // 2) - 5)
        self.mods["cha"] = ((self.attributes["charisma"] // 2) - 5)

    def point_buy(self):
        """function to perform the poiont buy action
        """
        spendable_points = 10

        while spendable_points > 0:
            response_text = f"You have {spendable_points} points left to spend. Chose one from " +\
                            "(str)ength, (dex)terity, (con)stitution, (int)elligence, (wis)dom, "+\
                            "(cha)risma"
            entered = get_user_response(possible_attributes, response_text)
            if self.attributes[attribute_shorthand[entered]] == 18:
                print_text = f"Sorry try again {attribute_shorthand[entered]} is already at 18 " +\
                             "which is the maximum when setting up a character"
                print(print_text)
                continue
            curr_attr = attribute_shorthand[entered]
            self.attributes[curr_attr] += 1
            self.spent_points[attribute_shorthand[curr_attr]] += 1

            spendable_points -= 1

    def calc_attributes(self) -> None:
        """calculate the attribute values of every attribute
        """
        for attribute in self.attributes:
            self.attributes[attribute] = 10 + self.race_attributes[attribute] +\
                                          self.theme_attributes[attribute] +\
                                          self.spent_points[attribute]
            for _ in range(self.ability_increases[attribute]):
                self.attributes[attribute] += 1
                if self.attributes[attribute] < 18:
                    self.attributes[attribute] += 1

        self.calc_attribut_mod()

    def calc_spell_level(self):
        """function to update the spell_level of the character
        """
        if self.class_name in ["mystic", "technomancer"] or (self.theme == "priest" and self.class_level >= 12):
            self.spell_level = self.class_level
        else:
            self.spell_level = -1
