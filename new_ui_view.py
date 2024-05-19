from typing import Literal, Optional
from PyQt5 import QtCore, QtWidgets

from character_classes.character import Character
from helpers.helper import initialize_frame
from ui.feat_window import FeatForm
from starfinder_gui_spells import SpellForm
from ui.ability_score import AbilityScore
from ui.armor import Armor
from ui.attack import Attack
from ui.character_flavor import CharacterFlavor
from ui.character_info import CharacterInfo
from ui.health import Health
from ui.initiative import Initiative
from ui.saves import Saves
from ui.skill_points import SkillPoints

SKILL_NAMES = Literal[
    "acrobatics",
    "athletics",
    "bluff",
    "computers",
    "culture",
    "diplomacy",
    "disguise",
    "engineering",
    "intimidate",
    "life science",
    "medicine",
    "mysticism",
    "perception",
    "physical science",
    "piloting",
    "profession",
    "profession2",
    "sense motive",
    "sleight of hand",
    "stealth",
    "survival"
]

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

        self.feat_window: FeatForm = None
        self.spell_window: SpellForm = None

        self.window.setObjectName("MainWindow")
        self.window.resize(1075, 984)
        self.centralwidget = QtWidgets.QWidget(self.window)
        self.centralwidget.setObjectName("centralwidget")


        self.nameframe = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.nameframe, "Nameframe", [20, 10, 451, 51])

        self.character_info = CharacterInfo(self)
        character_layout = QtWidgets.QVBoxLayout()
        character_layout.addWidget(self.character_info.widget)
        self.nameframe.setLayout(character_layout)


        self.abilityframe = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.abilityframe, "Abilityframe", [20, 130, 501, 311])

        ability_layout = QtWidgets.QVBoxLayout()
        self.ability_score = AbilityScore(self)
        ability_layout.addWidget(self.ability_score.widget)
        self.abilityframe.setLayout(ability_layout)


        self.skillframe = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.skillframe, "Skillframe", shape=[540, 130, 481, 801])

        self.skill_points = SkillPoints(self)
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

        self.flavor = CharacterFlavor(self)
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
        self.action_feats.triggered.connect(self.open_feats)
        self.action_spells = QtWidgets.QAction(self.window)
        self.action_spells.setObjectName("actionSpells")
        self.action_spells.setText("Spells")
        self.action_spells.triggered.connect(self.open_spells)

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
        self.ability_score.update_point_buy_spendable_points(self.character.attributes.spendable_point_buy)

    def character_name_changed(self, new_text):
        self.character.update_name(new_text)

    def choose_class(self, class_name: str, soldier_style: Optional[str]): # TODO
        self.character.choose_class(class_name, soldier_style)

        self.update_class_stats()
        self.update_saves()
        self.update_attack()
        mods = self.character.attributes.get_attribute_modifiers()
        self.skill_points.update_skill_buy_spendable_points(
            self.character.skills.skillpoints,
            self.character.starfinder_class.skills + mods['int']
        )

    def choose_theme(self, theme_name: str, themeless_style: Optional[str]):
        self.character.choose_theme(theme_name, themeless_style)

        self.ability_score.update_theme_stats(self.character.theme.attributes)
        self.update_ability_display()
        self.update_skills_ability_modifier()
        self.update_point_buys()

    def choose_race(self, race_name: str, human_style: Optional[str]):
        self.character.choose_race(race_name, human_style)

        self.ability_score.update_race_stats(self.character.race.attributes)
        self.update_ability_display()
        self.update_skills_ability_modifier()
        self.update_hp()
        self.update_point_buys()

    def update_point_buys(self, attribute: str=None, attribute_value: int=None):
        if attribute:
            self.character.attributes.update_point_buy(attribute, attribute_value)
        self.ability_score.update_point_buy_spendable_points(self.character.attributes.spendable_point_buy)
        self.ability_score.update_point_buys(spent_points_dict=self.character.attributes.ability_point_buy)
        self.update_abilities()
        self.update_ability_display()

    def update_increase_buys(self, attribute: str=None, attribute_value: int=None):
        if attribute:
            self.character.attributes.update_increase_buy(attribute, attribute_value)
        self.ability_score.update_ability_buy_spendable_points(self.character.attributes.spendable_ability_increase)
        self.ability_score.update_increase_buys(self.character.level, self.character.attributes.ability_increases)
        self.update_abilities()
        self.update_ability_display()

    def update_abilities(self):
        self.character.update_abilities()
        self.update_hp()
        self.update_initiative()
        self.update_saves()
        self.update_ac()
        self.update_attack()
        self.update_skills()
        self.update_skills_ability_modifier()

    def update_class_stats(self):
        self.skill_points.update_class_stats(self.character.skills.skill_class)
        self.update_skills()

    def update_level(self, level: int):
        self.character.update_level(level)
        self.character.update_spendable_ability_increase()
        mods = self.character.attributes.get_attribute_modifiers()
        self.skill_points.update_skill_buy_spendable_points(
            self.character.skills.skillpoints,
            self.character.starfinder_class.skills + mods['int']
        )
        self.update_abilities()
        self.update_increase_buys()

    def update_hp(self):
        self.health.update_hp(self.character.health.stamina_points,
                              self.character.health.hit_points,
                              self.character.health.resolve_points)

    def update_initiative(self):
        """update the initiative tab related items
        """
        mods = self.character.attributes.get_attribute_modifiers()
        self.character.initiaitve.update_initiative(mods["dex"])
        skills = [self.character.initiaitve.initiative, mods["dex"],
                    self.character.initiaitve.initiative_misc]
        self.initiative.update_initiative(skills)

    def update_ability_display(self):
        self.ability_score.update_score_values(self.character.attributes.get_attribute_stats())
        self.ability_score.update_mods(self.character.attributes.get_attribute_modifiers())

    def update_skills_ability_modifier(self):
        mods = self.character.attributes.get_attribute_modifiers()
        skills = [mods["dex"], mods["str"], mods["cha"], mods["int"],
                  mods["int"], mods["cha"], mods["cha"], mods["int"],
                  mods["cha"], mods["int"], mods["int"], mods["wis"],
                  mods["wis"], mods["int"], mods["dex"],
                  mods[self.character.skills.profession_ability],
                  mods[self.character.skills.profession2_ability],
                  mods["wis"], mods["dex"], mods["dex"], mods["wis"]]

        self.skill_points.update_ability_modifier(skills)
        self.update_ac()
        self.update_initiative()

    def update_ac(self):
        """update ac tab related boxes
        """
        mods = self.character.attributes.get_attribute_modifiers()
        self.character.armor.update_ac(mods["dex"])
        armor_stats = self.character.armor.get_armor_stats()
        skills = [armor_stats["eac"], armor_stats["armor_eac"], mods["dex"], 0,
                  armor_stats["kac"], armor_stats["armor_kac"], mods["dex"], 0,
                  armor_stats["ac_vs"], armor_stats["kac"]]
        self.armor.update_ac(skills)

    def update_saves(self):
        self.character.update_saves()
        mods = self.character.attributes.get_attribute_modifiers()
        save_skills = [self.character.saves.fort_save,
                       self.character.saves.reflex_save,
                       self.character.saves.will_save,
                       self.character.starfinder_class.get_fort(),
                       self.character.starfinder_class.get_reflex(),
                       self.character.starfinder_class.get_will(),
                       mods["con"],
                       mods["dex"],
                       mods["wis"],
                       self.character.saves.fort_save_misc,
                       self.character.saves.reflex_save_misc,
                       self.character.saves.will_save_misc]
        self.save.update_saves(save_skills)

    def update_attack(self):
        self.character.update_attack()
        mods = self.character.attributes.get_attribute_modifiers()
        attack_skills = [self.character.attacks.melee,
                         self.character.starfinder_class.get_bab(),
                         mods["str"],
                         self.character.attacks.melee_misc,
                         self.character.attacks.range,
                         self.character.starfinder_class.get_bab(),
                         mods["dex"],
                         self.character.attacks.range_misc,
                         self.character.attacks.throw,
                         self.character.starfinder_class.get_bab(),
                         mods["str"],
                         self.character.attacks.throw_misc]
        self.attack.update_attack(attack_skills)

    def update_skill_buy(self, changed_skill: SKILL_NAMES, changed_value: int):
        self.character.skills.update_point_buy_skill(changed_skill, changed_value)
        self.update_skills()

    def update_skills(self):
        self.character.update_class_stats()
        mods = self.character.attributes.get_attribute_modifiers()
        self.skill_points.update_rank_combos(self.character.level, self.character.skills.skill_ranks)
        self.skill_points.update_skill_buy_spendable_points(self.character.skills.skillpoints, self.character.starfinder_class.skills + mods['int'])
        skills_totals = list(self.character.skills.skills.values())
        skills_totals.append(self.character.skills.skillpoints)
        skills_totals.append(self.character.starfinder_class.skills + mods["int"])
        self.skill_points.update_skills(skills_totals)
        self.skill_points.update_misc_skills(self.character.skills.get_misc_mods(), self.character.skills.skill_dabbler)

    def update_professions(self, prof1: str, prof2: str) -> None:
        self.character.update_professions(prof1, prof2)
        self.update_abilities()

    # def save_character(self):

    # def load_character(self):

    def open_feats(self):
        """open the feats window
        """
        if self.feat_window is None:
            self.feat_window = FeatForm(self.character)
        self.feat_window.show()

    def open_spells(self):
        if self.spell_window is None:
            self.spell_window = SpellForm(self.character)
        self.spell_window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = UIMainWindow()
    sys.exit(app.exec_())
