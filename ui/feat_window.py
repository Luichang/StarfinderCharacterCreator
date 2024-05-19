from typing import Protocol
from PyQt5 import QtCore, QtGui, QtWidgets


import os
import sys


sys.path.append(os.path.abspath("."))

from helpers.helper import (initialize_combo,
                            initialize_frame, initialize_text,
                            initialize_widget)
from starfinder_feats.starfinder_feat_type import FeatType
from character_classes.character import Character
from starfinder_classes.starfinder_mystic import Mystic
from starfinder_classes.starfinder_operative import Operative
from starfinder_classes.starfinder_soldier import Soldier

class ClassGrid(QtWidgets.QFrame):
    def __init__(self, centralwidget):
        super().__init__(centralwidget)
        initialize_frame(self, "Skillframe", [20, 10, 781, 221])
        self.grid_layout_widget_2 = QtWidgets.QWidget(self)
        initialize_widget(self.grid_layout_widget_2, "gridLayoutWidget_2", [10, 10, 761, 201])
        self.skills_score_grid = QtWidgets.QGridLayout(self.grid_layout_widget_2)
        self.skills_score_grid.setContentsMargins(0, 0, 0, 0)
        self.skills_score_grid.setObjectName("SkillsScoreGrid")

        self.class_ability_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.class_ability_text, "ClassAbilityText", "Class Abilities", [70, 25])
        self.skills_score_grid.addWidget(self.class_ability_text, 0, 0, 1, 1)
        self.class1 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class2 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class3 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class4 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class5 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class6 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class7 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class8 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class9 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class10 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class11 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class12 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class13 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class14 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class15 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class16 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class17 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class18 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class19 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class20 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class21 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class22 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class23 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class24 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class25 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class26 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class27 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class28 = QtWidgets.QComboBox(self.grid_layout_widget_2)

        comboboxes = [self.class1, self.class2, self.class3, self.class4, self.class5, self.class6,
                      self.class7, self.class8, self.class9, self.class10, self.class11,
                      self.class12, self.class13, self.class14, self.class15, self.class16,
                      self.class17, self.class18, self.class19, self.class20, self.class21,
                      self.class22, self.class23, self.class24, self.class25, self.class26,
                      self.class27, self.class28]

        j = 1
        k = 0
        for i, combobox in enumerate(comboboxes):
            initialize_combo(combobox, f"Class{i}", [], [184, 20])
            self.skills_score_grid.addWidget(combobox, j, k, 1, 1)
            k = (k + 1) % 4
            if k == 0:
                j += 1

class ThemeGrid(QtWidgets.QFrame):
    def __init__(self, centralwidget):
        super().__init__(centralwidget)
        initialize_frame(self, "Skillframe_2", [20, 240, 781, 71])
        self.grid_layout_widget_3 = QtWidgets.QWidget(self)
        initialize_widget(self.grid_layout_widget_3, "gridLayoutWidget_3", [10, 10, 761, 51])
        self.skills_score_grid_2 = QtWidgets.QGridLayout(self.grid_layout_widget_3)
        self.skills_score_grid_2.setContentsMargins(0, 0, 0, 0)
        self.skills_score_grid_2.setObjectName("SkillsScoreGrid_2")

        self.theme_ability_text = QtWidgets.QLabel(self.grid_layout_widget_3)
        initialize_text(self.theme_ability_text, "ThemeAbilityText", "Theme Abilities", max_size=[70,25])
        self.skills_score_grid_2.addWidget(self.theme_ability_text, 0, 0, 1, 1)

        self.theme1 = QtWidgets.QComboBox(self.grid_layout_widget_3)
        self.theme2 = QtWidgets.QComboBox(self.grid_layout_widget_3)
        self.theme3 = QtWidgets.QComboBox(self.grid_layout_widget_3)
        self.theme4 = QtWidgets.QComboBox(self.grid_layout_widget_3)

        comboboxes = [self.theme1, self.theme2, self.theme3, self.theme4]

        j = 1
        k = 0
        for i, combobox in enumerate(comboboxes):
            initialize_combo(combobox, f"Theme{i}", [], [184, 20])
            self.skills_score_grid_2.addWidget(combobox, j, k, 1, 1)
            k = (k + 1) % 4

class RaceGrid(QtWidgets.QFrame):
    def __init__(self, centralwidget):
        super().__init__(centralwidget)
        initialize_frame(self, "Skillframe_3", [20, 320, 781, 71])
        self.grid_layout_widget_4 = QtWidgets.QWidget(self)
        initialize_widget(self.grid_layout_widget_4, "gridLayoutWidget_4", [10, 10, 761, 51])
        self.skills_score_grid_4 = QtWidgets.QGridLayout(self.grid_layout_widget_4)
        self.skills_score_grid_4.setContentsMargins(0, 0, 0, 0)
        self.skills_score_grid_4.setObjectName("SkillsScoreGrid_4")

        self.race_ability_text = QtWidgets.QLabel(self.grid_layout_widget_4)
        initialize_text(self.race_ability_text, "RaceAbilityText", "Race Abilities", [70, 25])
        self.skills_score_grid_4.addWidget(self.race_ability_text, 0, 0, 1, 1)
        self.race1 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        self.race2 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        self.race3 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        self.race4 = QtWidgets.QComboBox(self.grid_layout_widget_4)

        comboboxes = [self.race1, self.race2, self.race3, self.race4]

        j = 1
        k = 0
        for i, combobox in enumerate(comboboxes):
            initialize_combo(combobox, f"Race{i}", [], [184, 20])
            self.skills_score_grid_4.addWidget(combobox, j, k, 1, 1)
            k = (k + 1) % 4

class FeatsGrid(QtWidgets.QFrame):
    def __init__(self, centralwidget):
        super().__init__(centralwidget)
        initialize_frame(self, "Skillframe_4", [20, 400, 781, 221])
        self.grid_layout_widget_5 = QtWidgets.QWidget(self)
        initialize_widget(self.grid_layout_widget_5, "gridLayoutWidget_5", [10, 10, 761, 201])
        self.skills_score_grid_5 = QtWidgets.QGridLayout(self.grid_layout_widget_5)
        self.skills_score_grid_5.setContentsMargins(0, 0, 0, 0)
        self.skills_score_grid_5.setObjectName("SkillsScoreGrid_5")

        self.feats_text = QtWidgets.QLabel(self.grid_layout_widget_5)
        initialize_text(self.feats_text, "FeatsText", "Feats and Proficiencies", [113, 25])
        self.skills_score_grid_5.addWidget(self.feats_text, 0, 0, 1, 1)
        self.feats1 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats2 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats3 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats4 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats5 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats6 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats7 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats8 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats9 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats10 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats11 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats12 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats13 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats14 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats15 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats16 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats17 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats18 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats19 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats20 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats21 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats22 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats23 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats24 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats25 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats26 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats27 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats28 = QtWidgets.QComboBox(self.grid_layout_widget_5)

        comboboxes = [self.feats1, self.feats2, self.feats3, self.feats4, self.feats5, self.feats6,
                      self.feats7, self.feats8, self.feats9, self.feats10, self.feats11,
                      self.feats12, self.feats13, self.feats14, self.feats15, self.feats16,
                      self.feats17, self.feats18, self.feats19, self.feats20, self.feats21,
                      self.feats22, self.feats23, self.feats24, self.feats25, self.feats26,
                      self.feats27, self.feats28]

        j = 1
        k = 0
        for i, combobox in enumerate(comboboxes):
            initialize_combo(combobox, f"Feats{i}", [], [184, 20])
            self.skills_score_grid_5.addWidget(combobox, j, k, 1, 1)
            k = (k + 1) % 4
            if k == 0:
                j += 1

class Ability(Protocol):
    def __init__(self, name : str, level : int, _type : FeatType, *, short : str = None,
                 skills : list[(str, int)] = None, feat : list = None) -> None:
        ...

class FeatForm(QtWidgets.QWidget):
    """UI Class to display the character Feats

    Args:
        QtWidgets (_type_): _description_
    """
    def __init__(self, character: Character, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setGeometry(200,200,840,650)

        self.character = character

        self.centralwidget = QtWidgets.QFrame()
        self.centralwidget.resize(821, 635)

        layout=QtWidgets.QVBoxLayout()
        layout.addWidget(self.centralwidget)
        self.setLayout(layout)
        self.setWindowTitle("Character Feats")

        self.class_grid = ClassGrid(self.centralwidget)
        self.theme_grid = ThemeGrid(self.centralwidget)
        self.race_grid = RaceGrid(self.centralwidget)
        self.feats_grid = FeatsGrid(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(self.centralwidget)

        self.class_list_one = []
        self.class_list_two = []
        self.class_influence = []
        self.class_abilities = []
        self.replacables = []
        self.feats = []
        self.combats = []
        self.feat_to_add = [(self.character.level + 1) // 2, 0]
        self.feat_dict = {}

        self.update_class_feat_list()

    def update_class_feat_list(self):
        """does some class feature related update

        """

        boxes = [self.class_grid.class1, self.class_grid.class2, self.class_grid.class3,
                 self.class_grid.class4, self.class_grid.class5, self.class_grid.class6,
                 self.class_grid.class7, self.class_grid.class8, self.class_grid.class9,
                 self.class_grid.class10, self.class_grid.class11, self.class_grid.class12,
                 self.class_grid.class13, self.class_grid.class14, self.class_grid.class15,
                 self.class_grid.class16, self.class_grid.class17, self.class_grid.class18,
                 self.class_grid.class19, self.class_grid.class20, self.class_grid.class21,
                 self.class_grid.class22, self.class_grid.class23, self.class_grid.class24,
                 self.class_grid.class25, self.class_grid.class26, self.class_grid.class27,
                 self.class_grid.class28]
        boxcount = 0

        for ability in self.character.starfinder_class.current_abilities(self.character.level):
            try:
                boxes[boxcount].disconnect()
            except TypeError:
                pass
            self.update_feat_dict(ability)
            info_text = "None"

            if ability.get_type() in [FeatType.WORDS, FeatType.REPLACABLE, FeatType.MISC_INCREASE,
                                        FeatType.FEAT, FeatType.TECHNIQUE1, FeatType.TECHNIQUE2,
                                        FeatType.CPOWER, FeatType.SPELL, FeatType.WEAPON,
                                        FeatType.COMBAT]:
                info_text = "<<Fixed Feat>>"
                possible_class_feats = [ability]
                if ability.get_type() == FeatType.MISC_INCREASE:
                    self.character.misc_increase()
                elif ability.get_type() == FeatType.FEAT:
                    self.character.chosen_feats.append(ability.feat)
                elif ability.get_type() == FeatType.TECHNIQUE1:
                    possible_class_feats = [self.character.add_technique(0, ability.level)]
                    self.class_list_one.append(boxes[boxcount])
                    self.update_class_list_one()
                elif ability.get_type() == FeatType.TECHNIQUE2:
                    possible_class_feats = [self.character.add_technique(1, ability.level - 8)]
                    if isinstance(possible_class_feats[0], list):
                        level_list = [-7, -4, -1, 2, 5, 8]
                        try:
                            next_element = level_list[level_list.index(ability.level - 8 - 8) + 1]
                            if (self.character.class_level - 8) > next_element:
                                possible_class_feats = [possible_class_feats[0]]
                            else:
                                possible_class_feats = [possible_class_feats[1]]
                        except IndexError:
                            pass
                    if str(self.character.starfinder_class) == "Mystic":
                        spell_to_add = possible_class_feats[0]
                        spell_level = spell_to_add.level
                        self.character.spells[spell_level].append(spell_to_add)
                    self.class_list_one.append(boxes[boxcount])
                    self.update_class_list_one()
                elif ability.get_type() == FeatType.COMBAT:
                    self.feat_to_add[1] += 1
                elif ability.get_type() == FeatType.CPOWER:
                    skill_to_add = self.character.starfinder_class.connection_feat()
                    self.character.class_feats.append(skill_to_add[ability.level//3])
                elif ability.get_type() == FeatType.SPELL:
                    skill_to_add = self.character.starfinder_class.connection_spell()
                    spell_level = ((ability.level-1)//3)
                    self.character.additional_spells[spell_level + 1].append(
                                                                    skill_to_add[spell_level])
            elif ability.get_type() == FeatType.CHOOSE:
                possible_class_feats = self.character.select_new_class_feat(verbose=False)
                info_text = f"<<Select {str(ability)}>>"
                self.class_list_one.append(boxes[boxcount])
                self.character.other_abilities.append(possible_class_feats[0])
                self.update_class_list_one()
            elif ability.get_type() == FeatType.CHOOSE2:
                possible_class_feats = self.character.select_new_class_feat(secondary=True, verbose=False)
                info_text = f"<<Select {str(ability)}>>"
                self.class_list_two.append(boxes[boxcount])
                self.character.other_abilities.append(possible_class_feats[0])
                self.update_class_list_two()
            elif ability.get_type() == FeatType.INFLUENCE:
                possible_class_feats = self.character.starfinder_class.new_expertises(self.character.expertise)
                info_text = f"<<Select {str(ability)}>>"
                if len(possible_class_feats) == 1:
                    info_text = "<<Fixed Feat>>"
                    self.character.expertise.append(possible_class_feats[0])
                    possible_class_feats = [ability]
                else:
                    if isinstance(possible_class_feats[0], list):
                        self.class_influence.append(boxes[boxcount])
                        self.character.expertise.append(possible_class_feats[0][0])
                        self.update_feat_dict(possible_class_feats)
                        self.initialize_combobox(boxes[boxcount], len(self.character.expertise) - 1,
                                                    info_text, possible_class_feats[0])
                        boxcount += 1
                        possible_class_feats = possible_class_feats[1]
                    self.character.expertise.append(possible_class_feats[0])
                    self.class_influence.append(boxes[boxcount])
                    self.update_influence()
            elif ability.get_type() == FeatType.CLASS:
                info_text = "<<Fixed Feat>>"
                possible_class_feats = list(self.character.skills)
                self.update_feat_dict(possible_class_feats)
                self.class_abilities.append(boxes[boxcount])
                self.character.starfinder_class.bonuses.append(possible_class_feats[0])
                length = len(self.character.starfinder_class.bonuses) - 1
                self.initialize_combobox(boxes[boxcount], length,
                                            info_text, possible_class_feats)
                boxcount += 1
                self.class_abilities.append(boxes[boxcount])
                self.character.starfinder_class.bonuses.append(possible_class_feats[0])
                self.update_class_abilities()

            elif ability.get_type() == FeatType.SELECTION:
                possible_class_feats = self.character.starfinder_class.possible_selections()
                if isinstance(self.character.starfinder_class.selection, list):
                    for selection in self.character.starfinder_class.selection:
                        if selection:
                            possible_class_feats.remove(selection)
                info_text = f"<<Select {str(ability)}>>"
                self.character.starfinder_class.select_selection(possible_class_feats[0], (ability.level - 1) % 7)
                self.class_list_one.append(boxes[boxcount])
                self.character.other_abilities.append(possible_class_feats[0])
                self.update_class_list_one()




            if ability.get_type() in [FeatType.REPLACABLE, FeatType.MISC_INCREASE, FeatType.INFLUENCE]:
                result = [oldAbility for oldAbility in self.character.class_feats \
                            if ability.short and ability.short in str(oldAbility)]
                if len(result) != 0:
                    result = result[0]
                    self.update_feat_text(result, ability)
                    result = self.character.class_feats.index(result)
                    self.character.class_feats[result] = ability
                    if ability.get_type() != FeatType.INFLUENCE:
                        info_text = "None"
                else:
                    self.replacables.append(boxes[boxcount])
                    self.character.class_feats.append(ability)
            else:
                self.character.class_feats.append(ability)



            if info_text != "None":
                self.update_feat_dict(possible_class_feats)
                length = len(self.character.other_abilities) - 1
                if ability.get_type() == FeatType.INFLUENCE:
                    length = len(self.character.expertise) - 1
                elif ability.get_type() == FeatType.INFLUENCE:
                    length = len(self.character.starfinder_class.bonuses) - 1
                self.initialize_combobox(boxes[boxcount], length,
                                            info_text, possible_class_feats)
                boxcount += 1

        if self.class_list_one:
            if isinstance(self.character.starfinder_class, (Mystic, Operative, Soldier)):
                possible_class_feats = self.character.starfinder_class.possible_selections()
                selections = self.character.starfinder_class.selection
                if isinstance(selections, str):
                    selections = [selections]
                for selection in selections:
                    if selection:
                        self.update_selection(selection, selection)
            else:
                possible_class_feats = self.character.select_new_class_feat(verbose=False)
                self.update_boxes(self.class_list_one, possible_class_feats)
        if self.class_list_two:
            possible_class_feats = self.character.select_new_class_feat(secondary=True, verbose=False)
            self.update_boxes(self.class_list_two, possible_class_feats)
        if self.class_influence:
            self.update_expertise()

    
    def update_feat_dict(self, new_feat : list[Ability]) -> None:
        """Function to keep the feat dict updated

        Args:
            new_feat (Ability): Feat that is to be checked if it already is in the dict
        """
        if not isinstance(new_feat, list):
            new_feat = [new_feat]

        for feat in new_feat:
            try:
                self.feat_dict[str(feat)]
            except KeyError:
                self.feat_dict[str(feat)] = feat

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    characte = Character()
    characte.choose_class("Envoy", None)
    characte.update_level(2)
    window = FeatForm(characte)
    window.show()
    sys.exit(app.exec_())
