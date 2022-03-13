from PyQt5 import QtCore, QtWidgets

from character import Character
from helpers.helper import (initialize_combo, initialize_combo_model,
                            initialize_edit, initialize_frame, initialize_text,
                            initialize_widget)
from helpers.starfinder_class_dicts import classesStatBonus
from helpers.starfinder_race_dicts import raceAbilities
from helpers.starfinder_theme_dicts import themeAbilities
from starfinder_gui_feat import UiForm

class UIMainWindow(object):
    """Generated Function that has beed edited to contain function calls added afterwards.
    All to portray the GUI version of the starfinder character creator

    Args:
        object (????): some object
    """
    def setup_ui(self, main_window):
        """create the main window of the starfinder character creator

        Args:
            main_window (????): the main window?
        """
        # pylint: disable=attribute-defined-outside-init
        self.character = Character(gui=True)
        self.point_buy_spendable_points = 10
        self.skill_buy_spendable_points = 0
        self.ability_buy_spendable_points = 0

        self.window = None


        main_window.setObjectName("MainWindow")
        main_window.resize(1075, 984)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")

        self.nameframe = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.nameframe, "Nameframe", [20, 10, 451, 51])
        self.horizontal_layout_widget_2 = QtWidgets.QWidget(self.nameframe)
        initialize_widget(self.horizontal_layout_widget_2, "horizontalLayoutWidget_2",
                            [10, 10, 431, 31])
        self.character_name_grid = QtWidgets.QHBoxLayout(self.horizontal_layout_widget_2)
        self.character_name_grid.setContentsMargins(0, 0, 0, 0)
        self.character_name_grid.setObjectName("CharacterNameGrid")

        self.character_name_text = QtWidgets.QLabel(self.horizontal_layout_widget_2)
        initialize_text(self.character_name_text, "CharacterNameText", "Character Name")
        self.character_name_grid.addWidget(self.character_name_text)

        self.character_name_box = QtWidgets.QTextEdit(self.horizontal_layout_widget_2)
        self.character_name_box.setMaximumSize(QtCore.QSize(16777215, 25))
        self.character_name_box.setObjectName("CharacterNameBox")
        self.character_name_box.textChanged.connect(self.update_name)
        self.character_name_grid.addWidget(self.character_name_box)

        self.character_level_box = QtWidgets.QComboBox(self.horizontal_layout_widget_2)
        self.character_level_box.setMaximumSize(QtCore.QSize(100, 20))
        self.character_level_box.setObjectName("CharacterLevelBox")
        initialize_combo_model(self.character_level_box, [str(num) for num in range(1, 21)], "0",
                                connection=self.update_level)
        self.character_name_grid.addWidget(self.character_level_box)

        self.abilityframe = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.abilityframe, "Abilityframe", [20, 130, 501, 311])

        self.horizontal_layout_widget_7 = QtWidgets.QWidget(self.abilityframe)
        initialize_widget(self.horizontal_layout_widget_7, "horizontalLayoutWidget_7",
                            [120, 10, 181, 31])
        self.point_count_grid = QtWidgets.QHBoxLayout(self.horizontal_layout_widget_7)
        self.point_count_grid.setContentsMargins(0, 0, 0, 0)
        self.point_count_grid.setObjectName("PointCountGrid")
        self.remaining_point_text = QtWidgets.QLabel(self.horizontal_layout_widget_7)
        initialize_text(self.remaining_point_text, "RemainingPointText", "Remaining Point Buy")
        self.point_count_grid.addWidget(self.remaining_point_text)
        self.remaining_point_box = QtWidgets.QLineEdit(self.horizontal_layout_widget_7)
        initialize_edit(self.remaining_point_box, "RemainingPointBox", shape=[40, 25])
        self.point_count_grid.addWidget(self.remaining_point_box)

        self.horizontal_layout_widget_8 = QtWidgets.QWidget(self.abilityframe)
        initialize_widget(self.horizontal_layout_widget_8, "horizontalLayoutWidget_8",
                            [310, 10, 181, 31])
        self.ability_count_grid = QtWidgets.QHBoxLayout(self.horizontal_layout_widget_8)
        self.ability_count_grid.setContentsMargins(0, 0, 0, 0)
        self.ability_count_grid.setObjectName("AbilityCountGrid")
        self.remaining_ability_text = QtWidgets.QLabel(self.horizontal_layout_widget_8)
        initialize_text(self.remaining_ability_text, "RemainingAbilityText",
                        "Remaining Ability Increase")
        self.ability_count_grid.addWidget(self.remaining_ability_text)
        self.remaining_ability_box = QtWidgets.QLineEdit(self.horizontal_layout_widget_8)
        initialize_edit(self.remaining_ability_box, "RemainingAbilityBox", shape=[40, 25])
        self.ability_count_grid.addWidget(self.remaining_ability_box)

        self.grid_layout_widget = QtWidgets.QWidget(self.abilityframe)
        initialize_widget(self.grid_layout_widget, "gridLayoutWidget",
                            [10, 50, 484, 255])
        self.ability_score_grid = QtWidgets.QGridLayout(self.grid_layout_widget)
        self.ability_score_grid.setContentsMargins(0, 0, 0, 0)
        self.ability_score_grid.setObjectName("AbilityScoreGrid")

        self.ability_line1 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line1, "AbilityLine1", vertical=False)
        self.ability_score_grid.addWidget(self.ability_line1, 2, 0, 1, 12)
        self.ability_line2 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line2, "AbilityLine2", vertical=False)
        self.ability_score_grid.addWidget(self.ability_line2, 4, 0, 1, 12)
        self.ability_line3 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line3, "AbilityLine3", vertical=False)
        self.ability_score_grid.addWidget(self.ability_line3, 6, 0, 1, 12)
        self.ability_line4 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line4, "AbilityLine4", vertical=False)
        self.ability_score_grid.addWidget(self.ability_line4, 8, 0, 1, 12)
        self.ability_line5 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line5, "AbilityLine5", vertical=False)
        self.ability_score_grid.addWidget(self.ability_line5, 10, 0, 1, 12)

        self.ability_line9 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line9, "AbilityLine9", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line9, 5, 2, 1, 1)
        self.ability_line10 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line10, "AbilityLine10", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line10, 7, 2, 1, 1)
        self.ability_line11 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line11, "AbilityLine11", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line11, 9, 2, 1, 1)
        self.ability_line12 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line12, "AbilityLine12", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line12, 11, 2, 1, 1)
        self.ability_line13 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line13, "AbilityLine13", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line13, 7, 4, 1, 1)
        self.ability_line14 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line14, "AbilityLine14", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line14, 1, 4, 1, 1)
        self.ability_line15 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line15, "AbilityLine15", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line15, 3, 4, 1, 1)
        self.ability_line16 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line16, "AbilityLine16", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line16, 5, 4, 1, 1)
        self.ability_line17 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line17, "AbilityLine17", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line17, 1, 2, 1, 1)
        self.ability_line18 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line18, "AbilityLine18", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line18, 3, 2, 1, 1)
        self.ability_line19 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line19, "AbilityLine19", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line19, 11, 4, 1, 1)
        self.ability_line20 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line20, "AbilityLine20", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line20, 9, 4, 1, 1)
        self.ability_line21 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line21, "AbilityLine21", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line21, 1, 6, 1, 1)
        self.ability_line22 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line22, "AbilityLine22", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line22, 3, 6, 1, 1)
        self.ability_line23 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line23, "AbilityLine23", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line23, 5, 6, 1, 1)
        self.ability_line24 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line24, "AbilityLine24", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line24, 7, 6, 1, 1)
        self.ability_line25 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line25, "AbilityLine25", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line25, 9, 6, 1, 1)
        self.ability_line26 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line26, "AbilityLine26", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line26, 11, 6, 1, 1)

        self.ability_line28 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line28, "AbilityLine28", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line28, 1, 8, 1, 1)
        self.ability_line29 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line29, "AbilityLine29", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line29, 3, 8, 1, 1)
        self.ability_line30 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line30, "AbilityLine30", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line30, 5, 8, 1, 1)
        self.ability_line31 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line31, "AbilityLine31", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line31, 7, 8, 1, 1)
        self.ability_line32 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line32, "AbilityLine32", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line32, 9, 8, 1, 1)
        self.ability_line33 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line33, "AbilityLine33", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line33, 11, 8, 1, 1)

        self.ability_line35 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line35, "AbilityLine35", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line35, 1, 10, 1, 1)
        self.ability_line36 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line36, "AbilityLine36", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line36, 3, 10, 1, 1)
        self.ability_line37 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line37, "AbilityLine37", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line37, 5, 10, 1, 1)
        self.ability_line38 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line38, "AbilityLine38", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line38, 7, 10, 1, 1)
        self.ability_line39 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line39, "AbilityLine39", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line39, 9, 10, 1, 1)
        self.ability_line40 = QtWidgets.QFrame(self.grid_layout_widget)
        initialize_frame(self.ability_line40, "AbilityLine40", vertical=True)
        self.ability_score_grid.addWidget(self.ability_line40, 11, 10, 1, 1)


        self.score_text = QtWidgets.QLabel(self.grid_layout_widget)
        initialize_text(self.score_text, "ScoreText", "Score")
        self.ability_score_grid.addWidget(self.score_text, 0, 1, 1, 1)
        self.modifier_text = QtWidgets.QLabel(self.grid_layout_widget)
        initialize_text(self.modifier_text, "ModifierText", "Modifier")
        self.ability_score_grid.addWidget(self.modifier_text, 0, 3, 1, 1)
        self.race_point_text = QtWidgets.QLabel(self.grid_layout_widget)
        initialize_text(self.race_point_text, "RacePointText", "Race Points")
        self.ability_score_grid.addWidget(self.race_point_text, 0, 5, 1, 1)
        self.theme_point_text = QtWidgets.QLabel(self.grid_layout_widget)
        initialize_text(self.theme_point_text, "ThemePointText", "Theme Points")
        self.ability_score_grid.addWidget(self.theme_point_text, 0, 7, 1, 1)
        self.point_buy_text = QtWidgets.QLabel(self.grid_layout_widget)
        initialize_text(self.point_buy_text, "PointBuyText", "Point Buy")
        self.ability_score_grid.addWidget(self.point_buy_text, 0, 9, 1, 1)
        self.ability_increases_text = QtWidgets.QLabel(self.grid_layout_widget)
        initialize_text(self.ability_increases_text, "AbilityIncreasesText", "Ability Increases")
        self.ability_score_grid.addWidget(self.ability_increases_text, 0, 11, 1, 1)

        self.str_text = QtWidgets.QLabel(self.grid_layout_widget)
        initialize_text(self.str_text, "StrText", "Str", max_size=[20, 20])
        self.ability_score_grid.addWidget(self.str_text, 1, 0, 1, 1)
        self.dex_text = QtWidgets.QLabel(self.grid_layout_widget)
        initialize_text(self.dex_text, "DexText", "Dex", max_size=[20, 20])
        self.ability_score_grid.addWidget(self.dex_text, 3, 0, 1, 1)
        self.con_text = QtWidgets.QLabel(self.grid_layout_widget)
        initialize_text(self.con_text, "ConText", "Con", max_size=[20, 20])
        self.ability_score_grid.addWidget(self.con_text, 5, 0, 1, 1)
        self.int_text = QtWidgets.QLabel(self.grid_layout_widget)
        initialize_text(self.int_text, "IntText", "Int", max_size=[20, 20])
        self.ability_score_grid.addWidget(self.int_text, 7, 0, 1, 1)
        self.wis_text = QtWidgets.QLabel(self.grid_layout_widget)
        initialize_text(self.wis_text, "WisText", "Wis", max_size=[20, 20])
        self.ability_score_grid.addWidget(self.wis_text, 9, 0, 1, 1)
        self.cha_text = QtWidgets.QLabel(self.grid_layout_widget)
        initialize_text(self.cha_text, "ChaText", "Cha", max_size=[20, 20])
        self.ability_score_grid.addWidget(self.cha_text, 11, 0, 1, 1)

        self.str_score = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.str_score, "StrScore", shape=[50, 20])
        self.ability_score_grid.addWidget(self.str_score, 1, 1, 1, 1)
        self.dex_score = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.dex_score, "DexScore", shape=[50, 20])
        self.ability_score_grid.addWidget(self.dex_score, 3, 1, 1, 1)
        self.con_score = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.con_score, "ConScore", shape=[50, 20])
        self.ability_score_grid.addWidget(self.con_score, 5, 1, 1, 1)
        self.int_score = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.int_score, "IntScore", shape=[50, 20])
        self.ability_score_grid.addWidget(self.int_score, 7, 1, 1, 1)
        self.wis_score = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.wis_score, "WisScore", shape=[50, 20])
        self.ability_score_grid.addWidget(self.wis_score, 9, 1, 1, 1)
        self.cha_score = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.cha_score, "ChaScore", shape=[50, 20])
        self.ability_score_grid.addWidget(self.cha_score, 11, 1, 1, 1)

        self.str_mod = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.str_mod, "StrMod", shape=[50, 20])
        self.ability_score_grid.addWidget(self.str_mod, 1, 3, 1, 1)
        self.dex_mod = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.dex_mod, "DexMod", shape=[50, 20])
        self.ability_score_grid.addWidget(self.dex_mod, 3, 3, 1, 1)
        self.con_mod = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.con_mod, "ConMod", shape=[50, 20])
        self.ability_score_grid.addWidget(self.con_mod, 5, 3, 1, 1)
        self.int_mod = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.int_mod, "IntMod", shape=[50, 20])
        self.ability_score_grid.addWidget(self.int_mod, 7, 3, 1, 1)
        self.wis_mod = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.wis_mod, "WisMod", shape=[50, 20])
        self.ability_score_grid.addWidget(self.wis_mod, 9, 3, 1, 1)
        self.cha_mod = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.cha_mod, "ChaMod", shape=[50, 20])
        self.ability_score_grid.addWidget(self.cha_mod, 11, 3, 1, 1)

        self.str_race = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.str_race, "StrRace", shape=[50, 20])
        self.ability_score_grid.addWidget(self.str_race, 1, 5, 1, 1)
        self.dex_race = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.dex_race, "DexRace", shape=[50, 20])
        self.ability_score_grid.addWidget(self.dex_race, 3, 5, 1, 1)
        self.con_race = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.con_race, "ConRace", shape=[50, 20])
        self.ability_score_grid.addWidget(self.con_race, 5, 5, 1, 1)
        self.int_race = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.int_race, "IntRace", shape=[50, 20])
        self.ability_score_grid.addWidget(self.int_race, 7, 5, 1, 1)
        self.wis_race = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.wis_race, "WisRace", shape=[50, 20])
        self.ability_score_grid.addWidget(self.wis_race, 9, 5, 1, 1)
        self.cha_race = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.cha_race, "ChaRace", shape=[50, 20])
        self.ability_score_grid.addWidget(self.cha_race, 11, 5, 1, 1)

        self.str_theme = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.str_theme, "StrTheme", shape=[50, 20])
        self.ability_score_grid.addWidget(self.str_theme, 1, 7, 1, 1)
        self.dex_theme = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.dex_theme, "DexTheme", shape=[50, 20])
        self.ability_score_grid.addWidget(self.dex_theme, 3, 7, 1, 1)
        self.con_theme = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.con_theme, "ConTheme", shape=[50, 20])
        self.ability_score_grid.addWidget(self.con_theme, 5, 7, 1, 1)
        self.int_theme = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.int_theme, "IntTheme", shape=[50, 20])
        self.ability_score_grid.addWidget(self.int_theme, 7, 7, 1, 1)
        self.wis_theme = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.wis_theme, "WisTheme", shape=[50, 20])
        self.ability_score_grid.addWidget(self.wis_theme, 9, 7, 1, 1)
        self.cha_theme = QtWidgets.QLineEdit(self.grid_layout_widget)
        initialize_edit(self.cha_theme, "ChaTheme", shape=[50, 20])
        self.ability_score_grid.addWidget(self.cha_theme, 11, 7, 1, 1)

        self.point_buy_str_combo = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.point_buy_str_combo, "PointBuyStrCombo", ["0"], [43, 20],
                        self.update_point_buys)
        self.ability_score_grid.addWidget(self.point_buy_str_combo, 1, 9, 1, 1)
        self.point_buy_dex_combo = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.point_buy_dex_combo, "PointBuyDexCombo", ["0"], [43,20],
                         self.update_point_buys)
        self.ability_score_grid.addWidget(self.point_buy_dex_combo, 3, 9, 1, 1)
        self.point_buy_con_combo = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.point_buy_con_combo, "PointBuyConCombo", ["0"], [43,20],
                         self.update_point_buys)
        self.ability_score_grid.addWidget(self.point_buy_con_combo, 5, 9, 1, 1)
        self.point_buy_int_combo = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.point_buy_int_combo, "PointBuyIntCombo", ["0"], [43,20],
                         self.update_point_buys)
        self.ability_score_grid.addWidget(self.point_buy_int_combo, 7, 9, 1, 1)
        self.point_buy_wis_combo = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.point_buy_wis_combo, "PointBuyWisCombo", ["0"], [43,20],
                         self.update_point_buys)
        self.ability_score_grid.addWidget(self.point_buy_wis_combo, 9, 9, 1, 1)
        self.point_buy_cha_combo = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.point_buy_cha_combo, "PointBuyChaCombo", ["0"], [43,20],
                         self.update_point_buys)
        self.ability_score_grid.addWidget(self.point_buy_cha_combo, 11, 9, 1, 1)

        self.ability_str_combo = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.ability_str_combo, "AbilityStrCombo", ["0"], [43,20],
                         self.update_increase_buys)
        self.ability_score_grid.addWidget(self.ability_str_combo, 1, 11, 1, 1)
        self.ability_dex_combo = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.ability_dex_combo, "AbilityDexCombo", ["0"], [43,20],
                         self.update_increase_buys)
        self.ability_score_grid.addWidget(self.ability_dex_combo, 3, 11, 1, 1)
        self.ability_con_combo = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.ability_con_combo, "AbilityConCombo", ["0"], [43,20],
                         self.update_increase_buys)
        self.ability_score_grid.addWidget(self.ability_con_combo, 5, 11, 1, 1)
        self.ability_int_combo = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.ability_int_combo, "AbilityIntCombo", ["0"], [43,20],
                         self.update_increase_buys)
        self.ability_score_grid.addWidget(self.ability_int_combo, 7, 11, 1, 1)
        self.ability_wis_combo = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.ability_wis_combo, "AbilityWisCombo", ["0"], [43,20],
                         self.update_increase_buys)
        self.ability_score_grid.addWidget(self.ability_wis_combo, 9, 11, 1, 1)
        self.ability_cha_combo = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.ability_cha_combo, "AbilityChaCombo", ["0"], [43,20],
                         self.update_increase_buys)
        self.ability_score_grid.addWidget(self.ability_cha_combo, 11, 11, 1, 1)

        self.skillframe = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.skillframe, "Skillframe", shape=[540, 130, 481, 801])
        self.grid_layout_widget_2 = QtWidgets.QWidget(self.skillframe)
        initialize_widget(self.grid_layout_widget_2, "gridLayoutWidget_2",
                            [10, 40, 461, 757])
        self.skills_score_grid = QtWidgets.QGridLayout(self.grid_layout_widget_2)
        self.skills_score_grid.setContentsMargins(0, 0, 0, 0)
        self.skills_score_grid.setObjectName("SkillsScoreGrid")


        self.skills_line1 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line1, "SkillsLine1", vertical=False)
        self.skills_score_grid.addWidget(self.skills_line1, 2, 0, 1, 11)
        self.skills_line2 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line2, "SkillsLine2", vertical=False)
        self.skills_score_grid.addWidget(self.skills_line2, 4, 0, 1, 11)
        self.skills_line3 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line3, "SkillsLine3", vertical=False)
        self.skills_score_grid.addWidget(self.skills_line3, 6, 0, 1, 11)
        self.skills_line4 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line4, "SkillsLine4", vertical=False)
        self.skills_score_grid.addWidget(self.skills_line4, 8, 0, 1, 11)
        self.skills_line5 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line5, "SkillsLine5", vertical=False)
        self.skills_score_grid.addWidget(self.skills_line5, 10, 0, 1, 11)
        self.skills_line6 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line6, "SkillsLine6", vertical=False)
        self.skills_score_grid.addWidget(self.skills_line6, 12, 0, 1, 11)
        self.skills_line7 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line7, "SkillsLine7", vertical=False)
        self.skills_score_grid.addWidget(self.skills_line7, 14, 0, 1, 11)
        self.skills_line8 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line8, "SkillsLine8", vertical=False)
        self.skills_score_grid.addWidget(self.skills_line8, 16, 0, 1, 11)
        self.skills_line9 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line9, "SkillsLine9", vertical=False)
        self.skills_score_grid.addWidget(self.skills_line9, 18, 0, 1, 11)
        self.skills_line10 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line10, "SkillsLine10", vertical=False)
        self.skills_score_grid.addWidget(self.skills_line10, 20, 0, 1, 11)
        self.skills_line11 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line11, "SkillsLine11", vertical=False)
        self.skills_score_grid.addWidget(self.skills_line11, 22, 0, 1, 11)
        self.skills_line12 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line12, "SkillsLine12", vertical=False)
        self.skills_score_grid.addWidget(self.skills_line12, 24, 0, 1, 11)
        self.skills_line13 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line13, "SkillsLine13", vertical=False)
        self.skills_score_grid.addWidget(self.skills_line13, 26, 0, 1, 11)
        self.skills_line14 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line14, "SkillsLine14", vertical=False)
        self.skills_score_grid.addWidget(self.skills_line14, 28, 0, 1, 11)
        self.skills_line15 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line15, "SkillsLine15", vertical=False)
        self.skills_score_grid.addWidget(self.skills_line15, 30, 0, 1, 11)
        self.skills_line16 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line16, "SkillsLine16", vertical=False)
        self.skills_score_grid.addWidget(self.skills_line16, 32, 0, 1, 11)
        self.skills_line17 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line17, "SkillsLine17", vertical=False)
        self.skills_score_grid.addWidget(self.skills_line17, 34, 0, 1, 11)
        self.skills_line18 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line18, "SkillsLine18", vertical=False)
        self.skills_score_grid.addWidget(self.skills_line18, 36, 0, 1, 11)
        self.skills_line19 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line19, "SkillsLine19", vertical=False)
        self.skills_score_grid.addWidget(self.skills_line19, 38, 0, 1, 11)
        self.skills_line20 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line20, "SkillsLine20", vertical=False)
        self.skills_score_grid.addWidget(self.skills_line20, 40, 0, 1, 11)



        self.skills_line30 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line30, "SkillsLine30", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line30, 1, 9, 1, 1)
        self.skills_line31 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line31, "SkillsLine31", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line31, 3, 9, 1, 1)
        self.skills_line32 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line32, "SkillsLine32", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line32, 5, 9, 1, 1)
        self.skills_line33 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line33, "SkillsLine33", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line33, 7, 9, 1, 1)
        self.skills_line34 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line34, "SkillsLine34", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line34, 9, 9, 1, 1)
        self.skills_line35 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line35, "SkillsLine35", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line35, 11, 9, 1, 1)
        self.skills_line36 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line36, "SkillsLine36", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line36, 13, 9, 1, 1)
        self.skills_line37 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line37, "SkillsLine37", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line37, 15, 9, 1, 1)
        self.skills_line38 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line38, "SkillsLine38", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line38, 17, 9, 1, 1)
        self.skills_line39 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line39, "SkillsLine39", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line39, 19, 9, 1, 1)
        self.skills_line40 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line40, "SkillsLine40", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line40, 21, 9, 1, 1)
        self.skills_line41 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line41, "SkillsLine41", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line41, 23, 9, 1, 1)
        self.skills_line42 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line42, "SkillsLine42", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line42, 25, 9, 1, 1)
        self.skills_line43 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line43, "SkillsLine43", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line43, 27, 9, 1, 1)
        self.skills_line44 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line44, "SkillsLine44", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line44, 29, 9, 1, 1)
        self.skills_line45 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line45, "SkillsLine45", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line45, 31, 9, 1, 1)
        self.skills_line46 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line46, "SkillsLine46", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line46, 33, 9, 1, 1)
        self.skills_line47 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line47, "SkillsLine47", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line47, 35, 9, 1, 1)
        self.skills_line48 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line48, "SkillsLine48", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line48, 37, 9, 1, 1)
        self.skills_line49 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line49, "SkillsLine49", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line49, 39, 9, 1, 1)
        self.skills_line50 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line50, "SkillsLine50", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line50, 41, 9, 1, 1)


        self.skills_line51 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line51, "SkillsLine51", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line51, 1, 3, 1, 1)
        self.skills_line52 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line52, "SkillsLine52", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line52, 3, 3, 1, 1)
        self.skills_line53 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line53, "SkillsLine53", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line53, 5, 3, 1, 1)
        self.skills_line54 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line54, "SkillsLine54", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line54, 7, 3, 1, 1)
        self.skills_line55 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line55, "SkillsLine55", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line55, 9, 3, 1, 1)
        self.skills_line56 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line56, "SkillsLine56", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line56, 11, 3, 1, 1)
        self.skills_line57 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line57, "SkillsLine57", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line57, 13, 3, 1, 1)
        self.skills_line58 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line58, "SkillsLine58", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line58, 15, 3, 1, 1)
        self.skills_line59 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line59, "SkillsLine59", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line59, 17, 3, 1, 1)
        self.skills_line60 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line60, "SkillsLine60", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line60, 19, 3, 1, 1)
        self.skills_line61 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line61, "SkillsLine61", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line61, 21, 3, 1, 1)
        self.skills_line62 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line62, "SkillsLine62", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line62, 23, 3, 1, 1)
        self.skills_line63 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line63, "SkillsLine63", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line63, 25, 3, 1, 1)
        self.skills_line64 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line64, "SkillsLine64", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line64, 27, 3, 1, 1)
        self.skills_line65 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line65, "SkillsLine65", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line65, 29, 3, 1, 1)
        self.skills_line66 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line66, "SkillsLine66", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line66, 31, 3, 1, 1)
        self.skills_line67 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line67, "SkillsLine67", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line67, 33, 3, 1, 1)
        self.skills_line68 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line68, "SkillsLine68", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line68, 35, 3, 1, 1)
        self.skills_line69 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line69, "SkillsLine69", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line69, 37, 3, 1, 1)
        self.skills_line70 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line70, "SkillsLine70", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line70, 39, 3, 1, 1)
        self.skills_line71 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line71, "SkillsLine71", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line71, 41, 3, 1, 1)

        self.skills_line72 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line72, "SkillsLine72", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line72, 1, 5, 1, 1)
        self.skills_line73 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line73, "SkillsLine73", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line73, 3, 5, 1, 1)
        self.skills_line74 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line74, "SkillsLine74", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line74, 5, 5, 1, 1)
        self.skills_line75 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line75, "SkillsLine75", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line75, 7, 5, 1, 1)
        self.skills_line76 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line76, "SkillsLine76", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line76, 9, 5, 1, 1)
        self.skills_line77 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line77, "SkillsLine77", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line77, 11, 5, 1, 1)
        self.skills_line78 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line78, "SkillsLine78", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line78, 13, 5, 1, 1)
        self.skills_line79 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line79, "SkillsLine79", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line79, 15, 5, 1, 1)
        self.skills_line80 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line80, "SkillsLine80", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line80, 17, 5, 1, 1)
        self.skills_line81 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line81, "SkillsLine81", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line81, 19, 5, 1, 1)
        self.skills_line82 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line82, "SkillsLine82", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line82, 21, 5, 1, 1)
        self.skills_line83 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line83, "SkillsLine83", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line83, 23, 5, 1, 1)
        self.skills_line84 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line84, "SkillsLine84", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line84, 25, 5, 1, 1)
        self.skills_line85 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line85, "SkillsLine85", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line85, 27, 5, 1, 1)
        self.skills_line86 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line86, "SkillsLine86", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line86, 29, 5, 1, 1)
        self.skills_line87 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line87, "SkillsLine87", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line87, 31, 5, 1, 1)
        self.skills_line88 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line88, "SkillsLine88", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line88, 33, 5, 1, 1)
        self.skills_line89 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line89, "SkillsLine89", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line89, 35, 5, 1, 1)
        self.skills_line90 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line90, "SkillsLine90", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line90, 37, 5, 1, 1)
        self.skills_line91 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line91, "SkillsLine91", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line91, 39, 5, 1, 1)
        self.skills_line92 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line92, "SkillsLine92", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line92, 41, 5, 1, 1)


        self.skills_line93 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line93, "SkillsLine93", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line93, 1, 7, 1, 1)
        self.skills_line94 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line94, "SkillsLine94", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line94, 3, 7, 1, 1)
        self.skills_line95 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line95, "SkillsLine95", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line95, 5, 7, 1, 1)
        self.skills_line96 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line96, "SkillsLine96", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line96, 7, 7, 1, 1)
        self.skills_line97 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line97, "SkillsLine97", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line97, 9, 7, 1, 1)
        self.skills_line98 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line98, "SkillsLine98", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line98, 11, 7, 1, 1)
        self.skills_line99 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line99, "SkillsLine99", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line99, 13, 7, 1, 1)
        self.skills_line100 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line100, "SkillsLine100", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line100, 15, 7, 1, 1)
        self.skills_line101 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line101, "SkillsLine101", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line101, 17, 7, 1, 1)
        self.skills_line102 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line102, "SkillsLine102", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line102, 19, 7, 1, 1)
        self.skills_line103 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line103, "SkillsLine103", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line103, 21, 7, 1, 1)
        self.skills_line104 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line104, "SkillsLine104", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line104, 23, 7, 1, 1)
        self.skills_line105 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line105, "SkillsLine105", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line105, 25, 7, 1, 1)
        self.skills_line106 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line106, "SkillsLine106", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line106, 27, 7, 1, 1)
        self.skills_line107 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line107, "SkillsLine107", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line107, 29, 7, 1, 1)
        self.skills_line108 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line108, "SkillsLine108", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line108, 31, 7, 1, 1)
        self.skills_line109 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line109, "SkillsLine109", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line109, 33, 7, 1, 1)
        self.skills_line110 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line110, "SkillsLine110", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line110, 35, 7, 1, 1)
        self.skills_line111 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line111, "SkillsLine111", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line111, 37, 7, 1, 1)
        self.skills_line112 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line112, "SkillsLine112", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line112, 39, 7, 1, 1)
        self.skills_line113 = QtWidgets.QFrame(self.grid_layout_widget_2)
        initialize_frame(self.skills_line113, "SkillsLine113", vertical=True)
        self.skills_score_grid.addWidget(self.skills_line113, 41, 7, 1, 1)

        self.skill_total_text = QtWidgets.QLabel(self.grid_layout_widget_2) # TODO
        initialize_text(self.skill_total_text, "SkillTotalText", "Total")
        self.skills_score_grid.addWidget(self.skill_total_text, 0, 2, 1, 1)
        self.skill_ranks_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.skill_ranks_text, "SkillRanksText", "Ranks")
        self.skills_score_grid.addWidget(self.skill_ranks_text, 0, 4, 1, 1)
        self.skill_class_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.skill_class_text, "SkillClassText", "Class Bonus")
        self.skills_score_grid.addWidget(self.skill_class_text, 0, 6, 1, 1)
        self.skill_ability_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.skill_ability_text, "SkillAbilityText", "Ability Mod")
        self.skills_score_grid.addWidget(self.skill_ability_text, 0, 8, 1, 1)
        self.skill_misc_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.skill_misc_text, "SkillMiscText", "Misc Mod")
        self.skills_score_grid.addWidget(self.skill_misc_text, 0, 10, 1, 1)

        self.acrobatics_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.acrobatics_text, "AcrobaticsText", "Acrobatics (Dex)")
        self.skills_score_grid.addWidget(self.acrobatics_text, 1, 0, 1, 2)
        self.athletics_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.athletics_text, "AthleticsText", "Athletics (Str)")
        self.skills_score_grid.addWidget(self.athletics_text, 3, 0, 1, 2)
        self.bluff_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.bluff_text, "BluffText", "Bluff (Cha)")
        self.skills_score_grid.addWidget(self.bluff_text, 5, 0, 1, 2)
        self.computers_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.computers_text, "ComputersText", "Computers (Int)")
        self.skills_score_grid.addWidget(self.computers_text, 7, 0, 1, 2)
        self.culture_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.culture_text, "CultureText", "Culture (Int)")
        self.skills_score_grid.addWidget(self.culture_text, 9, 0, 1, 2)
        self.diplomacy_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.diplomacy_text, "DiplomacyText", "Diplomacy (Cha)")
        self.skills_score_grid.addWidget(self.diplomacy_text, 11, 0, 1, 2)
        self.disguise_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.disguise_text, "DisguiseText", "Disguise (Cha)")
        self.skills_score_grid.addWidget(self.disguise_text, 13, 0, 1, 2)

        self.engineering_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.engineering_text, "EngineeringText", "Engineering (Int)")
        self.skills_score_grid.addWidget(self.engineering_text, 15, 0, 1, 2)
        self.intimidate_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.intimidate_text, "IntimidateText", "Intimidate (Cha)")
        self.skills_score_grid.addWidget(self.intimidate_text, 17, 0, 1, 2)

        self.life_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.life_text, "LifeText", "Life Science (Int)")
        self.skills_score_grid.addWidget(self.life_text, 19, 0, 1, 2)
        self.medicine_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.medicine_text, "MedicineText", "Medicine (Int)")
        self.skills_score_grid.addWidget(self.medicine_text, 21, 0, 1, 2)
        self.mysticism_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.mysticism_text, "MysticismText", "Mysticism (Wis)")
        self.skills_score_grid.addWidget(self.mysticism_text, 23, 0, 1, 2)
        self.perception_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.perception_text, "PerceptionText", "Perception (Wis)")
        self.skills_score_grid.addWidget(self.perception_text, 25, 0, 1, 2)
        self.physical_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.physical_text, "PhysicalText", "Physical Science (Int)")
        self.skills_score_grid.addWidget(self.physical_text, 27, 0, 1, 2)

        self.piloting_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.piloting_text, "PilotingText", "Piloting (Dex)")
        self.skills_score_grid.addWidget(self.piloting_text, 29, 0, 1, 2)

        self.profession_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.profession_text, "ProfessionText", "Profession")
        self.skills_score_grid.addWidget(self.profession_text, 31, 0, 1, 1)
        self.rank_prof1_skill_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_prof1_skill_combo, "RankProf1SkillCombo", ["Wis", "Int", "Cha"],
                         [43, 20], self.update_profession)
        self.skills_score_grid.addWidget(self.rank_prof1_skill_combo, 31, 1, 1, 1)
        self.profession2_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.profession2_text, "Profession2Text", "Profession")
        self.skills_score_grid.addWidget(self.profession2_text, 33, 0, 1, 1)
        self.rank_prof2_skill_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_prof2_skill_combo, "RankProf2SkillCombo", ["Wis", "Int", "Cha"],
                         [43, 20], self.update_profession)
        self.skills_score_grid.addWidget(self.rank_prof2_skill_combo, 33, 1, 1, 1)
        self.sense_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.sense_text, "SenseText", "Sense Motive (Wis)")
        self.skills_score_grid.addWidget(self.sense_text, 35, 0, 1, 2)
        self.slight_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.slight_text, "SlightText", "Slight of Hand (Dex)")
        self.skills_score_grid.addWidget(self.slight_text, 37, 0, 1, 2)
        self.stealth_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.stealth_text, "StealthText", "Stealth (Dex)")
        self.skills_score_grid.addWidget(self.stealth_text, 39, 0, 1, 2)
        self.survival_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.survival_text, "SurvivalText", "Survival (Wis)")
        self.skills_score_grid.addWidget(self.survival_text, 41, 0, 1, 2)

        self.acrobatics_total = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.acrobatics_total, "AcrobaticsTotal", shape=[50, 20])
        self.skills_score_grid.addWidget(self.acrobatics_total, 1, 2, 1, 1)
        self.athletics_total = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.athletics_total, "AthleticsTotal", shape=[50, 20])
        self.skills_score_grid.addWidget(self.athletics_total, 3, 2, 1, 1)
        self.bluff_total = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.bluff_total, "BluffTotal", shape=[50, 20])
        self.skills_score_grid.addWidget(self.bluff_total, 5, 2, 1, 1)
        self.computers_total = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.computers_total, "ComputersTotal", shape=[50, 20])
        self.skills_score_grid.addWidget(self.computers_total, 7, 2, 1, 1)
        self.culture_total = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.culture_total, "CultureTotal", shape=[50, 20])
        self.skills_score_grid.addWidget(self.culture_total, 9, 2, 1, 1)
        self.diplomacy_total = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.diplomacy_total, "DiplomacyTotal", shape=[50, 20])
        self.skills_score_grid.addWidget(self.diplomacy_total, 11, 2, 1, 1)
        self.disguise_total = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.disguise_total, "DisguiseTotal", shape=[50, 20])
        self.skills_score_grid.addWidget(self.disguise_total, 13, 2, 1, 1)

        self.engineering_total = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.engineering_total, "EngineeringTotal", shape=[50, 20])
        self.skills_score_grid.addWidget(self.engineering_total, 15, 2, 1, 1)
        self.intimidate_total = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.intimidate_total, "IntimidateTotal", shape=[50, 20])
        self.skills_score_grid.addWidget(self.intimidate_total, 17, 2, 1, 1)

        self.life_total = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.life_total, "LifeTotal", shape=[50, 20])
        self.skills_score_grid.addWidget(self.life_total, 19, 2, 1, 1)
        self.medicine_total = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.medicine_total, "MedicineTotal", shape=[50, 20])
        self.skills_score_grid.addWidget(self.medicine_total, 21, 2, 1, 1)
        self.mysticism_total = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.mysticism_total, "MysticismTotal", shape=[50, 20])
        self.skills_score_grid.addWidget(self.mysticism_total, 23, 2, 1, 1)
        self.perception_total = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.perception_total, "PerceptionTotal", shape=[50, 20])
        self.skills_score_grid.addWidget(self.perception_total, 25, 2, 1, 1)
        self.physical_total = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.physical_total, "PhysicalTotal", shape=[50, 20])
        self.skills_score_grid.addWidget(self.physical_total, 27, 2, 1, 1)

        self.piloting_total = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.piloting_total, "PilotingTotal", shape=[50, 20])
        self.skills_score_grid.addWidget(self.piloting_total, 29, 2, 1, 1)

        self.profession_total = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.profession_total, "ProfessionTotal", shape=[50, 20])
        self.skills_score_grid.addWidget(self.profession_total, 31, 2, 1, 1)
        self.profession2_total = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.profession2_total, "Profession2Total", shape=[50, 20])
        self.skills_score_grid.addWidget(self.profession2_total, 33, 2, 1, 1)
        self.sense_total = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.sense_total, "SenseTotal", shape=[50, 20])
        self.skills_score_grid.addWidget(self.sense_total, 35, 2, 1, 1)
        self.slight_total = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.slight_total, "SlightTotal", shape=[50, 20])
        self.skills_score_grid.addWidget(self.slight_total, 37, 2, 1, 1)
        self.stealth_total = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.stealth_total, "StealthTotal", shape=[50, 20])
        self.skills_score_grid.addWidget(self.stealth_total, 39, 2, 1, 1)
        self.survival_total = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.survival_total, "SurvivalTotal", shape=[50, 20])
        self.skills_score_grid.addWidget(self.survival_total, 41, 2, 1, 1)

        self.rank_acrobatics_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_acrobatics_combo, "RankAcrobaticsCombo", ["0"], [43, 20],
                         self.update_skill_buy)
        self.skills_score_grid.addWidget(self.rank_acrobatics_combo, 1, 4, 1, 1)
        self.rank_athletics_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_athletics_combo, "RankAthleticsCombo", ["0"], [43, 20],
                         self.update_skill_buy)
        self.skills_score_grid.addWidget(self.rank_athletics_combo, 3, 4, 1, 1)
        self.rank_bluff_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_bluff_combo, "RankBluffCombo", ["0"], [43, 20],
                         self.update_skill_buy)
        self.skills_score_grid.addWidget(self.rank_bluff_combo, 5, 4, 1, 1)
        self.rank_computers_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_computers_combo, "RankComputersCombo", ["0"], [43, 20],
                         self.update_skill_buy)
        self.skills_score_grid.addWidget(self.rank_computers_combo, 7, 4, 1, 1)
        self.rank_culture_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_culture_combo, "RankCultureCombo", ["0"], [43, 20],
                         self.update_skill_buy)
        self.skills_score_grid.addWidget(self.rank_culture_combo, 9, 4, 1, 1)
        self.rank_diplomacy_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_diplomacy_combo, "RankDiplomacyCombo", ["0"], [43, 20],
                         self.update_skill_buy)
        self.skills_score_grid.addWidget(self.rank_diplomacy_combo, 11, 4, 1, 1)
        self.rank_disguise_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_disguise_combo, "RankDisguiseCombo", ["0"], [43, 20],
                         self.update_skill_buy)
        self.skills_score_grid.addWidget(self.rank_disguise_combo, 13, 4, 1, 1)

        self.rank_engineering_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_engineering_combo, "RankLifeCombo", ["0"], [43, 20],
                         self.update_skill_buy)
        self.skills_score_grid.addWidget(self.rank_engineering_combo, 15, 4, 1, 1)
        self.rank_intimidate_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_intimidate_combo, "RankMedicineCombo", ["0"], [43, 20],
                         self.update_skill_buy)
        self.skills_score_grid.addWidget(self.rank_intimidate_combo, 17, 4, 1, 1)

        self.rank_life_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_life_combo, "RankLifeCombo", ["0"], [43, 20],
                         self.update_skill_buy)
        self.skills_score_grid.addWidget(self.rank_life_combo, 19, 4, 1, 1)
        self.rank_medicine_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_medicine_combo, "RankMedicineCombo", ["0"], [43, 20],
                         self.update_skill_buy)
        self.skills_score_grid.addWidget(self.rank_medicine_combo, 21, 4, 1, 1)
        self.rank_mysticism_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_mysticism_combo, "RankMysticismCombo", ["0"], [43, 20],
                         self.update_skill_buy)
        self.skills_score_grid.addWidget(self.rank_mysticism_combo, 23, 4, 1, 1)
        self.rank_perception_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_perception_combo, "RankPerceptionCombo", ["0"], [43, 20],
                         self.update_skill_buy)
        self.skills_score_grid.addWidget(self.rank_perception_combo, 25, 4, 1, 1)
        self.rank_physical_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_physical_combo, "RankPhysicalCombo", ["0"], [43, 20],
                         self.update_skill_buy)
        self.skills_score_grid.addWidget(self.rank_physical_combo, 27, 4, 1, 1)

        self.rank_piloting_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_piloting_combo, "RankSenseCombo", ["0"], [43, 20],
                         self.update_skill_buy)
        self.skills_score_grid.addWidget(self.rank_piloting_combo, 29, 4, 1, 1)

        self.rank_profession1_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_profession1_combo, "RankProfession1Combo", ["0"], [43, 20],
                         self.update_skill_buy)
        self.skills_score_grid.addWidget(self.rank_profession1_combo, 31, 4, 1, 1)
        self.rank_profession2_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_profession2_combo, "RankProfession2Combo", ["0"], [43, 20],
                         self.update_skill_buy)
        self.skills_score_grid.addWidget(self.rank_profession2_combo, 33, 4, 1, 1)
        self.rank_sense_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_sense_combo, "RankSenseCombo", ["0"], [43, 20],
                         self.update_skill_buy)
        self.skills_score_grid.addWidget(self.rank_sense_combo, 35, 4, 1, 1)
        self.rank_slight_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_slight_combo, "RankSlightCombo", ["0"], [43, 20],
                         self.update_skill_buy)
        self.skills_score_grid.addWidget(self.rank_slight_combo, 37, 4, 1, 1)
        self.rank_stealth_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_stealth_combo, "RankStealthCombo", ["0"], [43, 20],
                         self.update_skill_buy)
        self.skills_score_grid.addWidget(self.rank_stealth_combo, 39, 4, 1, 1)
        self.rank_survival_combo = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.rank_survival_combo, "RankSurvivalCombo", ["0"], [43, 20],
                         self.update_skill_buy)
        self.skills_score_grid.addWidget(self.rank_survival_combo, 41, 4, 1, 1)


        self.acrobatics_class = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.acrobatics_class, "AcrobaticsClass", shape=[50, 20])
        self.skills_score_grid.addWidget(self.acrobatics_class, 1, 6, 1, 1)
        self.athletics_class = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.athletics_class, "AthleticsClass", shape=[50, 20])
        self.skills_score_grid.addWidget(self.athletics_class, 3, 6, 1, 1)
        self.bluff_class = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.bluff_class, "BluffClass", shape=[50, 20])
        self.skills_score_grid.addWidget(self.bluff_class, 5, 6, 1, 1)
        self.computers_class = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.computers_class, "ComputersClass", shape=[50, 20])
        self.skills_score_grid.addWidget(self.computers_class, 7, 6, 1, 1)
        self.culture_class = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.culture_class, "CultureClass", shape=[50, 20])
        self.skills_score_grid.addWidget(self.culture_class, 9, 6, 1, 1)
        self.diplomacy_class = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.diplomacy_class, "DiplomacyClass", shape=[50, 20])
        self.skills_score_grid.addWidget(self.diplomacy_class, 11, 6, 1, 1)
        self.disguise_class = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.disguise_class, "DisguiseClass", shape=[50, 20])
        self.skills_score_grid.addWidget(self.disguise_class, 13, 6, 1, 1)

        self.engineering_class = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.engineering_class, "EngineeringClass", shape=[50, 20])
        self.skills_score_grid.addWidget(self.engineering_class, 15, 6, 1, 1)
        self.intimidate_class = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.intimidate_class, "IntimidateClass", shape=[50, 20])
        self.skills_score_grid.addWidget(self.intimidate_class, 17, 6, 1, 1)

        self.life_class = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.life_class, "LifeClass", shape=[50, 20])
        self.skills_score_grid.addWidget(self.life_class, 19, 6, 1, 1)
        self.medicine_class = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.medicine_class, "MedicineClass", shape=[50, 20])
        self.skills_score_grid.addWidget(self.medicine_class, 21, 6, 1, 1)
        self.mysticism_class = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.mysticism_class, "MysticismClass", shape=[50, 20])
        self.skills_score_grid.addWidget(self.mysticism_class, 23, 6, 1, 1)
        self.perception_class = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.perception_class, "PerceptionClass", shape=[50, 20])
        self.skills_score_grid.addWidget(self.perception_class, 25, 6, 1, 1)
        self.physical_class = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.physical_class, "PhysicalClass", shape=[50, 20])
        self.skills_score_grid.addWidget(self.physical_class, 27, 6, 1, 1)
        self.profession_class = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.profession_class, "ProfessionClass", shape=[50, 20])
        self.skills_score_grid.addWidget(self.profession_class, 29, 6, 1, 1)
        self.profession2_class = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.profession2_class, "Profession2Class", shape=[50, 20])
        self.skills_score_grid.addWidget(self.profession2_class, 31, 6, 1, 1)

        self.piloting_class = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.piloting_class, "PilotingClass", shape=[50, 20])
        self.skills_score_grid.addWidget(self.piloting_class, 33, 6, 1, 1)

        self.sense_class = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.sense_class, "SenseClass", shape=[50, 20])
        self.skills_score_grid.addWidget(self.sense_class, 35, 6, 1, 1)
        self.slight_class = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.slight_class, "SlightClass", shape=[50, 20])
        self.skills_score_grid.addWidget(self.slight_class, 37, 6, 1, 1)
        self.stealth_class = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.stealth_class, "StealthClass", shape=[50, 20])
        self.skills_score_grid.addWidget(self.stealth_class, 39, 6, 1, 1)
        self.survival_class = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.survival_class, "SurvivalClass", shape=[50, 20])
        self.skills_score_grid.addWidget(self.survival_class, 41, 6, 1, 1)

        self.acrobatics_ability = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.acrobatics_ability, "AcrobaticsAbility", shape=[50, 20])
        self.skills_score_grid.addWidget(self.acrobatics_ability, 1, 8, 1, 1)
        self.athletics_ability = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.athletics_ability, "AthleticsAbility", shape=[50, 20])
        self.skills_score_grid.addWidget(self.athletics_ability, 3, 8, 1, 1)
        self.bluff_ability = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.bluff_ability, "BluffAbility", shape=[50, 20])
        self.skills_score_grid.addWidget(self.bluff_ability, 5, 8, 1, 1)
        self.computers_ability = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.computers_ability, "ComputersAbility", shape=[50, 20])
        self.computers_ability.setMaximumSize(QtCore.QSize(50, 20))
        self.computers_ability.setReadOnly(True)
        self.computers_ability.setObjectName("ComputersAbility")
        self.skills_score_grid.addWidget(self.computers_ability, 7, 8, 1, 1)
        self.culture_ability = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.culture_ability, "CultureAbility", shape=[50, 20])
        self.skills_score_grid.addWidget(self.culture_ability, 9, 8, 1, 1)
        self.diplomacy_ability = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.diplomacy_ability, "DiplomacyAbility", shape=[50, 20])
        self.skills_score_grid.addWidget(self.diplomacy_ability, 11, 8, 1, 1)
        self.disguise_ability = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.disguise_ability, "DisguiseAbility", shape=[50, 20])
        self.skills_score_grid.addWidget(self.disguise_ability, 13, 8, 1, 1)

        self.engineering_ability = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.engineering_ability, "EngineeringAbility", shape=[50, 20])
        self.skills_score_grid.addWidget(self.engineering_ability, 15, 8, 1, 1)
        self.intimidate_ability = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.intimidate_ability, "IntimidateAbility", shape=[50, 20])
        self.skills_score_grid.addWidget(self.intimidate_ability, 17, 8, 1, 1)

        self.life_ability = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.life_ability, "LifeAbility", shape=[50, 20])
        self.skills_score_grid.addWidget(self.life_ability, 19, 8, 1, 1)
        self.medicine_ability = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.medicine_ability, "MedicineAbility", shape=[50, 20])
        self.skills_score_grid.addWidget(self.medicine_ability, 21, 8, 1, 1)
        self.mysticism_ability = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.mysticism_ability, "MysticismAbility", shape=[50, 20])
        self.skills_score_grid.addWidget(self.mysticism_ability, 23, 8, 1, 1)
        self.perception_ability = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.perception_ability, "PerceptionAbility", shape=[50, 20])
        self.skills_score_grid.addWidget(self.perception_ability, 25, 8, 1, 1)
        self.physical_ability = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.physical_ability, "PhysicalAbility", shape=[50, 20])
        self.skills_score_grid.addWidget(self.physical_ability, 27, 8, 1, 1)

        self.piloting_ability = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.piloting_ability, "PilotingAbility", shape=[50, 20])
        self.skills_score_grid.addWidget(self.piloting_ability, 29, 8, 1, 1)

        self.profession_ability = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.profession_ability, "ProfessionAbility", shape=[50, 20])
        self.skills_score_grid.addWidget(self.profession_ability, 31, 8, 1, 1)
        self.profession2_ability = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.profession2_ability, "Profession2Ability", shape=[50, 20])
        self.skills_score_grid.addWidget(self.profession2_ability, 33, 8, 1, 1)
        self.sense_ability = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.sense_ability, "SenseAbility", shape=[50, 20])
        self.skills_score_grid.addWidget(self.sense_ability, 35, 8, 1, 1)
        self.slight_ability = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.slight_ability, "SlightAbility", shape=[50, 20])
        self.skills_score_grid.addWidget(self.slight_ability, 37, 8, 1, 1)
        self.stealth_ability = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.stealth_ability, "StealthAbility", shape=[50, 20])
        self.skills_score_grid.addWidget(self.stealth_ability, 39, 8, 1, 1)
        self.survival_ability = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.survival_ability, "SurvivalAbility", shape=[50, 20])
        self.skills_score_grid.addWidget(self.survival_ability, 41, 8, 1, 1)

        self.acrobatics_misc = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.acrobatics_misc, "AcrobaticsMisc", shape=[50, 20])
        self.skills_score_grid.addWidget(self.acrobatics_misc, 1, 10, 1, 1)
        self.athletics_misc = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.athletics_misc, "AthleticsMisc", shape=[50, 20])
        self.skills_score_grid.addWidget(self.athletics_misc, 3, 10, 1, 1)
        self.bluff_misc = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.bluff_misc, "BluffMisc", shape=[50, 20])
        self.skills_score_grid.addWidget(self.bluff_misc, 5, 10, 1, 1)
        self.computers_misc = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.computers_misc, "ComputersMisc", shape=[50, 20])
        self.skills_score_grid.addWidget(self.computers_misc, 7, 10, 1, 1)
        self.culture_misc = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.culture_misc, "CultureMisc", shape=[50, 20])
        self.skills_score_grid.addWidget(self.culture_misc, 9, 10, 1, 1)
        self.diplomacy_misc = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.diplomacy_misc, "DiplomacyMisc", shape=[50, 20])
        self.skills_score_grid.addWidget(self.diplomacy_misc, 11, 10, 1, 1)
        self.disguise_misc = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.disguise_misc, "DisguiseMisc", shape=[50, 20])
        self.skills_score_grid.addWidget(self.disguise_misc, 13, 10, 1, 1)

        self.engineering_misc = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.engineering_misc, "EngineeringMisc", shape=[50, 20])
        self.skills_score_grid.addWidget(self.engineering_misc, 15, 10, 1, 1)
        self.intimidate_misc = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.intimidate_misc, "IntimidateMisc", shape=[50, 20])
        self.skills_score_grid.addWidget(self.intimidate_misc, 17, 10, 1, 1)

        self.life_misc = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.life_misc, "LifeMisc", shape=[50, 20])
        self.skills_score_grid.addWidget(self.life_misc, 19, 10, 1, 1)
        self.medicine_misc = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.medicine_misc, "MedicineMisc", shape=[50, 20])
        self.skills_score_grid.addWidget(self.medicine_misc, 21, 10, 1, 1)
        self.mysticism_misc = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.mysticism_misc, "MysticismMisc", shape=[50, 20])
        self.skills_score_grid.addWidget(self.mysticism_misc, 23, 10, 1, 1)
        self.perception_misc = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.perception_misc, "PerceptionMisc", shape=[50, 20])
        self.skills_score_grid.addWidget(self.perception_misc, 25, 10, 1, 1)
        self.physical_misc = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.physical_misc, "PhysicalMisc", shape=[50, 20])
        self.skills_score_grid.addWidget(self.physical_misc, 27, 10, 1, 1)

        self.piloting_misc = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.piloting_misc, "PilotingMisc", shape=[50, 20])
        self.skills_score_grid.addWidget(self.piloting_misc, 29, 10, 1, 1)

        self.profession_misc = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.profession_misc, "ProfessionMisc", shape=[50, 20])
        self.skills_score_grid.addWidget(self.profession_misc, 31, 10, 1, 1)
        self.profession2_misc = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.profession2_misc, "Profession2Misc", shape=[50, 20])
        self.skills_score_grid.addWidget(self.profession2_misc, 33, 10, 1, 1)
        self.sense_misc = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.sense_misc, "SenseMisc", shape=[50, 20])
        self.skills_score_grid.addWidget(self.sense_misc, 35, 10, 1, 1)
        self.slight_misc = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.slight_misc, "SlightMisc", shape=[50, 20])
        self.skills_score_grid.addWidget(self.slight_misc, 37, 10, 1, 1)
        self.stealth_misc = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.stealth_misc, "StealthMisc", shape=[50, 20])
        self.skills_score_grid.addWidget(self.stealth_misc, 39, 10, 1, 1)
        self.survival_misc = QtWidgets.QLineEdit(self.grid_layout_widget_2)
        initialize_edit(self.survival_misc, "SurvivalMisc", shape=[50, 20])
        self.skills_score_grid.addWidget(self.survival_misc, 41, 10, 1, 1)

        self.horizontal_layout_widget = QtWidgets.QWidget(self.skillframe)
        initialize_widget(self.horizontal_layout_widget, "horizontalLayoutWidget",
                            [80, 10, 311, 31])

        self.skill_count_grid = QtWidgets.QHBoxLayout(self.horizontal_layout_widget)
        self.skill_count_grid.setContentsMargins(0, 0, 0, 0)
        self.skill_count_grid.setObjectName("SkillCountGrid")

        self.remaining_skill_text = QtWidgets.QLabel(self.horizontal_layout_widget)
        initialize_text(self.remaining_skill_text, "RemainingSkillText", "Remaining Skill Points")
        self.skill_count_grid.addWidget(self.remaining_skill_text)

        self.remaining_skill_box = QtWidgets.QLineEdit(self.horizontal_layout_widget)
        initialize_edit(self.remaining_skill_box, "RemainingSkillBox", shape=[40, 20])
        self.skill_count_grid.addWidget(self.remaining_skill_box)

        self.skills_per_text = QtWidgets.QLabel(self.horizontal_layout_widget)
        initialize_text(self.skills_per_text, "SkillsPerText", "Skill Ranks Per Level")
        self.skill_count_grid.addWidget(self.skills_per_text)

        self.skills_per_box = QtWidgets.QLineEdit(self.horizontal_layout_widget)
        initialize_edit(self.skills_per_box, "SkillsPerBox", shape=[40, 20])
        self.skill_count_grid.addWidget(self.skills_per_box)

        self.initframe = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.initframe, "Initframe", shape=[130, 70, 261, 51])
        self.horizontal_layout_widget_3 = QtWidgets.QWidget(self.initframe)
        initialize_widget(self.horizontal_layout_widget_3, "horizontalLayoutWidget_3",
                            [10, 10, 241, 31])
        self.initiative_grid = QtWidgets.QHBoxLayout(self.horizontal_layout_widget_3)
        self.initiative_grid.setContentsMargins(0, 0, 0, 0)
        self.initiative_grid.setObjectName("InitiativeGrid")

        self.initiative_text = QtWidgets.QLabel(self.horizontal_layout_widget_3)
        initialize_text(self.initiative_text, "InitiativeText", "Initiative", max_size=[50, 20])
        self.initiative_grid.addWidget(self.initiative_text)

        self.initiative_total = QtWidgets.QLineEdit(self.horizontal_layout_widget_3)
        initialize_edit(self.initiative_total, "InitiativeTotal", shape=[40, 20])
        self.initiative_grid.addWidget(self.initiative_total)

        self.initiative_equals = QtWidgets.QLabel(self.horizontal_layout_widget_3)
        initialize_text(self.initiative_equals, "InitiativeEquals", "=", max_size=[10, 25])
        self.initiative_grid.addWidget(self.initiative_equals)

        self.initiative_dex_mod = QtWidgets.QLineEdit(self.horizontal_layout_widget_3)
        initialize_edit(self.initiative_dex_mod, "InitiativeDexMod", shape=[40, 20])
        self.initiative_grid.addWidget(self.initiative_dex_mod)

        self.initiative_plus = QtWidgets.QLabel(self.horizontal_layout_widget_3)
        initialize_text(self.initiative_plus, "InitiativePlus", "+", max_size=[10, 25])
        self.initiative_grid.addWidget(self.initiative_plus)

        self.initiative_misc_mod = QtWidgets.QLineEdit(self.horizontal_layout_widget_3)
        initialize_edit(self.initiative_misc_mod, "InitiativeMiscMod", shape=[40, 20])
        self.initiative_grid.addWidget(self.initiative_misc_mod)

        self.hp_frame = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.hp_frame, "HPframe", shape=[490, 10, 261, 80])
        self.grid_layout_widget_3 = QtWidgets.QWidget(self.hp_frame)
        initialize_widget(self.grid_layout_widget_3, "gridLayoutWidget_3", [10, 10, 241, 65])
        self.hp_grid = QtWidgets.QGridLayout(self.grid_layout_widget_3)
        self.hp_grid.setContentsMargins(0, 0, 0, 0)
        self.hp_grid.setObjectName("HPGrid")

        self.hp_line1 = QtWidgets.QFrame(self.grid_layout_widget_3)
        initialize_frame(self.hp_line1, "HPLine1", vertical=True)
        self.hp_grid.addWidget(self.hp_line1, 2, 2, 1, 1)
        self.hp_line2 = QtWidgets.QFrame(self.grid_layout_widget_3)
        initialize_frame(self.hp_line2, "HPLine2", vertical=True)
        self.hp_grid.addWidget(self.hp_line2, 2, 4, 1, 1)
        self.hp_line3 = QtWidgets.QFrame(self.grid_layout_widget_3)
        initialize_frame(self.hp_line3, "HPLine3", vertical=False)
        self.hp_grid.addWidget(self.hp_line3, 1, 0, 1, 6)

        self.hp_total_text = QtWidgets.QLabel(self.grid_layout_widget_3)
        initialize_text(self.hp_total_text, "HPTotalText", "Total")
        self.hp_grid.addWidget(self.hp_total_text, 2, 0, 1, 1)
        self.sp_stamina_text = QtWidgets.QLabel(self.grid_layout_widget_3)
        initialize_text(self.sp_stamina_text, "HPStaminaText", "Stamina Points")
        self.sp_stamina_text.setObjectName("HPStaminaText")
        self.sp_stamina_text.setText("Stamina Points")
        self.hp_grid.addWidget(self.sp_stamina_text, 0, 1, 1, 1)
        self.hp_hit_text = QtWidgets.QLabel(self.grid_layout_widget_3)
        initialize_text(self.hp_hit_text, "HPHitText", "Hit Points")
        self.hp_grid.addWidget(self.hp_hit_text, 0, 3, 1, 1)
        self.hp_resolve_text = QtWidgets.QLabel(self.grid_layout_widget_3)
        initialize_text(self.hp_resolve_text, "HPResolveText", "Resolve")
        self.hp_grid.addWidget(self.hp_resolve_text, 0, 5, 1, 1)

        self.hp_hit_box = QtWidgets.QLineEdit(self.grid_layout_widget_3)
        initialize_edit(self.hp_hit_box, "HPHitBox", shape=[40, 25])
        self.hp_grid.addWidget(self.hp_hit_box, 2, 3, 1, 1)

        self.hp_resolve_box = QtWidgets.QLineEdit(self.grid_layout_widget_3)
        initialize_edit(self.hp_resolve_box, "HPResolveBox", shape=[40, 25])
        self.hp_grid.addWidget(self.hp_resolve_box, 2, 5, 1, 1)
        self.hp_stamina_box = QtWidgets.QLineEdit(self.grid_layout_widget_3)
        initialize_edit(self.hp_stamina_box, "HPStaminaBox", shape=[40, 25])
        self.hp_grid.addWidget(self.hp_stamina_box, 2, 1, 1, 1)

        self.armorframe = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.armorframe, "Armorframe", shape=[20, 450, 471, 141])
        self.grid_layout_widget_4 = QtWidgets.QWidget(self.armorframe)
        initialize_widget(self.grid_layout_widget_4, "gridLayoutWidget_4", [10, 10, 451, 126])
        self.grid_layout_widget_4.setGeometry(QtCore.QRect(10, 10, 451, 126))
        self.grid_layout_widget_4.setObjectName("gridLayoutWidget_4")
        self.ac_grid = QtWidgets.QGridLayout(self.grid_layout_widget_4)
        self.ac_grid.setContentsMargins(0, 0, 0, 0)
        self.ac_grid.setObjectName("ACGrid")

        self.armor_line1 = QtWidgets.QFrame(self.grid_layout_widget_4)
        initialize_frame(self.armor_line1, "ArmorLine1", vertical=False)
        self.ac_grid.addWidget(self.armor_line1, 3, 0, 1, 8)
        self.armor_line2 = QtWidgets.QFrame(self.grid_layout_widget_4)
        initialize_frame(self.armor_line2, "ArmorLine2", vertical=False)
        self.ac_grid.addWidget(self.armor_line2, 5, 0, 1, 8)

        self.eac_text = QtWidgets.QLabel(self.grid_layout_widget_4)
        initialize_text(self.eac_text, "EACText", "Energy Armor Class (EAC)")
        self.ac_grid.addWidget(self.eac_text, 2, 0, 1, 1)
        self.kac_text = QtWidgets.QLabel(self.grid_layout_widget_4)
        initialize_text(self.kac_text, "KACText", "Kinetic Armor Class (KAC)")
        self.ac_grid.addWidget(self.kac_text, 4, 0, 1, 1)
        self.acvs_text = QtWidgets.QLabel(self.grid_layout_widget_4)
        initialize_text(self.acvs_text, "ACVSText", "AC VS Combat Maneuvers")
        self.ac_grid.addWidget(self.acvs_text, 6, 0, 1, 1)
        self.ac_total_text = QtWidgets.QLabel(self.grid_layout_widget_4)
        initialize_text(self.ac_total_text, "ACTotalText", "Total")
        self.ac_grid.addWidget(self.ac_total_text, 0, 1, 1, 1)
        self.ac_armor_text = QtWidgets.QLabel(self.grid_layout_widget_4)
        initialize_text(self.ac_armor_text, "ACArmorText", "Armor Bonus")
        self.ac_grid.addWidget(self.ac_armor_text, 0, 3, 1, 1)
        self.ac_dex_text = QtWidgets.QLabel(self.grid_layout_widget_4)
        initialize_text(self.ac_dex_text, "ACDexText", "Dex Mod")
        self.ac_grid.addWidget(self.ac_dex_text, 0, 5, 1, 1)
        self.ac_misc_text = QtWidgets.QLabel(self.grid_layout_widget_4)
        initialize_text(self.ac_misc_text, "ACMiscText", "MiscMod")
        self.ac_grid.addWidget(self.ac_misc_text, 0, 7, 1, 1)

        self.eac_plus = QtWidgets.QLabel(self.grid_layout_widget_4)
        initialize_text(self.eac_plus, "EACPlus", "+", max_size=[10, 25])
        self.ac_grid.addWidget(self.eac_plus, 2, 4, 1, 1)
        self.eac_plus_2 = QtWidgets.QLabel(self.grid_layout_widget_4)
        initialize_text(self.eac_plus_2, "EACPlus_2", "+", max_size=[10, 25])
        self.ac_grid.addWidget(self.eac_plus_2, 2, 6, 1, 1)
        self.eac_equals = QtWidgets.QLabel(self.grid_layout_widget_4)
        initialize_text(self.eac_equals, "EACEquals", "= 10 +", max_size=[40, 25])
        self.ac_grid.addWidget(self.eac_equals, 2, 2, 1, 1)
        self.kac_plus = QtWidgets.QLabel(self.grid_layout_widget_4)
        initialize_text(self.kac_plus, "KACPlus", "+", max_size=[10, 25])
        self.ac_grid.addWidget(self.kac_plus, 4, 4, 1, 1)
        self.kac_plus_2 = QtWidgets.QLabel(self.grid_layout_widget_4)
        initialize_text(self.kac_plus_2, "KACPlus_2", "+", max_size=[10, 25])
        self.ac_grid.addWidget(self.kac_plus_2, 4, 6, 1, 1)
        self.kac_equals = QtWidgets.QLabel(self.grid_layout_widget_4)
        initialize_text(self.kac_equals, "KACEquals", "= 10 +", max_size=[40, 25])
        self.ac_grid.addWidget(self.kac_equals, 4, 2, 1, 1)
        self.acvs_equals = QtWidgets.QLabel(self.grid_layout_widget_4)
        initialize_text(self.acvs_equals, "ACVSEquals", "= 8 +", max_size=[40, 25])
        self.ac_grid.addWidget(self.acvs_equals, 6, 2, 1, 1)


        self.eac_total_box = QtWidgets.QLineEdit(self.grid_layout_widget_4)
        initialize_edit(self.eac_total_box, "EACTotalBox", shape=[40, 25])
        self.ac_grid.addWidget(self.eac_total_box, 2, 1, 1, 1)
        self.eac_armor_box = QtWidgets.QLineEdit(self.grid_layout_widget_4)
        initialize_edit(self.eac_armor_box, "EACArmorBox", shape=[40, 25])
        self.ac_grid.addWidget(self.eac_armor_box, 2, 3, 1, 1)
        self.eac_dex_box = QtWidgets.QLineEdit(self.grid_layout_widget_4)
        initialize_edit(self.eac_dex_box, "EACDexBox", shape=[40, 25])
        self.ac_grid.addWidget(self.eac_dex_box, 2, 5, 1, 1)
        self.eac_misc_box = QtWidgets.QLineEdit(self.grid_layout_widget_4)
        initialize_edit(self.eac_misc_box, "EACMiscBox", shape=[40, 25])
        self.ac_grid.addWidget(self.eac_misc_box, 2, 7, 1, 1)
        self.kac_total_box = QtWidgets.QLineEdit(self.grid_layout_widget_4)
        initialize_edit(self.kac_total_box, "KACTotalBox", shape=[40, 25])
        self.ac_grid.addWidget(self.kac_total_box, 4, 1, 1, 1)
        self.kac_armor_box = QtWidgets.QLineEdit(self.grid_layout_widget_4)
        initialize_edit(self.kac_armor_box, "KACArmorBox", shape=[40, 25])
        self.ac_grid.addWidget(self.kac_armor_box, 4, 3, 1, 1)
        self.kac_dex_box = QtWidgets.QLineEdit(self.grid_layout_widget_4)
        initialize_edit(self.kac_dex_box, "KACDexBox", shape=[40, 25])
        self.ac_grid.addWidget(self.kac_dex_box, 4, 5, 1, 1)
        self.kac_misc_box = QtWidgets.QLineEdit(self.grid_layout_widget_4)
        initialize_edit(self.kac_misc_box, "KACMiscBox", shape=[40, 25])
        self.ac_grid.addWidget(self.kac_misc_box, 4, 7, 1, 1)
        self.acvs_total_box = QtWidgets.QLineEdit(self.grid_layout_widget_4)
        initialize_edit(self.acvs_total_box, "ACVSTotalBox", shape=[40, 25])
        self.ac_grid.addWidget(self.acvs_total_box, 6, 1, 1, 1)
        self.acvs_kac_box = QtWidgets.QLineEdit(self.grid_layout_widget_4)
        initialize_edit(self.acvs_kac_box, "ACVSKACBox", shape=[40, 25])
        self.ac_grid.addWidget(self.acvs_kac_box, 6, 3, 1, 1)

        self.saveframe = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.saveframe, "Saveframe", shape=[20, 600, 361, 141])
        self.grid_layout_widget_5 = QtWidgets.QWidget(self.saveframe)
        initialize_widget(self.grid_layout_widget_5, "gridLayoutWidget_5", [10, 10, 341, 126])
        self.grid_layout_widget_5.setGeometry(QtCore.QRect(10, 10, 341, 126))
        self.grid_layout_widget_5.setObjectName("gridLayoutWidget_5")
        self.save_grid = QtWidgets.QGridLayout(self.grid_layout_widget_5)
        self.save_grid.setContentsMargins(0, 0, 0, 0)
        self.save_grid.setObjectName("SaveGrid")

        self.save_line1 = QtWidgets.QFrame(self.grid_layout_widget_5)
        initialize_frame(self.save_line1, "SaveLine1", vertical=False)
        self.save_grid.addWidget(self.save_line1, 2, 0, 1, 8)
        self.save_line2 = QtWidgets.QFrame(self.grid_layout_widget_5)
        initialize_frame(self.save_line2, "SaveLine2", vertical=False)
        self.save_grid.addWidget(self.save_line2, 4, 0, 1, 8)

        self.fortitude_text = QtWidgets.QLabel(self.grid_layout_widget_5)
        initialize_text(self.fortitude_text, "FortitudeText", "Fortitude")
        self.save_grid.addWidget(self.fortitude_text, 1, 0, 1, 1)
        self.reflex_text = QtWidgets.QLabel(self.grid_layout_widget_5)
        initialize_text(self.reflex_text, "ReflexText", "Reflex")
        self.save_grid.addWidget(self.reflex_text, 3, 0, 1, 1)
        self.will_text = QtWidgets.QLabel(self.grid_layout_widget_5)
        initialize_text(self.will_text, "WillText", "Will")
        self.save_grid.addWidget(self.will_text, 5, 0, 1, 1)

        self.save_total_text = QtWidgets.QLabel(self.grid_layout_widget_5)
        initialize_text(self.save_total_text, "SaveTotalText", "Total")
        self.save_grid.addWidget(self.save_total_text, 0, 1, 1, 1)
        self.save_base_text = QtWidgets.QLabel(self.grid_layout_widget_5)
        initialize_text(self.save_base_text, "SaveBaseText", "Base Save")
        self.save_grid.addWidget(self.save_base_text, 0, 3, 1, 1)
        self.save_ability_text = QtWidgets.QLabel(self.grid_layout_widget_5)
        initialize_text(self.save_ability_text, "SaveAbilityText", "Ability Mod")
        self.save_grid.addWidget(self.save_ability_text, 0, 5, 1, 1)
        self.save_misc_text = QtWidgets.QLabel(self.grid_layout_widget_5)
        initialize_text(self.save_misc_text, "SaveMiscText", "Misc Mod")
        self.save_grid.addWidget(self.save_misc_text, 0, 7, 1, 1)

        self.fortitude_equals = QtWidgets.QLabel(self.grid_layout_widget_5)
        initialize_text(self.fortitude_equals, "FortitudeEquals", "=", max_size=[10, 25])
        self.save_grid.addWidget(self.fortitude_equals, 1, 2, 1, 1)
        self.fortitude_plus = QtWidgets.QLabel(self.grid_layout_widget_5)
        initialize_text(self.fortitude_plus, "FortitudePlus", "+", max_size=[10, 25])
        self.save_grid.addWidget(self.fortitude_plus, 1, 4, 1, 1)
        self.fortitude_plus_2 = QtWidgets.QLabel(self.grid_layout_widget_5)
        initialize_text(self.fortitude_plus_2, "FortitudePlus_2", "+", max_size=[10, 25])
        self.save_grid.addWidget(self.fortitude_plus_2, 1, 6, 1, 1)
        self.reflex_equals = QtWidgets.QLabel(self.grid_layout_widget_5)
        initialize_text(self.reflex_equals, "ReflexEquals", "=", max_size=[10, 25])
        self.save_grid.addWidget(self.reflex_equals, 3, 2, 1, 1)
        self.reflex_plus = QtWidgets.QLabel(self.grid_layout_widget_5)
        initialize_text(self.reflex_plus, "ReflexPlus", "+", max_size=[10, 25])
        self.save_grid.addWidget(self.reflex_plus, 3, 4, 1, 1)
        self.reflex_plus_2 = QtWidgets.QLabel(self.grid_layout_widget_5)
        initialize_text(self.reflex_plus_2, "ReflexPlus_2", "+", max_size=[10, 25])
        self.save_grid.addWidget(self.reflex_plus_2, 3, 6, 1, 1)
        self.will_equals = QtWidgets.QLabel(self.grid_layout_widget_5)
        initialize_text(self.will_equals, "WillEquals", "=", max_size=[10, 25])
        self.save_grid.addWidget(self.will_equals, 5, 2, 1, 1)
        self.will_plus = QtWidgets.QLabel(self.grid_layout_widget_5)
        initialize_text(self.will_plus, "WillPlus", "+", max_size=[10, 25])
        self.save_grid.addWidget(self.will_plus, 5, 4, 1, 1)
        self.will_plus_2 = QtWidgets.QLabel(self.grid_layout_widget_5)
        initialize_text(self.will_plus_2, "WillPlus_2", "+", max_size=[10, 25])
        self.save_grid.addWidget(self.will_plus_2, 5, 6, 1, 1)

        self.fortitude_total_box = QtWidgets.QLineEdit(self.grid_layout_widget_5)
        initialize_edit(self.fortitude_total_box, "FortitudeTotalBox", shape=[40, 25])
        self.save_grid.addWidget(self.fortitude_total_box, 1, 1, 1, 1)
        self.fortitude_base_box = QtWidgets.QLineEdit(self.grid_layout_widget_5)
        initialize_edit(self.fortitude_base_box, "FortitudeBaseBox", shape=[40, 25])
        self.save_grid.addWidget(self.fortitude_base_box, 1, 3, 1, 1)
        self.fortitude_ability_box = QtWidgets.QLineEdit(self.grid_layout_widget_5)
        initialize_edit(self.fortitude_ability_box, "FortitudeAbilityBox", shape=[40, 25])
        self.save_grid.addWidget(self.fortitude_ability_box, 1, 5, 1, 1)
        self.fortitude_misc_box = QtWidgets.QLineEdit(self.grid_layout_widget_5)
        initialize_edit(self.fortitude_misc_box, "FortitudeMiscBox", shape=[40, 25])
        self.save_grid.addWidget(self.fortitude_misc_box, 1, 7, 1, 1)
        self.reflex_total_box = QtWidgets.QLineEdit(self.grid_layout_widget_5)
        initialize_edit(self.reflex_total_box, "ReflexTotalBox", shape=[40, 25])
        self.save_grid.addWidget(self.reflex_total_box, 3, 1, 1, 1)
        self.reflex_base_box = QtWidgets.QLineEdit(self.grid_layout_widget_5)
        initialize_edit(self.reflex_base_box, "ReflexBaseBox", shape=[40, 25])
        self.save_grid.addWidget(self.reflex_base_box, 3, 3, 1, 1)
        self.reflex_ability_box = QtWidgets.QLineEdit(self.grid_layout_widget_5)
        initialize_edit(self.reflex_ability_box, "ReflexAbilityBox", shape=[40, 25])
        self.save_grid.addWidget(self.reflex_ability_box, 3, 5, 1, 1)
        self.reflex_misc_box = QtWidgets.QLineEdit(self.grid_layout_widget_5)
        initialize_edit(self.reflex_misc_box, "ReflexMiscBox", shape=[40, 25])
        self.save_grid.addWidget(self.reflex_misc_box, 3, 7, 1, 1)
        self.will_total_box = QtWidgets.QLineEdit(self.grid_layout_widget_5)
        initialize_edit(self.will_total_box, "WillTotalBox", shape=[40, 25])
        self.save_grid.addWidget(self.will_total_box, 5, 1, 1, 1)
        self.will_base_box = QtWidgets.QLineEdit(self.grid_layout_widget_5)
        initialize_edit(self.will_base_box, "WillBaseBox", shape=[40, 25])
        self.save_grid.addWidget(self.will_base_box, 5, 3, 1, 1)
        self.will_ability_box = QtWidgets.QLineEdit(self.grid_layout_widget_5)
        initialize_edit(self.will_ability_box, "WillAbilityBox", shape=[40, 25])
        self.save_grid.addWidget(self.will_ability_box, 5, 5, 1, 1)
        self.will_misc_box = QtWidgets.QLineEdit(self.grid_layout_widget_5)
        initialize_edit(self.will_misc_box, "WillMiscBox", shape=[40, 25])
        self.save_grid.addWidget(self.will_misc_box, 5, 7, 1, 1)


        self.attackframe = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.attackframe, "Attackframe", shape=[20, 750, 361, 181])
        self.grid_layout_widget_6 = QtWidgets.QWidget(self.attackframe)
        initialize_widget(self.grid_layout_widget_6, "gridLayoutWidget_6", [10, 10, 341, 164])
        self.attack_grid = QtWidgets.QGridLayout(self.grid_layout_widget_6)
        self.attack_grid.setContentsMargins(0, 0, 0, 0)
        self.attack_grid.setObjectName("AttackGrid")

        self.attack_line1 = QtWidgets.QFrame(self.grid_layout_widget_6)
        initialize_frame(self.attack_line1, "AttackLine1", vertical=False)
        self.attack_grid.addWidget(self.attack_line1, 2, 0, 1, 8)
        self.attack_line2 = QtWidgets.QFrame(self.grid_layout_widget_6)
        initialize_frame(self.attack_line2, "AttackLine2", vertical=False)
        self.attack_grid.addWidget(self.attack_line2, 5, 0, 1, 8)

        self.melee_text = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.melee_text, "MeleeText", "Melee Attack")
        self.attack_grid.addWidget(self.melee_text, 1, 0, 1, 1)
        self.melee_total_text = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.melee_text, "MeleeTotalText", "Total")
        self.attack_grid.addWidget(self.melee_total_text, 0, 1, 1, 1)
        self.melee_bab_text = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.melee_bab_text, "MeleeBABText", "BAB")
        self.attack_grid.addWidget(self.melee_bab_text, 0, 3, 1, 1)
        self.melee_mod_text = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.melee_mod_text, "MeleeModText", "Str Mod")
        self.attack_grid.addWidget(self.melee_mod_text, 0, 5, 1, 1)
        self.melee_misc_text = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.melee_misc_text, "MeleeMiscText", "Misc Mod")
        self.attack_grid.addWidget(self.melee_misc_text, 0, 7, 1, 1)

        self.ranged_text = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.ranged_text, "RangedText", "Ranged Attack")
        self.attack_grid.addWidget(self.ranged_text, 4, 0, 1, 1)
        self.ranged_total_text = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.ranged_total_text, "RangedTotalText", "Total")
        self.attack_grid.addWidget(self.ranged_total_text, 3, 1, 1, 1)
        self.ranged_bab_text = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.ranged_bab_text, "RangedBABText", "BAB")
        self.attack_grid.addWidget(self.ranged_bab_text, 3, 3, 1, 1)
        self.ranged_mod_text = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.ranged_mod_text, "RangedModText", "Dex Mod")
        self.attack_grid.addWidget(self.ranged_mod_text, 3, 5, 1, 1)
        self.ranged_misc_text = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.ranged_misc_text, "RangedMiscText", "Misc Mod")
        self.ranged_misc_text.setMaximumSize(QtCore.QSize(16777215, 25))
        self.ranged_misc_text.setObjectName("RangedMiscText")
        self.ranged_misc_text.setText("Misc Mod")
        self.attack_grid.addWidget(self.ranged_misc_text, 3, 7, 1, 1)

        self.thrown_text = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.thrown_text, "ThrownText", "Thrown Attack")
        self.attack_grid.addWidget(self.thrown_text, 7, 0, 1, 1)
        self.thrown_total_text = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.thrown_total_text, "ThrownTotalText", "Total")
        self.attack_grid.addWidget(self.thrown_total_text, 6, 1, 1, 1)
        self.thrown_bab_text = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.thrown_bab_text, "ThrownBABText", "BAB")
        self.attack_grid.addWidget(self.thrown_bab_text, 6, 3, 1, 1)
        self.thrown_mod_text = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.thrown_mod_text, "ThrownModText", "Str Mod")
        self.attack_grid.addWidget(self.thrown_mod_text, 6, 5, 1, 1)
        self.thrown_misc_text = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.thrown_misc_text, "ThrownMiscText", "Misc Mod")
        self.attack_grid.addWidget(self.thrown_misc_text, 6, 7, 1, 1)


        self.attack_equals = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.attack_equals, "AttackEquals", "=", max_size=[10, 25])
        self.attack_grid.addWidget(self.attack_equals, 1, 2, 1, 1)
        self.attack_equals_2 = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.attack_equals_2, "AttackEquals_2", "=", max_size=[10, 25])
        self.attack_grid.addWidget(self.attack_equals_2, 4, 2, 1, 1)
        self.attack_equals_3 = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.attack_equals_3, "AttackEquals_3", "=", max_size=[10, 25])
        self.attack_grid.addWidget(self.attack_equals_3, 7, 2, 1, 1)
        self.attack_plus = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.attack_plus, "AttackPlus", "+", max_size=[10, 25])
        self.attack_grid.addWidget(self.attack_plus, 1, 4, 1, 1)
        self.attack_plus_2 = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.attack_plus_2, "AttackPlus_2", "+", max_size=[10, 25])
        self.attack_grid.addWidget(self.attack_plus_2, 1, 6, 1, 1)
        self.attack_plus_3 = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.attack_plus_3, "AttackPlus_3", "+", max_size=[10, 25])
        self.attack_grid.addWidget(self.attack_plus_3, 4, 4, 1, 1)
        self.attack_plus_4 = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.attack_plus_4, "AttackPlus_4", "+", max_size=[10, 25])
        self.attack_grid.addWidget(self.attack_plus_4, 7, 4, 1, 1)
        self.attack_plus_5 = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.attack_plus_5, "AttackPlus_5", "+", max_size=[10, 25])
        self.attack_grid.addWidget(self.attack_plus_5, 4, 6, 1, 1)
        self.attack_plus_6 = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.attack_plus_6, "AttackPlus_6", "+", max_size=[10, 25])
        self.attack_grid.addWidget(self.attack_plus_6, 7, 6, 1, 1)

        self.melee_total_box = QtWidgets.QLineEdit(self.grid_layout_widget_6)
        initialize_edit(self.melee_total_box, "MeleeTotalBox", shape=[40, 25])
        self.attack_grid.addWidget(self.melee_total_box, 1, 1, 1, 1)
        self.melee_bab_box = QtWidgets.QLineEdit(self.grid_layout_widget_6)
        initialize_edit(self.melee_bab_box, "MeleeBABBox", shape=[40, 25])
        self.attack_grid.addWidget(self.melee_bab_box, 1, 3, 1, 1)
        self.melee_mod_box = QtWidgets.QLineEdit(self.grid_layout_widget_6)
        initialize_edit(self.melee_mod_box, "MeleeModBox", shape=[40, 25])
        self.attack_grid.addWidget(self.melee_mod_box, 1, 5, 1, 1)
        self.melee_misc_box = QtWidgets.QLineEdit(self.grid_layout_widget_6)
        initialize_edit(self.melee_misc_box, "MeleeMiscBox", shape=[40, 25])
        self.attack_grid.addWidget(self.melee_misc_box, 1, 7, 1, 1)
        self.ranged_total_box = QtWidgets.QLineEdit(self.grid_layout_widget_6)
        initialize_edit(self.ranged_total_box, "RangedTotalBox", shape=[40, 25])
        self.attack_grid.addWidget(self.ranged_total_box, 4, 1, 1, 1)
        self.thrown_bab_box = QtWidgets.QLineEdit(self.grid_layout_widget_6)
        initialize_edit(self.thrown_bab_box, "ThrownBABBox", shape=[40, 25])
        self.attack_grid.addWidget(self.thrown_bab_box, 7, 3, 1, 1)
        self.ranged_mod_box = QtWidgets.QLineEdit(self.grid_layout_widget_6)
        initialize_edit(self.ranged_mod_box, "RangedModBox", shape=[40, 25])
        self.attack_grid.addWidget(self.ranged_mod_box, 4, 5, 1, 1)
        self.ranged_misc_box = QtWidgets.QLineEdit(self.grid_layout_widget_6)
        initialize_edit(self.ranged_misc_box, "RangedMiscBox", shape=[40, 25])
        self.attack_grid.addWidget(self.ranged_misc_box, 4, 7, 1, 1)
        self.thrown_total_box = QtWidgets.QLineEdit(self.grid_layout_widget_6)
        initialize_edit(self.thrown_total_box, "ThrownTotalBox", shape=[40, 25])
        self.attack_grid.addWidget(self.thrown_total_box, 7, 1, 1, 1)
        self.ranged_bab_box = QtWidgets.QLineEdit(self.grid_layout_widget_6)
        initialize_edit(self.ranged_bab_box, "RangedBABBox", shape=[40, 25])
        self.attack_grid.addWidget(self.ranged_bab_box, 4, 3, 1, 1)
        self.thrown_mod_box = QtWidgets.QLineEdit(self.grid_layout_widget_6)
        initialize_edit(self.thrown_mod_box, "ThrownModBox", shape=[40, 25])
        self.attack_grid.addWidget(self.thrown_mod_box, 7, 5, 1, 1)
        self.thrown_misc_box = QtWidgets.QLineEdit(self.grid_layout_widget_6)
        initialize_edit(self.thrown_misc_box, "ThrownMiscBox", shape=[40, 25])
        self.attack_grid.addWidget(self.thrown_misc_box, 7, 7, 1, 1)

        self.classframe = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.classframe, "Classframe", shape=[790, 10, 271, 111])

        self.horizontal_layout_widget_4 = QtWidgets.QWidget(self.classframe)
        initialize_widget(self.horizontal_layout_widget_4, "horizontalLayoutWidget_4",
                            [10, 40, 251, 31])
        self.horizontal_layout_widget_4.setGeometry(QtCore.QRect(10, 40, 251, 31))
        self.horizontal_layout_widget_4.setObjectName("horizontalLayoutWidget_4")

        self.race_grid = QtWidgets.QHBoxLayout(self.horizontal_layout_widget_4)
        self.race_grid.setContentsMargins(0, 0, 0, 0)
        self.race_grid.setObjectName("RaceGrid")

        self.race_text = QtWidgets.QLabel(self.horizontal_layout_widget_4)
        initialize_text(self.race_text, "RaceText", "Race", max_size=[30, 25])
        self.race_grid.addWidget(self.race_text)

        self.race_combo = QtWidgets.QComboBox()
        self.race_combo.setMaximumSize(QtCore.QSize(120, 20))
        self.race_combo.setObjectName("RaceCombo")

        initialize_combo_model(self.race_combo, [x.capitalize() for x in raceAbilities],
                                "<<Select Race>>", connection=self.race_activated)
        self.race_grid.addWidget(self.race_combo)

        self.race_ability_combo = QtWidgets.QComboBox(self.horizontal_layout_widget_4)
        initialize_combo(self.race_ability_combo, "RaceAbilityCombo", ["Blank"], [85, 20],
                         self.human_key_update)
        self.race_grid.addWidget(self.race_ability_combo)

        self.horizontal_layout_widget_5 = QtWidgets.QWidget(self.classframe)
        initialize_widget(self.horizontal_layout_widget_5, "horizontalLayoutWidget_5",
                            [10, 70, 251, 31])
        self.theme_grid = QtWidgets.QHBoxLayout(self.horizontal_layout_widget_5)
        self.theme_grid.setContentsMargins(0, 0, 0, 0)
        self.theme_grid.setObjectName("ThemeGrid")
        self.theme_text = QtWidgets.QLabel(self.horizontal_layout_widget_5)
        initialize_text(self.theme_text, "ThemeText", "Theme", max_size=[32, 25])
        self.theme_text.setMaximumSize(QtCore.QSize(32, 25))
        self.theme_text.setObjectName("ThemeText")
        self.theme_text.setText("Theme")
        self.theme_grid.addWidget(self.theme_text)

        self.theme_combo = QtWidgets.QComboBox()
        self.theme_combo.setMaximumSize(QtCore.QSize(120, 20))
        self.theme_combo.setObjectName("ThemeCombo")
        initialize_combo_model(self.theme_combo, [x.capitalize() for x in themeAbilities],
                                "<<Select Theme>>", connection=self.theme_activated)
        self.theme_grid.addWidget(self.theme_combo)

        self.theme_ability_combo = QtWidgets.QComboBox(self.horizontal_layout_widget_5)
        initialize_combo(self.theme_ability_combo, "ThemeAbilityCombo", ["Blank"], [85, 20],
                         self.themeless_key_update)
        self.theme_grid.addWidget(self.theme_ability_combo)

        self.horizontal_layout_widget_6 = QtWidgets.QWidget(self.classframe)
        initialize_widget(self.horizontal_layout_widget_6, "horizontalLayoutWidget_6",
                            [10, 10, 251, 31])

        self.class_grid = QtWidgets.QHBoxLayout(self.horizontal_layout_widget_6)
        self.class_grid.setContentsMargins(0, 0, 0, 0)
        self.class_grid.setObjectName("ClassGrid")

        self.class_text = QtWidgets.QLabel(self.horizontal_layout_widget_6)
        initialize_text(self.class_text, "ClassText", "Class", max_size=[27, 25])
        self.class_grid.addWidget(self.class_text)

        self.class_combo = QtWidgets.QComboBox(self.horizontal_layout_widget_6)
        self.class_combo.setMaximumSize(QtCore.QSize(120, 20))
        self.class_combo.setObjectName("ClassCombo")
        initialize_combo_model(self.class_combo, [x.capitalize() for x in classesStatBonus],
                                "<<Select Class>>", connection=self.class_activated)
        self.class_grid.addWidget(self.class_combo)

        self.class_ability_combo = QtWidgets.QComboBox(self.horizontal_layout_widget_6)
        initialize_combo(self.class_ability_combo, "ClassAbilityCombo", ["Blank"], [85, 20],
                         self.soldier_key_update)
        self.class_grid.addWidget(self.class_ability_combo)

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1075, 21))
        self.menubar.setObjectName("menubar")
        self.menu_save = QtWidgets.QMenu(self.menubar)
        self.menu_save.setObjectName("menuSave")
        self.menu_save.setTitle("Menu")
        self.menu_extras = QtWidgets.QMenu(self.menubar)
        self.menu_extras.setObjectName("menuExtras")
        self.menu_extras.setTitle("Extras")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.action_save = QtWidgets.QAction(main_window)
        self.action_save.setObjectName("actionSave")
        self.action_save.setText("Save")
        self.action_save.triggered.connect(self.save_character)
        self.action_load = QtWidgets.QAction(main_window)
        self.action_load.setObjectName("actionLoad")
        self.action_load.setText("Load")
        self.action_load.triggered.connect(self.load_character)
        self.action_feats = QtWidgets.QAction(main_window)
        self.action_feats.setObjectName("actionFeats")
        self.action_feats.setText("Feats")
        self.action_feats.triggered.connect(self.open_feats)
        self.action_spells = QtWidgets.QAction(main_window)
        self.action_spells.setObjectName("actionSpells")
        self.action_spells.setText("Spells")
        self.menu_save.addAction(self.action_save)
        self.menu_save.addAction(self.action_load)
        self.menu_extras.addAction(self.action_feats)
        self.menu_extras.addAction(self.action_spells)
        self.menubar.addAction(self.menu_save.menuAction())
        self.menubar.addAction(self.menu_extras.menuAction())


        main_window.setWindowTitle("CharacterSheetMaker")
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def update_name(self):
        """update the name of the character
        """
        self.character.set_name(self.character_name_box.toPlainText())

    def class_activated(self, text):
        """sets the extra combobox text depending on if the class is soldier or not

        Args:
            text (str): text of the combobox that determines the class
        """
        self.class_ability_combo.clear()
        if text == "Soldier":
            combo_text = ["Str", "Dex"]
            self.class_ability_combo.addItems(combo_text)
            self.character.set_class_name(text.lower(), combo_text[0].lower())
        else:
            self.class_ability_combo.addItem("Blank")
            self.character.set_class_name(text.lower())

        self.update_class_stats()
        self.update_hp()
        self.update_saves()
        self.update_attack()

    def theme_activated(self, text):
        """sets the extra combobox text depending on if the theme is themeless or not

        Args:
            text (str): text of the combobox that determines the theme
        """
        self.theme_ability_combo.clear()
        if text == "Themeless":
            combo_text = ["Str", "Dex", "Con", "Int", "Wis", "Cha"]
            self.theme_ability_combo.addItems(combo_text)
            self.character.set_theme(text.lower(), combo_text[0].lower())
        else:
            self.theme_ability_combo.addItem("Blank")
            self.character.set_theme(text.lower())

        self.update_theme_stats()

    def race_activated(self, text):
        """sets the extra combobox text depending on if the race is human or not

        Args:
            text (str): text of the combobox that determines the race
        """
        self.race_ability_combo.clear()
        if text == "Human":
            combo_text = ["Str", "Dex", "Con", "Int", "Wis", "Cha"]
            self.race_ability_combo.addItems(combo_text)
            self.character.set_race(text.lower(), combo_text[0].lower())
        else:
            self.race_ability_combo.addItem("Blank")
            self.character.set_race(text.lower())
        self.update_race_stats()

    def soldier_key_update(self, text):
        """sets the key attribute if the class is soldier

        Args:
            text (str): key of the character
        """
        if text != 'Blank':
            self.character.set_class_name("soldier", text.lower())
            self.update_class_stats()

    def themeless_key_update(self, text):
        """sets the key attribute if the theme is themeless

        Args:
            text (str): attribute of the themeless
        """
        if text != 'Blank':
            self.character.set_theme("themeless", text.lower())
            self.update_theme_stats()

    def human_key_update(self, text):
        """sets the key attribute if the theme is themeless
        Args:
            text (str): attribute of the race
        """
        if text != 'Blank':
            self.character.set_race("human", text.lower())
            self.update_race_stats()

    def update_class_stats(self):
        """updates the class blocks in the skills tab
        """
        boxes = [self.acrobatics_class, self.athletics_class, self.bluff_class,
                 self.computers_class, self.culture_class, self.diplomacy_class,
                 self.disguise_class, self.engineering_class, self.intimidate_class,
                 self.life_class, self.medicine_class, self.mysticism_class,
                 self.perception_class, self.physical_class, self.piloting_class,
                 self.profession_class, self.profession2_class, self.sense_class,
                 self.slight_class, self.stealth_class, self.survival_class]

        for skill, box in zip(self.character.skill_class.values(), boxes):
            box.setText(str(skill))
        self.update_skills()
        self.update_hp()

    def update_theme_stats(self):
        """updates the theme blocks in the attributes tab
        """
        boxes = [self.str_theme, self.dex_theme, self.con_theme, self.int_theme, self.wis_theme,
                 self.cha_theme]
        for skill, box in zip(self.character.theme_attributes.values(), boxes):
            box.setText(str(skill))
        self.update_abilities()
        self.update_point_buys()

    def update_race_stats(self):
        """updates the race blocks in the attributes tab
        """
        boxes = [self.str_race, self.dex_race, self.con_race, self.int_race, self.wis_race,
                 self.cha_race]
        for skill, box in zip(self.character.race_attributes.values(), boxes):
            box.setText(str(skill))
        self.update_abilities()
        self.update_hp()
        self.update_point_buys()
        self.update_misc_skills()
        self.update_skill_buy()

    def update_abilities(self):
        """updates the attribute scores in the attributes tab
        """
        self.character.calc_attributes()
        boxes = [self.str_score, self.dex_score, self.con_score, self.int_score, self.wis_score,
                 self.cha_score, self.remaining_point_box, self.remaining_ability_box]
        #classesStatBonus[self.className]["skills"] + self.mods["int"]
        for skill, box in zip([*self.character.attributes.values(),
                               self.point_buy_spendable_points, self.ability_buy_spendable_points], boxes):
            box.setText(str(skill))

        boxes = [self.str_mod, self.dex_mod, self.con_mod, self.int_mod, self.wis_mod,self.cha_mod]
        for skill, box in zip(self.character.mods.values(), boxes):
            box.setText(str(skill))
        boxes = [self.acrobatics_ability, self.athletics_ability, self.bluff_ability,
                 self.computers_ability, self.culture_ability, self.diplomacy_ability,
                 self.disguise_ability, self.engineering_ability, self.intimidate_ability,
                 self.life_ability, self.medicine_ability, self.mysticism_ability,
                 self.perception_ability, self.physical_ability, self.piloting_ability,
                 self.profession_ability, self.profession2_ability, self.sense_ability,
                 self.slight_ability, self.stealth_ability, self.survival_ability]

        skills = [self.character.mods["dex"], self.character.mods["str"],
                  self.character.mods["cha"], self.character.mods["int"],
                  self.character.mods["int"], self.character.mods["cha"],
                  self.character.mods["cha"], self.character.mods["int"],
                  self.character.mods["cha"], self.character.mods["int"],
                  self.character.mods["int"], self.character.mods["wis"],
                  self.character.mods["wis"], self.character.mods["int"],
                  self.character.mods["dex"],

                  self.character.mods[self.character.profession_ability],
                  self.character.mods[self.character.profession2_ability],
                  self.character.mods["wis"], self.character.mods["dex"],
                  self.character.mods["dex"], self.character.mods["wis"]]
        for skill, box in zip(skills, boxes):
            box.setText(str(skill))
        self.update_skills()
        self.update_hp()
        self.update_initiative()
        self.update_saves()
        self.update_ac()
        self.update_attack()

    def update_skills(self):
        """update the skill totals in the skills tab
        """
        if self.character.class_name:
            self.character.calc_skills(verbose=False)
            boxes = [self.acrobatics_total, self.athletics_total, self.bluff_total,
                     self.computers_total, self.culture_total, self.diplomacy_total,
                     self.disguise_total, self.engineering_total, self.intimidate_total,
                     self.life_total, self.medicine_total, self.mysticism_total,
                     self.perception_total, self.physical_total, self.piloting_total,
                     self.profession_total, self.profession2_total, self.sense_total,
                     self.slight_total, self.stealth_total, self.survival_total,
                     self.remaining_skill_box, self.skills_per_box]

            for skill, box in zip([*self.character.skills.values(),self.skill_buy_spendable_points,
                                    (classesStatBonus[self.character.class_name]["skills"] +\
                                        self.character.mods["int"])], boxes):
                box.setText(str(skill))

    def update_hp(self):
        """updates the HP tab related items
        """
        if self.character.race_name and self.character.class_name:
            self.character.calc_hit_points()
        boxes = [self.hp_stamina_box, self.hp_hit_box, self.hp_resolve_box]
        skills = [self.character.stamina_points, self.character.hit_points,
                    self.character.resolve_points]
        for skill, box in zip(skills, boxes):
            box.setText(str(skill))

    def update_initiative(self):
        """update the initiative tab related items
        """
        self.character.calc_init()
        boxes = [self.initiative_total, self.initiative_dex_mod, self.initiative_misc_mod]
        skills = [self.character.initiative, self.character.mods["dex"],
                    self.character.initiative_misc]
        for skill, box in zip(skills, boxes):
            box.setText(str(skill))

    def update_level(self, text):
        """update all boxes related to the level

        Args:
            text (int): entered level
        """
        self.character.class_level = int(text)
        self.update_hp()
        self.character.calc_init()
        self.update_initiative()
        self.update_point_buys()
        self.update_increase_buys()
        self.update_saves()
        self.update_attack()
        if self.character.class_name and self.character.class_level > 0:
            self.update_skill_buy()

    def update_point_buys(self):
        """update abilities based on the point buy system
        """
        point_buys = {
            "strength" : self.point_buy_str_combo,
            "dexterity" : self.point_buy_dex_combo,
            "constitution" : self.point_buy_con_combo,
            "intelligence" : self.point_buy_int_combo,
            "wisdom" : self.point_buy_wis_combo,
            "charisma" : self.point_buy_cha_combo
        }

        attrs = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        self.point_buy_spendable_points = 10
        for attr in attrs:
            tmp = int(point_buys[attr].currentText())
            self.point_buy_spendable_points -= tmp
            self.character.spent_points[attr] = tmp

        for attr in attrs:
            pbuy = point_buys[attr]
            pbuy.clear()
            val = self.point_buy_spendable_points + self.character.spent_points[attr] + 1
            max_val = 10 + self.character.race_attributes[attr] +\
                         self.character.theme_attributes[attr]
            points = [str(i) for i in range(val) if i + max_val <= 18]
            pbuy.addItems(points)
            pbuy.setCurrentIndex(self.character.spent_points[attr])
        self.update_abilities()
        if self.character.class_name and self.character.class_level > 0:
            self.update_skill_buy()

    def update_increase_buys(self):
        """update abilities based on ability increase buy system
        """
        ability_buys = {
            "strength" : self.ability_str_combo,
            "dexterity" : self.ability_dex_combo,
            "constitution" : self.ability_con_combo,
            "intelligence" : self.ability_int_combo,
            "wisdom" : self.ability_wis_combo,
            "charisma" : self.ability_cha_combo
        }
        attrs = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        self.ability_buy_spendable_points = (self.character.class_level // 5)*4
        for attr in attrs:
            tmp = int(ability_buys[attr].currentText())
            self.ability_buy_spendable_points -= tmp
            self.character.ability_increases[attr] = tmp
        
            # self.ability_increases[entered] += 1
            # self.attributes[entered] += 1
            # if self.attributes[entered] < 18:
            #     self.attributes[entered] += 1

        for attr in attrs:
            pbuy = ability_buys[attr]
            pbuy.clear()
            val = 2
            points = [str(i) for i in range(val)]
            pbuy.addItems(points)
            pbuy.setCurrentIndex(self.character.ability_increases[attr])
        self.update_abilities()
        if self.character.class_name and self.character.class_level > 0:
            self.update_skill_buy()


    def update_saves(self):
        """update the save tab related boxes
        """
        if self.character.class_name and self.character.class_level > 0:
            self.character.calc_save()
            boxes = [self.fortitude_total_box, self.reflex_total_box, self.will_total_box,
                     self.fortitude_base_box,  self.reflex_base_box, self.will_base_box,
                     self.fortitude_ability_box, self.reflex_ability_box, self.will_ability_box,
                     self.fortitude_misc_box, self.reflex_misc_box, self.will_misc_box]

            class_bonuses = classesStatBonus[self.character.class_name]
            skills = [self.character.fort_save,self.character.reflex_save,self.character.will_save,
                      class_bonuses["fort"][self.character.class_level - 1],
                      class_bonuses["reflex"][self.character.class_level - 1],
                      class_bonuses["will"][self.character.class_level - 1],
                      self.character.mods["con"], self.character.mods["dex"],
                      self.character.mods["wis"], self.character.fort_save_misc,
                      self.character.reflex_save_misc, self.character.will_save_misc]
            for skill, box in zip(skills, boxes):
                box.setText(str(skill))

    def update_ac(self):
        """update ac tab related boxes
        """
        self.character.calc_armor_class()
        boxes = [self.eac_total_box, self.eac_armor_box, self.eac_dex_box, self.eac_misc_box,
                 self.kac_total_box, self.kac_armor_box, self.kac_dex_box, self.kac_misc_box,
                 self.acvs_total_box, self.acvs_kac_box]
        skills = [self.character.eac, 0, self.character.mods["dex"], 0,
                  self.character.kac, 0, self.character.mods["dex"], 0,
                  self.character.vs_combat, self.character.kac]
        for skill, box in zip(skills, boxes):
            box.setText(str(skill))

    def update_attack(self):
        """update attack tab related boxes
        """
        if self.character.class_name and self.character.class_level > 0:
            self.character.calc_attack()
            boxes = [self.melee_total_box, self.melee_bab_box, self.melee_mod_box,
                     self.melee_misc_box, self.ranged_total_box, self.ranged_bab_box,
                     self.ranged_mod_box, self.ranged_misc_box, self.thrown_total_box,
                     self.thrown_bab_box, self.thrown_mod_box, self.thrown_misc_box]

            class_stat_boni = classesStatBonus[self.character.class_name]
            skills = [self.character.melee, class_stat_boni["bab"][self.character.class_level - 1],
                      self.character.mods["str"], self.character.melee_misc,
                      self.character.range, class_stat_boni["bab"][self.character.class_level - 1],
                      self.character.mods["dex"], self.character.range_misc,
                      self.character.throw, class_stat_boni["bab"][self.character.class_level - 1],
                      self.character.mods["str"], self.character.throw_misc]
            for skill, box in zip(skills, boxes):
                box.setText(str(skill))

    def update_skill_buy(self):
        """update skills based on the skill buys
        """
        skill_buys = {
            "acrobatics"       : self.rank_acrobatics_combo,
            "athletics"        : self.rank_athletics_combo,
            "bluff"            : self.rank_bluff_combo,
            "computers"        : self.rank_computers_combo,
            "culture"          : self.rank_culture_combo,
            "diplomacy"        : self.rank_diplomacy_combo,
            "disguise"         : self.rank_disguise_combo,
            "engineering"      : self.rank_engineering_combo,
            "intimidate"       : self.rank_intimidate_combo,
            "life science"     : self.rank_life_combo,
            "medicine"         : self.rank_medicine_combo,
            "mysticism"        : self.rank_mysticism_combo,
            "perception"       : self.rank_perception_combo,
            "physical science" : self.rank_physical_combo,
            "piloting"         : self.rank_piloting_combo,
            "profession"       : self.rank_profession1_combo,
            "profession2"      : self.rank_profession2_combo,
            "sense motive"     : self.rank_sense_combo,
            "sleight of hand"  : self.rank_slight_combo,
            "stealth"          : self.rank_stealth_combo,
            "survival"         : self.rank_survival_combo
        }
        self.skill_buy_spendable_points = (classesStatBonus[self.character.class_name]["skills"] +\
                                           self.character.mods["int"]) * self.character.class_level
        possible_skill = ["acrobatics", "athletics", "bluff", "computers", "culture", "diplomacy",
                          "disguise", "engineering", "intimidate", "life science", "medicine",
                          "mysticism", "perception", "physical science", "piloting", "profession",
                          "profession2", "sense motive", "sleight of hand", "stealth", "survival"]
        for skill in possible_skill:
            tmp = int(skill_buys[skill].currentText())
            self.skill_buy_spendable_points -= tmp
            self.character.skill_ranks[skill] = tmp

        for skill, pbuy in skill_buys.items():
            pbuy.clear()
            val = self.character.class_level + 1
            points = [str(i) for i in range(val) if i < self.skill_buy_spendable_points +\
                         self.character.skill_ranks[skill] + 1]
            pbuy.addItems(points)
            pbuy.setCurrentIndex(self.character.skill_ranks[skill])

        self.update_skills()


    def update_misc_skills(self):
        """update the misc skills in the skills tab
        """
        boxes = [self.acrobatics_misc, self.athletics_misc, self.bluff_misc, self.computers_misc,
                 self.culture_misc, self.diplomacy_misc, self.disguise_misc, self.engineering_misc,
                 self.intimidate_misc, self.life_misc, self.medicine_misc, self.mysticism_misc,
                 self.perception_misc, self.physical_misc, self.piloting_misc,self.profession_misc,
                 self.profession2_misc, self.sense_misc, self.slight_misc, self.stealth_misc,
                 self.survival_misc]

        for skill, dabbler, box in zip(self.character.skill_misc.values(),
                                        self.character.skill_dabbler.values(), boxes):
            box.setText(str(skill + dabbler))

    def update_profession(self):
        """function to update the ability modifiers for the two profession skills
        """
        prof1 = self.rank_prof1_skill_combo.currentText()
        prof2 = self.rank_prof2_skill_combo.currentText()
        self.character.update_professions(prof1.lower(), prof2.lower())
        self.update_abilities()

    def save_character(self):
        """saves the character to an HTML file
        """
        self.character.update_html()

    def load_character(self):
        """the user selects an HTML file that then gets loaded as a character
        """
        dig = QtWidgets.QFileDialog()
        dig.setFileMode(QtWidgets.QFileDialog.AnyFile)
        #dig.setFilter("HTML Files (*.html)")
        filenames = []

        if dig.exec_():
            filenames = dig.selectedFiles()
        if filenames[0][-5:] == ".html":
            pass

    def open_feats(self):
        """open the feats window
        """
        if self.window is None:
            self.window = UiForm(self.character)
        self.window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UIMainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
