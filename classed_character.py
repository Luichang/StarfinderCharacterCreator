import inspect
from copy import deepcopy

# from helpers.feats import feats
from helpers.helper import get_user_response, write_to_file
from helpers.starfinder_dicts import (attribute_shorthand, possible_attributes,
                                      skills, spells_bonus, spells_day,
                                      spells_known)
from helpers.starfinder_html_dict import htmlTags
# from helpers.starfinder_html_dict import htmlTags
# from helpers.starfinder_race_dicts import raceStatList
# from helpers.starfinder_theme_dicts import themes
from starfinder_classes.starfinder_class import StarfinderClass
from starfinder_feats.starfinder_feat import Feat
from starfinder_feats.starfinder_feat_type import FeatType
from starfinder_feats.starfinder_feats import feats, any_combat_feat
#from helpers.spells import spells
from starfinder_feats.starfinder_spells import (spells, spells_by_class,
                                                spells_by_level)
from starfinder_races.starfinder_race import StarfinderRace
from starfinder_themes.starfinder_theme import StarfinderTheme


class Character:
    """This class is to create a starfinder character
    """
    def __init__(self, file_name="", gui=False):

        self.name = ""
        self.spell_level = -1

        self.other_abilities = []
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

        # self.skill_class = []

        self.skill_misc = deepcopy(skills)

        self.skill_dabbler = deepcopy(skills)

        self.spent_points = {"strength" : 0, "dexterity" : 0, "constitution" : 0,
                            "intelligence" : 0, "wisdom": 0, "charisma" : 0}

        self.class_level = 1

        self.theme : StarfinderTheme
        self.race_name : StarfinderRace
        self.class_name : StarfinderClass

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

    def update_professions(self, profession1 : str=None, profession2 : str = None) -> None:
        """function to update the profession ability modifiers

        Args:
            profession1 (str, optional): ability modifier for profession1.
                                         Options are 'wis, int, and cha'. Defaults to None.
            profession2 (str, optional): ability modifier for profession2.
                                         Options are 'wis, int, and cha'. Defaults to None.
        """
        if profession1:
            self.profession_ability = profession1
        if profession2:
            self.profession2_ability = profession2

    def create_new(self):
        """create a new character
        """
        entered = get_user_response([""], "Enter a Character Name", False)
        self.set_name(entered)

        options = ["android", "human", "kasatha", "lashunta(korasha)", "lashunta(damaya)",
                    "shirren", "vesk", "ysoki"]

        response_text = "Please chose a race, options are: " + ", ".join(options)
        entered = get_user_response(options, response_text)
        self.race_name = StarfinderRace.create(entered)
        possible_attrs = ["str", "dex", "con", "int", "wis", "cha"]
        if str(self.race_name) in ["Human [" + x + "]" for x in possible_attrs]:
            response_text = "Humans have to chose the ability they want to boost. " +\
                             "Possible are " + ", ".join(possible_attrs)
            key = get_user_response(possible_attrs, response_text)
            self.race_name.select_improvement(key)

        options = ["ace pilot", "bounty hunter", "icon", "mercenary", "outlaw", "priest",
                   "scholar", "spacefarer", "xenoseeker", "themeless"]

        response_text = "Chose a theme. Possible themes are: " + ", ".join(options)
        entered = get_user_response(options, response_text)

        self.theme = StarfinderTheme.create(entered)
        possible_attrs = ["str", "dex", "con", "int", "wis", "cha"]
        if str(self.theme) in ["Themeless [" + x + "]" for x in possible_attrs]:
            response_text = "Themeless have to chose the ability they want to boost. " +\
                             "Possible are " + ", ".join(possible_attrs)
            key = get_user_response(possible_attrs, response_text)
            self.theme.select_improvement(key)

        options = ["envoy", "mechanic", "mystic", "operative", "solarian", "soldier",
                   "technomancer"]

        response_text = "Chose a Class. Possible Classes are: " + ", ".join(options)
        entered = get_user_response(options, response_text)
        self.class_name = StarfinderClass.create(entered)
        possible_attrs = ["str", "dex"]
        if str(self.class_name) in ["Soldier [" + x + "]" for x in possible_attrs]:
            response_text = "Soldier has to chose the key ability. Possible are str and dex"
            key = get_user_response(possible_attrs, response_text)
            self.class_name.select_key(key)

        self.chosen_feats = self.class_name.proficiencies

        self.calc_spell_level()

        self.point_buy()

        self.calc_attributes()

        self.calc_attribut_mod()

        self.calc_init()

        self.calc_armor_class()

        self.calc_hit_points()

        self.calc_save()

        self.calc_attack()

        self.add_skill_points()

        self.feats_and_abilities()

        self.add_spells()

        self.update_html()

    def set_name(self, name : str) -> None:
        """Sets the name of the character

        Args:
            name (str): Character Name
        """
        self.name = name

    def add_spells(self, gui : bool=False) -> None:
        """add spells to the character
        """
        if str(self.class_name) in ["Mystic", "Technomancer"]:
            list_of_pickable_spells = [[], [], [], [], [], [], []]
            for i in range(7):
                if spells_known[self.class_level - 1][i] > 0:
                    class_spells = spells_by_class(spells, str(self.class_name))
                    list_of_pickable_spells[i] = spells_by_level(class_spells, i)
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

    def update_dabbler(self) -> None:
        """function to update the dabbler stats
        """
        dabble = 0
        if str(self.theme) == "Spacefarer" and self.class_level >= 6:
            dabble = 2
        # +2 bonus to skill checks for skills with 0 ranks in skill
        for skill in self.skills:
            if self.skill_ranks[skill] == 0:
                self.skill_dabbler[skill] = dabble
            else:
                self.skill_dabbler[skill] = 0

    def feat_level_check(self, feat : Feat) -> bool:
        """function to check if the level requirement is met

        Args:
            feat (Feat): feat with potential level requirement

        Returns:
            bool: returns True if level requirement is met or non existent
        """
        if feat.requirements.level:
            if feat.requirements.level > self.class_level:
                return False
        return True

    def feat_spell_level_check(self, feat : Feat) -> bool:
        """function to check if the spell level requirement is met

        Args:
            feat (Feat): feat with potential spell level requirement

        Returns:
            bool: returns True if requirement is met or non existent
        """
        if feat.requirements.spell_level:
            if feat.requirements.spell_level == -1 == self.spell_level:
                return False
            if feat.requirements.spell_level > self.spell_level:
                return False
        return True

    def feat_skills_check(self, feat: Feat) -> bool:
        """function to check if the skills requirement is met

        Args:
            feat (Feat): feat with potential skills requirement

        Returns:
            bool: returns True if requirement is met or non existent
        """
        if feat.requirements.skills:
            for skill in feat.requirements.skills:
                if isinstance(skill, list):
                    for check_skill in skill[:-1]:
                        if self.skills[check_skill] > skill[-1]:
                            return True
                    return False
                else:
                    if self.skills[skill[0]] < skill[1]:
                        return False
        return True

    def feat_ability_check(self, feat : Feat) -> bool:
        """function to check if the ability requirement is met

        Args:
            feat (Feat): feat with potential ability requirement

        Returns:
            bool: returns True if requirement is met or non existent
        """
        if feat.requirements.ability:
            for ability in feat.requirements.ability:
                to_check = ability[0]
                if to_check == "key":
                    to_check = self.class_name.key
                if ability[1] > self.attributes[attribute_shorthand[to_check]]:
                    return False
        return True

    def feat_class_name_check(self, feat : Feat) -> bool:
        """function to check if the class name requirement is met

        Args:
            feat (Feat): feat with potential class name requirement

        Returns:
            bool: returns True if requirement is met or non existent
        """
        to_add = True
        if feat.requirements.class_name:
            if isinstance(feat.requirements.class_name, list):
                to_add = False
                for possible_class in feat.requirements.class_name:
                    if isinstance(self.class_name, possible_class):
                        to_add = True
            else:
                to_add = False
                if inspect.isclass(feat.requirements.class_name):
                    if isinstance(self.class_name, feat.requirements.class_name):
                        to_add = True
                elif type(feat.requirements.class_name) is type(self.class_name):
                    if feat.requirements.class_name.selection == self.class_name.selection:
                        to_add = True
        return to_add

    def feat_bab_check(self, feat : Feat) -> bool:
        """function to check if the bab requirement is met

        Args:
            feat (Feat): feat with potential bab requirement

        Returns:
            bool: returns True if requirement is met or non existent
        """
        if feat.requirements.bab:
            if feat.requirements.bab > self.class_name.bab[self.class_level]:
                return False
        return True

    def feat_reflex_check(self, feat : Feat) -> bool:
        """function to check if the reflex requirement is met

        Args:
            feat (Feat): feat with potential reflex requirement

        Returns:
            bool: returns True if requirement is met or non existent
        """
        if feat.requirements.reflex:
            if feat.requirements.reflex > self.class_name.reflex[self.class_level]:
                return False
        return True

    def feat_will_check(self, feat : Feat) -> bool:
        """function to check if the skills will is met

        Args:
            feat (Feat): feat with potential will requirement

        Returns:
            bool: returns True if requirement is met or non existent
        """
        if feat.requirements.will:
            if feat.requirements.will > self.class_name.will[self.class_level]:
                return False
        return True

    def feat_fort_check(self, feat : Feat) -> bool:
        """function to check if the fortitude requirement is met

        Args:
            feat (Feat): feat with potential fortitude requirement

        Returns:
            bool: returns True if requirement is met or non existent
        """
        if feat.requirements.fort:
            if feat.requirements.fort > self.class_name.fort[self.class_level]:
                return False
        return True

    def feat_race_check(self, feat : Feat) -> bool:
        """function to check if the race requirement is met

        Args:
            feat (Feat): feat with potential race requirement

        Returns:
            bool: returns True if requirement is met or non existent
        """
        if feat.requirements.race:
            if not isinstance(self.race_name, feat.requirements.race):
                return False
        return True

    def feat_feat_check(self, feat : Feat) -> bool:
        """function to check if the feats requiremed have already been selected

        Args:
            feat (Feat): feat with potential feat requirement

        Returns:
            bool: returns True if requirement is met or non existent
        """
        any_counter = 0
        if feat.requirements.feat:
            for feat_name in feat.requirements.feat: # check every feat in the list
                if feat_name == any_combat_feat:
                    any_counter += 1
                elif feat_name not in self.chosen_feats: # if required feat has not been selected
                    # yet, we don't want to offer this feat as a selectable so we break from
                    # the loop and continue the outer loop
                    return False
            if any_counter > 0:
                counter = 0
                for potential_combat_feat in self.chosen_feats:
                    if potential_combat_feat.combat:
                        counter += 1
                if any_counter > counter:
                    return False
        return True

    def feat_from_check(self, feat : Feat) -> bool:
        """function to check if the list of requirements depending on each other is met

        Args:
            feat (Feat): feat with potential list of requirements

        Returns:
            bool: returns True if requirements are met or non existent
        """
        to_add = True
        if feat.requirements.from_list:
            to_add = False
            for check in feat.requirements.from_list:
                if check[0] == "feat":
                    if isinstance(check[1], list):
                        for check_feat in check[1]:
                            if check_feat in self.chosen_feats:
                                to_add = True
                                break
                    else:
                        if check[1] in self.chosen_feats:
                                to_add = True
                                break
                elif check[0] == "class":
                    if isinstance(self.class_name, check[1]):
                        to_add = True
                        break
        return to_add

    def available_feats(self, combat : bool=False) -> list[Feat]:
        """function to return the possible feats that the player can chose from

        Args:
            combat (bool, optional): if the player gets to only choose combat feats. Defaults to False.

        Returns:
            list[Feat] : list of feats for which the character meets the requirements
        """
        # if combat bool is true only feats with combat are to be selected. if combat is false, all can be selected
        selected = []
        for feat in feats:
            if combat and not feat.combat:
                continue
            if feat.requirements:
                if not self.feat_level_check(feat):
                    continue
                if not self.feat_spell_level_check(feat):
                    continue
                if not self.feat_skills_check(feat):
                    continue
                if not self.feat_ability_check(feat):
                    continue
                if not self.feat_class_name_check(feat):
                    continue
                if not self.feat_bab_check(feat):
                    continue
                if not self.feat_reflex_check(feat):
                    continue
                if not self.feat_will_check(feat):
                    continue
                if not self.feat_fort_check(feat):
                    continue
                if not self.feat_race_check(feat):
                    continue
                if not self.feat_feat_check(feat):
                    continue
                if not self.feat_from_check(feat):
                    continue
            selected.append(feat)
        return selected


    def select_new_feat(self, combat : bool=False, verbose : bool=True) -> list:
        """function to add new feat to the character

        Args:
            combat (bool, optional): if the feat that is to be added needs to be a combat feat.
                                        Defaults to False.
            verbose (bool, optional): if the function should return a list or ask for user input.
                                        Defaults to True

        Returns:
            list: list of all possible feats. used in the GUI
        """
        possible_feats = self.available_feats(combat)
        for feat in self.chosen_feats:
            if feat in possible_feats:
                possible_feats.remove(feat)
        if not verbose:
            return possible_feats
        print_text = "please enter feat name you would like to add. Possible feats are: " +\
                            ", ".join([str(x) for x in possible_feats])
        lower_chosen_feats = [str(x).lower() for x in possible_feats]
        entered = get_user_response(lower_chosen_feats, print_text)
        entered_feat_index = lower_chosen_feats.index(entered)
        self.chosen_feats.append(possible_feats[entered_feat_index])

    def feats_and_abilities(self) -> None:
        """do something with the feats and abilities
        """

        # Race part
        for ability in self.race_name.abilities:
            if ability.get_type == FeatType.STATS:
                for skill in ability.skills:
                    skill_to_add, value = skill
                    if skill_to_add == "any":
                        possible_skill = list(self.skills)
                        print_text = f"please enter skill name to add {value} point(s) to. " +\
                                     "Possible skills are: " + ", ".join(possible_skill)
                        skill_to_add = get_user_response(possible_skill, print_text)
                    self.skill_misc[skill_to_add] += value
                    self.calc_skills()
            elif ability.get_type == FeatType.SPELL:
                for j in range(2):
                    for spell in self.race_name.spells[j]:
                        if spell not in self.additional_spells[j]:
                            self.additional_spells[j].append(spell)
            elif ability.get_type == FeatType.FEAT:
                self.select_new_feat()

        # Theme part
        for ability in self.theme.current_abilities(self.class_level):
            if ability.get_type() == FeatType.STATS:
                skill_to_add = ability.skills
                if len(skill_to_add) > 1 or "any" in skill_to_add:
                    if "any" in skill_to_add:
                        skill_to_add = list(self.skills)
                    response_text = "You get to select a Skill to be turned into a class " +\
                                    "skill. Options are " + ", ".join(skill_to_add)
                    skill_to_add = get_user_response(skill_to_add, response_text)
                else:
                    skill_to_add = skill_to_add[0]
                self.make_class_skill(skill_to_add)
            elif ability.get_type() == FeatType.DABBLER:
                self.update_dabbler()
            elif ability.get_type() == FeatType.SPELL:
                mystic_spells = spells_by_class(spells, "Mystic")
                possible_spells = spells_by_level(mystic_spells, 1)
                print_text = "as a priest you may choose one 1st-level mystic spell. " +\
                             "Possible spells are " + ", ".join(possible_spells)
                entered = get_user_response(possible_spells, print_text)
                self.additional_spells[1].append(entered)

        # Class part
        for ability in self.class_name.current_abilities(self.class_level):
            # add the ability to the class_feats list. this list only contains the names of the
            # things
            print([str(x) for x in self.class_feats])
            if ability.get_type() in [FeatType.REPLACABLE, FeatType.MISC_INCREASE,
                                        FeatType.INFLUENCE]:
                result = [oldAbility for oldAbility in self.class_feats \
                            if ability.short and ability.short in str(oldAbility)]
                if len(result) != 0:
                    result = result[0]
                    result = self.class_feats.index(result)
                    self.class_feats[result] = ability
                else:
                    self.class_feats.append(ability)
            else:
                self.class_feats.append(ability)
            print([str(x) for x in self.class_feats])
            print("--------")
            # perform ability logic
            if ability.get_type() == FeatType.CHOOSE:
                self.select_new_class_feat()
            elif ability.get_type() == FeatType.CHOOSE2:
                self.select_new_class_feat(secondary=True)
            elif ability.get_type() == FeatType.INFLUENCE:
                self.select_new_expertise()
            elif ability.get_type() == FeatType.SELECTION:
                self.select_selection()
                if ability.feat:
                    #self.chosen_feats.append(ability.feat)
                    skill1, skill2 = self.class_name.specialization_skills()
                    skill_feat1 = ability.feat.copy()
                    skill_feat1.name += f" [{skill1.title()}]"
                    skill_feat2 = ability.feat.copy()
                    skill_feat2.name += f" [{skill2.title()}]"
                    self.chosen_feats.append(skill_feat1)
                    self.chosen_feats.append(skill_feat2)
                    self.skill_misc[skill1] += 3
                    self.skill_misc[skill2] += 3
            elif ability.get_type() == FeatType.MISC_INCREASE:
                self.misc_increase()
            elif ability.get_type() == FeatType.COMBAT:
                self.select_new_feat(combat=True)
            elif ability.get_type() == FeatType.FEAT:
                self.chosen_feats.append(ability.feat)
            elif ability.get_type() == FeatType.TECHNIQUE1:
                self.add_technique(0, self.class_level)
            elif ability.get_type() == FeatType.TECHNIQUE2:
                self.add_technique(1, self.class_level - 8)
            elif ability.get_type() == FeatType.CLASS:
                possible_skill = list(self.skills)
                for _ in range(2):
                    response_text = "You get to select a Skill to be turned into a class " +\
                                    "skill. Options are " + ", ".join(possible_skill)
                    new_class_skill = get_user_response(possible_skill, response_text)
                    self.make_class_skill(new_class_skill)
            elif ability.get_type() == FeatType.CPOWER:
                skill_to_add = self.class_name.connection_feat()
                self.other_abilities.append(skill_to_add[self.class_level//3])
            elif ability.get_type() == FeatType.SPELL:
                skill_to_add = self.class_name.connection_spell()
                spell_level = ((self.class_level-1)//3)
                self.additional_spells[spell_level + 1].append(skill_to_add[spell_level])

        self.calc_skills()

    def add_technique(self, style : int, level : int):
        """takes a level and adds the technique in question to the class_feats list

        Args:
            style (int): which style is to be considered, the first or the second
            level (int): the level of the technique to be added
        """
        techniques = self.class_name.style_combat(style)
        self.other_abilities.append(techniques[level])
        return techniques[level]

    def misc_increase(self):
        """function to increase the misc value based on mystic Channel, operative Edge or
            technomancer Skills
        """
        to_increase = self.class_name.misc_additions()
        for skill in to_increase:
            if skill == "initiative":
                self.initiative_misc += 1
                continue
            self.skill_misc[skill] += 1

    def select_selection(self):
        """function to select the selection thing for mystic, operative, soldier
        """
        possible_selections = self.class_name.possible_selections()
        print_text = "please enter name of selection you would like to add. " +\
                        "Possible selections are: " + ", ".join(possible_selections)
        lower_selections = [x.lower() for x in possible_selections]
        entered = get_user_response(lower_selections, print_text)
        index = lower_selections.index(entered)
        self.class_name.select_selection(possible_selections[index], (self.class_level - 1) % 7)
        self.other_abilities.append(possible_selections[index])


    def make_class_skill(self, new_class_skill : str) -> None:
        """make a skill into a class skill or give it an extra misc charge

        Args:
            new_class_skill (str): skill to be made into a class skill
        """
        self.class_name.bonuses.append(new_class_skill)

    def select_new_expertise(self) -> None:
        """function to take care of the expertises for envoy and
        """
        possible_expertise = self.class_name.new_expertises(self.expertise)

        if len(possible_expertise) == 1:
            self.expertise.append(possible_expertise[0])
            return

        def enter_expertise(expertise_options : list):
            print_text = "please enter name of expertise you would like to add. " +\
                            "Possible expertises are: " + ", ".join(expertise_options)
            entered = get_user_response(expertise_options, print_text)
            self.expertise.append(entered)



        if isinstance(possible_expertise[0], list):
            enter_expertise(possible_expertise[0])
            enter_expertise(possible_expertise[1])
        else:#
            enter_expertise(possible_expertise)

    def select_new_class_feat(self, secondary : bool = False, verbose : bool=True) -> list:
        """Adds a new feature based on the entered featType and level. Should verbose be set to
           False the list of options is returned

        Args:
            secondary (bool, optional): If the secondary list is the one to be considered.
                                        Defaults to True.
            verbose (bool, optional): If this function is called in terminal it prompts the user
                                      to enter a response, otherwise it returns all possibilities.
                                      Defaults to True.

        Returns:
            list : list of class feats that can be selected
        """
        if secondary:
            possible_class_feats = self.class_name.list_of_secondaries(self.class_level)
        else:
            possible_class_feats = self.class_name.list_of_choosables(self.class_level)

        for feat in self.other_abilities:
            if feat in possible_class_feats:
                possible_class_feats.remove(feat)
        if verbose:
            print_text = "please enter class feat name you would like to add. " +\
                         "Possible feats are: " + ", ".join([str(x) for x in possible_class_feats])
            lower_class_feats = [str(x).lower() for x in possible_class_feats]
            entered = get_user_response(lower_class_feats, print_text)
            entered_feat_index = lower_class_feats.index(entered)
            # self.class_feats.append(possible_class_feats[entered_feat_index])
            self.other_abilities.append(possible_class_feats[entered_feat_index])
        return possible_class_feats

    def calc_skills(self) -> None:
        """calculate the total of every skill
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
                self.skills[skill] += self.skill_ranks[skill] +\
                                    self.skill_misc[skill] + self.skill_dabbler[skill]
                self.skills[skill] += self.calc_skill_class(skill)
            else:
                self.skills[skill] = 0

    def calc_skill_class(self, skill : str) -> int:
        """function to calculate the resulting skill class value

        Args:
            skill (str): name of the skill that is to be checked

        Returns:
            int: 0 if not a class skill. 3 if only once a class skill, anything above 3 is the
                 amount of duplicates the class skill
        """
        return_int = 0
        if skill in self.class_name.bonuses:
            return_int += 3
            if self.class_name.bonuses.count(skill) > 1:
                return_int += self.class_name.bonuses.count(skill) - 1
        return return_int

    def add_skill_points(self) -> None:
        """add points to skills, only used in terminal use
        """
        skillpoints = self.class_name.skills + self.mods["int"]
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
        self.stamina_points = max(1, (max(0, self.class_name.stamina_points +\
                                             self.mods["con"])) * self.class_level)
        self.hit_points = max(1, (self.class_name.hit_points * self.class_level) +\
                             self.race_name.hit_points)
        self.resolve_points = max(1, max(1, self.class_level // 2) + self.mods[self.class_name.key])

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
            self.attributes[attribute] = 10 + self.race_name.attributes[attribute] +\
                                          self.theme.attributes[attribute] +\
                                          self.spent_points[attribute]
            for _ in range(self.ability_increases[attribute]):
                self.attributes[attribute] += 1
                if self.attributes[attribute] < 18:
                    self.attributes[attribute] += 1

        self.calc_attribut_mod()

    def calc_spell_level(self):
        """function to update the spell_level of the character
        """
        if str(self.class_name) in ["Mystic", "Technomancer"] or (str(self.theme) == "Priest" and self.class_level >= 12):
            self.spell_level = self.class_level
        else:
            self.spell_level = -1

    def print_abilities(self) -> list:
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

        for i, ability in enumerate(self.race_name.abilities):
            list_to_write_to_file.append([race_boxes[i], str(ability)])

        if self.class_level >= 1:
            list_to_write_to_file.append([theme_boxes[0], str(self.theme.abilities[0])])
        if self.class_level >= 6:
            list_to_write_to_file.append([theme_boxes[1], str(self.theme.abilities[1])])
        if self.class_level >= 12:
            list_to_write_to_file.append([theme_boxes[2], str(self.theme.abilities[2])])
        if self.class_level >= 18:
            list_to_write_to_file.append([theme_boxes[3], str(self.theme.abilities[2])])

        j = 0
        for i, current_class_abilities in enumerate(self.class_feats):
            if self.expertise and \
                str(current_class_abilities).split()[:-1] == ['Skill', 'expertise']:
                # expertise and influence
                for expertise in self.expertise:
                    list_to_write_to_file.append([class_boxes[i + j], str(current_class_abilities) +\
                                                  f" [{expertise}]"])
                    j += 1
                j -= 1
            else:
                list_to_write_to_file.append([class_boxes[i + j], str(current_class_abilities)])

        for i, current_class_feat in enumerate(self.other_abilities):
            list_to_write_to_file.append([other_boxes[i], str(current_class_feat)])

        for i, current_chosen_feat in enumerate(self.chosen_feats):
            list_to_write_to_file.append([feat_boxes[i], str(current_chosen_feat)])
        return list_to_write_to_file

    def print_spell_numbers(self) -> list:
        """generate list to print spells to HTML

        Returns:
            list: list of objects to be printed to the HTML file
        """
        spell_word_boxes = [["spell0known"], ["spell1known", "spell1day"],
                          ["spell2known", "spell2day"], ["spell3known", "spell3day"],
                          ["spell4known", "spell4day"], ["spell5known", "spell5day"],
                          ["spell6known", "spell6day"]]

        list_to_write_to_file = []
        if str(self.class_name) == "Technomancer" or str(self.class_name) == "Mystic":

            bonus_list = []
            for bonus in spells_bonus:
                if bonus[0] > self.attributes[attribute_shorthand[self.class_name.key]]:
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

    def print_spells(self) -> list:
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

    def update_html(self) -> None:
        """Funtion that takes the internal variables and updates every single
           variable to the HTML file
        """
        list_to_write_to_file = []
        list_to_write_to_file.append([htmlTags["name"], str(self.name)])
        list_to_write_to_file.append([htmlTags["race"], str(self.race_name)])
        list_to_write_to_file.append([htmlTags["raceStr"], self.race_name.attributes["strength"]])
        list_to_write_to_file.append([htmlTags["raceDex"], self.race_name.attributes["dexterity"]])
        list_to_write_to_file.append([htmlTags["raceCon"],
                                        self.race_name.attributes["constitution"]])
        list_to_write_to_file.append([htmlTags["raceInt"],
                                        self.race_name.attributes["intelligence"]])
        list_to_write_to_file.append([htmlTags["raceWis"], self.race_name.attributes["wisdom"]])
        list_to_write_to_file.append([htmlTags["raceCha"], self.race_name.attributes["charisma"]])
        list_to_write_to_file.append([htmlTags["theme"], str(self.theme)])
        list_to_write_to_file.append([htmlTags["themeStr"], self.theme.attributes["strength"]])
        list_to_write_to_file.append([htmlTags["themeDex"], self.theme.attributes["dexterity"]])
        list_to_write_to_file.append([htmlTags["themeCon"], self.theme.attributes["constitution"]])
        list_to_write_to_file.append([htmlTags["themeInt"], self.theme.attributes["intelligence"]])
        list_to_write_to_file.append([htmlTags["themeWis"], self.theme.attributes["wisdom"]])
        list_to_write_to_file.append([htmlTags["themeCha"], self.theme.attributes["charisma"]])

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

        class_name = str(self.class_name) + " (" + str(self.class_level) + ")"
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

        list_to_write_to_file.append([htmlTags["fortSave"], self.fort_save])
        list_to_write_to_file.append([htmlTags["reflexSave"], self.reflex_save])
        list_to_write_to_file.append([htmlTags["willSave"], self.will_save])

        list_to_write_to_file.append([htmlTags["fortSaveBase"],
                                 self.class_name.fort[self.class_level - 1]])
        list_to_write_to_file.append([htmlTags["reflexSaveBase"],
                                 self.class_name.reflex[self.class_level - 1]])
        list_to_write_to_file.append([htmlTags["willSaveBase"],
                                 self.class_name.will[self.class_level - 1]])

        list_to_write_to_file.append([htmlTags["fortSaveAbility"], self.mods["con"]])
        list_to_write_to_file.append([htmlTags["reflexSaveAbility"], self.mods["dex"]])
        list_to_write_to_file.append([htmlTags["willSaveAbility"], self.mods["wis"]])

        list_to_write_to_file.append([htmlTags["fortSaveMisc"], self.fort_save_misc])
        list_to_write_to_file.append([htmlTags["reflexSaveMisc"], self.reflex_save_misc])
        list_to_write_to_file.append([htmlTags["willSaveMisc"], self.will_save_misc])

        list_to_write_to_file.append([htmlTags["melee"], self.melee])
        list_to_write_to_file.append([htmlTags["melee_bab"],
                                  self.class_name.bab[self.class_level - 1]])
        list_to_write_to_file.append([htmlTags["melee_ability"], self.mods["str"]])
        list_to_write_to_file.append([htmlTags["melee_misc"], self.melee_misc])

        list_to_write_to_file.append([htmlTags["range"], self.range])
        list_to_write_to_file.append([htmlTags["range_bab"],
                                  self.class_name.bab[self.class_level - 1]])
        list_to_write_to_file.append([htmlTags["range_ability"], self.mods["dex"]])
        list_to_write_to_file.append([htmlTags["range_misc"], self.range_misc])

        list_to_write_to_file.append([htmlTags["throw"], self.throw])
        list_to_write_to_file.append([htmlTags["throw_bab"],
                                  self.class_name.bab[self.class_level - 1]])
        list_to_write_to_file.append([htmlTags["throw_ability"], self.mods["str"]])
        list_to_write_to_file.append([htmlTags["throw_misc"], self.throw_misc])

        list_to_write_to_file.append([htmlTags["sp"], self.stamina_points])
        list_to_write_to_file.append([htmlTags["hp"], self.hit_points])
        list_to_write_to_file.append([htmlTags["rp"], self.resolve_points])

        list_to_write_to_file.append([htmlTags["spendablePoints"], 0])
        list_to_write_to_file.append([htmlTags["perLevelPoints"],
                                  self.class_name.skills + self.mods["int"]])

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
        list_to_write_to_file.append([htmlTags["professionMod"],
                                        self.mods[self.profession_ability]])
        list_to_write_to_file.append([htmlTags["profession2Mod"],
                                        self.mods[self.profession2_ability]])
        list_to_write_to_file.append([htmlTags["sense motiveMod"], self.mods["wis"]])
        list_to_write_to_file.append([htmlTags["sleight of handMod"], self.mods["dex"]])
        list_to_write_to_file.append([htmlTags["stealthMod"], self.mods["dex"]])
        list_to_write_to_file.append([htmlTags["survivalMod"], self.mods["wis"]])

        for skill in self.skills:
            list_to_write_to_file.append([htmlTags[skill], self.skills[skill]])
            list_to_write_to_file.append([htmlTags[skill + "Rank"], self.skill_ranks[skill]])
            val = 0
            if skill in self.class_name.bonuses:
                val = 3
            list_to_write_to_file.append([htmlTags[skill + "Class"], val])
            list_to_write_to_file.append([htmlTags[skill + "Misc"], self.skill_misc[skill] +\
                                                                self.skill_dabbler[skill]])
        list_to_write_to_file += self.print_abilities()

        list_to_write_to_file += self.print_spell_numbers()

        list_to_write_to_file += self.print_spells()

        write_to_file(self.name, "listPass", list_to_write_to_file)
