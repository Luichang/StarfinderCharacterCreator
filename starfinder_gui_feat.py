from PyQt5 import QtCore, QtGui, QtWidgets
from helpers.ability import Ability
from helpers.ProxyModel import ProxyModel
from helpers.helper import (initialize_combo, initialize_combo_model,
                            initialize_frame, initialize_text,
                            initialize_widget)
from starfinder_classes.starfinder_mystic import Mystic
from starfinder_classes.starfinder_operative import Operative
from starfinder_classes.starfinder_soldier import Soldier
from starfinder_feats.starfinder_feat_type import FeatType


class FeatForm(QtWidgets.QWidget):
    """UI Class to display the character Feats

    Args:
        QtWidgets (_type_): _description_
    """
    def __init__(self, character, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setGeometry(200,200,840,650)

        self.centralwidget = QtWidgets.QFrame()
        self.centralwidget.resize(821, 635)

        layout=QtWidgets.QVBoxLayout()
        layout.addWidget(self.centralwidget)
        self.setLayout(layout)
        self.setWindowTitle("Character Feats")

        self.character = character

        self.skillframe = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.skillframe, "Skillframe", [20, 10, 781, 221])
        self.grid_layout_widget_2 = QtWidgets.QWidget(self.skillframe)
        initialize_widget(self.grid_layout_widget_2, "gridLayoutWidget_2", [10, 10, 761, 201])
        self.skills_score_grid = QtWidgets.QGridLayout(self.grid_layout_widget_2)
        self.skills_score_grid.setContentsMargins(0, 0, 0, 0)
        self.skills_score_grid.setObjectName("SkillsScoreGrid")

        self.class_ability_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.class_ability_text, "ClassAbilityText", "Class Abilities", [70, 25])
        self.skills_score_grid.addWidget(self.class_ability_text, 0, 0, 1, 1)
        self.class1 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class1, "Class1", [], [184, 20])
        self.skills_score_grid.addWidget(self.class1, 1, 0, 1, 1)
        self.class2 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class2, "Class2", [], [184, 20])
        self.skills_score_grid.addWidget(self.class2, 1, 1, 1, 1)
        self.class3 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class3, "Class3", [], [184, 20])
        self.skills_score_grid.addWidget(self.class3, 1, 2, 1, 1)
        self.class4 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class4, "Class4", [], [184, 20])
        self.skills_score_grid.addWidget(self.class4, 1, 3, 1, 1)
        self.class5 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class5, "Class5", [], [184, 20])
        self.skills_score_grid.addWidget(self.class5, 2, 0, 1, 1)
        self.class6 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class6, "Class6", [], [184, 20])
        self.skills_score_grid.addWidget(self.class6, 2, 1, 1, 1)
        self.class7 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class7, "Class7", [], [184, 20])
        self.skills_score_grid.addWidget(self.class7, 2, 2, 1, 1)
        self.class8 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class8, "Class8", [], [184, 20])
        self.skills_score_grid.addWidget(self.class8, 2, 3, 1, 1)
        self.class9 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class9, "Class9", [], [184, 20])
        self.skills_score_grid.addWidget(self.class9, 3, 0, 1, 1)
        self.class10 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class10, "Class10", [], [184, 20])
        self.skills_score_grid.addWidget(self.class10, 3, 1, 1, 1)
        self.class11 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class11, "Class11", [], [184, 20])
        self.skills_score_grid.addWidget(self.class11, 3, 2, 1, 1)
        self.class12 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class12, "Class12", [], [184, 20])
        self.skills_score_grid.addWidget(self.class12, 3, 3, 1, 1)
        self.class13 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class13, "Class13", [], [184, 20])
        self.skills_score_grid.addWidget(self.class13, 4, 0, 1, 1)
        self.class14 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class14, "Class14", [], [184, 20])
        self.skills_score_grid.addWidget(self.class14, 4, 1, 1, 1)
        self.class15 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class15, "Class15", [], [184, 20])
        self.skills_score_grid.addWidget(self.class15, 4, 2, 1, 1)
        self.class16 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class16, "Class16", [], [184, 20])
        self.skills_score_grid.addWidget(self.class16, 4, 3, 1, 1)
        self.class17 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class17, "Class17", [], [184, 20])
        self.skills_score_grid.addWidget(self.class17, 5, 0, 1, 1)
        self.class18 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class18, "Class18", [], [184, 20])
        self.skills_score_grid.addWidget(self.class18, 5, 1, 1, 1)
        self.class19 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class19, "Class19", [], [184, 20])
        self.skills_score_grid.addWidget(self.class19, 5, 2, 1, 1)
        self.class20 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class20, "Class20", [], [184, 20])
        self.skills_score_grid.addWidget(self.class20, 5, 3, 1, 1)
        self.class21 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class21, "Class21", [], [184, 20])
        self.skills_score_grid.addWidget(self.class21, 6, 0, 1, 1)
        self.class22 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class22, "Class22", [], [184, 20])
        self.skills_score_grid.addWidget(self.class22, 6, 1, 1, 1)
        self.class23 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class23, "Class23", [], [184, 20])
        self.skills_score_grid.addWidget(self.class23, 6, 2, 1, 1)
        self.class24 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class24, "Class24", [], [184, 20])
        self.skills_score_grid.addWidget(self.class24, 6, 3, 1, 1)
        self.class25 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class25, "Class25", [], [184, 20])
        self.skills_score_grid.addWidget(self.class25, 7, 0, 1, 1)
        self.class26 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class26, "Class26", [], [184, 20])
        self.skills_score_grid.addWidget(self.class26, 7, 1, 1, 1)
        self.class27 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class27, "Class27", [], [184, 20])
        self.skills_score_grid.addWidget(self.class27, 7, 2, 1, 1)
        self.class28 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.class28, "Class28", [], [184, 20])
        self.skills_score_grid.addWidget(self.class28, 7, 3, 1, 1)

        self.skillframe_2 = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.skillframe_2, "Skillframe_2", [20, 240, 781, 71])
        self.grid_layout_widget_3 = QtWidgets.QWidget(self.skillframe_2)
        initialize_widget(self.grid_layout_widget_3, "gridLayoutWidget_3", [10, 10, 761, 51])
        self.skills_score_grid_2 = QtWidgets.QGridLayout(self.grid_layout_widget_3)
        self.skills_score_grid_2.setContentsMargins(0, 0, 0, 0)
        self.skills_score_grid_2.setObjectName("SkillsScoreGrid_2")

        self.theme_ability_text = QtWidgets.QLabel(self.grid_layout_widget_3)
        initialize_text(self.theme_ability_text, "ThemeAbilityText", "Theme Abilities", max_size=[70,25])
        self.skills_score_grid_2.addWidget(self.theme_ability_text, 0, 0, 1, 1)


        self.theme1 = QtWidgets.QComboBox(self.grid_layout_widget_3)
        initialize_combo(self.theme1, "Theme1", [], [184, 20])
        self.skills_score_grid_2.addWidget(self.theme1, 1, 0, 1, 1)
        self.theme2 = QtWidgets.QComboBox(self.grid_layout_widget_3)
        initialize_combo(self.theme2, "Theme2", [], [184, 20])
        self.skills_score_grid_2.addWidget(self.theme2, 1, 1, 1, 1)
        self.theme3 = QtWidgets.QComboBox(self.grid_layout_widget_3)
        initialize_combo(self.theme3, "Theme3", [], [184, 20])
        self.skills_score_grid_2.addWidget(self.theme3, 1, 2, 1, 1)
        self.theme4 = QtWidgets.QComboBox(self.grid_layout_widget_3)
        initialize_combo(self.theme4, "Theme4", [], [184, 20])
        self.skills_score_grid_2.addWidget(self.theme4, 1, 3, 1, 1)

        self.skillframe_3 = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.skillframe_3, "Skillframe_3", [20, 320, 781, 71])
        self.grid_layout_widget_4 = QtWidgets.QWidget(self.skillframe_3)
        initialize_widget(self.grid_layout_widget_4, "gridLayoutWidget_4", [10, 10, 761, 51])
        self.skills_score_grid_4 = QtWidgets.QGridLayout(self.grid_layout_widget_4)
        self.skills_score_grid_4.setContentsMargins(0, 0, 0, 0)
        self.skills_score_grid_4.setObjectName("SkillsScoreGrid_4")

        self.race_ability_text = QtWidgets.QLabel(self.grid_layout_widget_4)
        initialize_text(self.race_ability_text, "RaceAbilityText", "Race Abilities", [70, 25])
        self.skills_score_grid_4.addWidget(self.race_ability_text, 0, 0, 1, 1)
        self.race1 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        initialize_combo(self.race1, "Race1", [], [184, 20])
        self.skills_score_grid_4.addWidget(self.race1, 1, 0, 1, 1)
        self.race2 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        initialize_combo(self.race2, "Race2", [], [184, 20])
        self.skills_score_grid_4.addWidget(self.race2, 1, 1, 1, 1)
        self.race3 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        initialize_combo(self.race3, "Race3", [], [184, 20])
        self.skills_score_grid_4.addWidget(self.race3, 1, 2, 1, 1)
        self.race4 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        initialize_combo(self.race4, "Race4", [], [184, 20])
        self.skills_score_grid_4.addWidget(self.race4, 1, 3, 1, 1)

        self.skillframe_4 = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.skillframe_4, "Skillframe_4", [20, 400, 781, 221])
        self.grid_layout_widget_5 = QtWidgets.QWidget(self.skillframe_4)
        initialize_widget(self.grid_layout_widget_5, "gridLayoutWidget_5", [10, 10, 761, 201])
        self.skills_score_grid_5 = QtWidgets.QGridLayout(self.grid_layout_widget_5)
        self.skills_score_grid_5.setContentsMargins(0, 0, 0, 0)
        self.skills_score_grid_5.setObjectName("SkillsScoreGrid_5")

        self.feats_text = QtWidgets.QLabel(self.grid_layout_widget_5)
        initialize_text(self.feats_text, "FeatsText", "Feats and Proficiencies", [113, 25])
        self.skills_score_grid_5.addWidget(self.feats_text, 0, 0, 1, 1)
        self.feats1 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats1, "Feats1", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats1, 1, 0, 1, 1)
        self.feats2 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats2, "Feats2", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats2, 1, 1, 1, 1)
        self.feats3 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats3, "Feats3", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats3, 1, 2, 1, 1)
        self.feats4 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats4, "Feats4", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats4, 1, 3, 1, 1)
        self.feats5 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats5, "Feats5", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats5, 2, 0, 1, 1)
        self.feats6 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats6, "Feats6", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats6, 2, 1, 1, 1)
        self.feats7 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats7, "Feats7", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats7, 2, 2, 1, 1)
        self.feats8 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats8, "Feats8", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats8, 2, 3, 1, 1)
        self.feats9 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats9, "Feats9", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats9, 3, 0, 1, 1)
        self.feats10 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats10, "Feats10", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats10, 3, 1, 1, 1)
        self.feats11 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats11, "Feats11", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats11, 3, 2, 1, 1)
        self.feats12 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats12, "Feats12", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats12, 3, 3, 1, 1)
        self.feats13 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats13, "Feats13", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats13, 4, 0, 1, 1)
        self.feats14 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats14, "Feats14", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats14, 4, 1, 1, 1)
        self.feats15 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats15, "Feats15", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats15, 4, 2, 1, 1)
        self.feats16 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats16, "Feats16", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats16, 4, 3, 1, 1)
        self.feats17 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats17, "Feats17", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats17, 5, 0, 1, 1)
        self.feats18 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats18, "Feats18", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats18, 5, 1, 1, 1)
        self.feats19 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats19, "Feats19", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats19, 5, 2, 1, 1)
        self.feats20 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats20, "Feats20", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats20, 5, 3, 1, 1)
        self.feats21 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats21, "Feats21", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats21, 6, 0, 1, 1)
        self.feats22 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats22, "Feats22", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats22, 6, 1, 1, 1)
        self.feats23 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats23, "Feats23", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats23, 6, 2, 1, 1)
        self.feats24 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats24, "Feats24", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats24, 6, 3, 1, 1)
        self.feats25 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats25, "Feats25", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats25, 7, 0, 1, 1)
        self.feats26 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats26, "Feats26", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats26, 7, 1, 1, 1)
        self.feats27 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats27, "Feats27", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats27, 7, 2, 1, 1)
        self.feats28 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.feats28, "Feats28", [], [184, 20])
        self.skills_score_grid_5.addWidget(self.feats28, 7, 3, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(self.centralwidget)

        # for feat in self.character.class_name.proficiencies:
        #     self.character.chosen_feats.append(feat)

        self.class_list_one = []
        self.class_list_two = []
        self.class_influence = []
        self.class_abilities = []
        self.replacables = []
        self.feats = []
        self.combats = []
        self.feat_to_add = [(self.character.class_level + 1) // 2, 0]
        self.feat_dict = {}

        # self.update_class_feat_list()
        # self.update_theme_feat_list()
        # self.update_race_feat_list()
        # self.update_feats_and_abilities()

    def update_class_feat_list(self):
        """does some class feature related update

        """

        boxes = [self.class1, self.class2, self.class3, self.class4, self.class5,
                 self.class6, self.class7, self.class8, self.class9, self.class10,
                 self.class11, self.class12, self.class13, self.class14, self.class15,
                 self.class16, self.class17, self.class18, self.class19, self.class20,
                 self.class21, self.class22, self.class23, self.class24, self.class25,
                 self.class26, self.class27, self.class28]
        boxcount = 0

        for ability in self.character.class_name.current_abilities(self.character.class_level):
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
                    if str(self.character.class_name) == "Mystic":
                        spell_to_add = possible_class_feats[0]
                        spell_level = spell_to_add.level
                        self.character.spells[spell_level].append(spell_to_add)
                    self.class_list_one.append(boxes[boxcount])
                    self.update_class_list_one()
                elif ability.get_type() == FeatType.COMBAT:
                    self.feat_to_add[1] += 1
                elif ability.get_type() == FeatType.CPOWER:
                    skill_to_add = self.character.class_name.connection_feat()
                    self.character.class_feats.append(skill_to_add[ability.level//3])
                elif ability.get_type() == FeatType.SPELL:
                    skill_to_add = self.character.class_name.connection_spell()
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
                possible_class_feats = self.character.class_name.new_expertises(self.character.expertise)
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
                self.character.class_name.bonuses.append(possible_class_feats[0])
                length = len(self.character.class_name.bonuses) - 1
                self.initialize_combobox(boxes[boxcount], length,
                                            info_text, possible_class_feats)
                boxcount += 1
                self.class_abilities.append(boxes[boxcount])
                self.character.class_name.bonuses.append(possible_class_feats[0])
                self.update_class_abilities()

            elif ability.get_type() == FeatType.SELECTION:
                possible_class_feats = self.character.class_name.possible_selections()
                if isinstance(self.character.class_name.selection, list):
                    for selection in self.character.class_name.selection:
                        if selection:
                            possible_class_feats.remove(selection)
                info_text = f"<<Select {str(ability)}>>"
                self.character.class_name.select_selection(possible_class_feats[0], (ability.level - 1) % 7)
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
                    length = len(self.character.class_name.bonuses) - 1
                self.initialize_combobox(boxes[boxcount], length,
                                            info_text, possible_class_feats)
                boxcount += 1

        if self.class_list_one:
            if isinstance(self.character.class_name, (Mystic, Operative, Soldier)):
                possible_class_feats = self.character.class_name.possible_selections()
                selections = self.character.class_name.selection
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


    def update_feat_text(self, old_feat : Ability, new_feat : Ability) -> bool:
        """function that takes the replacable box list and checks if any box present contains
        similar language to what is to be replaced. Should a box have similar text that text
        is to be replaced with the new text. If none of the boxes have the text the combobox
        should be initialized. Probably needs to have a return.

        Args:
            new_feat (Ability): text that is to be added to the feats. If it already exists
                                somewhere this text replaces that text

        Returns:
            bool : if a replacement happened or not
        """

        for box in self.replacables:
            tmp = box.currentText() == str(old_feat)

            if tmp:
                class_model = QtGui.QStandardItemModel()
                class_model.appendRow(QtGui.QStandardItem(str(new_feat)))
                placeholder = box.model().data(box.model().index(0,0))
                box.setModel(ProxyModel(class_model, placeholder))
                box.setCurrentIndex(1)
                return True
        return False

    def initialize_combobox(self, box : QtWidgets.QComboBox, index : int, model_default : str,
                            possible_class_feats : list) -> None:
        """Initialize the entered combobox

        Args:
            box (QtWidgets.QComboBox): combobox that is to initialized
            index (int): index of the combobox/feat
            feat_type (str): Text that indicates the feat grouping
            possible_class_feats (list): list of possible feats
        """
        class_model = QtGui.QStandardItemModel()
        for feat in possible_class_feats:
            class_model.appendRow(QtGui.QStandardItem(str(feat)))
        box.setModel(ProxyModel(class_model, model_default))
        box.setCurrentIndex(1)
        box.activated[str].connect(self.update_feat)
        box.setProperty("class_feat_index", index)

    def update_class_list_one(self) -> None:
        """update the class_feat_function for the first class list feats
        """
        for box in self.class_list_one:
            box.setProperty("class_feat_function", [1, self.class_list_one])

    def update_class_list_two(self) -> None:
        """update the class_feat_function for talents
        """
        for box in self.class_list_two:
            box.setProperty("class_feat_function", [2, self.class_list_two])

    def update_influence(self) -> None:
        """update the class_feat_function for expertise
        """
        for box in self.class_influence:
            box.setProperty("class_feat_function", [3, self.class_influence])

    def update_class_abilities(self) -> None:
        """update the class_feat_function for expertise
        """
        for box in self.class_abilities:
            box.setProperty("class_feat_function", [4, self.class_abilities])

    def update_expertise(self):
        """function to update relevant expertise boxes
        """
        possible_class_feats = self.character.class_name.new_expertises(self.character.expertise)
        if isinstance(possible_class_feats[0], list):
            self.update_boxes(self.class_influence[::2], possible_class_feats[0])
            self.update_boxes(self.class_influence[1::2], possible_class_feats[1])
        else:
            self.update_boxes(self.class_influence, possible_class_feats)

    def update_class_ability_list(self, selected_ability : str):
        """function to update relevant class ability boxes
        """
        possible_abilities = list(self.character.skills)
        possible_abilities.remove(selected_ability)
        self.update_boxes(self.class_abilities, possible_abilities)

    def update_selection(self, old_selection : str, new_selection : str) -> None:
        """function to update the technique boxes. Only needed for Operative, Soldier and Mystic

        Args:
            old_selection (str): old selection
            new_selection (str): new selection
        """
        list_to_check = self.class_list_one
        selections = self.character.class_name.selection
        index = selections.index(old_selection)
        old_technique_dict = self.character.class_name.style_combat(index)
        self.character.class_name.select_selection(new_selection, index)
        possible_class_feats = self.character.class_name.possible_selections()
        selections = self.character.class_name.selection
        new_technique_dict = self.character.class_name.style_combat(index)
        if isinstance(selections, str):
            selections = [selections]
        for selection in selections:
            if selection:
                possible_class_feats.remove(selection)
        selection_boxes = [box for box in list_to_check if box.currentText() in selections + [new_selection]]
        self.update_boxes(selection_boxes, possible_class_feats)
        if len(list_to_check) > 1:
            info_text = "<<Fixed Feat>>"
            for box in list_to_check[1:]:
                index = box.property("class_feat_index")
                feat_text = self.character.other_abilities[index]
                old_technique_key_list = list(old_technique_dict.keys())
                old_technique_val_list = list(old_technique_dict.values())
                try:
                    tmp = old_technique_val_list.index(feat_text)
                except ValueError:
                    continue
                level = old_technique_key_list[tmp]
                selected_feat = new_technique_dict[level]
                if isinstance(selected_feat, list):
                    level_list = [-7, -4, -1, 2, 5, 8]
                    try:
                        next_element = level_list[level_list.index(level) + 1]
                        if (self.character.class_level - 8) > next_element:
                            selected_feat = selected_feat[0]
                        else:
                            selected_feat = selected_feat[1]
                    except IndexError:
                        pass
                if str(self.character.class_name) == "Mystic":
                    spell_to_add = selected_feat
                    spell_level = spell_to_add.level
                    self.spells[spell_level][0] = spell_to_add
                self.update_feat_dict(selected_feat)
                self.character.other_abilities[index] = selected_feat
                self.initialize_combobox(box, index, info_text, [selected_feat])


    def update_boxes(self, feat_list : list, possible_feats : list) -> None:
        """update all selectable feat class comboboxes

        Args:
            feat_list (list): list of comboboxes that are to be updated
            possible_feats (list): list of options that can be entered
        """
        for box in feat_list:
            model = QtGui.QStandardItemModel()
            current_item = box.currentText()
            model.appendRow(QtGui.QStandardItem(current_item))
            for feat in possible_feats:
                model.appendRow(QtGui.QStandardItem(str(feat)))
            placeholder = box.model().data(box.model().index(0,0))
            box.setModel(ProxyModel(model, placeholder))
            box.setCurrentIndex(1)

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

    def update_feat(self, selected_feat : str) -> None:
        """replace the class feat with the newly selected class feat

        Args:
            selected_feat (str): feat selected in the combobox
        """
        combo = self.sender()
        index = combo.property("class_feat_index")
        feat_function = combo.property("class_feat_function")
        if feat_function:
            if feat_function[0] == 3:
                self.character.expertise[index] = selected_feat
                self.update_expertise()
                return
            elif feat_function[0] == 4:
                self.character.class_name.bonuses[index] = selected_feat
                self.update_class_ability_list(selected_feat)
                return
            feat_text = self.character.other_abilities[index]
            if feat_function[0] == 1:
                self.character.other_abilities[index] = self.feat_dict[selected_feat]
                if isinstance(self.character.class_name, (Mystic, Operative, Soldier)):
                    self.update_selection(feat_text, selected_feat)
                    return
                possible_class_feats = self.character.select_new_class_feat(verbose=False)
            elif feat_function[0] == 2:
                possible_class_feats = self.character.select_new_class_feat(secondary=True,
                                                                            verbose=False)
            self.update_boxes(feat_function[1], possible_class_feats)
        self.character.other_abilities[index] = self.feat_dict[selected_feat]

    def update_chose_feats(self, selected_feat : Ability) -> None:
        """function to handle chosen feat updates

        Args:
            selected_feat (Ability): new selected feat
        """
        combo = self.sender()
        index = combo.property("feat_index")
        self.character.chosen_feats[index] = self.feat_dict[selected_feat]
        possible_class_feats = self.character.select_new_feat(verbose=False)
        self.update_boxes(self.feats, possible_class_feats)
        possible_class_feats = self.character.select_new_feat(combat=True, verbose=False)
        self.update_boxes(self.combats, possible_class_feats)

    def update_chose_combat_feats(self, selected_feat : Ability) -> None:
        """function to handle chosen combat feat updates

        Args:
            selected_feat (Ability): new selected combat feat
        """
        combo = self.sender()
        index = combo.property("feat_index")
        self.character.chosen_feats[index] = self.feat_dict[selected_feat]
        possible_class_feats = self.character.select_new_feat(combat=True, verbose=False)
        self.update_boxes(self.combats, possible_class_feats)
        possible_class_feats = self.character.select_new_feat(verbose=False)
        self.update_boxes(self.feats, possible_class_feats)


    def update_theme_feat_list(self): # TODO needs logic for the skill increases
        """function that uptates the theme feats of the character in the GUI
        """
        boxes = [self.theme1, self.theme2, self.theme3, self.theme4]
        if self.character.class_level >= 1:
            initialize_combo_model(boxes[0], [str(self.character.theme.abilities[0])],
                                    "<<Theme Feat>>", index=1)
        if self.character.class_level >= 6:
            initialize_combo_model(boxes[1], [str(self.character.theme.abilities[1])],
                                    "<<Theme Feat>>", index=1)
        if self.character.class_level >= 12:
            initialize_combo_model(boxes[2], [str(self.character.theme.abilities[2])],
                                    "<<Theme Feat>>", index=1)
            if self.character.theme.abilities[2].get_type() == FeatType.SPELL:
                self.character.additional_spells[1].append(["MYSTICSPELL"])

        if self.character.class_level >= 18:
            initialize_combo_model(boxes[3], [str(self.character.theme.abilities[3])],
                                    "<<Theme Feat>>", index=1)

    def update_race_feat_list(self):
        """function that updates the race feats of the character in the GUI
        """
        boxes = [self.race1, self.race2, self.race3, self.race4]
        for feat, box in zip(self.character.race_name.abilities, boxes):
            initialize_combo_model(box, [str(feat)], "<<Race Feat>>", index=1)
            if feat.get_type() == FeatType.FEAT:
                self.feat_to_add[0] += 1
            elif feat.get_type() == FeatType.SPELL:
                for j in range(2):
                    for spell in self.character.race_name.spells[j]:
                        if spell not in self.character.additional_spells[j]:
                            self.character.additional_spells[j].append(spell)
            elif feat.get_type() == FeatType.STATS: # TODO needs logic
                pass
            elif feat.get_type() == FeatType.WORDS:
                pass

    def update_feats_and_abilities(self):
        """function that updates the feats and abilities tab of the character in the GUI
        """
        boxes = [self.feats1, self.feats2, self.feats3, self.feats4, self.feats5,
                 self.feats6, self.feats7, self.feats8, self.feats9, self.feats10,
                 self.feats11, self.feats12, self.feats13, self.feats14, self.feats15,
                 self.feats16, self.feats17, self.feats18, self.feats19, self.feats20,
                 self.feats21, self.feats22, self.feats23, self.feats24, self.feats25,
                 self.feats26, self.feats27, self.feats28]

        boxcount = 0
        for current_chosen_feat in self.character.chosen_feats:
            initialize_combo_model(boxes[boxcount], [current_chosen_feat], "<<Fixed Feat>>",
                                    index=1)
            boxcount += 1

        normal_feats = self.character.select_new_feat(verbose=False)
        self.update_feat_dict(normal_feats)
        normal_feat, combat_feat = self.feat_to_add
        for _ in range(normal_feat):
            self.feats.append(boxes[boxcount])
            initialize_combo_model(boxes[boxcount], normal_feats, "<<Select Feat>>",
                                    index=1, connection=self.update_chose_feats)
            boxes[boxcount].setProperty("feat_index", len(self.character.chosen_feats))
            selected_feat = normal_feats.pop(0)
            self.character.chosen_feats.append(selected_feat)
            boxcount += 1
        self.update_boxes(self.feats, normal_feats)

        combat_feats = self.character.select_new_feat(combat=True, verbose=False)
        self.update_feat_dict(combat_feats)
        for _ in range(combat_feat):
            self.combats.append(boxes[boxcount])
            initialize_combo_model(boxes[boxcount], combat_feats, "<<Select Combat Feat>>",
                                    index=1, connection=self.update_chose_combat_feats)
            boxes[boxcount].setProperty("feat_index", len(self.character.chosen_feats))
            selected_feat = combat_feats.pop(0)
            self.character.chosen_feats.append(selected_feat)
            boxcount += 1
        self.update_boxes(self.combats, combat_feats)
