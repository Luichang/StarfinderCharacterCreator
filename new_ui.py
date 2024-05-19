from PyQt5 import QtCore, QtWidgets
from helpers.helper import (initialize_combo, initialize_combo_model,
                            initialize_edit, initialize_frame, initialize_text,
                            initialize_widget, update_combo)
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
        self.window = QtWidgets.QWidget()
        self.setup_ui()
        self.window.show()

    def setup_ui(self):
        layout = QtWidgets.QGridLayout()
        self.window.setObjectName("MainWindow")
        self.window.setGeometry(100, 100, 1075, 984)

        self._initialize_nameframe(layout)
        self._initialize_abilityframe(layout)
        self._initialize_skillframe(layout)
        self._initialize_initframe(layout)
        self._initialize_healthframe(layout)
        self._initialize_armorframe(layout)
        self._initialize_saveframe(layout)
        self._initialize_attackframe(layout)
        self._initialize_flavorframe(layout)

        self.window.setLayout(layout)
        self.window.setWindowTitle("Main Menu")

    def _initialize_nameframe(self, layout: QtWidgets.QGridLayout):
        nameframe = QtWidgets.QFrame()
        nameframe.setFixedSize(451, 51)
        nameframe.setFrameShape(QtWidgets.QFrame.Box)
        nameframe.setFrameShadow(QtWidgets.QFrame.Raised)
        nameframe.setLineWidth(2)
        nameframe.setObjectName("Nameframe")

        self.character_info = CharacterInfo()
        character_layout = QtWidgets.QVBoxLayout()
        character_layout.addWidget(self.character_info.widget)
        nameframe.setLayout(character_layout)

        layout.addWidget(nameframe, 0, 0)

    def _initialize_abilityframe(self, layout: QtWidgets.QGridLayout):
        abilityframe = QtWidgets.QFrame()
        abilityframe.setFixedSize(501, 311)
        abilityframe.setFrameShape(QtWidgets.QFrame.Box)
        abilityframe.setFrameShadow(QtWidgets.QFrame.Raised)
        abilityframe.setLineWidth(2)
        abilityframe.setObjectName("Abilityframe")

        self.ability_score = AbilityScore()
        ability_layout = QtWidgets.QVBoxLayout()
        ability_layout.addWidget(self.ability_score.widget)
        abilityframe.setLayout(ability_layout)

        layout.addWidget(abilityframe, 1, 0)

    def _initialize_skillframe(self, layout: QtWidgets.QGridLayout):
        skillframe = QtWidgets.QFrame()
        skillframe.setFixedSize(481, 801)
        skillframe.setFrameShape(QtWidgets.QFrame.Box)
        skillframe.setFrameShadow(QtWidgets.QFrame.Raised)
        skillframe.setLineWidth(2)
        skillframe.setObjectName("Skillframe")

        self.skill_points = SkillPoints()
        skill_points_layout = QtWidgets.QVBoxLayout()
        skill_points_layout.addWidget(self.skill_points.widget)
        skillframe.setLayout(skill_points_layout)

        layout.addWidget(skillframe, 0, 1)

    def _initialize_initframe(self, layout: QtWidgets.QGridLayout):
        initframe = QtWidgets.QFrame()
        initframe.setFixedSize(241, 51)
        initframe.setFrameShape(QtWidgets.QFrame.Box)
        initframe.setFrameShadow(QtWidgets.QFrame.Raised)
        initframe.setLineWidth(2)
        initframe.setObjectName("Initframe")

        self.initiative = Initiative()
        initiative_layout = QtWidgets.QVBoxLayout()
        initiative_layout.addWidget(self.initiative.widget)
        initframe.setLayout(initiative_layout)

        layout.addWidget(initframe, 0, 1)

    def _initialize_healthframe(self, layout: QtWidgets.QGridLayout):
        healthframe = QtWidgets.QFrame()
        healthframe.setFixedSize(261, 80)
        healthframe.setFrameShape(QtWidgets.QFrame.Box)
        healthframe.setFrameShadow(QtWidgets.QFrame.Raised)
        healthframe.setLineWidth(2)
        healthframe.setObjectName("HPframe")

        self.health = Health()
        health_layout = QtWidgets.QVBoxLayout()
        health_layout.addWidget(self.health.widget)
        healthframe.setLayout(health_layout)

        layout.addWidget(healthframe, 0, 1)

    def _initialize_armorframe(self, layout: QtWidgets.QGridLayout):
        armorframe = QtWidgets.QFrame()
        armorframe.setFixedSize(451, 126)
        armorframe.setFrameShape(QtWidgets.QFrame.Box)
        armorframe.setFrameShadow(QtWidgets.QFrame.Raised)
        armorframe.setLineWidth(2)
        armorframe.setObjectName("Armorframe")

        self.armor = Armor()
        armor_layout = QtWidgets.QVBoxLayout()
        armor_layout.addWidget(self.armor.widget)
        armorframe.setLayout(armor_layout)

        layout.addWidget(armorframe, 0, 1)

    def _initialize_saveframe(self, layout: QtWidgets.QGridLayout):
        saveframe = QtWidgets.QFrame()
        saveframe.setFixedSize(451, 126)
        saveframe.setFrameShape(QtWidgets.QFrame.Box)
        saveframe.setFrameShadow(QtWidgets.QFrame.Raised)
        saveframe.setLineWidth(2)
        saveframe.setObjectName("Armorframe")

        self.save = Saves()
        save_layout = QtWidgets.QVBoxLayout()
        save_layout.addWidget(self.save.widget)
        saveframe.setLayout(save_layout)

        layout.addWidget(saveframe, 0, 1)

    def _initialize_attackframe(self, layout: QtWidgets.QGridLayout):
        attackframe = QtWidgets.QFrame()
        attackframe.setFixedSize(451, 126)
        attackframe.setFrameShape(QtWidgets.QFrame.Box)
        attackframe.setFrameShadow(QtWidgets.QFrame.Raised)
        attackframe.setLineWidth(2)
        attackframe.setObjectName("Armorframe")

        self.attack = Attack()
        attack_layout = QtWidgets.QVBoxLayout()
        attack_layout.addWidget(self.attack.widget)
        attackframe.setLayout(attack_layout)

        layout.addWidget(attackframe, 0, 1)

    def _initialize_flavorframe(self, layout: QtWidgets.QGridLayout):
        flavorframe = QtWidgets.QFrame()
        flavorframe.setFixedSize(451, 126)
        flavorframe.setFrameShape(QtWidgets.QFrame.Box)
        flavorframe.setFrameShadow(QtWidgets.QFrame.Raised)
        flavorframe.setLineWidth(2)
        flavorframe.setObjectName("Armorframe")

        self.flavor = CharacterFlavor()
        flavor_layout = QtWidgets.QVBoxLayout()
        flavor_layout.addWidget(self.flavor.widget)
        flavorframe.setLayout(flavor_layout)

        layout.addWidget(flavorframe, 0, 1)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = UIMainWindow()
    sys.exit(app.exec_())
