from typing import Optional
from PyQt5 import QtCore, QtWidgets

from character_classes.character import Character
from helpers.helper import initialize_frame, update_combo
from starfinder_classes.starfinder_class import StarfinderClass
from starfinder_gui_feat import FeatForm
from starfinder_gui_spells import SpellForm
from starfinder_races.starfinder_race import StarfinderRace
from starfinder_themes.starfinder_theme import StarfinderTheme
from ui.ability_score import AbilityScore
from ui.armor import Armor
from ui.attack import Attack
from ui.character_flavor import CharacterFlavor
from ui.character_info import CharacterInfo
from ui.health import Health
from ui.initiative import Initiative
from ui.saves import Saves
from ui.skill_points import SkillPoints


class UIMainWindow:
    """Generated Function that has beed edited to contain function calls added afterwards.
    All to portray the GUI version of the starfinder character creator

    Args:
        object (????): some object
    """
    def __init__(self) -> None:
        self.window = QtWidgets.QMainWindow()
        self.setup_ui()
        self.window.show()

    def setup_ui(self):
        """create the main window of the starfinder character creator
        """
        self.character = Character()

        self.feat_window = None
        self.spell_window = None

        self.window.setObjectName("MainWindow")
        self.window.resize(1075, 984)
        self.centralwidget = QtWidgets.QWidget(self.window)
        self.centralwidget.setObjectName("centralwidget")


        self.nameframe = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.nameframe, "Nameframe", [20, 10, 451, 51])

        self.character_info = CharacterInfo(self.character)
        character_layout = QtWidgets.QVBoxLayout()
        character_layout.addWidget(self.character_info.widget)
        self.nameframe.setLayout(character_layout)


        self.abilityframe = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.abilityframe, "Abilityframe", [20, 130, 501, 311])

        ability_layout = QtWidgets.QVBoxLayout()
        self.ability_score = AbilityScore(self.character)
        ability_layout.addWidget(self.ability_score.widget)
        self.abilityframe.setLayout(ability_layout)


        self.skillframe = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.skillframe, "Skillframe", shape=[540, 130, 481, 801])

        self.skill_points = SkillPoints(self.character)
        skill_points_layout = QtWidgets.QVBoxLayout()
        skill_points_layout.addWidget(self.skill_points.widget)
        self.skillframe.setLayout(skill_points_layout)


        self.initframe = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.initframe, "Initframe", shape=[130, 70, 261, 51])

        self.initiative = Initiative()
        initiative_layout = QtWidgets.QVBoxLayout()
        initiative_layout.addWidget(self.initiative.widget)
        self.initframe.setLayout(initiative_layout)


        self.hp_frame = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.hp_frame, "HPframe", shape=[490, 10, 261, 80])

        self.health = Health()
        health_layout = QtWidgets.QVBoxLayout()
        health_layout.addWidget(self.health.widget)
        self.hp_frame.setLayout(health_layout)


        self.armorframe = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.armorframe, "Armorframe", shape=[20, 450, 471, 141])

        self.armor = Armor()
        armor_layout = QtWidgets.QVBoxLayout()
        armor_layout.addWidget(self.armor.widget)
        self.armorframe.setLayout(armor_layout)


        self.saveframe = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.saveframe, "Saveframe", shape=[20, 600, 361, 141])

        self.save = Saves()
        save_layout = QtWidgets.QVBoxLayout()
        save_layout.addWidget(self.save.widget)
        self.saveframe.setLayout(save_layout)


        self.attackframe = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.attackframe, "Attackframe", shape=[20, 750, 361, 181])

        self.attack = Attack()
        attack_layout = QtWidgets.QVBoxLayout()
        attack_layout.addWidget(self.attack.widget)
        self.attackframe.setLayout(attack_layout)


        self.classframe = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.classframe, "Classframe", shape=[790, 10, 271, 111])

        self.flavor = CharacterFlavor(self.character)
        flavor_layout = QtWidgets.QVBoxLayout()
        flavor_layout.addWidget(self.flavor.widget)
        self.classframe.setLayout(flavor_layout)



        # self.statusbar = QtWidgets.QStatusBar(self.window)
        # self.statusbar.setObjectName("statusbar")
        # self.window.setStatusBar(self.statusbar)
        self.action_save = QtWidgets.QAction(self.window)
        self.action_save.setObjectName("actionSave")
        self.action_save.setText("Save")
        # self.action_save.triggered.connect(self.save_character)
        self.action_load = QtWidgets.QAction(self.window)
        self.action_load.setObjectName("actionLoad")
        self.action_load.setText("Load")
        # self.action_load.triggered.connect(self.load_character)
        self.action_feats = QtWidgets.QAction(self.window)
        self.action_feats.setObjectName("actionFeats")
        self.action_feats.setText("Feats")
        # self.action_feats.triggered.connect(self.open_feats)
        self.action_spells = QtWidgets.QAction(self.window)
        self.action_spells.setObjectName("actionSpells")
        self.action_spells.setText("Spells")
        # self.action_spells.triggered.connect(self.open_spells)

        self.window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1075, 21))
        self.menubar.setObjectName("menubar")
        self.menu_save = QtWidgets.QMenu(self.menubar)
        self.menu_save.setObjectName("menuSave")
        self.menu_save.setTitle("Menu")
        self.menu_extras = QtWidgets.QMenu(self.menubar)
        self.menu_extras.setObjectName("menuExtras")
        self.menu_extras.setTitle("Extras")
        self.window.setMenuBar(self.menubar)

        self.menu_save.addAction(self.action_save)
        self.menu_save.addAction(self.action_load)
        self.menu_extras.addAction(self.action_feats)
        self.menu_extras.addAction(self.action_spells)
        self.menubar.addAction(self.menu_save.menuAction())
        self.menubar.addAction(self.menu_extras.menuAction())


        self.window.setWindowTitle("CharacterSheetMaker")
        QtCore.QMetaObject.connectSlotsByName(self.window)

    # def class_activated(self, class_name: str, soldier_style: Optional[str]): # TODO

    # def character_name_changed(self, new_text):

    # def theme_activated(self, theme_name: str, themeless_style: Optional[str]):

    # def race_activated(self, race_name: str, human_style: Optional[str]):

    # def update_class_stats(self):

    # def update_theme_stats(self):

    # def update_race_stats(self):

    # def update_level(self, text):

    # def update_hp(self):

    # def update_initiative(self):

    # def update_point_buys(self):

    # def update_increase_buys(self):

    # def update_abilities(self):

    # def update_ac(self):

    # def update_saves(self):

    # def update_attack(self):

    # def update_skill_buy(self):

    # def update_skills(self):

    # def update_dabbler(self) -> None:

    # def update_professions(self, prof1: str, prof2: str) -> None:

    # def save_character(self):

    # def load_character(self):

    # def open_feats(self):

    # def open_spells(self):


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = UIMainWindow()
    sys.exit(app.exec_())
