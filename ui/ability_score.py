from typing import Protocol
from PyQt5 import QtCore, QtWidgets

from helpers.helper import initialize_edit, initialize_text, initialize_widget, initialize_combo

def add_vertical_lines_from_to(add_to: QtWidgets.QGridLayout, starting_v_from: int, ending_v_at: int, starting_h_from: int, ending_h_at: int):
    for h_index in range(starting_h_from, ending_h_at + 1, 2):
        for v_index in range(starting_v_from, ending_v_at + 1, 2):
            horizontal_line = QtWidgets.QFrame()
            horizontal_line.setFrameShape(QtWidgets.QFrame.VLine)
            horizontal_line.setFrameShadow(QtWidgets.QFrame.Sunken)
            add_to.addWidget(horizontal_line, v_index, h_index, 1, 1)

def add_horizontal_lines_from_to(add_to: QtWidgets.QGridLayout, starting_from: int, ending_at: int):
    for index in range(starting_from, ending_at + 1, 2):
        horizontal_line = QtWidgets.QFrame()
        horizontal_line.setFrameShape(QtWidgets.QFrame.HLine)
        horizontal_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        add_to.addWidget(horizontal_line, index, 0, 1, 12)

class UIWindow(Protocol):
    def update_point_buys(self) -> None:
        ...

    def update_increase_buys(self) -> None:
        ...

class AbilityScore:
    def __init__(self, parent: UIWindow) -> None:
        self.parent = parent
        self.ability_buy_spendable_points = 0
        self.point_buy_spendable_points = 0
        self.widget = QtWidgets.QWidget()
        ability_score_layout = QtWidgets.QVBoxLayout()

        point_count_grid = QtWidgets.QHBoxLayout()
        point_count_grid.setContentsMargins(0, 0, 0, 5)
        point_count_grid.setObjectName("PointCountGrid")

        remaining_point_text = QtWidgets.QLabel()
        initialize_text(remaining_point_text, "RemainingPointText", "Remaining Point Buy")

        self.remaining_point_box = QtWidgets.QLineEdit()
        initialize_edit(self.remaining_point_box, "RemainingPointBox", shape=[40, 25])

        ability_count_grid = QtWidgets.QHBoxLayout()
        ability_count_grid.setContentsMargins(0, 0, 0, 0)
        ability_count_grid.setObjectName("AbilityCountGrid")
        remaining_ability_text = QtWidgets.QLabel()
        initialize_text(remaining_ability_text, "RemainingAbilityText",
                        "Remaining Ability Increase")
        self.remaining_ability_box = QtWidgets.QLineEdit()
        initialize_edit(self.remaining_ability_box, "RemainingAbilityBox", shape=[40, 25])

        ability_score_grid = QtWidgets.QGridLayout()
        ability_score_grid.setContentsMargins(0, 0, 0, 0)
        ability_score_grid.setObjectName("AbilityScoreGrid")

        add_horizontal_lines_from_to(ability_score_grid, 2, 10)
        add_vertical_lines_from_to(ability_score_grid, 1, 11, 2, 10)

        self.score_text = QtWidgets.QLabel()
        initialize_text(self.score_text, "ScoreText", "Score")
        self.modifier_text = QtWidgets.QLabel()
        initialize_text(self.modifier_text, "ModifierText", "Modifier")
        self.race_point_text = QtWidgets.QLabel()
        initialize_text(self.race_point_text, "RacePointText", "Race Points")
        self.theme_point_text = QtWidgets.QLabel()
        initialize_text(self.theme_point_text, "ThemePointText", "Theme Points")
        self.point_buy_text = QtWidgets.QLabel()
        initialize_text(self.point_buy_text, "PointBuyText", "Point Buy")
        self.ability_increases_text = QtWidgets.QLabel()
        initialize_text(self.ability_increases_text, "AbilityIncreasesText", "Ability Increases")

        self.str_text = QtWidgets.QLabel()
        initialize_text(self.str_text, "StrText", "Str", max_size=[20, 20])
        self.dex_text = QtWidgets.QLabel()
        initialize_text(self.dex_text, "DexText", "Dex", max_size=[20, 20])
        self.con_text = QtWidgets.QLabel()
        initialize_text(self.con_text, "ConText", "Con", max_size=[20, 20])
        self.int_text = QtWidgets.QLabel()
        initialize_text(self.int_text, "IntText", "Int", max_size=[20, 20])
        self.wis_text = QtWidgets.QLabel()
        initialize_text(self.wis_text, "WisText", "Wis", max_size=[20, 20])
        self.cha_text = QtWidgets.QLabel()
        initialize_text(self.cha_text, "ChaText", "Cha", max_size=[20, 20])

        self.str_score = QtWidgets.QLineEdit()
        initialize_edit(self.str_score, "StrScore", shape=[50, 20])
        self.dex_score = QtWidgets.QLineEdit()
        initialize_edit(self.dex_score, "DexScore", shape=[50, 20])
        self.con_score = QtWidgets.QLineEdit()
        initialize_edit(self.con_score, "ConScore", shape=[50, 20])
        self.int_score = QtWidgets.QLineEdit()
        initialize_edit(self.int_score, "IntScore", shape=[50, 20])
        self.wis_score = QtWidgets.QLineEdit()
        initialize_edit(self.wis_score, "WisScore", shape=[50, 20])
        self.cha_score = QtWidgets.QLineEdit()
        initialize_edit(self.cha_score, "ChaScore", shape=[50, 20])

        self.str_mod = QtWidgets.QLineEdit()
        initialize_edit(self.str_mod, "StrMod", shape=[50, 20])
        self.dex_mod = QtWidgets.QLineEdit()
        initialize_edit(self.dex_mod, "DexMod", shape=[50, 20])
        self.con_mod = QtWidgets.QLineEdit()
        initialize_edit(self.con_mod, "ConMod", shape=[50, 20])
        self.int_mod = QtWidgets.QLineEdit()
        initialize_edit(self.int_mod, "IntMod", shape=[50, 20])
        self.wis_mod = QtWidgets.QLineEdit()
        initialize_edit(self.wis_mod, "WisMod", shape=[50, 20])
        self.cha_mod = QtWidgets.QLineEdit()
        initialize_edit(self.cha_mod, "ChaMod", shape=[50, 20])

        self.str_race = QtWidgets.QLineEdit()
        initialize_edit(self.str_race, "StrRace", shape=[50, 20])
        self.dex_race = QtWidgets.QLineEdit()
        initialize_edit(self.dex_race, "DexRace", shape=[50, 20])
        self.con_race = QtWidgets.QLineEdit()
        initialize_edit(self.con_race, "ConRace", shape=[50, 20])
        self.int_race = QtWidgets.QLineEdit()
        initialize_edit(self.int_race, "IntRace", shape=[50, 20])
        self.wis_race = QtWidgets.QLineEdit()
        initialize_edit(self.wis_race, "WisRace", shape=[50, 20])
        self.cha_race = QtWidgets.QLineEdit()
        initialize_edit(self.cha_race, "ChaRace", shape=[50, 20])

        self.str_theme = QtWidgets.QLineEdit()
        initialize_edit(self.str_theme, "StrTheme", shape=[50, 20])
        self.dex_theme = QtWidgets.QLineEdit()
        initialize_edit(self.dex_theme, "DexTheme", shape=[50, 20])
        self.con_theme = QtWidgets.QLineEdit()
        initialize_edit(self.con_theme, "ConTheme", shape=[50, 20])
        self.int_theme = QtWidgets.QLineEdit()
        initialize_edit(self.int_theme, "IntTheme", shape=[50, 20])
        self.wis_theme = QtWidgets.QLineEdit()
        initialize_edit(self.wis_theme, "WisTheme", shape=[50, 20])
        self.cha_theme = QtWidgets.QLineEdit()
        initialize_edit(self.cha_theme, "ChaTheme", shape=[50, 20])

        self.point_buy_str_combo = QtWidgets.QComboBox()
        initialize_combo(self.point_buy_str_combo, "PointBuyStrCombo", ["0"], [43, 20])
        self.point_buy_str_combo.activated.connect(self.update_point_buys)
        self.point_buy_dex_combo = QtWidgets.QComboBox()
        initialize_combo(self.point_buy_dex_combo, "PointBuyDexCombo", ["0"], [43,20])
        self.point_buy_dex_combo.activated.connect(self.update_point_buys)
        self.point_buy_con_combo = QtWidgets.QComboBox()
        initialize_combo(self.point_buy_con_combo, "PointBuyConCombo", ["0"], [43,20])
        self.point_buy_con_combo.activated.connect(self.update_point_buys)
        self.point_buy_int_combo = QtWidgets.QComboBox()
        initialize_combo(self.point_buy_int_combo, "PointBuyIntCombo", ["0"], [43,20])
        self.point_buy_int_combo.activated.connect(self.update_point_buys)
        self.point_buy_wis_combo = QtWidgets.QComboBox()
        initialize_combo(self.point_buy_wis_combo, "PointBuyWisCombo", ["0"], [43,20])
        self.point_buy_wis_combo.activated.connect(self.update_point_buys)
        self.point_buy_cha_combo = QtWidgets.QComboBox()
        initialize_combo(self.point_buy_cha_combo, "PointBuyChaCombo", ["0"], [43,20])
        self.point_buy_cha_combo.activated.connect(self.update_point_buys)

        self.ability_str_combo = QtWidgets.QComboBox()
        initialize_combo(self.ability_str_combo, "AbilityStrCombo", ["0"], [43,20])
        self.ability_str_combo.activated.connect(self.update_increase_buys)
        self.ability_dex_combo = QtWidgets.QComboBox()
        initialize_combo(self.ability_dex_combo, "AbilityDexCombo", ["0"], [43,20])
        self.ability_dex_combo.activated.connect(self.update_increase_buys)
        self.ability_con_combo = QtWidgets.QComboBox()
        initialize_combo(self.ability_con_combo, "AbilityConCombo", ["0"], [43,20])
        self.ability_con_combo.activated.connect(self.update_increase_buys)
        self.ability_int_combo = QtWidgets.QComboBox()
        initialize_combo(self.ability_int_combo, "AbilityIntCombo", ["0"], [43,20])
        self.ability_int_combo.activated.connect(self.update_increase_buys)
        self.ability_wis_combo = QtWidgets.QComboBox()
        initialize_combo(self.ability_wis_combo, "AbilityWisCombo", ["0"], [43,20])
        self.ability_wis_combo.activated.connect(self.update_increase_buys)
        self.ability_cha_combo = QtWidgets.QComboBox()
        initialize_combo(self.ability_cha_combo, "AbilityChaCombo", ["0"], [43,20])
        self.ability_cha_combo.activated.connect(self.update_increase_buys)

        ability_score_grid.addWidget(self.score_text, 0, 1, 1, 1)
        ability_score_grid.addWidget(self.modifier_text, 0, 3, 1, 1)
        ability_score_grid.addWidget(self.race_point_text, 0, 5, 1, 1)
        ability_score_grid.addWidget(self.theme_point_text, 0, 7, 1, 1)
        ability_score_grid.addWidget(self.point_buy_text, 0, 9, 1, 1)
        ability_score_grid.addWidget(self.ability_increases_text, 0, 11, 1, 1)

        ability_score_grid.addWidget(self.str_text, 1, 0, 1, 1)
        ability_score_grid.addWidget(self.dex_text, 3, 0, 1, 1)
        ability_score_grid.addWidget(self.con_text, 5, 0, 1, 1)
        ability_score_grid.addWidget(self.int_text, 7, 0, 1, 1)
        ability_score_grid.addWidget(self.wis_text, 9, 0, 1, 1)
        ability_score_grid.addWidget(self.cha_text, 11, 0, 1, 1)

        ability_score_grid.addWidget(self.str_score, 1, 1, 1, 1)
        ability_score_grid.addWidget(self.dex_score, 3, 1, 1, 1)
        ability_score_grid.addWidget(self.con_score, 5, 1, 1, 1)
        ability_score_grid.addWidget(self.int_score, 7, 1, 1, 1)
        ability_score_grid.addWidget(self.wis_score, 9, 1, 1, 1)
        ability_score_grid.addWidget(self.cha_score, 11, 1, 1, 1)

        ability_score_grid.addWidget(self.str_mod, 1, 3, 1, 1)
        ability_score_grid.addWidget(self.dex_mod, 3, 3, 1, 1)
        ability_score_grid.addWidget(self.con_mod, 5, 3, 1, 1)
        ability_score_grid.addWidget(self.int_mod, 7, 3, 1, 1)
        ability_score_grid.addWidget(self.wis_mod, 9, 3, 1, 1)
        ability_score_grid.addWidget(self.cha_mod, 11, 3, 1, 1)

        ability_score_grid.addWidget(self.str_race, 1, 5, 1, 1)
        ability_score_grid.addWidget(self.dex_race, 3, 5, 1, 1)
        ability_score_grid.addWidget(self.con_race, 5, 5, 1, 1)
        ability_score_grid.addWidget(self.int_race, 7, 5, 1, 1)
        ability_score_grid.addWidget(self.wis_race, 9, 5, 1, 1)
        ability_score_grid.addWidget(self.cha_race, 11, 5, 1, 1)

        ability_score_grid.addWidget(self.str_theme, 1, 7, 1, 1)
        ability_score_grid.addWidget(self.dex_theme, 3, 7, 1, 1)
        ability_score_grid.addWidget(self.con_theme, 5, 7, 1, 1)
        ability_score_grid.addWidget(self.int_theme, 7, 7, 1, 1)
        ability_score_grid.addWidget(self.wis_theme, 9, 7, 1, 1)
        ability_score_grid.addWidget(self.cha_theme, 11, 7, 1, 1)

        ability_score_grid.addWidget(self.point_buy_str_combo, 1, 9, 1, 1)
        ability_score_grid.addWidget(self.point_buy_dex_combo, 3, 9, 1, 1)
        ability_score_grid.addWidget(self.point_buy_con_combo, 5, 9, 1, 1)
        ability_score_grid.addWidget(self.point_buy_int_combo, 7, 9, 1, 1)
        ability_score_grid.addWidget(self.point_buy_wis_combo, 9, 9, 1, 1)
        ability_score_grid.addWidget(self.point_buy_cha_combo, 11, 9, 1, 1)

        ability_score_grid.addWidget(self.ability_str_combo, 1, 11, 1, 1)
        ability_score_grid.addWidget(self.ability_dex_combo, 3, 11, 1, 1)
        ability_score_grid.addWidget(self.ability_con_combo, 5, 11, 1, 1)
        ability_score_grid.addWidget(self.ability_int_combo, 7, 11, 1, 1)
        ability_score_grid.addWidget(self.ability_wis_combo, 9, 11, 1, 1)
        ability_score_grid.addWidget(self.ability_cha_combo, 11, 11, 1, 1)

        ability_count_grid.addWidget(remaining_ability_text, alignment=QtCore.Qt.AlignRight)
        ability_count_grid.addWidget(self.remaining_ability_box)

        point_count_grid.addWidget(remaining_point_text, alignment=QtCore.Qt.AlignRight)
        point_count_grid.addWidget(self.remaining_point_box)

        ability_and_count_grid = QtWidgets.QHBoxLayout()

        ability_and_count_grid.addLayout(ability_count_grid)
        ability_and_count_grid.addLayout(point_count_grid)

        ability_score_layout.addLayout(ability_and_count_grid)
        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        ability_score_layout.addWidget(line)
        ability_score_layout.addLayout(ability_score_grid)

        self.widget.setLayout(ability_score_layout)

    def get_ability_score_combos(self) -> dict[str, QtWidgets.QComboBox]:
        point_buys = {
            "strength" : self.point_buy_str_combo,
            "dexterity" : self.point_buy_dex_combo,
            "constitution" : self.point_buy_con_combo,
            "intelligence" : self.point_buy_int_combo,
            "wisdom" : self.point_buy_wis_combo,
            "charisma" : self.point_buy_cha_combo
        }
        return point_buys

    def get_ability_score_bought_rank(self) -> dict[str, int]:
        ability_score_bought_rank = {}
        for skill, rank_combo in self.get_ability_score_combos().items():
            ability_score_bought_rank[skill] = int(rank_combo.currentText())

        return ability_score_bought_rank

    def update_point_buy_spendable_points(self, point_buy_spendable_points: int):
        self.point_buy_spendable_points = point_buy_spendable_points

    def get_ability_increase_buy_combo(self) -> dict[str, QtWidgets.QComboBox]:
        ability_buys = {
            "strength" : self.ability_str_combo,
            "dexterity" : self.ability_dex_combo,
            "constitution" : self.ability_con_combo,
            "intelligence" : self.ability_int_combo,
            "wisdom" : self.ability_wis_combo,
            "charisma" : self.ability_cha_combo
        }
        return ability_buys

    def get_ability_increase_buy_ranks(self) -> dict[str, int]:
        ability_score_bought_rank = {}
        for skill, rank_combo in self.get_ability_increase_buy_combo().items():
            ability_score_bought_rank[skill] = int(rank_combo.currentText())

        return ability_score_bought_rank

    def update_ability_buy_spendable_points(self, ability_buy_spendable_points: int):
        self.ability_buy_spendable_points = ability_buy_spendable_points

    def update_score_values(self, character_attributes):
        boxes = [self.str_score, self.dex_score, self.con_score, self.int_score, self.wis_score,
                 self.cha_score, self.remaining_point_box, self.remaining_ability_box]
        #classesStatBonus[self.className]["skills"] + self.mods["int"]
        for skill, box in zip([*character_attributes.values(),
                               self.point_buy_spendable_points, self.ability_buy_spendable_points], boxes):
            box.setText(str(skill))

    def update_mods(self, character_mods):
        boxes = [self.str_mod, self.dex_mod, self.con_mod, self.int_mod, self.wis_mod,self.cha_mod]
        for skill, box in zip(character_mods.values(), boxes):
            box.setText(str(skill))

    def update_theme_stats(self, theme_skills: dict[str, int]) -> None:
        attributes = {
            "strength" : self.str_theme,
            "dexterity" : self.dex_theme,
            "constitution" : self.con_theme,
            "intelligence" : self.int_theme,
            "wisdom" : self.wis_theme,
            "charisma" : self.cha_theme
        }

        for key, value in attributes.items():
            value.setText(str(theme_skills[key]))

    def update_race_stats(self, race_skills: dict[str, int]):
        attributes = {
            "strength" : self.str_race,
            "dexterity" : self.dex_race,
            "constitution" : self.con_race,
            "intelligence" : self.int_race,
            "wisdom" : self.wis_race,
            "charisma" : self.cha_race
        }

        for key, value in attributes.items():
            value.setText(str(race_skills[key]))

    def update_point_buys(self):
        """update abilities based on the point buy system
        """
        self.parent.update_point_buys()

    def update_increase_buys(self):
        self.parent.update_increase_buys()
