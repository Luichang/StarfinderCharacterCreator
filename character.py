from copy import deepcopy

from bs4 import BeautifulSoup

from feats import feats
from spells import spells
from starfinder_dicts import possible_attributes, attribute_shorthand, attribute_shortener, \
                             spells_known, spells_day, spells_bonus, skills
from starfinder_html_dict import htmlTags
from starfinder_race_dicts import raceAbilities, raceStatList
from starfinder_theme_dicts import themes, themeAbilities
from starfinder_class_dicts import classesStatFocus, classChoseFeats, classAbilities, \
                                   classesStatBonus


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

        self.class_level = 1

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
            else:
                self.read_from_html(file_name)


    def set_name(self, name):
        """Sets the name of the character

        Args:
            name (str): Character Name
        """
        self.name = name

    def add_attribute(self, text):
        """Add a new attribute to the character

        Args:
            text (str): Input Text

        Returns:
            string: chosen value
        """
        entered = self.get_user_response(possible_attributes, text)
        return entered

    def set_race(self, race, attr=None):
        """Sets the race of the character

        Args:
            race (str): Race of the character
            attr (str, optional): chosen attribute of human. Defaults to None.
        """
        self.race_name = race
        self.race_attributes = deepcopy(raceStatList[self.race_name])

        if self.race_name == "human":
            if attr is None:
                attr_text = "Humans get to increase one stat by 2. Possible attributes: " +\
                            "(str)ength, (dex)terity, (con)stitution, (int)elligence, (wis)dom, " +\
                            "(cha)risma"
                attr = self.add_attribute(attr_text)

            attribute = attribute_shorthand[attr]
            self.race_attributes[attribute] = 2

            self.race_name += " (" + attribute_shortener[attribute] + ")"
        self.calc_attributes()


    def set_theme(self, theme, attr=None):
        """Sets the character Theme

        Args:
            theme (str): Theme of the character
            attr (str, optional): chosen attribute of themeless. Defaults to None.
        """
        self.theme = theme
        self.theme_attributes = themes[self.theme]

        if self.theme == "themeless":
            if attr is None:
                attr_text = "Themeless get to increase one stat by 1. Possible attributes: " +\
                            "(str)ength, (dex)terity, (con)stitution, (int)elligence, (wis)dom, "+\
                            "(cha)risma"
                attr = self.add_attribute(attr_text)

            attribute = attribute_shorthand[attr]
            self.theme_attributes[attribute] = 1
            self.theme += " (" + attribute_shortener[attribute] + ")"
        self.calc_attributes()

    def calc_attributes(self):
        """calculate the attribute values of every attribute
        """
        self.attributes["strength"]     = 10 + self.race_attributes["strength"]     +\
                                          self.theme_attributes["strength"]         +\
                                          self.spent_points["strength"]

        self.attributes["dexterity"]    = 10 + self.race_attributes["dexterity"]    +\
                                          self.theme_attributes["dexterity"]        +\
                                          self.spent_points["dexterity"]

        self.attributes["constitution"] = 10 + self.race_attributes["constitution"] +\
                                          self.theme_attributes["constitution"]     +\
                                          self.spent_points["constitution"]

        self.attributes["intelligence"] = 10 + self.race_attributes["intelligence"] +\
                                          self.theme_attributes["intelligence"]     +\
                                          self.spent_points["intelligence"]

        self.attributes["wisdom"]       = 10 + self.race_attributes["wisdom"]       +\
                                          self.theme_attributes["wisdom"]           +\
                                          self.spent_points["wisdom"]

        self.attributes["charisma"]     = 10 + self.race_attributes["charisma"]     +\
                                          self.theme_attributes["charisma"]         +\
                                          self.spent_points["charisma"]
        self.calc_attribut_mod()

    def set_class_name(self, name, key=None):
        """Sets the character class

        Args:
            name (str): Class Name
            key (str, optional): Used for Soldier, can either be Str or Dex. Defaults to None.

        Returns:
            str: name of the class
        """
        self.class_name = name
        class_name = self.class_name
        if self.class_name == "soldier":
            if key is None:
                response_text = "Soldier has to chose the key ability. Possible are str and dex"
                key = self.get_user_response(["str", "dex"], response_text)
            self.key = key
        else:
            self.key = classesStatBonus[self.class_name]["key"]

        for skill in classesStatBonus[self.class_name]["classBonus"]:
            self.skill_class[skill] = classesStatBonus[self.class_name]["classBonus"][skill]
        return class_name

    def calc_armor_class(self):
        """calculate the armor classes
        """
        self.eac = 10 + 0 + self.mods["dex"] + 0
        self.kac = 10 + 0 + self.mods["dex"] + 0
        self.vs_combat = 8 + self.kac

    def calc_init(self):
        """calculate the initiative values
        """
        self.initiative = self.mods["dex"] + self.initiative_misc

    def create_new(self):
        """create a new character
        """
        entered = self.get_user_response([""], "Enter a Character Name", False)
        self.set_name(entered)

        self.write_to_file(htmlTags["name"], self.name.title())

        response_text = "Please chose a race, options are: android, human, kasatha, " +\
                        "lashunta(korasha), lashunta(damaya), shirren, vesk, ysoki"
        entered = self.get_user_response(["android", "human", "kasatha", "lashunta(korasha)",
                                         "lashunta(damaya)", "shirren", "vesk", "ysoki"],
                                         response_text
                                        )
        self.set_race(entered)

        list_to_write_to_file = []
        list_to_write_to_file.append([htmlTags["race"], self.race_name.title()])
        list_to_write_to_file.append([htmlTags["raceStr"], self.race_attributes["strength"]])
        list_to_write_to_file.append([htmlTags["raceDex"], self.race_attributes["dexterity"]])
        list_to_write_to_file.append([htmlTags["raceCon"], self.race_attributes["constitution"]])
        list_to_write_to_file.append([htmlTags["raceInt"], self.race_attributes["intelligence"]])
        list_to_write_to_file.append([htmlTags["raceWis"], self.race_attributes["wisdom"]])
        list_to_write_to_file.append([htmlTags["raceCha"], self.race_attributes["charisma"]])

        self.write_to_file("listPass", list_to_write_to_file)


        response_text = 'Chose a theme. Possible themes are: "ace pilot, bounty hunter, icon, ' +\
                        'mercenary, outlaw, priest, scholar, spacefarer, xenoseeker, themeless'
        entered = self.get_user_response(["ace pilot", "bounty hunter", "icon", "mercenary",
                                        "outlaw", "priest", "scholar", "spacefarer",
                                        "xenoseeker", "themeless"],
                                      )

        self.set_theme(entered)
        self.write_to_file(htmlTags["theme"], self.theme.title())

        list_to_write_to_file = []
        list_to_write_to_file.append([htmlTags["themeStr"], self.theme_attributes["strength"]])
        list_to_write_to_file.append([htmlTags["themeDex"], self.theme_attributes["dexterity"]])
        list_to_write_to_file.append([htmlTags["themeCon"], self.theme_attributes["constitution"]])
        list_to_write_to_file.append([htmlTags["themeInt"], self.theme_attributes["intelligence"]])
        list_to_write_to_file.append([htmlTags["themeWis"], self.theme_attributes["wisdom"]])
        list_to_write_to_file.append([htmlTags["themeCha"], self.theme_attributes["charisma"]])

        list_to_write_to_file.append([htmlTags["attrStr"], self.attributes["strength"]])
        list_to_write_to_file.append([htmlTags["attrDex"], self.attributes["dexterity"]])
        list_to_write_to_file.append([htmlTags["attrCon"], self.attributes["constitution"]])
        list_to_write_to_file.append([htmlTags["attrInt"], self.attributes["intelligence"]])
        list_to_write_to_file.append([htmlTags["attrWis"], self.attributes["wisdom"]])
        list_to_write_to_file.append([htmlTags["attrCha"], self.attributes["charisma"]])

        list_to_write_to_file.append([htmlTags["abilityStr"], self.ability_increases["strength"]])
        list_to_write_to_file.append([htmlTags["abilityDex"], self.ability_increases["dexterity"]])
        list_to_write_to_file.append([htmlTags["abilityCon"],
                                        self.ability_increases["constitution"]])
        list_to_write_to_file.append([htmlTags["abilityInt"],
                                        self.ability_increases["intelligence"]])
        list_to_write_to_file.append([htmlTags["abilityWis"], self.ability_increases["wisdom"]])
        list_to_write_to_file.append([htmlTags["abilityCha"], self.ability_increases["charisma"]])

        self.write_to_file("listPass", list_to_write_to_file)

        list_to_write_to_file = []

        response_text = "Chose a Class. Possible Classes are: envoy, mechanic, mystic, " +\
                        "operative, solarian, soldier, technomancer"
        entered = self.get_user_response(["envoy", "mechanic", "mystic", "operative", "solarian",
                                        "soldier", "technomancer"], response_text
                                      )

        class_name = self.set_class_name(entered).capitalize()
        if self.class_name == "Soldier":
            class_name += " [" + str(self.key) + "]"
        class_name += " (" + str(self.class_level) + ")"

        list_to_write_to_file.append([htmlTags["className"], class_name])

        for skill in classesStatBonus[self.class_name]["classBonus"]:
            list_to_write_to_file.append([htmlTags[skill + "Class"], self.skill_class[skill]])

        for feat in classesStatBonus[self.class_name]["proficiencies"]:
            self.chosen_feats.append(feat)

        print("Currently only point buy system is implemented, if you want to use another system"+\
              "figure out the conversion yourself.")
        print(f"{self.class_name} tend to want more points in {classesStatFocus[self.class_name]}")

        spendable_points = 10

        list_to_write_to_file.append([htmlTags["attrStrPoint"], 0])
        list_to_write_to_file.append([htmlTags["attrDexPoint"], 0])
        list_to_write_to_file.append([htmlTags["attrConPoint"], 0])
        list_to_write_to_file.append([htmlTags["attrIntPoint"], 0])
        list_to_write_to_file.append([htmlTags["attrWisPoint"], 0])
        list_to_write_to_file.append([htmlTags["attrChaPoint"], 0])
        self.write_to_file("listPass", list_to_write_to_file)

        while spendable_points > 0:
            response_text = f"You have {spendable_points} points left to spend. Chose one from " +\
                            "(str)ength, (dex)terity, (con)stitution, (int)elligence, (wis)dom, "+\
                            "(cha)risma"
            entered = self.get_user_response(possible_attributes,
                                           )
            if self.attributes[attribute_shorthand[entered]] == 18:
                print_text = f"Sorry try again {attribute_shorthand[entered]} is already at 18 " +\
                             "which is the maximum when setting up a character"
                print(print_text)
                continue
            curr_attr = attribute_shorthand[entered]
            self.attributes[curr_attr] += 1
            self.spent_points[attribute_shorthand[curr_attr]] += 1

            self.write_to_file(htmlTags["attr" + attribute_shortener[curr_attr] + "Point"],
                             self.spent_points[attribute_shorthand[curr_attr]])

            spendable_points -= 1

            list_to_write_to_file = []
            list_to_write_to_file.append([htmlTags["attrStr"], self.attributes["strength"]])
            list_to_write_to_file.append([htmlTags["attrDex"], self.attributes["dexterity"]])
            list_to_write_to_file.append([htmlTags["attrCon"], self.attributes["constitution"]])
            list_to_write_to_file.append([htmlTags["attrInt"], self.attributes["intelligence"]])
            list_to_write_to_file.append([htmlTags["attrWis"], self.attributes["wisdom"]])
            list_to_write_to_file.append([htmlTags["attrCha"], self.attributes["charisma"]])
            self.write_to_file("listPass", list_to_write_to_file)

        self.calc_attribut_mod()

        list_to_write_to_file.append([htmlTags["attrStrMod"], self.mods["str"]])
        list_to_write_to_file.append([htmlTags["attrDexMod"], self.mods["dex"]])
        list_to_write_to_file.append([htmlTags["attrConMod"], self.mods["con"]])
        list_to_write_to_file.append([htmlTags["attrIntMod"], self.mods["int"]])
        list_to_write_to_file.append([htmlTags["attrWisMod"], self.mods["wis"]])
        list_to_write_to_file.append([htmlTags["attrChaMod"], self.mods["cha"]])

        self.calc_init()

        list_to_write_to_file.append([htmlTags["init_total"], self.initiative])
        list_to_write_to_file.append([htmlTags["init_dex"], self.mods["dex"]])
        list_to_write_to_file.append([htmlTags["init_misc"], self.initiative_misc])

        self.calc_armor_class()

        list_to_write_to_file.append([htmlTags["eac"], self.eac])
        list_to_write_to_file.append([htmlTags["eac_armor"], 0])
        list_to_write_to_file.append([htmlTags["eac_dex"], self.mods["dex"]])
        list_to_write_to_file.append([htmlTags["eac_misc"], 0])

        list_to_write_to_file.append([htmlTags["kac"], self.kac])
        list_to_write_to_file.append([htmlTags["kac_armor"], 0])
        list_to_write_to_file.append([htmlTags["kac_dex"], self.mods["dex"]])
        list_to_write_to_file.append([htmlTags["kac_misc"], 0])

        list_to_write_to_file.append([htmlTags["vsCombat"], self.vs_combat])

        self.calc_hit_points()

        list_to_write_to_file.append([htmlTags["sp"], self.stamina_points])
        list_to_write_to_file.append([htmlTags["hp"], self.hit_points])
        list_to_write_to_file.append([htmlTags["rp"], self.resolve_points])

        self.calc_save()
        list_to_write_to_file += self.print_save()

        self.calc_attack()
        list_to_write_to_file += self.print_attack()

        list_to_write_to_file.append([htmlTags["spendablePoints"], 0])
        list_to_write_to_file.append([htmlTags["perLevelPoints"],
                                 classesStatBonus[self.class_name]["skills"] + self.mods["int"]])

        self.write_to_file("listPass", list_to_write_to_file)

        self.add_skill_points()

        list_to_write_to_file = self.calc_skills()
        self.write_to_file("listPass", list_to_write_to_file)
        self.feats_and_abilities()

        self.add_spells()

    def calc_save(self):
        """calculate the values of the saving throw bases
        """
        self.fort_save = classesStatBonus[self.class_name]["fort"][self.class_level - 1] +\
                         self.mods["con"] + self.fort_save_misc
        self.reflex_save = classesStatBonus[self.class_name]["reflex"][self.class_level - 1] +\
                          self.mods["dex"] + self.reflex_save_misc
        self.will_save = classesStatBonus[self.class_name]["will"][self.class_level - 1] +\
                          self.mods["wis"] + self.will_save_misc

    def print_save(self):
        """Print the values of the saves into the HTML file

        Returns:
            list: list of objects to be printed
        """
        list_to_write_to_file = []
        list_to_write_to_file.append([htmlTags["fortSave"], self.fort_save])
        list_to_write_to_file.append([htmlTags["reflexSave"], self.reflex_save])
        list_to_write_to_file.append([htmlTags["willSave"], self.will_save])

        list_to_write_to_file.append([htmlTags["fortSaveBase"],
                                 classesStatBonus[self.class_name]["fort"][self.class_level - 1]])
        list_to_write_to_file.append([htmlTags["reflexSaveBase"],
                                 classesStatBonus[self.class_name]["reflex"][self.class_level - 1]])
        list_to_write_to_file.append([htmlTags["willSaveBase"],
                                 classesStatBonus[self.class_name]["will"][self.class_level - 1]])

        list_to_write_to_file.append([htmlTags["fortSaveAbility"], self.mods["con"]])
        list_to_write_to_file.append([htmlTags["reflexSaveAbility"], self.mods["dex"]])
        list_to_write_to_file.append([htmlTags["willSaveAbility"], self.mods["wis"]])

        list_to_write_to_file.append([htmlTags["fortSaveMisc"], self.fort_save_misc])
        list_to_write_to_file.append([htmlTags["reflexSaveMisc"], self.reflex_save_misc])
        list_to_write_to_file.append([htmlTags["willSaveMisc"], self.will_save_misc])
        return list_to_write_to_file

    def calc_attack(self):
        """calculates the base attack values
        """
        self.melee = classesStatBonus[self.class_name]["bab"][self.class_level - 1] +\
                     self.mods["str"] + self.melee_misc
        self.range = classesStatBonus[self.class_name]["bab"][self.class_level - 1] +\
                     self.mods["dex"] + self.range_misc
        self.throw = classesStatBonus[self.class_name]["bab"][self.class_level - 1] +\
                     self.mods["str"] + self.throw_misc

    def print_attack(self):
        """prints the attack values to the HTML file

        Returns:
            list: list of objects to be added to the HTML
        """
        list_to_write_to_file = []
        list_to_write_to_file.append([htmlTags["melee"], self.melee])
        list_to_write_to_file.append([htmlTags["melee_bab"],
                                  classesStatBonus[self.class_name]["bab"][self.class_level - 1]])
        list_to_write_to_file.append([htmlTags["melee_ability"], self.mods["str"]])
        list_to_write_to_file.append([htmlTags["melee_misc"], self.melee_misc])

        list_to_write_to_file.append([htmlTags["range"], self.range])
        list_to_write_to_file.append([htmlTags["range_bab"],
                                  classesStatBonus[self.class_name]["bab"][self.class_level - 1]])
        list_to_write_to_file.append([htmlTags["range_ability"], self.mods["dex"]])
        list_to_write_to_file.append([htmlTags["range_misc"], self.range_misc])

        list_to_write_to_file.append([htmlTags["throw"], self.throw])
        list_to_write_to_file.append([htmlTags["throw_bab"],
                                  classesStatBonus[self.class_name]["bab"][self.class_level - 1]])
        list_to_write_to_file.append([htmlTags["throw_ability"], self.mods["str"]])
        list_to_write_to_file.append([htmlTags["throw_misc"], self.throw_misc])
        return list_to_write_to_file

    def print_spells(self):
        """create list to print spells to the HTML file

        Returns:
            list: list of objects to print to the HTML file
        """
        list_to_write_to_file = []
        spell_boxes = [
            ["spell001", "spell002", "spell003", "spell004", "spell005", "spell006", "spell007",
             "spell008"],
            ["spell101", "spell102", "spell103", "spell104", "spell105", "spell106", "spell107",
             "spell108"],
            ["spell201", "spell202", "spell203", "spell204", "spell205", "spell206", "spell207"],
            ["spell301", "spell302", "spell303", "spell304", "spell305", "spell306", "spell307"],
            ["spell401", "spell402", "spell403", "spell404", "spell405", "spell406", "spell407"],
            ["spell501", "spell502", "spell503", "spell504", "spell505", "spell506"],
            ["spell601", "spell602", "spell603", "spell604", "spell605", "spell606"]
        ]
        for i in range(7):
            full_spell_list = self.spells[i] + self.additional_spells[i]
            for j, full_spell in enumerate(full_spell_list):
                list_to_write_to_file.append([htmlTags[spell_boxes[i][j]], full_spell])
        return list_to_write_to_file

    def print_spell_numbers(self):
        """generate list to print spells to HTML

        Returns:
            list: list of objects to be printed to the HTML file
        """
        spell_word_boxes = [["spell0known"], ["spell1known", "spell1day"],
                          ["spell2known", "spell2day"], ["spell3known", "spell3day"],
                          ["spell4known", "spell4day"], ["spell5known", "spell5day"],
                          ["spell6known", "spell6day"]]

        list_to_write_to_file = []
        if self.class_name == "technomancer" or self.class_name == "mystic":
            self.spell_level = self.class_level

            bonus_list = []
            for bonus in spells_bonus:
                if bonus[0] > self.attributes[attribute_shorthand[self.key]]:
                    break
                bonus_list = bonus[1:]

            for i in range(7):
                list_to_write_to_file.append([htmlTags[spell_word_boxes[i][0]],
                                          spells_known[self.class_level - 1][i]])
                if len(spell_word_boxes[i]) > 1:
                    per_day = spells_day[self.class_level - 1][i - 1] + bonus_list[i]
                    list_to_write_to_file.append([htmlTags[spell_word_boxes[i][1]], per_day])
        else:
            for i in range(7):
                list_to_write_to_file.append([htmlTags[spell_word_boxes[i][0]], 0])
                if len(spell_word_boxes[i]) > 1:
                    per_day = 0
                    list_to_write_to_file.append([htmlTags[spell_word_boxes[i][1]], per_day])
        return list_to_write_to_file


    def add_spells(self):
        """add spells to the character
        """
        list_to_write_to_file = []
        if self.class_name == "technomancer" or self.class_name == "mystic":
            list_of_pickable_spells = [[], [], [], [], [], [], []]
            for i in range(7):
                if spells_known[self.class_level - 1][i] > 0:
                    list_of_pickable_spells[i] += spells[self.class_name][i]

            if self.class_level > 1:
                for i in range(7):
                    if spells_known[self.class_level - 1][i] - \
                        spells_known[self.class_level - 2][i] == 0:
                        list_of_pickable_spells[i] = []

            for i in range(7):
                for spell in self.spells[i]:
                    if spell in list_of_pickable_spells[i]:
                        list_of_pickable_spells[i].remove(spell)

            for i in range(7):
                if list_of_pickable_spells[i] != []:
                    num_to_add = spells_known[self.class_level - 1][i]
                    if self.class_level > 1:
                        num_to_add -= spells_known[self.class_level - 2][i]
                    for _ in range(num_to_add):
                        print_text = f"please enter spell name of level {i} to add. "+\
                                      "Possible spells are: " +\
                                      ", ".join(list_of_pickable_spells[i])
                        entered = self.get_user_response([x.lower() for x in \
                                                        list_of_pickable_spells[i]], print_text)
                        entered = entered.title()
                        list_of_pickable_spells[i].remove(entered)
                        self.spells[i].append(entered)

            list_to_write_to_file += self.print_spells()
        list_to_write_to_file += self.print_spell_numbers()
        self.write_to_file("listPass", list_to_write_to_file)


    def calc_skills(self, verbose=True):
        """calculate the total of every skill

        Args:
            verbose (bool, optional): If the results are to be printed to the HTML file.
                                      Defaults to True.

        Returns:
            list: list of objects to be printed to the HTML file
        """
        if verbose:
            list_to_write_to_file = []
            list_to_write_to_file.append([htmlTags["acrobaticsMod"], self.mods["dex"]])
            list_to_write_to_file.append([htmlTags["athleticsMod"], self.mods["str"]])
            list_to_write_to_file.append([htmlTags["bluffMod"], self.mods["cha"]])
            list_to_write_to_file.append([htmlTags["computersMod"], self.mods["int"]])
            list_to_write_to_file.append([htmlTags["cultureMod"], self.mods["int"]])
            list_to_write_to_file.append([htmlTags["diplomacyMod"], self.mods["cha"]])
            list_to_write_to_file.append([htmlTags["disguiseMod"], self.mods["cha"]])
            list_to_write_to_file.append([htmlTags["engineeringMod"], self.mods["int"]])
            list_to_write_to_file.append([htmlTags["intimidateMod"], self.mods["cha"]])
            list_to_write_to_file.append([htmlTags["life scienceMod"], self.mods["int"]])
            list_to_write_to_file.append([htmlTags["medicineMod"], self.mods["int"]])
            list_to_write_to_file.append([htmlTags["mysticismMod"], self.mods["wis"]])
            list_to_write_to_file.append([htmlTags["perceptionMod"], self.mods["wis"]])
            list_to_write_to_file.append([htmlTags["physical scienceMod"], self.mods["int"]])
            list_to_write_to_file.append([htmlTags["pilotingMod"], self.mods["dex"]])
            list_to_write_to_file.append([htmlTags["professionMod"], -1])
            list_to_write_to_file.append([htmlTags["profession2Mod"], -1])
            list_to_write_to_file.append([htmlTags["sense motiveMod"], self.mods["wis"]])
            list_to_write_to_file.append([htmlTags["sleight of handMod"], self.mods["dex"]])
            list_to_write_to_file.append([htmlTags["stealthMod"], self.mods["dex"]])
            list_to_write_to_file.append([htmlTags["survivalMod"], self.mods["wis"]])
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
            "profession2"      : self.mods[self.profession_ability],
            "sense motive"     : self.mods["wis"],
            "sleight of hand"  : self.mods["dex"],
            "stealth"          : self.mods["dex"],
            "survival"         : self.mods["wis"],
        }
        for skill in self.skills:
            self.skills[skill] += self.skill_ranks[skill] + self.skill_class[skill] +\
                                  self.skill_misc[skill]
            if verbose:
                list_to_write_to_file.append([htmlTags[skill], self.skills[skill]])
                list_to_write_to_file.append([htmlTags[skill + "Rank"], self.skill_ranks[skill]])
                list_to_write_to_file.append([htmlTags[skill + "Class"], self.skill_class[skill]])
                list_to_write_to_file.append([htmlTags[skill + "Misc"], self.skill_misc[skill] +\
                                                                    self.skill_dabbler[skill]])
        if verbose:
            return list_to_write_to_file

    def calc_hit_points(self):
        """calculates the current HP, SP, and RP
        """
        self.stamina_points = max(1, (max(0, classesStatBonus[self.class_name]["sp"] +\
                                             self.mods["con"])) * self.class_level)
        self.hit_points = max(1, (classesStatBonus[self.class_name]["hp"] * self.class_level) +\
                             raceStatList[self.race_name.split()[0]]["hp"])
        self.resolve_points = max(1, max(1, self.class_level // 2) + self.mods[self.key])

    def add_skill_points(self):
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
            entered = self.get_user_response(possible_skill, response_text)
            possible_skill.remove(entered)
            self.skill_ranks[entered] += 1
            skillpoints -= 1
            self.write_to_file(htmlTags["spendablePoints"], skillpoints)


    def calc_attribut_mod(self): # TODO
        """calculate the attribute modifiers
        """
        self.mods["str"] = ((self.attributes["strength"] // 2) - 5)
        self.mods["dex"] = ((self.attributes["dexterity"] // 2) - 5)
        self.mods["con"] = ((self.attributes["constitution"] // 2) - 5)
        self.mods["int"] = ((self.attributes["intelligence"] // 2) - 5)
        self.mods["wis"] = ((self.attributes["wisdom"] // 2) - 5)
        self.mods["cha"] = ((self.attributes["charisma"] // 2) - 5)

    def check_combat_feats(self, check_feat):
        """checks if a feat is a combat feat

        Args:
            check_feat (str): which combat feat in particular, when any is chosen

        Returns:
            bool: True if the feat is a combat feat, False if not
        """
        # need a combat list to track how many combat feats have been selected
        any_counter = 0
        to_add = True
        combat = []

        for long_feat in self.chosen_feats:
            feat = long_feat
            if long_feat in ["weapon focus", "weapon specialization", "skill focus"]:
                feat = long_feat.split("[")[0].rstrip()
            if feats[feat][0] == "combat":
                combat.append(feat)
        for feat in check_feat:
            if feat == "any":
                any_counter += 1
            else:
                if feat not in combat:
                    to_add = False
                    break

        if any_counter > len(combat):
            to_add = False
        return to_add

    def check_for_feat(self, check_feat):
        """checks to see if the feat is in the chosen_feats list

        Args:
            checkFeat (str): the feat to be checked

        Returns:
            bool: if the entered feat is in chosen_feats
        """
        # need a list to track how many feats have been selected
        to_add = True
        for feat in check_feat:
            if feat not in self.chosen_feats:
                to_add = False
                break
        return to_add

    def check_for_skills(self, check_skills):
        """does some skill check

        Args:
            check_skills (list): list of skills to be checked

        Returns:
            bool: if the skill can be added
        """
        to_add = True
        for check_skill in check_skills:
            if not to_add:
                break
            if check_skill[0] == "from":
                to_add = False
                for from_check_skill in check_skill[1]:
                    if self.skills[from_check_skill] >= check_skill[2]:
                        to_add = True
                        break
            elif len(check_skill) > 2:
                if self.skills[check_skill[0]] != check_skill[1]:
                    to_add = False
            else:
                if self.skills[check_skill[0]] < check_skill[1]:
                    to_add = False
        return to_add

    def check_for_attribute(self, check_attribute):
        """checks if the attribute is high enough for the feat to be added

        Args:
            check_attribute (list): list of attribute and value

        Returns:
            bool: if the ability score is high enough return True
        """
        check_ability = check_attribute[0]
        if check_attribute[0] == "key":
            check_ability = self.key
        if self.attributes[attribute_shorthand[check_ability]] >= check_attribute[1]:
            return True
        return False

    def check_for_spell_level(self, check_spell_level):
        """checks to see if the players spell level is high enough to be able to use
            the feat in question

        Args:
            check_spell_level (int): spell level of character

        Returns:
            bool: True if the spell level is high enough for the feat
        """
        if check_spell_level == -1:
            if self.spell_level == -1:
                return True
        elif self.spell_level >= check_spell_level:
            return True
        return False

    def check_for_bab(self, check_bab):
        """check to see if the bab of the player is high enough for the feat

        Args:
            check_bab (int ): bab of the character

        Returns:
            bool: if the characters bab is high enough return True
        """
        if classesStatBonus[self.class_name]["bab"][self.class_level - 1] >= check_bab:
            return True
        return False

    def check_for_level(self, check_level):
        """checks if the character level is high enough for the feat in question

        Args:
            check_level (int): level of the character

        Returns:
            bool: if the level of the character is high enough return True
        """
        if self.class_level >= check_level:
            return True
        return False

    def check_for_saves(self, check_saves):
        """checks to see if the given save stat is high enough

        Args:
            check_saves (list): list of save type and value

        Returns:
            bool: if the save value is high enough return True
        """
        if classesStatBonus[self.class_name][check_saves[0]][self.class_level-1] >= check_saves[1]:
            return True
        return False

    def check_for_race(self, check_race):
        """check if the race is what is needed for the feat

        Args:
            check_race (str): race required for the feat

        Returns:
            bool: if the race of the player is the needed one for the feat return True
        """
        if self.race_name == check_race:
            return True
        return False

    def check_for_style(self, check_style):
        """checks if the style the player chose is what is needed for the feat in question

        Args:
            check_style (list): list of styles

        Returns:
            bool: if the player chose the needed style return True
        """
        for style in self.styles:
            if style == check_style:
                return True
        return False

    def check_from(self, from_list):
        """Performs multiple checks at once

        Args:
            from_list (list): list of things that need to be checked

        Returns:
            bool: returns True if any of the requirements are met
        """
        feat_true = False
        class_true = False
        for from_check in from_list:
            if from_check[0] == "feat":
                for feat in from_check[1]:
                    if feat in self.chosen_feats:
                        feat_true = True
                        break
            elif from_check[0] == "class":
                class_true = from_check[1] == self.class_name

            else:
                print(f"from {from_check[0]} not implemented {from_list}")
        return feat_true or class_true

    def filter_feats(self, combat=False):
        """generates list of feats the player can chose from

        Args:
            combat (bool, optional): used to filter out combat feats. Defaults to False.

        Returns:
            list: list of choosable feats
        """
        selected = []
        for feat, tmp in feats.items():
            #tmp = feats[feat]
            if not combat or tmp[0] == "combat":
                to_add = True
                for check in tmp[1]:
                    if len(check) > 0:
                        if check[0] == "combat":
                            if not self.check_combat_feats(check[1]):
                                to_add = False
                        elif check[0] == "feat":
                            if not self.check_for_feat(check[1]):
                                to_add = False
                        elif check[0] == "skills":
                            if not self.check_for_skills(check[1]):
                                to_add = False
                        elif check[0] == "ability":
                            if not self.check_for_attribute(check[1]):
                                to_add = False
                        elif check[0] == "spellLevel":
                            if not self.check_for_spell_level(check[1]):
                                to_add = False
                        elif check[0] == "bab":
                            if not self.check_for_bab(check[1]):
                                to_add = False
                        elif check[0] == "level":
                            if not self.check_for_level(check[1]):
                                to_add = False
                        elif check[0] == "save":
                            if not self.check_for_saves(check[1]):
                                to_add = False
                        elif check[0] == "race":
                            if not self.check_for_race(check[1]):
                                to_add = False
                        # casterLevel check: check if lashunta and greater than level required,
                        # or class of technomancer or mystic
                        elif check[0] == "style":
                            if not self.check_for_style(check[1]):
                                to_add = False
                        elif check[0] == "from":
                            if not self.check_from(check[1]):
                                to_add = False
                if to_add:
                    selected.append(feat)
        return selected

    def select_new_feat(self, combat=False):
        """function to add a feat to the character. only used in terminal version

        Args:
            combat (bool, optional): used to filter out combat feats. Defaults to False.
        """
        add_feat = False
        additional_info = ""
        possible_feats = self.filter_feats(combat)
        for feat in self.chosen_feats:
            if feat in possible_feats:
                possible_feats.remove(feat)
        while not add_feat:
            print_text = "please enter feat name you would like to add. Possible feats are: " +\
                         ", ".join(possible_feats)
            lower_chosen_feats = [x.lower() for x in possible_feats]
            entered = self.get_user_response(lower_chosen_feats, print_text)
            add_feat = True
            if entered == "weapon focus" or entered == "weapon specialization":
                weapon_feats = ["advanced melee", "advanced melee weapon", "basic melee",
                               "basic melee weapon", "grenade", "heavy", "heavy weapon",
                               "longarm", "small arm", "sniper", "sniper weapon", "special",
                               "special weapon"]
                weapon_feats_small = ["advanced melee weapon", "basic melee weapon", "grenade",
                                    "heavy weapon", "longarm", "small arm", "sniper weapon",
                                    "special weapon"]
                if entered == "weapon specialization":
                    weapon_feats.remove("grenade")
                    weapon_feats_small.remove("grenade")

                weapon_type_text = "With which weapon type do you wish to use this feat? \n" +\
                                 "Possible weapon types are: " + ", ".join(weapon_feats_small)
                weapon_entered = self.get_user_response(weapon_feats, weapon_type_text)
                weapon_feats_dict = {
                    "advanced melee"        : "Advanced Melee Weapon Proficiency",
                    "advanced melee weapon" : "Advanced Melee Weapon Proficiency",
                    "basic melee"           : "Basic Melee Weapon Proficiency",
                    "basic melee weapon"    : "Basic Melee Weapon Proficiency",
                    "grenade"               : "Grenade Proficiency",
                    "heavy"                 : "Heavy Weapon Proficiency",
                    "heavy weapon"          : "Heavy Weapon Proficiency",
                    "longarm"               : "Longarm Proficiency",
                    "small arm"             : "Small Arm Proficiency",
                    "sniper"                : "Sniper Weapon Proficiency",
                    "sniper weapon"         : "Sniper Weapon Proficiency",
                    "special"               : "Special Weapon Proficiency",
                    "special weapon"        : "Special Weapon Proficiency"
                }
                additional_info = f" [{weapon_feats_dict[weapon_entered]}]"
                if weapon_feats_dict[weapon_entered] not in self.chosen_feats:
                    add_feat = False
                    print(f"You do not have the {weapon_feats_dict[weapon_entered]}, please " +\
                           "selsct a different feat")
                    additional_info = ""
            elif entered == "skill focus":
                print_text = "please enter the skill you would like to focus. " +\
                             "Possible skills are: " + ", ".join([x for x in self.skills])
                skill_entered = self.get_user_response([x for x in self.skills], print_text)
                additional_info = f" [{skill_entered.title()}]".format()
                self.skill_misc[skill_entered] += 3

        entered_feat_index = lower_chosen_feats.index(entered)
        self.chosen_feats.append(possible_feats[entered_feat_index] + additional_info)

        # entered = self.getUserResponse([x.lower() for x in possibleFeats], printText)
        # self.chosenFeats.append(entered)

    def select_new_class_feat(self, feat_type : str, level : int, verbose : bool=True) -> list:
        """Adds a new feature based on the entered featType and level. Should verbose be set to
           False the list of options is returned

        Args:
            featType (str): the type of feat that is to be added
            level (int): player level
            verbose (bool, optional): If this function is called in terminal it prompts the user
                                      to enter a response, otherwise it returns all possibilities.
                                      Defaults to True.

        Returns:
            list : list of class feats that can be selected
        """
        possible_class_feats = []
        for feat_list in classChoseFeats[self.class_name][feat_type]:
            if level >= feat_list[0]:
                possible_class_feats += feat_list[1:]
        for feat in self.class_feats:
            if feat in possible_class_feats:
                possible_class_feats.remove(feat)
        if verbose:
            print_text = "please enter class feat name you would like to add. " +\
                         "Possible feats are: " + ", ".join(possible_class_feats)
            lower_class_feats = [x.lower() for x in possible_class_feats]
            entered = self.get_user_response(lower_class_feats, print_text)
            entered_feat_index = lower_class_feats.index(entered)
            self.class_feats.append(possible_class_feats[entered_feat_index])
        return possible_class_feats

    def feats_and_abilities(self):
        """do something with the feats and abilities
        """

        possible_skill = ["acrobatics", "athletics", "bluff", "computers", "culture", "diplomacy",
                         "disguise", "engineering", "intimidate", "life science", "medicine",
                         "mysticism", "perception", "physical science", "profession1",
                         "profession2", "piloting", "sense motive", "sleight of hand", "stealth",
                         "survival"]

        list_to_write_to_file = []
        for i in range(len(raceAbilities[self.race_name.split()[0]])):
            race_ability_block = raceAbilities[self.race_name.split()[0]][i]
            if race_ability_block[1] == "stats":
                for block in race_ability_block[2]:
                    if block[0] == "any":
                        print_text = f"please enter skill name to add {block[1]} point(s) to. " +\
                                     "Possible skills are: " + ", ".join(possible_skill)
                        block[0] = self.get_user_response(possible_skill, print_text)
                    self.skill_misc[block[0]] += block[1]
                    self.skills[block[0]] += block[1]
                    list_to_write_to_file.append([htmlTags[block[0]], self.skills[block[0]]])
                    list_to_write_to_file.append([htmlTags[block[0] + "Misc"],
                                              self.skill_misc[block[0]]])
            elif race_ability_block[1] == "spell": # TODO
                for j in range(2):
                    for spell in race_ability_block[2][j]:
                        if spell not in self.additional_spells:
                            self.additional_spells[j].append(spell)
            elif race_ability_block[1] == "feat":
                self.select_new_feat()
            elif race_ability_block[1] == "words":
                pass
            else:
                print(f"The race Ability {race_ability_block[1]} has not yet been implemented")

        theme_name = self.theme.split("(")[0].rstrip()
        if self.class_level == 1:
            if isinstance(themeAbilities[theme_name][0][1], str):
                new_class_skill = themeAbilities[theme_name][0][1]
                if new_class_skill == "any":
                    new_class_skill = self.get_user_response(possible_skill,
                                    "You get to select a Skill to be turned into a class skill." +\
                                        " Options are " + ", ".join(possible_skill))
                self.make_class_skill(new_class_skill)
            elif isinstance(themeAbilities[theme_name][0][1], list):
                new_class_skill = self.get_user_response(themeAbilities[theme_name][0][1],
                                "You get to select a Skill to be turned into a class skill. " +\
                                "Options are " + ", ".join(themeAbilities[theme_name][0][1]))
                self.make_class_skill(new_class_skill)
            else:
                print_string = f"themeAbility {themeAbilities[theme_name][0][1]} " +\
                                "has not yet been implemented"
                print(print_string)
        if self.class_level >= 6:
            if themeAbilities[theme_name][1][1] != "words":
                # +2 bonus to skill checks for skills with 0 ranks in skill
                for skill in self.skills:
                    if self.skill_ranks[skill] == 0:
                        self.skill_dabbler[skill] = 2
        if self.class_level == 12:
            if themeAbilities[theme_name][2][1] != "words":
                # ^Choose one 1st-level mystic spell with some connection to your deity's portfolio
                # (subject to the GM's approval). If you have levels in the mystic class, you
                # gain 1 additional 1stlevel spell per day and add the chosen spell to your list
                # of mystic spells known. Otherwise, you can use the chosen spell once per day as
                # a spell-like ability.
                possible_spells = spells["mystic"][1]
                print_text = "as a priest you may choose one 1st-level mystic spell. " +\
                             "Possible spells are " + ", ".join(possible_spells)
                entered = self.get_user_response(possible_spells, print_text)
                self.additional_spells[1].append(entered)
            else:
                pass # TODO # the alternative is spell and needs to add a spell,
                     # only priest will have this


        list_replaceables = ["Expertise", "Bypass", "Miracle", "Coordinated", "Channel",
                            "Operative's", # Operative's might not be just words
                            "Trick", "Quick", "Sidereal", # Sidereal is not just words
                            "Techlore", # Techlore is not just words
                            "Cache", "Skill"]
        #for level in range(1, self.class_level + 1):
        for ability in classAbilities[self.class_name][self.class_level - 1]:
            if ability[1] == "improvisation": # classChoseFeats, lists with levels
                self.select_new_class_feat("improvisation", self.class_level)
            elif ability[1] == "talent": # classChoseFeats, lists with levels
                self.select_new_class_feat("talent", self.class_level)
            elif ability[1] == "trick": # classChoseFeats, lists with levels
                self.select_new_class_feat("trick", self.class_level)
            elif ability[1] == "class":
                to_make_class = ability[2]
                for make_class in to_make_class:
                    new_class_skill = make_class
                    if new_class_skill == "any":
                        response_text = "You get to select a Skill to be turned into a class " +\
                                        "skill. Options are " + ", ".join(possible_skill)
                        new_class_skill = self.get_user_response(possible_skill, response_text)
                    self.make_class_skill(new_class_skill)
            elif ability[1] == "skills":
                for skill in ability[2]:
                    self.skill_misc[skill[0]] += skill[1]
            elif ability[1] == "revelation": # classChoseFeats, lists with levels
                self.select_new_class_feat("revelation", self.class_level)
            elif ability[1] == "zenith": # classChoseFeats, single list
                self.select_new_class_feat("zenith", self.class_level)
            elif ability[1] == "style": # classChoseFeats, dictionary
                possible_styles = [x for x in classChoseFeats["soldier"]["styles"]]
                for style in self.styles:
                    possible_styles.remove(style)
                print_text = "please enter the style name you would like to add. " +\
                             "Possible styles are: " + ", ".join(possible_styles)
                entered = self.get_user_response(possible_styles, print_text)
                self.styles.append(entered)
                self.class_feats.append(entered.title())
            elif ability[1] == "technique1":
                self.class_feats.append(
                    classChoseFeats["soldier"]["styles"][self.styles[0]][self.class_level - 1])
            elif ability[1] == "technique2":
                self.class_feats.append(
                    classChoseFeats["soldier"]["styles"][self.styles[1]][(self.class_level - 1) -8])
            elif ability[1] == "combat":
                self.select_new_feat(combat=True)
            elif ability[1] == "gear": # classChoseFeats, lists with levels
                self.select_new_class_feat("gear", self.class_level)
            elif ability[1] == "hack": # classChoseFeats, lists with levels
                self.select_new_class_feat("hack", self.class_level)
            elif ability[1] == "feat":
                self.chosen_feats.append(ability[2])
            elif ability[1] == "edge":
                self.initiative_misc += 1
                self.calc_init()
                list_to_write_to_file.append([htmlTags["init_total"], self.initiative])
                list_to_write_to_file.append([htmlTags["init_dex"], self.mods["dex"]])
                list_to_write_to_file.append([htmlTags["init_misc"], self.initiative_misc])
                for skill in self.skill_misc:
                    self.skill_misc[skill] += 1
            elif ability[1] == "specialization":
                if ability[2][0] == "feat":
                    self.chosen_feats.append(ability[2][1])
                    possible_specialization = list(classChoseFeats["operative"]["specialization"])
                    print_text = "please enter the specialization name you would like to add. " +\
                                 "Possible specialization are: {}" +\
                                     ", ".join(possible_specialization)

                    entered = self.get_user_response([x.lower() for x in possible_specialization],
                                                    print_text)
                    entered = entered.title()
                    self.styles.append(entered)
                    self.class_feats.append(entered)
                    skill1, skill2 = \
                        classChoseFeats["operative"]["specialization"][self.styles[0]][0]
                    self.chosen_feats.append(f"Skill Focus [{skill1.title()}]")
                    self.chosen_feats.append(f"Skill Focus [{skill2.title()}]")
                    self.skill_misc[skill1] += 3
                    self.skill_misc[skill2] += 3
                elif ability[2][0] == "exploit":
                    self.class_feats.append(
                        classChoseFeats["operative"]["specialization"][self.styles[0]][1])
                elif ability[2][0] == "power":
                    self.class_feats.append(
                        classChoseFeats["operative"]["specialization"][self.styles[0]][2])
            elif ability[1] == "exploit":
                self.select_new_class_feat("exploit", self.class_level)
            elif ability[1] == "connection":
                possible_connection = list(classChoseFeats["mystic"]["connection"])
                print_text = "please enter the connnection name you would like to add. " +\
                            "Possible connections are: " + ", ".join(possible_connection)
                entered = self.get_user_response([x.lower() for x in possible_connection],
                                                  print_text)
                entered = entered.title()
                self.styles.append(entered)
                self.class_feats.append(entered)
            elif ability[1] == "cpower":
                self.class_feats.append(
                    classChoseFeats["mystic"]["connection"][self.styles[0]]["feat"][ability[2]])
            elif ability[1] == "spell":
                self.additional_spells[ability[2] + 1].append(
                    classChoseFeats["mystic"]["connection"][self.styles[0]]["spell"][ability[2]])
            elif ability[1] == "channel":
                skill1, skill2 = classChoseFeats["mystic"]["connection"][self.styles[0]]["skill"]
                self.skill_misc[skill1] += 1
                self.skill_misc[skill2] += 1
            elif ability[1] == "expertise":
                self.expertise.append("sense motive")
            elif ability[1] == "add expertise":
                # this is not shown on the excel sheet, might just ignore it then # TODO
                possible_expertise = ["bluff", "computers", "culture", "diplomacy", "disguise",
                                     "engineering", "intimidate", "medicine"]
                for expertise in self.expertise:
                    if expertise in possible_expertise:
                        possible_expertise.remove(expertise)
                print_text = "please enter the skill you would like to add as additional " +\
                            "expertise. Possible expertise are: " + ", ".join(possible_expertise)
                entered = self.get_user_response(possible_expertise, print_text)
                self.expertise.append(entered)
            elif ability[1] == "influence": # solarian # add two skills, one each from two lists
                possible_graviton = classChoseFeats["solarian"]["graviton"]
                possible_photon = classChoseFeats["solarian"]["photon"]
                for influence in self.expertise:
                    if influence in possible_graviton:
                        possible_graviton.remove(influence)
                    if influence in possible_photon:
                        possible_photon.remove(influence)
                print_text = "please enter the influence you would like to add as the Graviton " +\
                    "influence. Possible influences are: " + ", ".join(possible_graviton)
                entered = self.get_user_response(possible_graviton, print_text)
                self.expertise.append(entered)
                print_text = "please enter the influence you would like to add as the Photon " +\
                    "influence. Possible influences are: " + ", ".join(possible_photon)
                entered = self.get_user_response(possible_photon, print_text)
                self.expertise.append(entered)

            elif ability[1] == "weapon": # all # TODO
                pass
            elif ability[1] == "words": # nothing happens
                pass
            elif ability[1] == "None":
                pass
            else:
                print(f"{ability} has not yet been implemented")


            result = [replacable for replacable in list_replaceables if replacable in ability[0]]
            if len(result) != 0:
                result = result[0]
                result = [oldAbility for oldAbility in self.list_class_abilities \
                            if result in oldAbility]
                if len(result) != 0:
                    result = result[0]
                    result = self.list_class_abilities.index(result)
                    self.list_class_abilities[result] = ability[0]
                else:
                    self.list_class_abilities.append(ability[0])
            else:
                self.list_class_abilities.append(ability[0])

        list_to_write_to_file += self.calc_skills()

        list_to_write_to_file += self.print_abilities()

        list_to_write_to_file += self.print_spells()

        self.write_to_file("listPass", list_to_write_to_file)

    def print_abilities(self):
        """generates list to print objects to the HTML file

        Returns:
            list: list of objects to be printed to HTML
        """
        race_boxes = [htmlTags["raceAbility1"], htmlTags["raceAbility2"], htmlTags["raceAbility3"],
                     htmlTags["raceAbility4"]]
        theme_boxes = [htmlTags["themeAbility1"], htmlTags["themeAbility2"],
                      htmlTags["themeAbility3"], htmlTags["themeAbility4"]]
        class_boxes = [htmlTags["classAbility1"], htmlTags["classAbility2"],
                      htmlTags["classAbility3"], htmlTags["classAbility4"],
                      htmlTags["classAbility5"], htmlTags["classAbility6"],
                      htmlTags["classAbility7"], htmlTags["classAbility8"],
                      htmlTags["classAbility9"], htmlTags["classAbility10"],
                      htmlTags["classAbility11"], htmlTags["classAbility12"],
                      htmlTags["classAbility13"], htmlTags["classAbility14"],
                      htmlTags["classAbility15"], htmlTags["classAbility16"],
                      htmlTags["classAbility17"], htmlTags["classAbility18"],
                      htmlTags["classAbility19"], htmlTags["classAbility20"],
                      htmlTags["classAbility21"], htmlTags["classAbility22"],
                      htmlTags["classAbility23"], htmlTags["classAbility24"],
                      htmlTags["classAbility25"], htmlTags["classAbility26"],
                      htmlTags["classAbility27"], htmlTags["classAbility28"]]
        other_boxes = [htmlTags["otherAbility1"], htmlTags["otherAbility2"],
                      htmlTags["otherAbility3"], htmlTags["otherAbility4"],
                      htmlTags["otherAbility5"], htmlTags["otherAbility6"],
                      htmlTags["otherAbility7"], htmlTags["otherAbility8"],
                      htmlTags["otherAbility9"], htmlTags["otherAbility10"],
                      htmlTags["otherAbility11"], htmlTags["otherAbility12"],
                      htmlTags["otherAbility13"], htmlTags["otherAbility14"],
                      htmlTags["otherAbility15"], htmlTags["otherAbility16"]]
        feat_boxes = [htmlTags["feat1"], htmlTags["feat2"], htmlTags["feat3"], htmlTags["feat4"],
                     htmlTags["feat5"], htmlTags["feat6"], htmlTags["feat7"], htmlTags["feat8"],
                     htmlTags["feat9"], htmlTags["feat10"], htmlTags["feat11"], htmlTags["feat12"],
                     htmlTags["feat13"], htmlTags["feat14"], htmlTags["feat15"],htmlTags["feat16"],
                     htmlTags["feat17"], htmlTags["feat18"], htmlTags["feat19"],htmlTags["feat20"],
                     htmlTags["feat21"], htmlTags["feat22"], htmlTags["feat23"],htmlTags["feat24"],
                     htmlTags["feat25"], htmlTags["feat26"], htmlTags["feat27"],htmlTags["feat28"]]

        list_to_write_to_file = []

        for i in range(len(raceAbilities[self.race_name.split()[0]])):
            race_ability_block = raceAbilities[self.race_name.split()[0]][i]
            list_to_write_to_file.append([race_boxes[i], race_ability_block[0]])

        theme_name = self.theme.split("(")[0].rstrip()
        if self.class_level >= 1:
            list_to_write_to_file.append([theme_boxes[0], themeAbilities[theme_name][0][0]])
        if self.class_level >= 6:
            list_to_write_to_file.append([theme_boxes[1], themeAbilities[theme_name][1][0]])
        if self.class_level >= 12:
            list_to_write_to_file.append([theme_boxes[2], themeAbilities[theme_name][2][0]])
        if self.class_level >= 18:
            list_to_write_to_file.append([theme_boxes[3], themeAbilities[theme_name][3][0]])

        j = 0
        for i, current_class_abilities in enumerate(self.list_class_abilities):
            if "Expertise" in current_class_abilities: # expertise and influence
                for expertise in self.expertise:
                    list_to_write_to_file.append([class_boxes[i + j], current_class_abilities +\
                                                  f" [{expertise}]"])
                    j += 1
                j -= 1
            else:
                list_to_write_to_file.append([class_boxes[i + j], current_class_abilities])

        for i, current_class_feat in enumerate(self.class_feats):
            list_to_write_to_file.append([other_boxes[i], current_class_feat])

        for i, current_chosen_feat in enumerate(self.chosen_feats):
            list_to_write_to_file.append([feat_boxes[i], current_chosen_feat])
        return list_to_write_to_file


    def make_class_skill(self, new_class_skill):
        """make a skill into a class skill or give it an extra misc charge

        Args:
            new_class_skill (str): skill to be made into a class skill
        """
        if self.skill_class[new_class_skill] == 0:
            self.skill_class[new_class_skill] = 3
        else:
            self.skill_misc[new_class_skill] += 1

    def ability_increase(self):
        """every two levels this function adds a new feat to the character, every 5 the character
        can improve 4 stats
        """
        if self.class_level % 2 == 1:
            self.select_new_feat()
        if self.class_level % 5 == 0:
            possible_abilities = ["(str)ength", "(dex)terity", "(con)stitution", "(int)elligence",
                                 "(wis)dom", "(cha)risma"]
            to_increase_number = 4
            while to_increase_number > 0:
                print_text = f"You get to increase {to_increase_number} more attributes. " +\
                             f"Possible attributes: {possible_abilities}"
                entered = self.get_user_response(possible_attributes, print_text)
                entered = attribute_shorthand[entered]
                self.ability_increases[entered] += 1
                self.attributes[entered] += 1
                if self.attributes[entered] < 18:
                    self.attributes[entered] += 1
                index = [x for x in possible_abilities \
                            if attribute_shortener[entered].lower() in x][0]
                possible_abilities.remove(index)
                to_increase_number -= 1
            self.calc_attribut_mod()
            self.initiative = self.mods["dex"] + self.initiative_misc

            list_to_write_to_file = []
            list_to_write_to_file.append([htmlTags["init_total"], self.initiative])
            list_to_write_to_file.append([htmlTags["init_dex"], self.mods["dex"]])
            list_to_write_to_file.append([htmlTags["init_misc"], self.initiative_misc])
            list_to_write_to_file.append([htmlTags["abilityStr"],
                                          self.ability_increases["strength"]])
            list_to_write_to_file.append([htmlTags["abilityDex"],
                                          self.ability_increases["dexterity"]])
            list_to_write_to_file.append([htmlTags["abilityCon"],
                                      self.ability_increases["constitution"]])
            list_to_write_to_file.append([htmlTags["abilityInt"],
                                      self.ability_increases["intelligence"]])
            list_to_write_to_file.append([htmlTags["abilityWis"],
                                          self.ability_increases["wisdom"]])
            list_to_write_to_file.append([htmlTags["abilityCha"],
                                          self.ability_increases["charisma"]])
            list_to_write_to_file.append([htmlTags["attrStrMod"], self.mods["str"]])
            list_to_write_to_file.append([htmlTags["attrDexMod"], self.mods["dex"]])
            list_to_write_to_file.append([htmlTags["attrConMod"], self.mods["con"]])
            list_to_write_to_file.append([htmlTags["attrIntMod"], self.mods["int"]])
            list_to_write_to_file.append([htmlTags["attrWisMod"], self.mods["wis"]])
            list_to_write_to_file.append([htmlTags["attrChaMod"], self.mods["cha"]])
            list_to_write_to_file.append([htmlTags["attrStr"], self.attributes["strength"]])
            list_to_write_to_file.append([htmlTags["attrDex"], self.attributes["dexterity"]])
            list_to_write_to_file.append([htmlTags["attrCon"], self.attributes["constitution"]])
            list_to_write_to_file.append([htmlTags["attrInt"], self.attributes["intelligence"]])
            list_to_write_to_file.append([htmlTags["attrWis"], self.attributes["wisdom"]])
            list_to_write_to_file.append([htmlTags["attrCha"], self.attributes["charisma"]])
            list_to_write_to_file+= self.calc_skills()
            self.write_to_file("listPass", list_to_write_to_file)

    def level_up(self): # TODO Spells
        """Level the character up and call all relevant functions
        """
        #levels = [1300, 3300, 6000, 10000, 15000, 23000, 34000, 50000, 71000, 105000,
        #          14500, 210000, 295000, 425000, 600000, 850000, 1200000, 1700000, 2400000]
        #currLevel = 1
        #for level in levels:
        #    if self.experience >= level:
        #        currLevel += 1
        #    else:
        #        break
        if self.class_level < 20:
            self.class_level = self.class_level + 1
            self.ability_increase()
            self.add_skill_points()
            list_to_write_to_file = []
            list_to_write_to_file += self.calc_skills()
            self.feats_and_abilities()
            self.calc_hit_points()
            list_to_write_to_file.append([htmlTags["sp"], self.stamina_points])
            list_to_write_to_file.append([htmlTags["hp"], self.hit_points])
            list_to_write_to_file.append([htmlTags["rp"], self.resolve_points])
            class_name = self.class_name.title() + " (" + str(self.class_level) + ")"
            if self.class_name == "soldier":
                class_name += " [" + str(self.key) + "]"
            list_to_write_to_file.append([htmlTags["className"], class_name])
            self.add_spells()
            self.calc_attack()
            list_to_write_to_file += self.print_attack()
            self.calc_save()
            list_to_write_to_file += self.print_save()
            self.write_to_file("listPass", list_to_write_to_file)

    def get_user_response(self, options, text="", include=True):
        """Function to get user response from input options

        Args:
            options (list): list of possible options the user can choose from
            text (str, optional): text to inform the user what they are responding to.
                                  Defaults to "".
            include (bool, optional): if include is True the entered text must be in the options
                                      list, False means the input can't be in the options.
                                      Defaults to True.

        Returns:
            str: the entered text that was allowed
        """
        entered = ""
        if include:
            while entered not in options:
                entered = input(text).lower()
        else:
            while entered in options:
                entered = input(text).lower()
        return entered

    def update_html(self):
        """Funtion that takes the internal variables and updates every single
           variable to the HTML file
        """
        list_to_write_to_file = []
        list_to_write_to_file.append([htmlTags["name"], self.name.title()])
        list_to_write_to_file.append([htmlTags["race"], self.race_name.title()])
        list_to_write_to_file.append([htmlTags["raceStr"],
                                  raceStatList[self.race_name.split()[0]]["strength"]])
        list_to_write_to_file.append([htmlTags["raceDex"],
                                  raceStatList[self.race_name.split()[0]]["dexterity"]])
        list_to_write_to_file.append([htmlTags["raceCon"],
                                  raceStatList[self.race_name.split()[0]]["constitution"]])
        list_to_write_to_file.append([htmlTags["raceInt"],
                                  raceStatList[self.race_name.split()[0]]["intelligence"]])
        list_to_write_to_file.append([htmlTags["raceWis"],
                                  raceStatList[self.race_name.split()[0]]["wisdom"]])
        list_to_write_to_file.append([htmlTags["raceCha"],
                                  raceStatList[self.race_name.split()[0]]["charisma"]])
        list_to_write_to_file.append([htmlTags["theme"], self.theme.title()])
        list_to_write_to_file.append([htmlTags["themeStr"], self.theme_attributes["strength"]])
        list_to_write_to_file.append([htmlTags["themeDex"], self.theme_attributes["dexterity"]])
        list_to_write_to_file.append([htmlTags["themeCon"], self.theme_attributes["constitution"]])
        list_to_write_to_file.append([htmlTags["themeInt"], self.theme_attributes["intelligence"]])
        list_to_write_to_file.append([htmlTags["themeWis"], self.theme_attributes["wisdom"]])
        list_to_write_to_file.append([htmlTags["themeCha"], self.theme_attributes["charisma"]])

        list_to_write_to_file.append([htmlTags["attrStr"], self.attributes["strength"]])
        list_to_write_to_file.append([htmlTags["attrDex"], self.attributes["dexterity"]])
        list_to_write_to_file.append([htmlTags["attrCon"], self.attributes["constitution"]])
        list_to_write_to_file.append([htmlTags["attrInt"], self.attributes["intelligence"]])
        list_to_write_to_file.append([htmlTags["attrWis"], self.attributes["wisdom"]])
        list_to_write_to_file.append([htmlTags["attrCha"], self.attributes["charisma"]])

        list_to_write_to_file.append([htmlTags["attrStrPoint"], self.spent_points["strength"]])
        list_to_write_to_file.append([htmlTags["attrDexPoint"], self.spent_points["dexterity"]])
        list_to_write_to_file.append([htmlTags["attrConPoint"], self.spent_points["constitution"]])
        list_to_write_to_file.append([htmlTags["attrIntPoint"], self.spent_points["intelligence"]])
        list_to_write_to_file.append([htmlTags["attrWisPoint"], self.spent_points["wisdom"]])
        list_to_write_to_file.append([htmlTags["attrChaPoint"], self.spent_points["charisma"]])

        list_to_write_to_file.append([htmlTags["abilityStr"], self.ability_increases["strength"]])
        list_to_write_to_file.append([htmlTags["abilityDex"], self.ability_increases["dexterity"]])
        list_to_write_to_file.append([htmlTags["abilityCon"],
                                      self.ability_increases["constitution"]])
        list_to_write_to_file.append([htmlTags["abilityInt"],
                                      self.ability_increases["intelligence"]])
        list_to_write_to_file.append([htmlTags["abilityWis"], self.ability_increases["wisdom"]])
        list_to_write_to_file.append([htmlTags["abilityCha"], self.ability_increases["charisma"]])

        class_name = self.class_name.title() + " (" + str(self.class_level) + ")"
        if self.class_name == "soldier":
            class_name += " [" + str(self.key) + "]"
        list_to_write_to_file.append([htmlTags["className"], class_name])

        list_to_write_to_file.append([htmlTags["eac"], self.eac])
        list_to_write_to_file.append([htmlTags["eac_armor"], 0])
        list_to_write_to_file.append([htmlTags["eac_dex"], self.mods["dex"]])
        list_to_write_to_file.append([htmlTags["eac_misc"], 0])
        list_to_write_to_file.append([htmlTags["kac"], self.kac])
        list_to_write_to_file.append([htmlTags["kac_armor"], 0])
        list_to_write_to_file.append([htmlTags["kac_dex"], self.mods["dex"]])
        list_to_write_to_file.append([htmlTags["kac_misc"], 0])
        list_to_write_to_file.append([htmlTags["vsCombat"], self.vs_combat])

        list_to_write_to_file.append([htmlTags["attrStrMod"], self.mods["str"]])
        list_to_write_to_file.append([htmlTags["attrDexMod"], self.mods["dex"]])
        list_to_write_to_file.append([htmlTags["attrConMod"], self.mods["con"]])
        list_to_write_to_file.append([htmlTags["attrIntMod"], self.mods["int"]])
        list_to_write_to_file.append([htmlTags["attrWisMod"], self.mods["wis"]])
        list_to_write_to_file.append([htmlTags["attrChaMod"], self.mods["cha"]])

        list_to_write_to_file.append([htmlTags["init_total"], self.initiative])
        list_to_write_to_file.append([htmlTags["init_dex"], self.mods["dex"]])
        list_to_write_to_file.append([htmlTags["init_misc"], self.initiative_misc])

        list_to_write_to_file += self.print_save()

        self.calc_attack()
        list_to_write_to_file += self.print_attack()

        list_to_write_to_file.append([htmlTags["sp"], self.stamina_points])
        list_to_write_to_file.append([htmlTags["hp"], self.hit_points])
        list_to_write_to_file.append([htmlTags["rp"], self.resolve_points])

        list_to_write_to_file.append([htmlTags["spendablePoints"], 0])
        list_to_write_to_file.append([htmlTags["perLevelPoints"],
                                  classesStatBonus[self.class_name]["skills"] + self.mods["int"]])

        list_to_write_to_file += self.calc_skills()
        list_to_write_to_file += self.print_abilities()

        list_to_write_to_file += self.print_spell_numbers()

        list_to_write_to_file += self.print_spells()

        self.write_to_file("listPass", list_to_write_to_file)

    def read_from_html(self, file_name):
        """takes input html file and creates a character from it

        Args:
            file_name (str) : HTML file name
        """
        class_boxes = [htmlTags["classAbility1"], htmlTags["classAbility2"],
                      htmlTags["classAbility3"], htmlTags["classAbility4"],
                      htmlTags["classAbility5"], htmlTags["classAbility6"],
                      htmlTags["classAbility7"], htmlTags["classAbility8"],
                      htmlTags["classAbility9"], htmlTags["classAbility10"],
                      htmlTags["classAbility11"], htmlTags["classAbility12"],
                      htmlTags["classAbility13"], htmlTags["classAbility14"],
                      htmlTags["classAbility15"], htmlTags["classAbility16"],
                      htmlTags["classAbility17"], htmlTags["classAbility18"],
                      htmlTags["classAbility19"], htmlTags["classAbility20"],
                      htmlTags["classAbility21"], htmlTags["classAbility22"],
                      htmlTags["classAbility23"], htmlTags["classAbility24"],
                      htmlTags["classAbility25"], htmlTags["classAbility26"],
                      htmlTags["classAbility27"], htmlTags["classAbility28"]]

        other_boxes = [htmlTags["otherAbility1"], htmlTags["otherAbility2"],
                      htmlTags["otherAbility3"], htmlTags["otherAbility4"],
                      htmlTags["otherAbility5"], htmlTags["otherAbility6"],
                      htmlTags["otherAbility7"], htmlTags["otherAbility8"],
                      htmlTags["otherAbility9"], htmlTags["otherAbility10"],
                      htmlTags["otherAbility11"], htmlTags["otherAbility12"],
                      htmlTags["otherAbility13"], htmlTags["otherAbility14"],
                      htmlTags["otherAbility15"], htmlTags["otherAbility16"]]


        feat_boxes = [htmlTags["feat1"], htmlTags["feat2"], htmlTags["feat3"], htmlTags["feat4"],
                     htmlTags["feat5"], htmlTags["feat6"], htmlTags["feat7"], htmlTags["feat8"],
                     htmlTags["feat9"], htmlTags["feat10"], htmlTags["feat11"], htmlTags["feat12"],
                     htmlTags["feat13"], htmlTags["feat14"],htmlTags["feat15"], htmlTags["feat16"],
                     htmlTags["feat17"], htmlTags["feat18"],htmlTags["feat19"], htmlTags["feat20"],
                     htmlTags["feat21"], htmlTags["feat22"],htmlTags["feat23"], htmlTags["feat24"],
                     htmlTags["feat25"], htmlTags["feat26"],htmlTags["feat27"], htmlTags["feat28"]]

        spell_boxes = [
            ["spell001", "spell002", "spell003", "spell004", "spell005", "spell006", "spell007",
             "spell008"],
            ["spell101", "spell102", "spell103", "spell104", "spell105", "spell106", "spell107",
             "spell108"],
            ["spell201", "spell202", "spell203", "spell204", "spell205", "spell206", "spell207"],
            ["spell301", "spell302", "spell303", "spell304", "spell305", "spell306", "spell307"],
            ["spell401", "spell402", "spell403", "spell404", "spell405", "spell406", "spell407"],
            ["spell501", "spell502", "spell503", "spell504", "spell505", "spell506"],
            ["spell601", "spell602", "spell603", "spell604", "spell605", "spell606"]]
        try:
            file = open(f"{file_name}.html", encoding='utf-8')
            soup = BeautifulSoup(file, 'html.parser')

            self.name                          = soup.find(attrs={"id": htmlTags["name"]})["value"]

            theme = soup.find(attrs={"id": htmlTags["theme"]})["value"].lower()
            theme = theme.split()
            if len(theme) == 2:
                theme[1] = theme[1][1:-1]
            self.set_theme(*theme)

            self.vs_combat = soup.find(attrs={"id": htmlTags["vsCombat"]})["value"]
            race_name = soup.find(attrs={"id": htmlTags["race"]})["value"].lower()
            race_name = race_name.split()
            if len(race_name) == 2:
                race_name[1] = race_name[1][1:-1]
            self.set_race(*race_name)

            class_name_level = soup.find(attrs={"id": htmlTags["className"]})["value"]
            class_name_level                      = class_name_level.split()
            self.class_name                       = class_name_level[0].lower()
            self.class_level                      = int(class_name_level[-1][1:-1])
            self.key                             = classesStatBonus[self.class_name]["key"]
            if self.class_name == "soldier":
                self.key                         = class_name_level[1][1:-1]

            self.melee_misc = int(soup.find(attrs={"id": htmlTags["melee_misc"]})["value"])
            self.range_misc = int(soup.find(attrs={"id": htmlTags["range_misc"]})["value"])
            self.throw_misc = int(soup.find(attrs={"id": htmlTags["throw_misc"]})["value"])

            self.calc_attack()

            self.spent_points["strength"]         = int(soup.find(attrs={"id": \
                                                    htmlTags["attrStrPoint"]})["value"])
            self.spent_points["dexterity"]        = int(soup.find(attrs={"id": \
                                                    htmlTags["attrDexPoint"]})["value"])
            self.spent_points["constitution"]     = int(soup.find(attrs={"id": \
                                                    htmlTags["attrConPoint"]})["value"])
            self.spent_points["intelligence"]     = int(soup.find(attrs={"id": \
                                                    htmlTags["attrIntPoint"]})["value"])
            self.spent_points["wisdom"]           = int(soup.find(attrs={"id": \
                                                    htmlTags["attrWisPoint"]})["value"])
            self.spent_points["charisma"]         = int(soup.find(attrs={"id": \
                htmlTags["attrChaPoint"]})["value"])

            self.ability_increases["strength"]    = int(soup.find(attrs={"id": \
                                                    htmlTags["abilityStr"]})["value"])
            self.ability_increases["dexterity"]   = int(soup.find(attrs={"id": \
                                                    htmlTags["abilityDex"]})["value"])
            self.ability_increases["constitution"]= int(soup.find(attrs={"id": \
                                                    htmlTags["abilityCon"]})["value"])
            self.ability_increases["intelligence"]= int(soup.find(attrs={"id": \
                                                    htmlTags["abilityInt"]})["value"])
            self.ability_increases["wisdom"]      = int(soup.find(attrs={"id": \
                                                    htmlTags["abilityWis"]})["value"])
            self.ability_increases["charisma"]    = int(soup.find(attrs={"id": \
                                                    htmlTags["abilityCha"]})["value"])

            self.calc_attributes()
            self.calc_attribut_mod()

            self.calc_hit_points()

            self.initiative_misc = int(soup.find(attrs={"id": htmlTags["init_misc"]})["value"])
            self.calc_init()

            self.calc_armor_class()

            self.fort_save_misc = int(soup.find(attrs={"id": htmlTags["fortSaveMisc"]})["value"])
            self.reflex_save_misc=int(soup.find(attrs={"id": htmlTags["reflexSaveMisc"]})["value"])
            self.will_save_misc = int(soup.find(attrs={"id": htmlTags["willSaveMisc"]})["value"])

            self.calc_save()

            for skill in classesStatBonus["envoy"]["classBonus"]:
                self.skills[skill] = int(soup.find(attrs={"id": htmlTags[skill]})["value"])
                self.skill_ranks[skill] = int(soup.find(attrs={"id": htmlTags[skill + "Rank"]}
                                                )["value"])
                self.skill_class[skill] = int(soup.find(attrs={"id": htmlTags[skill + "Class"]}
                                                )["value"])
                self.skill_misc[skill] = int(soup.find(attrs={"id": htmlTags[skill + "Misc"]}
                                                )["value"])
                if self.theme == "spacefarer" and self.skill_ranks[skill] == 0:
                    self.skill_dabbler[skill] = 2
                    self.skill_misc[skill] -= 2

            for class_box in class_boxes:
                try:
                    class_feat = soup.find(attrs={"id": class_box})["value"]
                    if "Expertise" in class_feat:
                        self.expertise.append(class_feat.split()[1][1:-1])
                        if "Expertise" not in self.list_class_abilities:
                            self.list_class_abilities.append(class_feat.split()[0])
                    else:
                        self.list_class_abilities.append(class_feat)

                except KeyError:
                    break

            for other_box in other_boxes:
                try:
                    other_feat = soup.find(attrs={"id": other_box})["value"]
                    self.class_feats.append(other_feat)
                    if self.class_name == "soldier":
                        if other_feat in classChoseFeats["soldier"]["styles"]:
                            self.styles.append(other_feat)
                    elif self.class_name == "operative":
                        if other_feat in classChoseFeats["operative"]["specialization"]:
                            self.styles.append(other_feat)
                    elif self.class_name == "mystic":
                        if other_feat in classChoseFeats["mystic"]["connection"]:
                            self.styles.append(other_feat)
                except KeyError:
                    break

            for feat_box in feat_boxes:
                try:
                    chosen_feat = soup.find(attrs={"id": feat_box})["value"]
                    self.chosen_feats.append(chosen_feat)
                except KeyError:
                    break


            for i in range(7):
                full_spell_list = []
                for spell_box in spell_boxes[i]:
                    try:

                        adding_spell = soup.find(attrs={"id": htmlTags[spell_box]})["value"]
                        full_spell_list.append(adding_spell)
                    except KeyError:
                        break
                #self.spells[i] + self.additionalSpells[i]
                for j, current_spell in enumerate(full_spell_list):
                    if j < spells_known[self.class_level - 1][i]:
                        self.spells[i].append(current_spell)
                    else:
                        self.additional_spells[i].append(current_spell)

            # self.expertise
            # self.chosenFeats "weapon focus" or "weapon specialization" or "skill focus"

        except FileNotFoundError:
            print("""The Character name you entered does not have a file.
                    Please create the character with the wizard or enter another name""")



    def write_to_file(self, attribute_name, attribute_name_value):
        """funtion to write the input to the HTML

        Args:
            attribute_name (str): either the string "listPass" or the box in which the
                                  attribute_name_value is to be entered
            attribute_name_value (str): the string gets entered into the attribute_name box
                                        unless attribute_name was "listPass" in which case it
                                        is a list of lists where the first element of each internal
                                        list is what is here considered the attribute_name and the
                                        second is the attribute_name_value
        """
        try:
            file = open(f"{self.name}.html", mode="r+", encoding='utf-8')
        except FileNotFoundError:
            file = open("CharacterSheet.html", mode="r+", encoding='utf-8')

        soup = BeautifulSoup(file, 'html.parser')
        if attribute_name == "listPass":
            for a_name, a_name_value in attribute_name_value:
                try:
                    soup.find(attrs={"id": a_name})["value"] = a_name_value
                except TypeError:
                    print("------------------")
                    print(a_name)
                    print(a_name_value)
                    print(soup.find(attrs={"id": a_name}))
                    print("------------------")
        else:
            try:
                soup.find(attrs={"id": attribute_name})["value"] = attribute_name_value
            except TypeError:
                print("------------------")
                print(attribute_name)
                print(attribute_name_value)
                print(soup.find(attrs={"id": attribute_name}))
                print("------------------")

        with open(f"{self.name.lower()}.html", "w", encoding='utf-8') as out:
            out.write(str(soup))
        file.close()
