from PyQt5 import QtCore, QtGui, QtWidgets
from helpers.starfinder_class_dicts import (classAbilities, classChoseFeats,
                                            class_feat_replacables, classesStatBonus)

from helpers.starfinder_dicts import skills
from helpers.ProxyModel import ProxyModel
from helpers.starfinder_theme_dicts import themeAbilities
from helpers.starfinder_race_dicts import raceAbilities
from helpers.helper import (initialize_combo, initialize_combo_model,
                            initialize_edit, initialize_frame, initialize_text,
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
        self.grid_layout_widget_2.setGeometry(QtCore.QRect(10, 10, 761, 201))
        self.grid_layout_widget_2.setObjectName("gridLayoutWidget_2")
        self.skills_score_grid = QtWidgets.QGridLayout(self.grid_layout_widget_2)
        self.skills_score_grid.setContentsMargins(0, 0, 0, 0)
        self.skills_score_grid.setObjectName("SkillsScoreGrid")

        self.class_ability_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        self.class_ability_text.setMaximumSize(QtCore.QSize(70, 25))
        self.class_ability_text.setObjectName("ClassAbilityText")
        self.class_ability_text.setText("Class Abilities")
        self.skills_score_grid.addWidget(self.class_ability_text, 0, 0, 1, 1)
        self.class1 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class1.setMinimumSize(QtCore.QSize(184, 20))
        self.class1.setMaximumSize(QtCore.QSize(184, 20))
        self.class1.setObjectName("Class1")

        self.class1_model = QtGui.QStandardItemModel()
        self.class1.setModel(ProxyModel(self.class1_model, "<<Select Feat>>"))
        self.class1.setCurrentIndex(0)
        #self.Class1.activated[str].connect(self.UpdateClassList)
        self.skills_score_grid.addWidget(self.class1, 1, 0, 1, 1)
        self.class2 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class2.setMinimumSize(QtCore.QSize(184, 20))
        self.class2.setMaximumSize(QtCore.QSize(184, 20))
        self.class2.setObjectName("Class2")
        self.skills_score_grid.addWidget(self.class2, 1, 1, 1, 1)
        self.class3 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class3.setMinimumSize(QtCore.QSize(184, 20))
        self.class3.setMaximumSize(QtCore.QSize(184, 20))
        self.class3.setObjectName("Class3")
        self.skills_score_grid.addWidget(self.class3, 1, 2, 1, 1)
        self.class4 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class4.setMinimumSize(QtCore.QSize(184, 20))
        self.class4.setMaximumSize(QtCore.QSize(184, 20))
        self.class4.setObjectName("Class4")
        self.skills_score_grid.addWidget(self.class4, 1, 3, 1, 1)
        self.class5 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class5.setMinimumSize(QtCore.QSize(184, 20))
        self.class5.setMaximumSize(QtCore.QSize(184, 20))
        self.class5.setObjectName("Class5")
        self.skills_score_grid.addWidget(self.class5, 2, 0, 1, 1)
        self.class6 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class6.setMinimumSize(QtCore.QSize(184, 20))
        self.class6.setMaximumSize(QtCore.QSize(184, 20))
        self.class6.setObjectName("Class6")
        self.skills_score_grid.addWidget(self.class6, 2, 1, 1, 1)
        self.class7 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class7.setMinimumSize(QtCore.QSize(184, 20))
        self.class7.setMaximumSize(QtCore.QSize(184, 20))
        self.class7.setObjectName("Class7")
        self.skills_score_grid.addWidget(self.class7, 2, 2, 1, 1)
        self.class8 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class8.setMinimumSize(QtCore.QSize(184, 20))
        self.class8.setMaximumSize(QtCore.QSize(184, 20))
        self.class8.setObjectName("Class8")
        self.skills_score_grid.addWidget(self.class8, 2, 3, 1, 1)
        self.class9 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class9.setMinimumSize(QtCore.QSize(184, 20))
        self.class9.setMaximumSize(QtCore.QSize(184, 20))
        self.class9.setObjectName("Class9")
        self.skills_score_grid.addWidget(self.class9, 3, 0, 1, 1)
        self.class10 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class10.setMinimumSize(QtCore.QSize(184, 20))
        self.class10.setMaximumSize(QtCore.QSize(184, 20))
        self.class10.setObjectName("Class10")
        self.skills_score_grid.addWidget(self.class10, 3, 1, 1, 1)
        self.class11 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class11.setMinimumSize(QtCore.QSize(184, 20))
        self.class11.setMaximumSize(QtCore.QSize(184, 20))
        self.class11.setObjectName("Class11")
        self.skills_score_grid.addWidget(self.class11, 3, 2, 1, 1)
        self.class12 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class12.setMinimumSize(QtCore.QSize(184, 20))
        self.class12.setMaximumSize(QtCore.QSize(184, 20))
        self.class12.setObjectName("Class12")
        self.skills_score_grid.addWidget(self.class12, 3, 3, 1, 1)
        self.class13 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class13.setMinimumSize(QtCore.QSize(184, 20))
        self.class13.setMaximumSize(QtCore.QSize(184, 20))
        self.class13.setObjectName("Class13")
        self.skills_score_grid.addWidget(self.class13, 4, 0, 1, 1)
        self.class14 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class14.setMinimumSize(QtCore.QSize(184, 20))
        self.class14.setMaximumSize(QtCore.QSize(184, 20))
        self.class14.setObjectName("Class14")
        self.skills_score_grid.addWidget(self.class14, 4, 1, 1, 1)
        self.class15 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class15.setMinimumSize(QtCore.QSize(184, 20))
        self.class15.setMaximumSize(QtCore.QSize(184, 20))
        self.class15.setObjectName("Class15")
        self.skills_score_grid.addWidget(self.class15, 4, 2, 1, 1)
        self.class16 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class16.setMinimumSize(QtCore.QSize(184, 20))
        self.class16.setMaximumSize(QtCore.QSize(184, 20))
        self.class16.setObjectName("Class16")
        self.skills_score_grid.addWidget(self.class16, 4, 3, 1, 1)
        self.class17 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class17.setMinimumSize(QtCore.QSize(184, 20))
        self.class17.setMaximumSize(QtCore.QSize(184, 20))
        self.class17.setObjectName("Class17")
        self.skills_score_grid.addWidget(self.class17, 5, 0, 1, 1)
        self.class18 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class18.setMinimumSize(QtCore.QSize(184, 20))
        self.class18.setMaximumSize(QtCore.QSize(184, 20))
        self.class18.setObjectName("Class18")
        self.skills_score_grid.addWidget(self.class18, 5, 1, 1, 1)
        self.class19 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class19.setMinimumSize(QtCore.QSize(184, 20))
        self.class19.setMaximumSize(QtCore.QSize(184, 20))
        self.class19.setObjectName("Class19")
        self.skills_score_grid.addWidget(self.class19, 5, 2, 1, 1)
        self.class20 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class20.setMinimumSize(QtCore.QSize(184, 20))
        self.class20.setMaximumSize(QtCore.QSize(184, 20))
        self.class20.setObjectName("Class20")
        self.skills_score_grid.addWidget(self.class20, 5, 3, 1, 1)
        self.class21 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class21.setMinimumSize(QtCore.QSize(184, 20))
        self.class21.setMaximumSize(QtCore.QSize(184, 20))
        self.class21.setObjectName("Class21")
        self.skills_score_grid.addWidget(self.class21, 6, 0, 1, 1)
        self.class22 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class22.setMinimumSize(QtCore.QSize(184, 20))
        self.class22.setMaximumSize(QtCore.QSize(184, 20))
        self.class22.setObjectName("Class22")
        self.skills_score_grid.addWidget(self.class22, 6, 1, 1, 1)
        self.class23 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class23.setMinimumSize(QtCore.QSize(184, 20))
        self.class23.setMaximumSize(QtCore.QSize(184, 20))
        self.class23.setObjectName("Class23")
        self.skills_score_grid.addWidget(self.class23, 6, 2, 1, 1)
        self.class24 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class24.setMinimumSize(QtCore.QSize(184, 20))
        self.class24.setMaximumSize(QtCore.QSize(184, 20))
        self.class24.setObjectName("Class24")
        self.skills_score_grid.addWidget(self.class24, 6, 3, 1, 1)
        self.class25 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class25.setMinimumSize(QtCore.QSize(184, 20))
        self.class25.setMaximumSize(QtCore.QSize(184, 20))
        self.class25.setObjectName("Class25")
        self.skills_score_grid.addWidget(self.class25, 7, 0, 1, 1)
        self.class26 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class26.setMinimumSize(QtCore.QSize(184, 20))
        self.class26.setMaximumSize(QtCore.QSize(184, 20))
        self.class26.setObjectName("Class26")
        self.skills_score_grid.addWidget(self.class26, 7, 1, 1, 1)
        self.class27 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class27.setMinimumSize(QtCore.QSize(184, 20))
        self.class27.setMaximumSize(QtCore.QSize(184, 20))
        self.class27.setObjectName("Class27")
        self.skills_score_grid.addWidget(self.class27, 7, 2, 1, 1)
        self.class28 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.class28.setMinimumSize(QtCore.QSize(184, 20))
        self.class28.setMaximumSize(QtCore.QSize(184, 20))
        self.class28.setObjectName("Class28")
        self.skills_score_grid.addWidget(self.class28, 7, 3, 1, 1)

        self.skillframe_2 = QtWidgets.QFrame(self.centralwidget)
        self.skillframe_2.setGeometry(QtCore.QRect(20, 240, 781, 71))
        self.skillframe_2.setFrameShape(QtWidgets.QFrame.Box)
        self.skillframe_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.skillframe_2.setLineWidth(2)
        self.skillframe_2.setObjectName("Skillframe_2")
        self.grid_layout_widget_3 = QtWidgets.QWidget(self.skillframe_2)
        self.grid_layout_widget_3.setGeometry(QtCore.QRect(10, 10, 761, 51))
        self.grid_layout_widget_3.setObjectName("gridLayoutWidget_3")
        self.skills_score_grid_2 = QtWidgets.QGridLayout(self.grid_layout_widget_3)
        self.skills_score_grid_2.setContentsMargins(0, 0, 0, 0)
        self.skills_score_grid_2.setObjectName("SkillsScoreGrid_2")

        self.theme_ability_text = QtWidgets.QLabel(self.grid_layout_widget_3)
        self.theme_ability_text.setMaximumSize(QtCore.QSize(70, 25))
        self.theme_ability_text.setObjectName("ThemeAbilityText")
        self.theme_ability_text.setText("Theme Abilities")
        self.skills_score_grid_2.addWidget(self.theme_ability_text, 0, 0, 1, 1)


        self.theme1 = QtWidgets.QComboBox(self.grid_layout_widget_3)
        self.theme1.setMaximumSize(QtCore.QSize(184, 20))
        self.theme1.setMinimumSize(QtCore.QSize(184, 20))
        self.theme1.setMaximumSize(QtCore.QSize(184, 20))
        self.skills_score_grid_2.addWidget(self.theme1, 1, 0, 1, 1)
        self.theme2 = QtWidgets.QComboBox(self.grid_layout_widget_3)
        self.theme2.setMinimumSize(QtCore.QSize(184, 20))
        self.theme2.setMaximumSize(QtCore.QSize(184, 20))
        self.theme2.setObjectName("Theme2")
        self.skills_score_grid_2.addWidget(self.theme2, 1, 1, 1, 1)
        self.theme3 = QtWidgets.QComboBox(self.grid_layout_widget_3)
        self.theme3.setMinimumSize(QtCore.QSize(184, 20))
        self.theme3.setMaximumSize(QtCore.QSize(184, 20))
        self.theme3.setObjectName("Theme3")
        self.skills_score_grid_2.addWidget(self.theme3, 1, 2, 1, 1)
        self.theme4 = QtWidgets.QComboBox(self.grid_layout_widget_3)
        self.theme4.setMinimumSize(QtCore.QSize(184, 20))
        self.theme4.setMaximumSize(QtCore.QSize(184, 20))
        self.theme4.setObjectName("Theme4")
        self.skills_score_grid_2.addWidget(self.theme4, 1, 3, 1, 1)

        self.skillframe_3 = QtWidgets.QFrame(self.centralwidget)
        self.skillframe_3.setGeometry(QtCore.QRect(20, 320, 781, 71))
        self.skillframe_3.setFrameShape(QtWidgets.QFrame.Box)
        self.skillframe_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.skillframe_3.setLineWidth(2)
        self.skillframe_3.setObjectName("Skillframe_3")
        self.grid_layout_widget_4 = QtWidgets.QWidget(self.skillframe_3)
        self.grid_layout_widget_4.setGeometry(QtCore.QRect(10, 10, 761, 51))
        self.grid_layout_widget_4.setObjectName("gridLayoutWidget_4")
        self.skills_score_grid_4 = QtWidgets.QGridLayout(self.grid_layout_widget_4)
        self.skills_score_grid_4.setContentsMargins(0, 0, 0, 0)
        self.skills_score_grid_4.setObjectName("SkillsScoreGrid_4")

        self.race_ability_text = QtWidgets.QLabel(self.grid_layout_widget_4)
        self.race_ability_text.setMaximumSize(QtCore.QSize(70, 25))
        self.race_ability_text.setObjectName("RaceAbilityText")
        self.race_ability_text.setText("Race Abilities")
        self.skills_score_grid_4.addWidget(self.race_ability_text, 0, 0, 1, 1)
        self.race1 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        self.race1.setMinimumSize(QtCore.QSize(184, 20))
        self.race1.setMaximumSize(QtCore.QSize(184, 20))
        self.race1.setObjectName("Race1")
        self.skills_score_grid_4.addWidget(self.race1, 1, 0, 1, 1)
        self.race2 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        self.race2.setMinimumSize(QtCore.QSize(184, 20))
        self.race2.setMaximumSize(QtCore.QSize(184, 20))
        self.race2.setObjectName("Race2")
        self.skills_score_grid_4.addWidget(self.race2, 1, 1, 1, 1)
        self.race3 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        self.race3.setMinimumSize(QtCore.QSize(184, 20))
        self.race3.setMaximumSize(QtCore.QSize(184, 20))
        self.race3.setObjectName("Race3")
        self.skills_score_grid_4.addWidget(self.race3, 1, 2, 1, 1)
        self.race4 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        self.race4.setMinimumSize(QtCore.QSize(184, 20))
        self.race4.setMaximumSize(QtCore.QSize(184, 20))
        self.race4.setObjectName("Race4")
        self.skills_score_grid_4.addWidget(self.race4, 1, 3, 1, 1)

        self.skillframe_4 = QtWidgets.QFrame(self.centralwidget)
        self.skillframe_4.setGeometry(QtCore.QRect(20, 400, 781, 221))
        self.skillframe_4.setFrameShape(QtWidgets.QFrame.Box)
        self.skillframe_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.skillframe_4.setLineWidth(2)
        self.skillframe_4.setObjectName("Skillframe_4")
        self.grid_layout_widget_5 = QtWidgets.QWidget(self.skillframe_4)
        self.grid_layout_widget_5.setGeometry(QtCore.QRect(10, 10, 761, 201))
        self.grid_layout_widget_5.setObjectName("gridLayoutWidget_5")
        self.skills_score_grid_5 = QtWidgets.QGridLayout(self.grid_layout_widget_5)
        self.skills_score_grid_5.setContentsMargins(0, 0, 0, 0)
        self.skills_score_grid_5.setObjectName("SkillsScoreGrid_5")

        self.feats_text = QtWidgets.QLabel(self.grid_layout_widget_5)
        self.feats_text.setMaximumSize(QtCore.QSize(113, 25))
        self.feats_text.setObjectName("FeatsText")
        self.feats_text.setText("Feats and Proficiencies")
        self.skills_score_grid_5.addWidget(self.feats_text, 0, 0, 1, 1)
        self.feats1 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats1.setMinimumSize(QtCore.QSize(184, 20))
        self.feats1.setMaximumSize(QtCore.QSize(184, 20))
        self.feats1.setObjectName("Feats1")
        self.skills_score_grid_5.addWidget(self.feats1, 1, 0, 1, 1)
        self.feats2 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats2.setMinimumSize(QtCore.QSize(184, 20))
        self.feats2.setMaximumSize(QtCore.QSize(184, 20))
        self.feats2.setObjectName("Feats2")
        self.skills_score_grid_5.addWidget(self.feats2, 1, 1, 1, 1)
        self.feats3 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats3.setMinimumSize(QtCore.QSize(184, 20))
        self.feats3.setMaximumSize(QtCore.QSize(184, 20))
        self.feats3.setObjectName("Feats3")
        self.skills_score_grid_5.addWidget(self.feats3, 1, 2, 1, 1)
        self.feats4 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats4.setMinimumSize(QtCore.QSize(184, 20))
        self.feats4.setMaximumSize(QtCore.QSize(184, 20))
        self.feats4.setObjectName("Feats4")
        self.skills_score_grid_5.addWidget(self.feats4, 1, 3, 1, 1)
        self.feats5 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats5.setMinimumSize(QtCore.QSize(184, 20))
        self.feats5.setMaximumSize(QtCore.QSize(184, 20))
        self.feats5.setObjectName("Feats5")
        self.skills_score_grid_5.addWidget(self.feats5, 2, 0, 1, 1)
        self.feats6 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats6.setMinimumSize(QtCore.QSize(184, 20))
        self.feats6.setMaximumSize(QtCore.QSize(184, 20))
        self.feats6.setObjectName("Feats6")
        self.skills_score_grid_5.addWidget(self.feats6, 2, 1, 1, 1)
        self.feats7 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats7.setMinimumSize(QtCore.QSize(184, 20))
        self.feats7.setMaximumSize(QtCore.QSize(184, 20))
        self.feats7.setObjectName("Feats7")
        self.skills_score_grid_5.addWidget(self.feats7, 2, 2, 1, 1)
        self.feats8 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats8.setMinimumSize(QtCore.QSize(184, 20))
        self.feats8.setMaximumSize(QtCore.QSize(184, 20))
        self.feats8.setObjectName("Feats8")
        self.skills_score_grid_5.addWidget(self.feats8, 2, 3, 1, 1)
        self.feats9 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats9.setMinimumSize(QtCore.QSize(184, 20))
        self.feats9.setMaximumSize(QtCore.QSize(184, 20))
        self.feats9.setObjectName("Feats9")
        self.skills_score_grid_5.addWidget(self.feats9, 3, 0, 1, 1)
        self.feats10 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats10.setMinimumSize(QtCore.QSize(184, 20))
        self.feats10.setMaximumSize(QtCore.QSize(184, 20))
        self.feats10.setObjectName("Feats10")
        self.skills_score_grid_5.addWidget(self.feats10, 3, 1, 1, 1)
        self.feats11 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats11.setMinimumSize(QtCore.QSize(184, 20))
        self.feats11.setMaximumSize(QtCore.QSize(184, 20))
        self.feats11.setObjectName("Feats11")
        self.skills_score_grid_5.addWidget(self.feats11, 3, 2, 1, 1)
        self.feats12 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats12.setMinimumSize(QtCore.QSize(184, 20))
        self.feats12.setMaximumSize(QtCore.QSize(184, 20))
        self.feats12.setObjectName("Feats12")
        self.skills_score_grid_5.addWidget(self.feats12, 3, 3, 1, 1)
        self.feats13 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats13.setMinimumSize(QtCore.QSize(184, 20))
        self.feats13.setMaximumSize(QtCore.QSize(184, 20))
        self.feats13.setObjectName("Feats13")
        self.skills_score_grid_5.addWidget(self.feats13, 4, 0, 1, 1)
        self.feats14 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats14.setMinimumSize(QtCore.QSize(184, 20))
        self.feats14.setMaximumSize(QtCore.QSize(184, 20))
        self.feats14.setObjectName("Feats14")
        self.skills_score_grid_5.addWidget(self.feats14, 4, 1, 1, 1)
        self.feats15 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats15.setMinimumSize(QtCore.QSize(184, 20))
        self.feats15.setMaximumSize(QtCore.QSize(184, 20))
        self.feats15.setObjectName("Feats15")
        self.skills_score_grid_5.addWidget(self.feats15, 4, 2, 1, 1)
        self.feats16 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats16.setMinimumSize(QtCore.QSize(184, 20))
        self.feats16.setMaximumSize(QtCore.QSize(184, 20))
        self.feats16.setObjectName("Feats16")
        self.skills_score_grid_5.addWidget(self.feats16, 4, 3, 1, 1)
        self.feats17 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats17.setMinimumSize(QtCore.QSize(184, 20))
        self.feats17.setMaximumSize(QtCore.QSize(184, 20))
        self.feats17.setObjectName("Feats17")
        self.skills_score_grid_5.addWidget(self.feats17, 5, 0, 1, 1)
        self.feats18 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats18.setMinimumSize(QtCore.QSize(184, 20))
        self.feats18.setMaximumSize(QtCore.QSize(184, 20))
        self.feats18.setObjectName("Feats18")
        self.skills_score_grid_5.addWidget(self.feats18, 5, 1, 1, 1)
        self.feats19 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats19.setMinimumSize(QtCore.QSize(184, 20))
        self.feats19.setMaximumSize(QtCore.QSize(184, 20))
        self.feats19.setObjectName("Feats19")
        self.skills_score_grid_5.addWidget(self.feats19, 5, 2, 1, 1)
        self.feats20 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats20.setMinimumSize(QtCore.QSize(184, 20))
        self.feats20.setMaximumSize(QtCore.QSize(184, 20))
        self.feats20.setObjectName("Feats20")
        self.skills_score_grid_5.addWidget(self.feats20, 5, 3, 1, 1)
        self.feats21 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats21.setMinimumSize(QtCore.QSize(184, 20))
        self.feats21.setMaximumSize(QtCore.QSize(184, 20))
        self.feats21.setObjectName("Feats21")
        self.skills_score_grid_5.addWidget(self.feats21, 6, 0, 1, 1)
        self.feats22 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats22.setMinimumSize(QtCore.QSize(184, 20))
        self.feats22.setMaximumSize(QtCore.QSize(184, 20))
        self.feats22.setObjectName("Feats22")
        self.skills_score_grid_5.addWidget(self.feats22, 6, 1, 1, 1)
        self.feats23 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats23.setMinimumSize(QtCore.QSize(184, 20))
        self.feats23.setMaximumSize(QtCore.QSize(184, 20))
        self.feats23.setObjectName("Feats23")
        self.skills_score_grid_5.addWidget(self.feats23, 6, 2, 1, 1)
        self.feats24 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats24.setMinimumSize(QtCore.QSize(184, 20))
        self.feats24.setMaximumSize(QtCore.QSize(184, 20))
        self.feats24.setObjectName("Feats24")
        self.skills_score_grid_5.addWidget(self.feats24, 6, 3, 1, 1)
        self.feats25 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats25.setMinimumSize(QtCore.QSize(184, 20))
        self.feats25.setMaximumSize(QtCore.QSize(184, 20))
        self.feats25.setObjectName("Feats25")
        self.skills_score_grid_5.addWidget(self.feats25, 7, 0, 1, 1)
        self.feats26 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats26.setMinimumSize(QtCore.QSize(184, 20))
        self.feats26.setMaximumSize(QtCore.QSize(184, 20))
        self.feats26.setObjectName("Feats26")
        self.skills_score_grid_5.addWidget(self.feats26, 7, 1, 1, 1)
        self.feats27 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats27.setMinimumSize(QtCore.QSize(184, 20))
        self.feats27.setMaximumSize(QtCore.QSize(184, 20))
        self.feats27.setObjectName("Feats27")
        self.skills_score_grid_5.addWidget(self.feats27, 7, 2, 1, 1)
        self.feats28 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.feats28.setMinimumSize(QtCore.QSize(184, 20))
        self.feats28.setMaximumSize(QtCore.QSize(184, 20))
        self.feats28.setObjectName("Feats28")
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
