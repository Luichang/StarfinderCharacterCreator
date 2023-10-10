from typing import Optional
from PyQt5 import QtCore, QtWidgets

from classed_character import Character
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
        self.character = Character(gui=True)

        self.feat_window = None
        self.spell_window = None

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
        self.action_save.triggered.connect(self.save_character)
        self.action_load = QtWidgets.QAction(self.window)
        self.action_load.setObjectName("actionLoad")
        self.action_load.setText("Load")
        self.action_load.triggered.connect(self.load_character)
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

    def class_activated(self, class_name: str, soldier_style: Optional[str]): # TODO
        """sets the extra combobox text depending on if the class is soldier or not

        Args:
            text (str): text of the combobox that determines the class
        """
        if class_name == "Soldier":
            self.character.class_name = StarfinderClass.create(class_name.lower(), soldier_style.lower())
        else:
            self.character.class_name = StarfinderClass.create(class_name.lower())

        self.update_class_stats()
        self.update_saves()
        self.update_attack()

    def character_name_changed(self, new_text):
        self.character.set_name(new_text)

    
    def theme_activated(self, theme_name: str, themeless_style: Optional[str]):
        """sets the extra combobox text depending on if the theme is themeless or not

        Args:
            text (str): text of the combobox that determines the theme
        """
        if theme_name == "Themeless":
            self.character.theme = StarfinderTheme.create(theme_name.lower(), themeless_style.lower())
        else:
            self.character.theme = StarfinderTheme.create(theme_name.lower())

        self.update_theme_stats()

    def race_activated(self, race_name: str, human_style: Optional[str]):
        """sets the extra combobox text depending on if the race is human or not

        Args:
            text (str): text of the combobox that determines the race
        """
        if race_name == "Human":
            self.character.race_name = StarfinderRace.create(race_name.lower(), human_style.lower())
        else:
            self.character.race_name = StarfinderRace.create(race_name.lower())

        self.update_race_stats()

    def update_class_stats(self):
        """updates the class blocks in the skills tab
        """
        character_skills = {}
        for skill_name, skill_value in self.character.skills.items():
            val = 0
            if skill_value in self.character.class_name.bonuses:
                val = 3
            character_skills[skill_name] = val
        self.skill_points.update_class_stats(character_skills)
        self.update_skills()
        self.update_skill_buy()
        self.update_hp()

    def update_theme_stats(self):
        """updates the theme blocks in the attributes tab
        """
        self.ability_score.update_theme_stats(self.character.theme.attributes)
        self.update_dabbler()
        self.update_abilities()
        self.update_point_buys()

    def update_race_stats(self):
        """updates the race blocks in the attributes tab
        """
        self.ability_score.update_race_stats(self.character.race_name.attributes)
        self.update_abilities()
        self.update_hp()
        self.update_point_buys()
        self.update_skill_buy()

    def update_level(self, text):
        """update all boxes related to the level

        Args:
            text (int): entered level
        """
        self.character.class_level = int(text)
        self.character.calc_spell_level()
        self.update_hp()
        self.character.calc_init()
        self.update_initiative()
        self.update_point_buys()
        self.update_increase_buys()
        self.update_saves()
        self.update_attack()
        if self.character.class_name and self.character.class_level > 0:
            self.update_skill_buy()

    def update_hp(self):
        """updates the HP tab related items. calc_hit_points need race_name and class_name to be
            set
        """
        try:
            self.character.race_name
            self.character.class_name
            self.character.calc_hit_points()
        except AttributeError:
            pass

        self.health.update_hp(self.character.stamina_points, self.character.hit_points,
                    self.character.resolve_points)

    def update_initiative(self):
        """update the initiative tab related items
        """
        self.character.calc_init()
        skills = [self.character.initiative, self.character.mods["dex"],
                    self.character.initiative_misc]
        self.initiative.update_initiative(skills)

    def update_point_buys(self):
        """update abilities based on the point buy system
        """
        point_buy_spendable_points = 10
        for attr, rank in self.ability_score.get_ability_score_bought_rank().items():
            point_buy_spendable_points -= rank
            self.character.spent_points[attr] = rank

        self.ability_score.update_point_buy_spendable_points(point_buy_spendable_points)

        for attr, combo in self.ability_score.get_ability_score_combos().items():
            val = self.ability_score.point_buy_spendable_points + self.character.spent_points[attr] + 1
            try:
                race_val = self.character.race_name.attributes[attr]
            except AttributeError:
                race_val = 0
            try:
                theme_val = self.character.theme.attributes[attr]
            except AttributeError:
                theme_val = 0
            max_val = 10 + race_val + theme_val
            points = [str(i) for i in range(val) if i + max_val <= 18]
            update_combo(combo, points)
            combo.setCurrentIndex(self.character.spent_points[attr])
        self.update_abilities()

        try:
            self.character.class_name
            if self.character.class_level > 0:
                self.update_skill_buy()
        except AttributeError:
            pass

    def update_increase_buys(self):
        """update abilities based on ability increase buy system
        """
        ability_buy_spendable_points = (self.character.class_level // 5) * 4
        for attr, rank in self.ability_score.get_ability_increase_buy_ranks().items():
            ability_buy_spendable_points -= rank
            self.character.ability_increases[attr] = rank
        self.ability_score.update_ability_buy_spendable_points(ability_buy_spendable_points)

        for attr, combo in self.ability_score.get_ability_increase_buy_combo().items():
            val = (self.character.class_level // 5) + 1
            points = [str(i) for i in range(val)]
            update_combo(combo, points)
            combo.setCurrentIndex(self.character.ability_increases[attr])
        self.update_abilities()
        if self.character.class_name and self.character.class_level > 0:
            self.update_skill_buy()

    def update_abilities(self):
        """updates the attribute scores in the attributes tab
        """
        try:
            self.character.race_name
            self.character.theme
            self.character.calc_attributes()
        except AttributeError:
            pass

        self.ability_score.update_score_values(self.character.attributes)
        self.ability_score.update_mods(self.character.mods)

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

        self.skill_points.update_abilities(skills)

        self.update_skills()
        self.update_hp()
        self.update_initiative()
        self.update_saves()
        self.update_ac()
        self.update_attack()

    def update_ac(self):
        """update ac tab related boxes
        """
        self.character.calc_armor_class()
        skills = [self.character.eac, 0, self.character.mods["dex"], 0,
                  self.character.kac, 0, self.character.mods["dex"], 0,
                  self.character.vs_combat, self.character.kac]
        self.armor.update_ac(skills)

    def update_saves(self):
        """update the save tab related boxes. Needs class_name to be set
        """
        try:
            self.character.class_name
            if self.character.class_level > 0:
                self.character.calc_save()
                skills = [self.character.fort_save,self.character.reflex_save,self.character.will_save,
                        self.character.class_name.fort[self.character.class_level - 1],
                        self.character.class_name.reflex[self.character.class_level - 1],
                        self.character.class_name.will[self.character.class_level - 1],
                        self.character.mods["con"], self.character.mods["dex"],
                        self.character.mods["wis"], self.character.fort_save_misc,
                        self.character.reflex_save_misc, self.character.will_save_misc]
                
                self.save.update_saves(skills)
                
        except AttributeError:
            pass

    def update_attack(self):
        """update attack tab related boxes. Needs class_name to be set
        """
        try:
            self.character.class_name
            if self.character.class_level > 0:
                self.character.calc_attack()
                skills = [self.character.melee, self.character.class_name.bab[self.character.class_level - 1],
                        self.character.mods["str"], self.character.melee_misc,
                        self.character.range, self.character.class_name.bab[self.character.class_level - 1],
                        self.character.mods["dex"], self.character.range_misc,
                        self.character.throw, self.character.class_name.bab[self.character.class_level - 1],
                        self.character.mods["str"], self.character.throw_misc]
                self.attack.update_attack(skills)
        except AttributeError:
            pass

    def update_skill_buy(self):
        """update skills based on the skill buys. Needs class_name to be set
        """
        try:
            self.character.class_name
            skill_buy_spendable_points = (self.character.class_name.skills +\
                                          self.character.mods["int"]) * self.character.class_level

            for skill, rank in self.skill_points.get_skill_bought_rank().items():
                skill_buy_spendable_points -= rank
                self.character.skill_ranks[skill] = rank
            self.skill_points.update_skill_buy_spendable_points(skill_buy_spendable_points)

            for skill, pbuy in self.skill_points.get_skill_rank_combos().items():
                val = self.character.class_level + 1
                points = [str(i) for i in range(val) if i < self.skill_points.skill_buy_spendable_points +\
                            self.character.skill_ranks[skill] + 1]
                update_combo(pbuy, points)
                pbuy.setCurrentIndex(self.character.skill_ranks[skill])

            self.update_dabbler()
            self.update_skills()
        except AttributeError:
            pass

    def update_skills(self):
        try:
            self.character.class_name
            self.character.calc_skills()
            skills_list = [*self.character.skills.values(),
                           self.skill_points.skill_buy_spendable_points,
                           (self.character.class_name.skills + self.character.mods["int"])]
            self.skill_points.update_skills(skills_list)
        except AttributeError:
            pass

    def update_dabbler(self) -> None:
        """function to update the dabbler stats
        """
        dabble = 0
        if self.character.theme == "spacefarer" and self.character.class_level >= 6:
            dabble = 2
        # +2 bonus to skill checks for skills with 0 ranks in skill
        for skill in self.character.skills:
            if self.character.skill_ranks[skill] == 0:
                self.character.skill_dabbler[skill] = dabble
            else:
                self.character.skill_dabbler[skill] = 0

        self.skill_points.update_misc_skills(self.character.skill_misc, self.character.skill_dabbler)

    def update_professions(self, prof1: str, prof2: str) -> None:
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
        if self.feat_window is None:
            self.feat_window = FeatForm(self.character)
        self.feat_window.show()

    def open_spells(self):
        """open the spells window
        """
        if self.spell_window is None:
            self.spell_window = SpellForm(self.character)
        self.spell_window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = UIMainWindow()
    sys.exit(app.exec_())
