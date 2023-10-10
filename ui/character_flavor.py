from typing import Protocol, Optional

from PyQt5 import QtCore, QtWidgets

from helpers.helper import initialize_combo, initialize_text, update_combo, initialize_combo_model
from starfinder_classes.starfinder_class import StarfinderClass
from starfinder_races.starfinder_race import StarfinderRace
from starfinder_themes.starfinder_theme import StarfinderTheme


class UIWindow(Protocol):
    def choose_class(self, class_name: str, soldier_style: Optional[str]) -> None:
        ...

    def choose_race(self, class_name: str, human_style: Optional[str]) -> None:
        ...

    def choose_theme(self, class_name: str, themeless_style: Optional[str]) -> None:
        ...

class CharacterFlavor:
    def __init__(self, parent: UIWindow) -> None:
        self.parent = parent
        self.widget = QtWidgets.QWidget()
        attack_layout = QtWidgets.QGridLayout()

        self.class_text = QtWidgets.QLabel()
        initialize_text(self.class_text, "ClassText", "Class", max_size=[27, 25])

        self.class_combo = QtWidgets.QComboBox()
        self.class_combo.setMaximumSize(QtCore.QSize(120, 20))
        self.class_combo.setObjectName("ClassCombo")

        initialize_combo_model(self.class_combo, [x.capitalize() for x in StarfinderClass.subclasses],
                                "<<Select Class>>")
        self.class_combo.currentTextChanged.connect(self.class_activated)

        self.class_ability_combo = QtWidgets.QComboBox()
        initialize_combo(self.class_ability_combo, "ClassAbilityCombo", ["Blank"], [85, 20])
        self.class_ability_combo.activated.connect(self.soldier_key_update)

        self.race_text = QtWidgets.QLabel()
        initialize_text(self.race_text, "RaceText", "Race", max_size=[30, 25])

        self.race_combo = QtWidgets.QComboBox()
        self.race_combo.setMaximumSize(QtCore.QSize(120, 20))
        self.race_combo.setObjectName("RaceCombo")

        initialize_combo_model(self.race_combo, [x.capitalize() for x in StarfinderRace.subraces], "<<Select Race>>")
        self.race_combo.currentTextChanged.connect(self.race_activated)

        self.race_ability_combo = QtWidgets.QComboBox()
        initialize_combo(self.race_ability_combo, "RaceAbilityCombo", ["Blank"], [85, 20])
        self.race_ability_combo.activated.connect(self.human_key_update)

        self.theme_text = QtWidgets.QLabel()
        initialize_text(self.theme_text, "ThemeText", "Theme", max_size=[32, 25])
        self.theme_text.setMaximumSize(QtCore.QSize(32, 25))
        self.theme_text.setObjectName("ThemeText")
        self.theme_text.setText("Theme")

        self.theme_combo = QtWidgets.QComboBox()
        self.theme_combo.setMaximumSize(QtCore.QSize(120, 20))
        self.theme_combo.setObjectName("ThemeCombo")
        initialize_combo_model(self.theme_combo, [x.capitalize() for x in StarfinderTheme.subthemes], "<<Select Theme>>")
        self.theme_combo.currentTextChanged.connect(self.theme_activated)

        self.theme_ability_combo = QtWidgets.QComboBox()
        initialize_combo(self.theme_ability_combo, "ThemeAbilityCombo", ["Blank"], [85, 20])
        self.theme_ability_combo.activated.connect(self.themeless_key_update)

        attack_layout.addWidget(self.class_text, 0, 0)
        attack_layout.addWidget(self.class_combo, 0, 1)
        attack_layout.addWidget(self.class_ability_combo, 0, 2)

        attack_layout.addWidget(self.race_text, 1, 0)
        attack_layout.addWidget(self.race_combo, 1, 1)
        attack_layout.addWidget(self.race_ability_combo, 1, 2)

        attack_layout.addWidget(self.theme_text, 2, 0)
        attack_layout.addWidget(self.theme_combo, 2, 1)
        attack_layout.addWidget(self.theme_ability_combo, 2, 2)


        self.widget.setLayout(attack_layout)

    def class_activated(self, text): # TODO
        """sets the extra combobox text depending on if the class is soldier or not

        Args:
            text (str): text of the combobox that determines the class
        """
        if text == "Soldier":
            combo_text = ["Str", "Dex"]
        else:
            combo_text = ["Blank"]
        update_combo(self.class_ability_combo, combo_text)
        self.parent.choose_class(text, combo_text[0])

    def soldier_key_update(self):
        text = self.class_ability_combo.currentText()
        if text not in ('Blank', ''):
            self.parent.choose_class(self.class_combo.currentText(), text)

            combo_text = ["Str", "Dex"]
            combo_text.remove(text)
            combo_text = [text] + combo_text
            update_combo(self.class_ability_combo, combo_text)

    def theme_activated(self, text):
        """sets the extra combobox text depending on if the theme is themeless or not

        Args:
            text (str): text of the combobox that determines the theme
        """
        if text == "Themeless":
            combo_text = ["Str", "Dex", "Con", "Int", "Wis", "Cha"]
        else:
            combo_text = ["Blank"]

        update_combo(self.theme_ability_combo, combo_text)
        self.parent.choose_theme(text, combo_text[0])

    def themeless_key_update(self):
        """sets the key attribute if the theme is themeless

        Args:
            text (str): attribute of the themeless
        """
        text = self.theme_ability_combo.currentText()
        if text != 'Blank':
            self.parent.choose_theme(self.theme_combo.currentText(), text)

            combo_text = ["Str", "Dex", "Con", "Int", "Wis", "Cha"]
            combo_text.remove(text)
            combo_text = [text] + combo_text
            update_combo(self.theme_ability_combo, combo_text)

    def race_activated(self, text):
        """sets the extra combobox text depending on if the race is human or not

        Args:
            text (str): text of the combobox that determines the race
        """
        if text == "Human":
            combo_text = ["Str", "Dex", "Con", "Int", "Wis", "Cha"]
        else:
            combo_text = ["Blank"]

        update_combo(self.race_ability_combo, combo_text)
        self.parent.choose_race(text, combo_text[0])

    def human_key_update(self, text):
        """sets the key attribute if the theme is themeless
        Args:
            text (str): attribute of the race
        """
        text = self.theme_ability_combo.currentText()
        if text != 'Blank':
            self.parent.choose_race(self.race_combo, text)

            combo_text = ["Str", "Dex", "Con", "Int", "Wis", "Cha"]
            combo_text.remove(text)
            combo_text = [text] + combo_text
            update_combo(self.race_ability_combo, combo_text)
