from PyQt5 import QtCore, QtGui, QtWidgets
from helpers.starfinder_class_dicts import (classAbilities, classChoseFeats,
                                            class_feat_replacables, classesStatBonus)

from helpers.starfinder_dicts import skills
from helpers.ProxyModel import ProxyModel
from helpers.starfinder_theme_dicts import themeAbilities
from helpers.starfinder_race_dicts import raceAbilities
from helpers.helper import (initialize_combo, initialize_combo_model,
                            initialize_frame, initialize_text,
                            initialize_widget)


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

        for feat in classesStatBonus[self.character.class_name]["proficiencies"]:
            self.character.chosen_feats.append(feat)

        self.class_list_one = []
        self.class_list_two = []
        self.expertises = []
        self.replacables = []
        self.feats = []
        self.combats = []
        self.feat_to_add = [(self.character.class_level + 1) // 2, 0]

        self.update_class_feat_list()
        self.update_theme_feat_list()
        self.update_race_feat_list()
        self.update_feats_and_abilities()

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

        for i in range(self.character.class_level):
            for ability in classAbilities[self.character.class_name][i]:
                try:
                    boxes[boxcount].disconnect()
                except TypeError:
                    pass
                info_text = "None"

                if ability[1] in ["improvisation", "trick", "revelation", "hack"] +\
                                 ["talent", "exploit", "zenith", "gear"]:
                    # improvisation : Envoy
                    # trick : Mechanic
                    # revelation : Solarian
                    # hack : Technomancer

                    # talent : Envoy
                    # exploit : Operative
                    # zenith : Solarian
                    # gear : Soldier

                    # list_replaceables = ["Bypass", "Miracle", "Coordinated",
                    #
                    #        "Trick attack", "Quick",
                    #
                    #        "Cache capacitor", "Skill"]
                    possible_class_feats = self.character.select_new_class_feat(ability[1],
                                                self.character.class_level, verbose=False)
                    info_text = f"<<Select {ability[1].capitalize()}>>"
                    if ability[1] in ["talent", "exploit", "zenith", "gear"]:
                        self.class_list_two.append(boxes[boxcount])
                        self.update_class_list_two(ability[1])
                        self.update_boxes(ability[1], self.class_list_two, possible_class_feats)
                    else:
                        self.class_list_one.append(boxes[boxcount])
                        self.update_class_list_one(ability[1])
                        self.update_boxes(ability[1], self.class_list_one, possible_class_feats)

                elif ability[1] in ["words", "weapon", "expertise", "skills", "spell", "channel",
                                    "edge", "cpower", "feat", "combat"]:
                    info_text = "<<Fixed Feat>>"
                    possible_class_feats = [ability[0]]
                    # self.initialize_combobox(boxes[boxcount], boxcount, "<<Fixed Feat>>",
                    #                             [ability[0]])
                    if ability[1] == "expertise":
                        self.character.expertise.append("sense motive")
                    elif ability[1] == "skills":
                        for skill in ability[2]:
                            self.character.skill_misc[skill[0]] += skill[1]
                    elif ability[1] == "spell":
                        connections = classChoseFeats["mystic"]["connection"]
                        current_connection = connections[self.character.styles[0]]
                        spell_to_add = current_connection["spell"][ability[2]]
                        self.character.additional_spells[ability[2] + 1].append(spell_to_add)
                    elif ability[1] == "channel":
                        connections = classChoseFeats["mystic"]["connection"]
                        skill1, skill2 = connections[self.character.styles[0]]["skill"]
                        self.character.skill_misc[skill1] += 1
                        self.character.skill_misc[skill2] += 1
                    elif ability[1] == "edge":
                        self.character.initiative_misc += 1
                        self.character.calc_init()
                        for skill in self.character.skill_misc:
                            self.character.skill_misc[skill] += 1
                    elif ability[1] == "cpower":
                        self.class_list_one.append(boxes[boxcount])
                        connections = classChoseFeats["mystic"]["connection"]
                        mystic_styles = connections[self.character.styles[0]]
                        new_feat = mystic_styles["feat"][ability[2]]
                        possible_class_feats = new_feat

                    elif ability[1] == "feat":
                        self.character.chosen_feats.append(ability[2])
                        possible_class_feats = [ability[2]]
                    elif ability[1] == "combat":
                        self.feat_to_add[1] += 1

                elif ability[1] == "connection":
                    self.class_list_one.append(boxes[boxcount])
                    possible_class_feats = list(classChoseFeats["mystic"]["connection"])
                    info_text = f"<<Select {ability[1].capitalize()}>>"
                    self.character.styles.append(possible_class_feats[0])
                    self.character.class_feats.append(possible_class_feats[0])

                elif ability[1] == "specialization":
                    self.class_list_one.append(boxes[boxcount])
                    if ability[2][0] == "feat":
                        self.character.chosen_feats.append(ability[2][1])
                        info_text = f"<<Select {ability[1].capitalize()}>>"
                        possible_class_feats = list(classChoseFeats["operative"]["specialization"])
                        self.character.styles.append(possible_class_feats[0])
                        self.character.class_feats.append(possible_class_feats[0])
                        specialization = classChoseFeats["operative"]["specialization"]
                        skill1, skill2 = specialization[self.character.styles[0]][0]
                        self.character.chosen_feats.append(f"Skill Focus [{skill1.title()}]")
                        self.character.chosen_feats.append(f"Skill Focus [{skill2.title()}]")
                        self.character.skill_misc[skill1] += 3
                        self.character.skill_misc[skill2] += 3

                    elif ability[2][0] == "exploit":
                        specialization = classChoseFeats["operative"]["specialization"]
                        new_feat = specialization[self.character.styles[0]][1]
                        self.character.class_feats.append(new_feat[0])
                        info_text = "<<Fixed Feat>>"
                        possible_class_feats = [new_feat]

                    elif ability[2][0] == "power":
                        specialization = classChoseFeats["operative"]["specialization"]
                        new_feat = specialization[self.character.styles[0]][2]
                        self.character.class_feats.append(new_feat[0])
                        info_text = "<<Fixed Feat>>"
                        possible_class_feats = [new_feat]
                elif ability[1] == "class": # TODO needs functions connecting it
                    info_text = "<<Select Class Skill>>"
                    possible_class_feats = [x.capitalize() for x in skills]
                    self.initialize_combobox(boxes[boxcount], boxcount, info_text,
                                                possible_class_feats)
                    boxcount += 1
                    #     self.character.make_class_skill(possible_class_feats[0])
                    #     self.character.make_class_skill(possible_class_feats[0])
                    try:
                        boxes[boxcount].disconnect()
                    except TypeError:
                        pass
                elif ability[1] == "influence": # solarian # add two skills, one each from two lists
                    solarian_dicts = classChoseFeats["solarian"]
                    possible_graviton = [x.capitalize() for x in solarian_dicts["graviton"]]
                    possible_class_feats = [x.capitalize() for x in solarian_dicts["photon"]]
                    for influence in self.character.expertise:
                        if influence in possible_graviton:
                            possible_graviton.remove(influence)
                        if influence in possible_class_feats:
                            possible_class_feats.remove(influence)
                    info_text = "<<Select Graviton>>"
                    self.character.expertise.append(possible_graviton[0])
                    self.initialize_combobox(boxes[boxcount], boxcount, info_text,
                                                possible_graviton)
                    boxcount += 1
                    try:
                        boxes[boxcount].disconnect()
                    except TypeError:
                        pass
                    info_text = "<<Select Photon>>"
                    self.character.expertise.append(possible_class_feats[0])

                elif ability[1] == "add expertise": # envoy
                    # this is not shown on the excel sheet, might just ignore it then # TODO
                    possible_class_feats = ["Bluff", "Computers", "Culture", "Diplomacy",
                                            "Disguise", "Engineering", "Intimidate", "Medicine"]
                    for expertise in self.character.expertise:
                        if expertise.capitalize() in possible_class_feats:
                            possible_class_feats.remove(expertise.capitalize())
                    info_text = "<<Select Expertise>>"
                    # self.initialize_combobox(boxes[boxcount], boxcount, "<<Select Expertise>>",
                    #                             possible_class_feats)
                    self.character.expertise.append(possible_class_feats[0])
                    self.expertises.append(boxes[boxcount])
                    self.update_expertise()
                    self.update_boxes("expertise", self.expertises, possible_class_feats)
                elif ability[1] == "style": # there's 2 styles they need to be connected
                    possible_class_feats = [x.capitalize()
                                            for x in classChoseFeats["soldier"]["styles"]]
                    for style in self.character.styles:
                        possible_class_feats.remove(style)
                    self.character.styles.append(possible_class_feats[0])
                    self.character.class_feats.append(possible_class_feats[0])
                    info_text = "<<Select Style>>"

                elif ability[1] == "technique1":
                    soldier_style = classChoseFeats["soldier"]["styles"]
                    soldier_style = soldier_style[self.character.styles[0].lower()]
                    new_feat = soldier_style[i + 1]
                    info_text = "<<Fixed Feat>>"
                    possible_class_feats = [new_feat]

                elif ability[1] == "technique2":
                    soldier_style = classChoseFeats["soldier"]["styles"]
                    soldier_style = soldier_style[self.character.styles[1].lower()]
                    new_feat = soldier_style[i - 8 + 1]
                    info_text = "<<Fixed Feat>>"
                    possible_class_feats = [new_feat]

                elif ability[1] in ["None"]:
                    pass

                tmp = next((s for s in class_feat_replacables if s in ability[0]), None)
                if tmp:
                    if self.update_feat_text(ability[0], info_text):
                        continue
                    self.replacables.append(boxes[boxcount])



                if info_text != "None":
                    self.initialize_combobox(boxes[boxcount], boxcount, info_text,
                                                possible_class_feats)
                    if ability[1] == "specialization":
                        if ability[2][0] == "feat":
                            boxes[boxcount].activated[str].connect(self.update_specialization)
                    elif ability[1] == "connection":
                        boxes[boxcount].activated[str].connect(self.update_connection)
                    boxcount += 1

    def update_connection(self):
        """function to update the mystic connection
        """
        old_specialization = self.character.styles[0]
        feat_index = self.character.class_feats.index(old_specialization)
        specializations = classChoseFeats["mystic"]["connection"]
        for i, box in enumerate(self.class_list_one):
            model = QtGui.QStandardItemModel()
            current_item = box.currentText()
            if i == 0:
                self.character.styles[0] = current_item
                self.character.class_feats[feat_index] = current_item
                for feat in list(dict.fromkeys([current_item] + list(specializations))):
                    model.appendRow(QtGui.QStandardItem(feat))
                box.setModel(ProxyModel(model, "<<Select Connection>>"))
                box.setCurrentIndex(1)

            if i in [1, 2, 3, 4, 5, 6, 7]:
                new_feat = specializations[self.character.styles[0]]["feat"][i - 1][0]
                old_feat_index = self.character.class_feats.index(current_item)
                self.character.class_feats[old_feat_index] = new_feat
                model.appendRow(QtGui.QStandardItem(new_feat))
                box.setModel(ProxyModel(model, "<<Fixed Feat>>"))
                box.setCurrentIndex(1)

    def update_feat_text(self, new_text : str, model_default : str) -> bool:
        """function that takes the replacable box list and checks if any box present contains
        similar language to what is to be replaced. Should a box have similar text that text
        is to be replaced with the new text. If none of the boxes have the text the combobox
        should be initialized. Probably needs to have a return.

        Args:
            new_text (str): text that is to be added to the feats. If it already exists somewhere
                            this text replaces that text
            model_default (str): used for the model. If possible remove this down the line

        Returns:
            bool : if a replacement happened or not
        """

        # tmp = next((s for s in class_feat_replacables if s in j[0]), None)

        # if tmp:
        #     index = class_feat_replacables.index(tmp)

        for box in self.replacables:
            tmp = next((s for s in class_feat_replacables if s in box.currentText()), None)

            if tmp:
                class_model = QtGui.QStandardItemModel()
                class_model.appendRow(QtGui.QStandardItem(new_text))
                box.setModel(ProxyModel(class_model, model_default))
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
            class_model.appendRow(QtGui.QStandardItem(feat))
        box.setModel(ProxyModel(class_model, model_default))
        box.setCurrentIndex(1)
        box.activated[str].connect(self.update_feat)
        self.character.class_feats.append(possible_class_feats[0])
        box.setProperty("class_feat_index", index)

    def update_class_list_one(self, key : str) -> None:
        """update the class_feat_function for the first class list feats

        Args:
            key (str): key for the select_new_class_feat function
        """
        for box in self.class_list_one:
            box.setProperty("class_feat_function", [key, self.class_list_one])

    def update_class_list_two(self, key : str) -> None:
        """update the class_feat_function for talents

        Args:
            key (str): key for the select_new_class_feat function
        """
        for box in self.class_list_two:
            box.setProperty("class_feat_function", [key, self.class_list_two])

    def update_expertise(self) -> None:
        """update the class_feat_function for expertise
        """
        for box in self.expertises:
            box.setProperty("class_feat_function", ["expertise", self.expertises])

    def update_specialization(self):
        """function to handle the three boxes of the operative that depend on the specialization
        """
        old_specialization = self.character.styles[0]
        feat_index = self.character.class_feats.index(old_specialization)
        specializations = classChoseFeats["operative"]["specialization"]
        for i, box in enumerate(self.class_list_one):
            model = QtGui.QStandardItemModel()
            current_item = box.currentText()
            if i == 0:
                self.character.styles[0] = current_item
                self.character.class_feats[feat_index] = current_item
                for feat in list(dict.fromkeys([current_item] + list(specializations))):
                    model.appendRow(QtGui.QStandardItem(feat))
                box.setModel(ProxyModel(model, "<<Select Specialization>>"))
                box.setCurrentIndex(1)

                old_skill1, old_skill2 = specializations[old_specialization][0]
                skill1, skill2 = specializations[self.character.styles[0]][0]
                self.character.skill_misc[old_skill1] -= 3
                self.character.skill_misc[old_skill2] -= 3
                self.character.skill_misc[skill1] += 3
                self.character.skill_misc[skill2] += 3
            if i in [1, 2]:
                new_feat = specializations[self.character.styles[0]][i]
                old_feat_index = self.character.class_feats.index(current_item)
                self.character.class_feats[old_feat_index] = new_feat
                model.appendRow(QtGui.QStandardItem(new_feat))
                box.setModel(ProxyModel(model, "<<Fixed Feat>>"))
                box.setCurrentIndex(1)

    def update_boxes(self, feat_type : str, feat_list : list, possible_feats : list) -> None:
        """update all selectable feat class comboboxes

        Args:
            feat_type (str): the type of feat that should be checked in the select_new(_class)_feat
            feat_list (list): list of comboboxes that are to be updated
            possible_feats (list): list of options that can be entered
        """
        for box in feat_list:
            model = QtGui.QStandardItemModel()
            current_item = box.currentText()
            model.appendRow(QtGui.QStandardItem(current_item))
            for feat in possible_feats:
                model.appendRow(QtGui.QStandardItem(feat))
            box.setModel(ProxyModel(model, f"<<Select {feat_type.capitalize()}>>"))
            box.setCurrentIndex(1)

    def update_feat(self, selected_feat : str) -> None:
        """replace the class feat with the newly selected class feat

        Args:
            selected_feat (str): feat selected in the combobox
        """
        combo = self.sender()
        index = combo.property("class_feat_index")
        feat_function = combo.property("class_feat_function")
        feat_text = self.character.class_feats[index]
        self.character.class_feats[index] = selected_feat
        if feat_function:
            if feat_function[0] != "expertise":
                possible_class_feats = self.character.select_new_class_feat(feat_function[0],
                                            self.character.class_level, verbose=False)

            else:
                index = self.character.expertise.index(feat_text)
                self.character.expertise[index] = selected_feat
                possible_class_feats = ["Bluff", "Computers", "Culture", "Diplomacy", "Disguise",
                                          "Engineering", "Intimidate", "Medicine"]
                for expertise in self.character.expertise:
                    if expertise.capitalize() in possible_class_feats:
                        possible_class_feats.remove(expertise.capitalize())
            self.update_boxes(*feat_function, possible_class_feats)

    def update_chose_feats(self, selected_feat : str) -> None:
        """function to handle chosen feat updates

        Args:
            selected_feat (str): new selected feat
        """
        combo = self.sender()
        index = combo.property("feat_index")
        self.character.chosen_feats[index] = selected_feat
        possible_class_feats = self.character.select_new_feat(gui=True)
        self.update_boxes("Feat", self.feats, possible_class_feats)

    def update_chose_combat_feats(self, selected_feat : str) -> None:
        """function to handle chosen combat feat updates

        Args:
            selected_feat (str): new selected combat feat
        """
        combo = self.sender()
        index = combo.property("feat_index")
        self.character.chosen_feats[index] = selected_feat
        possible_class_feats = self.character.select_new_feat(combat=True, gui=True)
        self.update_boxes("Combat Feat", self.combats, possible_class_feats)


    def update_theme_feat_list(self):
        """function that uptates the theme feats of the character in the GUI
        """
        boxes = [self.theme1, self.theme2, self.theme3, self.theme4]
        character_themes = themeAbilities[self.character.theme]
        if self.character.class_level >= 1:
            initialize_combo_model(boxes[0], [character_themes[0][0]],
                                    "<<Theme Feat>>", index=1)
        if self.character.class_level >= 6:
            initialize_combo_model(boxes[1], [character_themes[1][0]],
                                    "<<Theme Feat>>", index=1)
        if self.character.class_level >= 12:
            initialize_combo_model(boxes[2], [character_themes[2][0]],
                                    "<<Theme Feat>>", index=1)
        if self.character.class_level >= 18:
            initialize_combo_model(boxes[3], [character_themes[3][0]],
                                    "<<Theme Feat>>", index=1)

    def update_race_feat_list(self):
        """function that updates the race feats of the character in the GUI
        """
        boxes = [self.race1, self.race2, self.race3, self.race4]
        character_races = raceAbilities[self.character.race_name]
        for feat, box in zip(character_races, boxes):
            initialize_combo_model(box, [feat[0]], "<<Race Feat>>", index=1)
            if feat[1] == "feat":
                self.feat_to_add[0] += 1
            elif feat[1] == "spell":
                pass
            elif feat[1] == "stats": # TODO needs logic
                pass
            elif feat[1] == "words":
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

        normal_feats = self.character.select_new_feat(gui=True)
        normal_feat, combat_feat = self.feat_to_add
        for _ in range(normal_feat):
            self.feats.append(boxes[boxcount])
            initialize_combo_model(boxes[boxcount], normal_feats, "<<Select Feat>>",
                                    index=1, connection=self.update_chose_feats)
            boxes[boxcount].setProperty("feat_index", len(self.feats))
            normal_feats.pop(0)
            boxcount += 1
        self.update_boxes("Feat", self.feats, normal_feats)

        combat_feats = self.character.select_new_feat(combat=True, gui=True)
        for _ in range(combat_feat):
            self.combats.append(boxes[boxcount])
            initialize_combo_model(boxes[boxcount], combat_feats, "<<Select Combat Feat>>",
                                    index=1, connection=self.update_chose_combat_feats)
            boxes[boxcount].setProperty("feat_index", len(self.combats))
            combat_feats.pop(0)
            boxcount += 1
        self.update_boxes("Combat Feat", self.combats, combat_feats)
