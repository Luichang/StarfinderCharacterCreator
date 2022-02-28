from PyQt5 import QtCore, QtGui, QtWidgets
from starfinder_class_dicts import classAbilities, classChoseFeats

from character import Character
from ProxyModel import ProxyModel


class UiForm(QtWidgets.QWidget):
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
        self.skillframe.setGeometry(QtCore.QRect(20, 10, 781, 221))
        self.skillframe.setFrameShape(QtWidgets.QFrame.Box)
        self.skillframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.skillframe.setLineWidth(2)
        self.skillframe.setObjectName("Skillframe")
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

        self.update_class_feat_list()


    def update_classes(self):
        """some update of class related comboboxes
        """

    def update_class_feat_list(self):
        """does some class feature related update

        """

        self.character.classFeats = []
        # for i in self.character.class_level:
        #     for ability in classAbilities[self.class_name][i]:


        boxes = [self.class1, self.class2, self.class3, self.class4, self.class5,
                 self.class6, self.class7, self.class8, self.class9, self.class10,
                 self.class11, self.class12, self.class13, self.class14, self.class15,
                 self.class16, self.class17, self.class18, self.class19, self.class20,
                 self.class21, self.class22, self.class23, self.class24, self.class25,
                 self.class26, self.class27, self.class28]
        boxcount = 0
        for i in range(self.character.class_level):
            for ability in classAbilities[self.character.class_name][i]:
                class_model = QtGui.QStandardItemModel()
                if ability[1] == "improvisation": # classChoseFeats, lists with levels
                    possible_class_feats = self.character.select_new_class_feat("improvisation",
                                                        self.character.class_level, verbose=False)
                    for feat in possible_class_feats:
                        class_model.appendRow(QtGui.QStandardItem(feat))
                    boxes[boxcount].setModel(ProxyModel(class_model, "<<Select Improvisation>>"))
                    boxes[boxcount].setCurrentIndex(1)
                elif ability[1] == "talent": # classChoseFeats, lists with levels
                    possible_class_feats = self.character.select_new_class_feat("talent",
                                                    self.character.class_level, verbose=False)
                    for feat in possible_class_feats:
                        class_model.appendRow(QtGui.QStandardItem(feat))
                    boxes[boxcount].setModel(ProxyModel(class_model, "<<Select Talent>>"))
                    boxes[boxcount].setCurrentIndex(1)
                elif ability[1] == "trick": # classChoseFeats, lists with levels
                    possible_class_feats = self.character.select_new_class_feat("trick",
                                                self.character.class_level, verbose=False)
                    for feat in possible_class_feats:
                        class_model.appendRow(QtGui.QStandardItem(feat))
                    boxes[boxcount].setModel(ProxyModel(class_model, "<<Select Trick>>"))
                    boxes[boxcount].setCurrentIndex(1)
                elif ability[1] == "class":
                    pass
                elif ability[1] == "skills":
                    self.character.classFeats.append(ability[0])
                    class_model.appendRow(QtGui.QStandardItem(ability[0]))
                    boxes[boxcount].setModel(ProxyModel(class_model, "<<Fixed Feat>>"))
                    boxes[boxcount].setCurrentIndex(1)
                    for skill in ability[2]:
                        self.character.skillMisc[skill[0]] += skill[1]
                elif ability[1] == "revelation": # classChoseFeats, lists with levels
                    possible_class_feats = self.character.select_new_class_feat("revelation",
                                                    self.character.class_level, verbose=False)
                    for feat in possible_class_feats:
                        class_model.appendRow(QtGui.QStandardItem(feat))
                    boxes[boxcount].setModel(ProxyModel(class_model, "<<Select Revelation>>"))
                    boxes[boxcount].setCurrentIndex(1)
                elif ability[1] == "zenith": # classChoseFeats, single list
                    possible_class_feats = self.character.select_new_class_feat("zenith",
                                                self.character.class_level, verbose=False)
                    for feat in possible_class_feats:
                        class_model.appendRow(QtGui.QStandardItem(feat))
                    boxes[boxcount].setModel(ProxyModel(class_model, "<<Select Zenith>>"))
                    boxes[boxcount].setCurrentIndex(1)
                elif ability[1] == "style": # classChoseFeats, dictionary
                    possible_styles = [x for x in classChoseFeats["soldier"]["styles"]]
                    for style in self.character.styles:
                        possible_styles.remove(style)
                    for feat in possible_styles:
                        class_model.appendRow(QtGui.QStandardItem(feat))
                    boxes[boxcount].setModel(ProxyModel(class_model, "<<Select Style>>"))
                    boxes[boxcount].setCurrentIndex(1)
                    # TODO add new function connection
                elif ability[1] == "technique1":
                    soldier_style = classChoseFeats["soldier"]["styles"][self.styles[0]]
                    new_feat = soldier_style[self.character.class_level - 1]
                    self.character.classFeats.append(new_feat)
                    class_model.appendRow(QtGui.QStandardItem(new_feat))
                    boxes[boxcount].setModel(ProxyModel(class_model, "<<Fixed Feat>>"))
                    boxes[boxcount].setCurrentIndex(1)
                elif ability[1] == "technique2":
                    soldier_style = classChoseFeats["soldier"]["styles"][self.styles[1]]
                    new_feat = soldier_style[(self.character.class_level - 1) - 8]
                    self.character.classFeats.append(new_feat)
                    class_model.appendRow(QtGui.QStandardItem(new_feat))
                    boxes[boxcount].setModel(ProxyModel(class_model, "<<Fixed Feat>>"))
                    boxes[boxcount].setCurrentIndex(1)
                elif ability[1] == "combat":
                    pass
                elif ability[1] == "gear": # classChoseFeats, lists with levels
                    possible_class_feats = self.character.select_new_class_feat("gear",
                                            self.character.class_level, verbose=False)
                    for feat in possible_class_feats:
                        class_model.appendRow(QtGui.QStandardItem(feat))
                    boxes[boxcount].setModel(ProxyModel(class_model, "<<Select Gear>>"))
                    boxes[boxcount].setCurrentIndex(1)
                elif ability[1] == "hack": # classChoseFeats, lists with levels
                    possible_class_feats = self.character.select_new_class_feat("hack",
                                            self.character.class_level, verbose=False)
                    for feat in possible_class_feats:
                        class_model.appendRow(QtGui.QStandardItem(feat))
                    boxes[boxcount].setModel(ProxyModel(class_model, "<<Select Hack>>"))
                    boxes[boxcount].setCurrentIndex(1)
                elif ability[1] == "feat":
                    pass
                elif ability[1] == "edge":
                    pass
                elif ability[1] == "specialization":
                    if ability[2][0] == "feat":
                        pass
                    elif ability[2][0] == "exploit":
                        new_feat = classChoseFeats["operative"]["specialization"][self.styles[0]][1]
                        self.character.classFeats.append(new_feat)
                        class_model.appendRow(QtGui.QStandardItem(new_feat))
                        boxes[boxcount].setModel(ProxyModel(class_model, "<<Fixed Feat>>"))
                        boxes[boxcount].setCurrentIndex(1)
                    elif ability[2][0] == "power":
                        new_feat = classChoseFeats["operative"]["specialization"][self.styles[0]][2]
                        self.character.classFeats.append(new_feat)
                        class_model.appendRow(QtGui.QStandardItem(new_feat))
                        boxes[boxcount].setModel(ProxyModel(class_model, "<<Fixed Feat>>"))
                        boxes[boxcount].setCurrentIndex(1)
                elif ability[1] == "exploit":
                    possible_class_feats = self.character.select_new_class_feat("exploit",
                                            self.character.class_level, verbose=False)
                    for feat in possible_class_feats:
                        class_model.appendRow(QtGui.QStandardItem(feat))
                    boxes[boxcount].setModel(ProxyModel(class_model, "<<Select Exploit>>"))
                    boxes[boxcount].setCurrentIndex(1)
                elif ability[1] == "connection":
                    pass
                elif ability[1] == "cpower":
                    mystic_styles = classChoseFeats["mystic"]["connection"][self.styles[0]]
                    new_feat = mystic_styles["feat"][ability[2]]
                    self.character.classFeats.append(new_feat)
                    class_model.appendRow(QtGui.QStandardItem(new_feat))
                    boxes[boxcount].setModel(ProxyModel(class_model, "<<Fixed Feat>>"))
                    boxes[boxcount].setCurrentIndex(1)
                elif ability[1] == "spell":
                    pass
                elif ability[1] == "channel":
                    pass
                elif ability[1] == "expertise": # TODO add expertise things
                    self.character.classFeats.append(ability[0])
                    class_model.appendRow(QtGui.QStandardItem(ability[0]))
                    boxes[boxcount].setModel(ProxyModel(class_model, "<<Fixed Feat>>"))
                    boxes[boxcount].setCurrentIndex(1)
                    self.character.expertise.append("sense motive")
                elif ability[1] == "add expertise": # envoy
                    # this is not shown on the excel sheet, might just ignore it then # TODO
                    possible_expertise = ["bluff", "computers", "culture", "diplomacy", "disguise",
                                          "engineering", "intimidate", "medicine"]
                    for expertise in self.character.expertise:
                        if expertise in possible_expertise:
                            possible_expertise.remove(expertise)
                    for feat in possible_expertise:
                        class_model.appendRow(QtGui.QStandardItem(feat))
                    boxes[boxcount].setModel(ProxyModel(class_model, "<<Select Expertise>>"))
                    boxes[boxcount].setCurrentIndex(1)
                elif ability[1] == "influence": # solarian # add two skills, one each from two lists
                    pass
                elif ability[1] == "weapon": # all # TODO
                    self.character.classFeats.append(ability[0])
                    class_model.appendRow(QtGui.QStandardItem(ability[0]))
                    boxes[boxcount].setModel(ProxyModel(class_model, "<<Fixed Feat>>"))
                    boxes[boxcount].setCurrentIndex(1)
                elif ability[1] == "words": # nothing happens
                    self.character.classFeats.append(ability[0])
                    class_model.appendRow(QtGui.QStandardItem(ability[0]))
                    boxes[boxcount].setModel(ProxyModel(class_model, "<<Fixed Feat>>"))
                    boxes[boxcount].setCurrentIndex(1)
                boxcount += 1




        # for box in boxes:
            # if box.currentText() != "<<Select Feat>>":
            #     self.character.classFeats.append(box.currentText())
            #     print(box.currentText())

    # def UpdateClassList(self, sender=None): # if character class_name

    #     # self.UpdatecClassFeatList()

    #     if not sender:
    #         sender = self.sender()
    #     if not isinstance(sender, QtWidgets.QAction):

    #         selectedFeat = sender.currentText()

    #         classList = [selectedFeat]
    #     else:
    #         classList = []

    #     for featType in classChoseFeats[self.character.class_name]:
    #         for featList in classChoseFeats[self.character.class_name][featType]:
    #             try:
    #                 if self.character.class_level >= int(featList[0]):
    #                     classList += featList[1:]
    #             except ValueError:
    #                 pass
    #     for feat in self.character.classFeats:
    #         if feat in classList:
    #             classList.remove(feat)

    #     if not isinstance(sender, QtWidgets.QAction):
    #         ClassModel = QtGui.QStandardItemModel()
    #         for feat in classList:
    #             ClassModel.appendRow(QtGui.QStandardItem(feat))
    #         sender.setModel(ProxyModel(ClassModel, "<<Select Feat>>"))
    #         sender.setCurrentIndex(1)
