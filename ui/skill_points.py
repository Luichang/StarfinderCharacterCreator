from typing import Protocol
from PyQt5 import QtCore, QtWidgets

from helpers.helper import initialize_combo, initialize_edit, initialize_text, update_combo


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
        add_to.addWidget(horizontal_line, index, 0, 1, 11)

def add_widgets_to_layout(add_to: QtWidgets.QGridLayout, widgets, start_from: int, column_value: int, column_span: int):
    for widget, index in zip(widgets, range(start_from, start_from + len(widgets)*2, 2)):
        add_to.addWidget(widget, index, column_value, 1, column_span)

class UIWindow(Protocol):
    def update_professions(self, prof1: str, prof2: str) -> None:
        ...

    def update_skill_buy(self) -> None:
        ...

class SkillPoints:
    def __init__(self, parent: UIWindow) -> None:
        self.parent = parent
        self.skill_buy_spendable_points = 0
        self.widget = QtWidgets.QWidget()
        skill_points_layout = QtWidgets.QVBoxLayout()

        skills_score_grid = QtWidgets.QGridLayout()
        skills_score_grid.setContentsMargins(0, 0, 0, 0)
        skills_score_grid.setObjectName("SkillsScoreGrid")

        add_horizontal_lines_from_to(skills_score_grid, 1, 41)
        add_vertical_lines_from_to(skills_score_grid, 0, 40, 3, 9)

        self.skill_total_text = QtWidgets.QLabel()
        initialize_text(self.skill_total_text, "SkillTotalText", "Total")
        self.skill_ranks_text = QtWidgets.QLabel()
        initialize_text(self.skill_ranks_text, "SkillRanksText", "Ranks")
        self.skill_class_text = QtWidgets.QLabel()
        initialize_text(self.skill_class_text, "SkillClassText", "Class Bonus")
        self.skill_ability_text = QtWidgets.QLabel()
        initialize_text(self.skill_ability_text, "SkillAbilityText", "Ability Mod")
        self.skill_misc_text = QtWidgets.QLabel()
        initialize_text(self.skill_misc_text, "SkillMiscText", "Misc Mod")

        self.acrobatics_text = QtWidgets.QLabel()
        initialize_text(self.acrobatics_text, "AcrobaticsText", "Acrobatics (Dex)")
        self.athletics_text = QtWidgets.QLabel()
        initialize_text(self.athletics_text, "AthleticsText", "Athletics (Str)")
        self.bluff_text = QtWidgets.QLabel()
        initialize_text(self.bluff_text, "BluffText", "Bluff (Cha)")
        self.computers_text = QtWidgets.QLabel()
        initialize_text(self.computers_text, "ComputersText", "Computers (Int)")
        self.culture_text = QtWidgets.QLabel()
        initialize_text(self.culture_text, "CultureText", "Culture (Int)")
        self.diplomacy_text = QtWidgets.QLabel()
        initialize_text(self.diplomacy_text, "DiplomacyText", "Diplomacy (Cha)")
        self.disguise_text = QtWidgets.QLabel()
        initialize_text(self.disguise_text, "DisguiseText", "Disguise (Cha)")
        self.engineering_text = QtWidgets.QLabel()
        initialize_text(self.engineering_text, "EngineeringText", "Engineering (Int)")
        self.intimidate_text = QtWidgets.QLabel()
        initialize_text(self.intimidate_text, "IntimidateText", "Intimidate (Cha)")
        self.life_text = QtWidgets.QLabel()
        initialize_text(self.life_text, "LifeText", "Life Science (Int)")
        self.medicine_text = QtWidgets.QLabel()
        initialize_text(self.medicine_text, "MedicineText", "Medicine (Int)")
        self.mysticism_text = QtWidgets.QLabel()
        initialize_text(self.mysticism_text, "MysticismText", "Mysticism (Wis)")
        self.perception_text = QtWidgets.QLabel()
        initialize_text(self.perception_text, "PerceptionText", "Perception (Wis)")
        self.physical_text = QtWidgets.QLabel()
        initialize_text(self.physical_text, "PhysicalText", "Physical Science (Int)")
        self.piloting_text = QtWidgets.QLabel()
        initialize_text(self.piloting_text, "PilotingText", "Piloting (Dex)")
        self.profession_text = QtWidgets.QLabel()
        initialize_text(self.profession_text, "ProfessionText", "Profession")
        self.rank_prof1_skill_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_prof1_skill_combo, "RankProf1SkillCombo", ["Wis", "Int", "Cha"], [43, 20])
        self.rank_prof1_skill_combo.activated.connect(self.update_profession)
        self.profession2_text = QtWidgets.QLabel()
        initialize_text(self.profession2_text, "Profession2Text", "Profession")
        self.rank_prof2_skill_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_prof2_skill_combo, "RankProf2SkillCombo", ["Wis", "Int", "Cha"], [43, 20])
        self.rank_prof2_skill_combo.activated.connect(self.update_profession)
        self.sense_text = QtWidgets.QLabel()
        initialize_text(self.sense_text, "SenseText", "Sense Motive (Wis)")
        self.slight_text = QtWidgets.QLabel()
        initialize_text(self.slight_text, "SlightText", "Slight of Hand (Dex)")
        self.stealth_text = QtWidgets.QLabel()
        initialize_text(self.stealth_text, "StealthText", "Stealth (Dex)")
        self.survival_text = QtWidgets.QLabel()
        initialize_text(self.survival_text, "SurvivalText", "Survival (Wis)")

        self.acrobatics_total = QtWidgets.QLineEdit()
        initialize_edit(self.acrobatics_total, "AcrobaticsTotal", shape=[50, 20])
        self.athletics_total = QtWidgets.QLineEdit()
        initialize_edit(self.athletics_total, "AthleticsTotal", shape=[50, 20])
        self.bluff_total = QtWidgets.QLineEdit()
        initialize_edit(self.bluff_total, "BluffTotal", shape=[50, 20])
        self.computers_total = QtWidgets.QLineEdit()
        initialize_edit(self.computers_total, "ComputersTotal", shape=[50, 20])
        self.culture_total = QtWidgets.QLineEdit()
        initialize_edit(self.culture_total, "CultureTotal", shape=[50, 20])
        self.diplomacy_total = QtWidgets.QLineEdit()
        initialize_edit(self.diplomacy_total, "DiplomacyTotal", shape=[50, 20])
        self.disguise_total = QtWidgets.QLineEdit()
        initialize_edit(self.disguise_total, "DisguiseTotal", shape=[50, 20])
        self.engineering_total = QtWidgets.QLineEdit()
        initialize_edit(self.engineering_total, "EngineeringTotal", shape=[50, 20])
        self.intimidate_total = QtWidgets.QLineEdit()
        initialize_edit(self.intimidate_total, "IntimidateTotal", shape=[50, 20])
        self.life_total = QtWidgets.QLineEdit()
        initialize_edit(self.life_total, "LifeTotal", shape=[50, 20])
        self.medicine_total = QtWidgets.QLineEdit()
        initialize_edit(self.medicine_total, "MedicineTotal", shape=[50, 20])
        self.mysticism_total = QtWidgets.QLineEdit()
        initialize_edit(self.mysticism_total, "MysticismTotal", shape=[50, 20])
        self.perception_total = QtWidgets.QLineEdit()
        initialize_edit(self.perception_total, "PerceptionTotal", shape=[50, 20])
        self.physical_total = QtWidgets.QLineEdit()
        initialize_edit(self.physical_total, "PhysicalTotal", shape=[50, 20])
        self.piloting_total = QtWidgets.QLineEdit()
        initialize_edit(self.piloting_total, "PilotingTotal", shape=[50, 20])
        self.profession_total = QtWidgets.QLineEdit()
        initialize_edit(self.profession_total, "ProfessionTotal", shape=[50, 20])
        self.profession2_total = QtWidgets.QLineEdit()
        initialize_edit(self.profession2_total, "Profession2Total", shape=[50, 20])
        self.sense_total = QtWidgets.QLineEdit()
        initialize_edit(self.sense_total, "SenseTotal", shape=[50, 20])
        self.slight_total = QtWidgets.QLineEdit()
        initialize_edit(self.slight_total, "SlightTotal", shape=[50, 20])
        self.stealth_total = QtWidgets.QLineEdit()
        initialize_edit(self.stealth_total, "StealthTotal", shape=[50, 20])
        self.survival_total = QtWidgets.QLineEdit()
        initialize_edit(self.survival_total, "SurvivalTotal", shape=[50, 20])
        self.rank_acrobatics_combo = QtWidgets.QComboBox()

        initialize_combo(self.rank_acrobatics_combo, "RankAcrobaticsCombo", ["0"], [43, 20])
        self.rank_acrobatics_combo.activated.connect(self.update_skill_buy)
        self.rank_athletics_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_athletics_combo, "RankAthleticsCombo", ["0"], [43, 20])
        self.rank_athletics_combo.activated.connect(self.update_skill_buy)
        self.rank_bluff_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_bluff_combo, "RankBluffCombo", ["0"], [43, 20])
        self.rank_bluff_combo.activated.connect(self.update_skill_buy)
        self.rank_computers_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_computers_combo, "RankComputersCombo", ["0"], [43, 20])
        self.rank_computers_combo.activated.connect(self.update_skill_buy)
        self.rank_culture_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_culture_combo, "RankCultureCombo", ["0"], [43, 20])
        self.rank_culture_combo.activated.connect(self.update_skill_buy)
        self.rank_diplomacy_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_diplomacy_combo, "RankDiplomacyCombo", ["0"], [43, 20])
        self.rank_diplomacy_combo.activated.connect(self.update_skill_buy)
        self.rank_disguise_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_disguise_combo, "RankDisguiseCombo", ["0"], [43, 20])
        self.rank_disguise_combo.activated.connect(self.update_skill_buy)
        self.rank_engineering_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_engineering_combo, "RankLifeCombo", ["0"], [43, 20])
        self.rank_engineering_combo.activated.connect(self.update_skill_buy)
        self.rank_intimidate_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_intimidate_combo, "RankMedicineCombo", ["0"], [43, 20])
        self.rank_intimidate_combo.activated.connect(self.update_skill_buy)
        self.rank_life_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_life_combo, "RankLifeCombo", ["0"], [43, 20])
        self.rank_life_combo.activated.connect(self.update_skill_buy)
        self.rank_medicine_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_medicine_combo, "RankMedicineCombo", ["0"], [43, 20])
        self.rank_medicine_combo.activated.connect(self.update_skill_buy)
        self.rank_mysticism_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_mysticism_combo, "RankMysticismCombo", ["0"], [43, 20])
        self.rank_mysticism_combo.activated.connect(self.update_skill_buy)
        self.rank_perception_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_perception_combo, "RankPerceptionCombo", ["0"], [43, 20])
        self.rank_perception_combo.activated.connect(self.update_skill_buy)
        self.rank_physical_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_physical_combo, "RankPhysicalCombo", ["0"], [43, 20])
        self.rank_physical_combo.activated.connect(self.update_skill_buy)
        self.rank_piloting_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_piloting_combo, "RankSenseCombo", ["0"], [43, 20])
        self.rank_piloting_combo.activated.connect(self.update_skill_buy)
        self.rank_profession1_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_profession1_combo, "RankProfession1Combo", ["0"], [43, 20])
        self.rank_profession1_combo.activated.connect(self.update_skill_buy)
        self.rank_profession2_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_profession2_combo, "RankProfession2Combo", ["0"], [43, 20])
        self.rank_profession2_combo.activated.connect(self.update_skill_buy)
        self.rank_sense_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_sense_combo, "RankSenseCombo", ["0"], [43, 20])
        self.rank_sense_combo.activated.connect(self.update_skill_buy)
        self.rank_slight_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_slight_combo, "RankSlightCombo", ["0"], [43, 20])
        self.rank_slight_combo.activated.connect(self.update_skill_buy)
        self.rank_stealth_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_stealth_combo, "RankStealthCombo", ["0"], [43, 20])
        self.rank_stealth_combo.activated.connect(self.update_skill_buy)
        self.rank_survival_combo = QtWidgets.QComboBox()
        initialize_combo(self.rank_survival_combo, "RankSurvivalCombo", ["0"], [43, 20])
        self.rank_survival_combo.activated.connect(self.update_skill_buy)

        self.acrobatics_class = QtWidgets.QLineEdit()
        initialize_edit(self.acrobatics_class, "AcrobaticsClass", shape=[50, 20])
        self.athletics_class = QtWidgets.QLineEdit()
        initialize_edit(self.athletics_class, "AthleticsClass", shape=[50, 20])
        self.bluff_class = QtWidgets.QLineEdit()
        initialize_edit(self.bluff_class, "BluffClass", shape=[50, 20])
        self.computers_class = QtWidgets.QLineEdit()
        initialize_edit(self.computers_class, "ComputersClass", shape=[50, 20])
        self.culture_class = QtWidgets.QLineEdit()
        initialize_edit(self.culture_class, "CultureClass", shape=[50, 20])
        self.diplomacy_class = QtWidgets.QLineEdit()
        initialize_edit(self.diplomacy_class, "DiplomacyClass", shape=[50, 20])
        self.disguise_class = QtWidgets.QLineEdit()
        initialize_edit(self.disguise_class, "DisguiseClass", shape=[50, 20])
        self.engineering_class = QtWidgets.QLineEdit()
        initialize_edit(self.engineering_class, "EngineeringClass", shape=[50, 20])
        self.intimidate_class = QtWidgets.QLineEdit()
        initialize_edit(self.intimidate_class, "IntimidateClass", shape=[50, 20])
        self.life_class = QtWidgets.QLineEdit()
        initialize_edit(self.life_class, "LifeClass", shape=[50, 20])
        self.medicine_class = QtWidgets.QLineEdit()
        initialize_edit(self.medicine_class, "MedicineClass", shape=[50, 20])
        self.mysticism_class = QtWidgets.QLineEdit()
        initialize_edit(self.mysticism_class, "MysticismClass", shape=[50, 20])
        self.perception_class = QtWidgets.QLineEdit()
        initialize_edit(self.perception_class, "PerceptionClass", shape=[50, 20])
        self.physical_class = QtWidgets.QLineEdit()
        initialize_edit(self.physical_class, "PhysicalClass", shape=[50, 20])
        self.profession_class = QtWidgets.QLineEdit()
        initialize_edit(self.profession_class, "ProfessionClass", shape=[50, 20])
        self.profession2_class = QtWidgets.QLineEdit()
        initialize_edit(self.profession2_class, "Profession2Class", shape=[50, 20])
        self.piloting_class = QtWidgets.QLineEdit()
        initialize_edit(self.piloting_class, "PilotingClass", shape=[50, 20])
        self.sense_class = QtWidgets.QLineEdit()
        initialize_edit(self.sense_class, "SenseClass", shape=[50, 20])
        self.slight_class = QtWidgets.QLineEdit()
        initialize_edit(self.slight_class, "SlightClass", shape=[50, 20])
        self.stealth_class = QtWidgets.QLineEdit()
        initialize_edit(self.stealth_class, "StealthClass", shape=[50, 20])
        self.survival_class = QtWidgets.QLineEdit()
        initialize_edit(self.survival_class, "SurvivalClass", shape=[50, 20])

        self.acrobatics_ability = QtWidgets.QLineEdit()
        initialize_edit(self.acrobatics_ability, "AcrobaticsAbility", shape=[50, 20])
        self.athletics_ability = QtWidgets.QLineEdit()
        initialize_edit(self.athletics_ability, "AthleticsAbility", shape=[50, 20])
        self.bluff_ability = QtWidgets.QLineEdit()
        initialize_edit(self.bluff_ability, "BluffAbility", shape=[50, 20])
        self.computers_ability = QtWidgets.QLineEdit()
        initialize_edit(self.computers_ability, "ComputersAbility", shape=[50, 20])
        self.culture_ability = QtWidgets.QLineEdit()
        initialize_edit(self.culture_ability, "CultureAbility", shape=[50, 20])
        self.diplomacy_ability = QtWidgets.QLineEdit()
        initialize_edit(self.diplomacy_ability, "DiplomacyAbility", shape=[50, 20])
        self.disguise_ability = QtWidgets.QLineEdit()
        initialize_edit(self.disguise_ability, "DisguiseAbility", shape=[50, 20])
        self.engineering_ability = QtWidgets.QLineEdit()
        initialize_edit(self.engineering_ability, "EngineeringAbility", shape=[50, 20])
        self.intimidate_ability = QtWidgets.QLineEdit()
        initialize_edit(self.intimidate_ability, "IntimidateAbility", shape=[50, 20])
        self.life_ability = QtWidgets.QLineEdit()
        initialize_edit(self.life_ability, "LifeAbility", shape=[50, 20])
        self.medicine_ability = QtWidgets.QLineEdit()
        initialize_edit(self.medicine_ability, "MedicineAbility", shape=[50, 20])
        self.mysticism_ability = QtWidgets.QLineEdit()
        initialize_edit(self.mysticism_ability, "MysticismAbility", shape=[50, 20])
        self.perception_ability = QtWidgets.QLineEdit()
        initialize_edit(self.perception_ability, "PerceptionAbility", shape=[50, 20])
        self.physical_ability = QtWidgets.QLineEdit()
        initialize_edit(self.physical_ability, "PhysicalAbility", shape=[50, 20])
        self.piloting_ability = QtWidgets.QLineEdit()
        initialize_edit(self.piloting_ability, "PilotingAbility", shape=[50, 20])
        self.profession_ability = QtWidgets.QLineEdit()
        initialize_edit(self.profession_ability, "ProfessionAbility", shape=[50, 20])
        self.profession2_ability = QtWidgets.QLineEdit()
        initialize_edit(self.profession2_ability, "Profession2Ability", shape=[50, 20])
        self.sense_ability = QtWidgets.QLineEdit()
        initialize_edit(self.sense_ability, "SenseAbility", shape=[50, 20])
        self.slight_ability = QtWidgets.QLineEdit()
        initialize_edit(self.slight_ability, "SlightAbility", shape=[50, 20])
        self.stealth_ability = QtWidgets.QLineEdit()
        initialize_edit(self.stealth_ability, "StealthAbility", shape=[50, 20])
        self.survival_ability = QtWidgets.QLineEdit()
        initialize_edit(self.survival_ability, "SurvivalAbility", shape=[50, 20])

        self.acrobatics_misc = QtWidgets.QLineEdit()
        initialize_edit(self.acrobatics_misc, "AcrobaticsMisc", shape=[50, 20])
        self.athletics_misc = QtWidgets.QLineEdit()
        initialize_edit(self.athletics_misc, "AthleticsMisc", shape=[50, 20])
        self.bluff_misc = QtWidgets.QLineEdit()
        initialize_edit(self.bluff_misc, "BluffMisc", shape=[50, 20])
        self.computers_misc = QtWidgets.QLineEdit()
        initialize_edit(self.computers_misc, "ComputersMisc", shape=[50, 20])
        self.culture_misc = QtWidgets.QLineEdit()
        initialize_edit(self.culture_misc, "CultureMisc", shape=[50, 20])
        self.diplomacy_misc = QtWidgets.QLineEdit()
        initialize_edit(self.diplomacy_misc, "DiplomacyMisc", shape=[50, 20])
        self.disguise_misc = QtWidgets.QLineEdit()
        initialize_edit(self.disguise_misc, "DisguiseMisc", shape=[50, 20])
        self.engineering_misc = QtWidgets.QLineEdit()
        initialize_edit(self.engineering_misc, "EngineeringMisc", shape=[50, 20])
        self.intimidate_misc = QtWidgets.QLineEdit()
        initialize_edit(self.intimidate_misc, "IntimidateMisc", shape=[50, 20])
        self.life_misc = QtWidgets.QLineEdit()
        initialize_edit(self.life_misc, "LifeMisc", shape=[50, 20])
        self.medicine_misc = QtWidgets.QLineEdit()
        initialize_edit(self.medicine_misc, "MedicineMisc", shape=[50, 20])
        self.mysticism_misc = QtWidgets.QLineEdit()
        initialize_edit(self.mysticism_misc, "MysticismMisc", shape=[50, 20])
        self.perception_misc = QtWidgets.QLineEdit()
        initialize_edit(self.perception_misc, "PerceptionMisc", shape=[50, 20])
        self.physical_misc = QtWidgets.QLineEdit()
        initialize_edit(self.physical_misc, "PhysicalMisc", shape=[50, 20])
        self.piloting_misc = QtWidgets.QLineEdit()
        initialize_edit(self.piloting_misc, "PilotingMisc", shape=[50, 20])
        self.profession_misc = QtWidgets.QLineEdit()
        initialize_edit(self.profession_misc, "ProfessionMisc", shape=[50, 20])
        self.profession2_misc = QtWidgets.QLineEdit()
        initialize_edit(self.profession2_misc, "Profession2Misc", shape=[50, 20])
        self.sense_misc = QtWidgets.QLineEdit()
        initialize_edit(self.sense_misc, "SenseMisc", shape=[50, 20])
        self.slight_misc = QtWidgets.QLineEdit()
        initialize_edit(self.slight_misc, "SlightMisc", shape=[50, 20])
        self.stealth_misc = QtWidgets.QLineEdit()
        initialize_edit(self.stealth_misc, "StealthMisc", shape=[50, 20])
        self.survival_misc = QtWidgets.QLineEdit()
        initialize_edit(self.survival_misc, "SurvivalMisc", shape=[50, 20])

        skill_count_grid = QtWidgets.QHBoxLayout()
        skill_count_grid.setContentsMargins(0, 0, 0, 0)
        skill_count_grid.setObjectName("SkillCountGrid")

        remaining_skill_text = QtWidgets.QLabel()
        initialize_text(remaining_skill_text, "RemainingSkillText", "Remaining Skill Points")

        self.remaining_skill_box = QtWidgets.QLineEdit()
        initialize_edit(self.remaining_skill_box, "RemainingSkillBox", shape=[40, 20])

        self.skills_per_text = QtWidgets.QLabel()
        initialize_text(self.skills_per_text, "SkillsPerText", "Skill Ranks Per Level")

        self.skills_per_box = QtWidgets.QLineEdit()
        initialize_edit(self.skills_per_box, "SkillsPerBox", shape=[40, 20])

        skills_score_grid.addWidget(self.skill_total_text, 0, 2, 1, 1)
        skills_score_grid.addWidget(self.skill_ranks_text, 0, 4, 1, 1)
        skills_score_grid.addWidget(self.skill_class_text, 0, 6, 1, 1)
        skills_score_grid.addWidget(self.skill_ability_text, 0, 8, 1, 1)
        skills_score_grid.addWidget(self.skill_misc_text, 0, 10, 1, 1)

        add_widgets_to_layout(skills_score_grid, [self.acrobatics_text,
                                                  self.athletics_text,
                                                  self.bluff_text,
                                                  self.computers_text,
                                                  self.culture_text,
                                                  self.diplomacy_text,
                                                  self.disguise_text,
                                                  self.engineering_text,
                                                  self.intimidate_text,
                                                  self.life_text,
                                                  self.medicine_text,
                                                  self.mysticism_text,
                                                  self.perception_text,
                                                  self.physical_text,
                                                  self.piloting_text],
                              2, 0, 2)
        skills_score_grid.addWidget(self.profession_text,        32, 0, 1, 1)
        skills_score_grid.addWidget(self.rank_prof1_skill_combo, 32, 1, 1, 1)
        skills_score_grid.addWidget(self.profession2_text,       34, 0, 1, 1)
        skills_score_grid.addWidget(self.rank_prof2_skill_combo, 34, 1, 1, 1)
        add_widgets_to_layout(skills_score_grid, [self.sense_text,
                                                  self.slight_text,
                                                  self.stealth_text,
                                                  self.survival_text],
                              36, 0, 2)

        add_widgets_to_layout(skills_score_grid, [self.acrobatics_total,
                                                  self.athletics_total,
                                                  self.bluff_total,
                                                  self.computers_total,
                                                  self.culture_total,
                                                  self.diplomacy_total,
                                                  self.disguise_total,
                                                  self.engineering_total,
                                                  self.intimidate_total,
                                                  self.life_total,
                                                  self.medicine_total,
                                                  self.mysticism_total,
                                                  self.perception_total,
                                                  self.physical_total,
                                                  self.piloting_total,
                                                  self.profession_total,
                                                  self.profession2_total,
                                                  self.sense_total,
                                                  self.slight_total,
                                                  self.stealth_total,
                                                  self.survival_total],
                              2, 2, 1)

        add_widgets_to_layout(skills_score_grid, [self.rank_acrobatics_combo,
                                                  self.rank_athletics_combo,
                                                  self.rank_bluff_combo,
                                                  self.rank_computers_combo,
                                                  self.rank_culture_combo,
                                                  self.rank_diplomacy_combo,
                                                  self.rank_disguise_combo,
                                                  self.rank_engineering_combo,
                                                  self.rank_intimidate_combo,
                                                  self.rank_life_combo,
                                                  self.rank_medicine_combo,
                                                  self.rank_mysticism_combo,
                                                  self.rank_perception_combo,
                                                  self.rank_physical_combo,
                                                  self.rank_piloting_combo,
                                                  self.rank_profession1_combo,
                                                  self.rank_profession2_combo,
                                                  self.rank_sense_combo,
                                                  self.rank_slight_combo,
                                                  self.rank_stealth_combo,
                                                  self.rank_survival_combo],
                              2, 4, 1)

        add_widgets_to_layout(skills_score_grid, [self.acrobatics_class,
                                                  self.athletics_class,
                                                  self.bluff_class,
                                                  self.computers_class,
                                                  self.culture_class,
                                                  self.diplomacy_class,
                                                  self.disguise_class,
                                                  self.engineering_class,
                                                  self.intimidate_class,
                                                  self.life_class,
                                                  self.medicine_class,
                                                  self.mysticism_class,
                                                  self.perception_class,
                                                  self.physical_class,
                                                  self.profession_class,
                                                  self.profession2_class,
                                                  self.piloting_class,
                                                  self.sense_class,
                                                  self.slight_class,
                                                  self.stealth_class,
                                                  self.survival_class],
                              2, 6, 1)

        add_widgets_to_layout(skills_score_grid, [self.acrobatics_ability,
                                                  self.athletics_ability,
                                                  self.bluff_ability,
                                                  self.computers_ability,
                                                  self.culture_ability,
                                                  self.diplomacy_ability,
                                                  self.disguise_ability,
                                                  self.engineering_ability,
                                                  self.intimidate_ability,
                                                  self.life_ability,
                                                  self.medicine_ability,
                                                  self.mysticism_ability,
                                                  self.perception_ability,
                                                  self.physical_ability,
                                                  self.piloting_ability,
                                                  self.profession_ability,
                                                  self.profession2_ability,
                                                  self.sense_ability,
                                                  self.slight_ability,
                                                  self.stealth_ability,
                                                  self.survival_ability],
                              2, 8, 1)

        add_widgets_to_layout(skills_score_grid, [self.acrobatics_misc,
                                                  self.athletics_misc,
                                                  self.bluff_misc,
                                                  self.computers_misc,
                                                  self.culture_misc,
                                                  self.diplomacy_misc,
                                                  self.disguise_misc,
                                                  self.engineering_misc,
                                                  self.intimidate_misc,
                                                  self.life_misc,
                                                  self.medicine_misc,
                                                  self.mysticism_misc,
                                                  self.perception_misc,
                                                  self.physical_misc,
                                                  self.piloting_misc,
                                                  self.profession_misc,
                                                  self.profession2_misc,
                                                  self.sense_misc,
                                                  self.slight_misc,
                                                  self.stealth_misc,
                                                  self.survival_misc],
                              2, 10, 1)

        skill_count_grid.addWidget(remaining_skill_text, alignment=QtCore.Qt.AlignRight)
        skill_count_grid.addWidget(self.remaining_skill_box, alignment=QtCore.Qt.AlignLeft)
        skill_count_grid.addWidget(self.skills_per_text, alignment=QtCore.Qt.AlignRight)
        skill_count_grid.addWidget(self.skills_per_box)

        skill_points_layout.addLayout(skill_count_grid)
        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        skill_points_layout.addWidget(line)
        skill_points_layout.addLayout(skills_score_grid)

        self.widget.setLayout(skill_points_layout)

    def get_skill_rank_combos(self) -> dict[str, QtWidgets.QComboBox]:
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
        return skill_buys

    def get_skill_bought_rank(self) -> dict[str, int]:

        skill_bought_rank = {}
        for skill, rank_combo in self.get_skill_rank_combos().items():
            skill_bought_rank[skill] = int(rank_combo.currentText())

        return skill_bought_rank

    def update_skill_buy_spendable_points(self, skill_buy_spendable_points: int):
        """update skills based on the skill buys. Needs class_name to be set
        """
        self.skill_buy_spendable_points = skill_buy_spendable_points

    def update_misc_skills(self, skill_misc: dict, skill_dabbler: dict):
        """update the misc skills in the skills tab
        """
        boxes = [self.acrobatics_misc, self.athletics_misc, self.bluff_misc, self.computers_misc,
                 self.culture_misc, self.diplomacy_misc, self.disguise_misc, self.engineering_misc,
                 self.intimidate_misc, self.life_misc, self.medicine_misc, self.mysticism_misc,
                 self.perception_misc, self.physical_misc, self.piloting_misc,self.profession_misc,
                 self.profession2_misc, self.sense_misc, self.slight_misc, self.stealth_misc,
                 self.survival_misc]

        for skill, dabbler, box in zip(skill_misc.values(),
                                        skill_dabbler.values(), boxes):
            box.setText(str(skill + dabbler))

    def update_skills(self, skills_list: list) -> None:
        """update the skill totals in the skills tab. Needs the class_name to be set
        """
        boxes = [self.acrobatics_total, self.athletics_total, self.bluff_total,
                    self.computers_total, self.culture_total, self.diplomacy_total,
                    self.disguise_total, self.engineering_total, self.intimidate_total,
                    self.life_total, self.medicine_total, self.mysticism_total,
                    self.perception_total, self.physical_total, self.piloting_total,
                    self.profession_total, self.profession2_total, self.sense_total,
                    self.slight_total, self.stealth_total, self.survival_total,
                    self.remaining_skill_box, self.skills_per_box]

        for skill, box in zip(skills_list, boxes):
            box.setText(str(skill))

    def update_abilities(self, skills):
        """updates the attribute scores in the attributes tab
        """
        boxes = [self.acrobatics_ability, self.athletics_ability, self.bluff_ability,
                 self.computers_ability, self.culture_ability, self.diplomacy_ability,
                 self.disguise_ability, self.engineering_ability, self.intimidate_ability,
                 self.life_ability, self.medicine_ability, self.mysticism_ability,
                 self.perception_ability, self.physical_ability, self.piloting_ability,
                 self.profession_ability, self.profession2_ability, self.sense_ability,
                 self.slight_ability, self.stealth_ability, self.survival_ability]

        for skill, box in zip(skills, boxes):
            box.setText(str(skill))

    def update_class_stats(self, character_skills: dict[str, int]):
        boxes = [self.acrobatics_class, self.athletics_class, self.bluff_class,
                 self.computers_class, self.culture_class, self.diplomacy_class,
                 self.disguise_class, self.engineering_class, self.intimidate_class,
                 self.life_class, self.medicine_class, self.mysticism_class,
                 self.perception_class, self.physical_class, self.piloting_class,
                 self.profession_class, self.profession2_class, self.sense_class,
                 self.slight_class, self.stealth_class, self.survival_class]

        for skill, box in zip(character_skills.values(), boxes):
            box.setText(str(skill))

    def update_profession(self):
        """function to update the ability modifiers for the two profession skills
        """
        prof1 = self.rank_prof1_skill_combo.currentText()
        prof2 = self.rank_prof2_skill_combo.currentText()
        self.parent.update_professions(prof1, prof2)

    def update_skill_buy(self):
        self.parent.update_skill_buy()
