from PyQt5 import QtCore, QtWidgets

from helpers.helper import initialize_text, initialize_edit, initialize_frame, initialize_widget

class Saves:
    def __init__(self) -> None:
        self.widget = QtWidgets.QWidget()

        save_grid = QtWidgets.QGridLayout()
        save_grid.setContentsMargins(0, 0, 0, 0)
        save_grid.setObjectName("SaveGrid")

        self.save_line1 = QtWidgets.QFrame()
        initialize_frame(self.save_line1, "SaveLine1", vertical=False)
        save_grid.addWidget(self.save_line1, 2, 0, 1, 8)
        self.save_line2 = QtWidgets.QFrame()
        initialize_frame(self.save_line2, "SaveLine2", vertical=False)
        save_grid.addWidget(self.save_line2, 4, 0, 1, 8)

        self.fortitude_text = QtWidgets.QLabel()
        initialize_text(self.fortitude_text, "FortitudeText", "Fortitude")
        save_grid.addWidget(self.fortitude_text, 1, 0, 1, 1)
        self.reflex_text = QtWidgets.QLabel()
        initialize_text(self.reflex_text, "ReflexText", "Reflex")
        save_grid.addWidget(self.reflex_text, 3, 0, 1, 1)
        self.will_text = QtWidgets.QLabel()
        initialize_text(self.will_text, "WillText", "Will")
        save_grid.addWidget(self.will_text, 5, 0, 1, 1)

        self.save_total_text = QtWidgets.QLabel()
        initialize_text(self.save_total_text, "SaveTotalText", "Total")
        save_grid.addWidget(self.save_total_text, 0, 1, 1, 1)
        self.save_base_text = QtWidgets.QLabel()
        initialize_text(self.save_base_text, "SaveBaseText", "Base Save")
        save_grid.addWidget(self.save_base_text, 0, 3, 1, 1)
        self.save_ability_text = QtWidgets.QLabel()
        initialize_text(self.save_ability_text, "SaveAbilityText", "Ability Mod")
        save_grid.addWidget(self.save_ability_text, 0, 5, 1, 1)
        self.save_misc_text = QtWidgets.QLabel()
        initialize_text(self.save_misc_text, "SaveMiscText", "Misc Mod")
        save_grid.addWidget(self.save_misc_text, 0, 7, 1, 1)

        self.fortitude_equals = QtWidgets.QLabel()
        initialize_text(self.fortitude_equals, "FortitudeEquals", "=", max_size=[10, 25])
        save_grid.addWidget(self.fortitude_equals, 1, 2, 1, 1)
        self.fortitude_plus = QtWidgets.QLabel()
        initialize_text(self.fortitude_plus, "FortitudePlus", "+", max_size=[10, 25])
        save_grid.addWidget(self.fortitude_plus, 1, 4, 1, 1)
        self.fortitude_plus_2 = QtWidgets.QLabel()
        initialize_text(self.fortitude_plus_2, "FortitudePlus_2", "+", max_size=[10, 25])
        save_grid.addWidget(self.fortitude_plus_2, 1, 6, 1, 1)
        self.reflex_equals = QtWidgets.QLabel()
        initialize_text(self.reflex_equals, "ReflexEquals", "=", max_size=[10, 25])
        save_grid.addWidget(self.reflex_equals, 3, 2, 1, 1)
        self.reflex_plus = QtWidgets.QLabel()
        initialize_text(self.reflex_plus, "ReflexPlus", "+", max_size=[10, 25])
        save_grid.addWidget(self.reflex_plus, 3, 4, 1, 1)
        self.reflex_plus_2 = QtWidgets.QLabel()
        initialize_text(self.reflex_plus_2, "ReflexPlus_2", "+", max_size=[10, 25])
        save_grid.addWidget(self.reflex_plus_2, 3, 6, 1, 1)
        self.will_equals = QtWidgets.QLabel()
        initialize_text(self.will_equals, "WillEquals", "=", max_size=[10, 25])
        save_grid.addWidget(self.will_equals, 5, 2, 1, 1)
        self.will_plus = QtWidgets.QLabel()
        initialize_text(self.will_plus, "WillPlus", "+", max_size=[10, 25])
        save_grid.addWidget(self.will_plus, 5, 4, 1, 1)
        self.will_plus_2 = QtWidgets.QLabel()
        initialize_text(self.will_plus_2, "WillPlus_2", "+", max_size=[10, 25])
        save_grid.addWidget(self.will_plus_2, 5, 6, 1, 1)

        self.fortitude_total_box = QtWidgets.QLineEdit()
        initialize_edit(self.fortitude_total_box, "FortitudeTotalBox", shape=[40, 25])
        save_grid.addWidget(self.fortitude_total_box, 1, 1, 1, 1)
        self.fortitude_base_box = QtWidgets.QLineEdit()
        initialize_edit(self.fortitude_base_box, "FortitudeBaseBox", shape=[40, 25])
        save_grid.addWidget(self.fortitude_base_box, 1, 3, 1, 1)
        self.fortitude_ability_box = QtWidgets.QLineEdit()
        initialize_edit(self.fortitude_ability_box, "FortitudeAbilityBox", shape=[40, 25])
        save_grid.addWidget(self.fortitude_ability_box, 1, 5, 1, 1)
        self.fortitude_misc_box = QtWidgets.QLineEdit()
        initialize_edit(self.fortitude_misc_box, "FortitudeMiscBox", shape=[40, 25])
        save_grid.addWidget(self.fortitude_misc_box, 1, 7, 1, 1)
        self.reflex_total_box = QtWidgets.QLineEdit()
        initialize_edit(self.reflex_total_box, "ReflexTotalBox", shape=[40, 25])
        save_grid.addWidget(self.reflex_total_box, 3, 1, 1, 1)
        self.reflex_base_box = QtWidgets.QLineEdit()
        initialize_edit(self.reflex_base_box, "ReflexBaseBox", shape=[40, 25])
        save_grid.addWidget(self.reflex_base_box, 3, 3, 1, 1)
        self.reflex_ability_box = QtWidgets.QLineEdit()
        initialize_edit(self.reflex_ability_box, "ReflexAbilityBox", shape=[40, 25])
        save_grid.addWidget(self.reflex_ability_box, 3, 5, 1, 1)
        self.reflex_misc_box = QtWidgets.QLineEdit()
        initialize_edit(self.reflex_misc_box, "ReflexMiscBox", shape=[40, 25])
        save_grid.addWidget(self.reflex_misc_box, 3, 7, 1, 1)
        self.will_total_box = QtWidgets.QLineEdit()
        initialize_edit(self.will_total_box, "WillTotalBox", shape=[40, 25])
        save_grid.addWidget(self.will_total_box, 5, 1, 1, 1)
        self.will_base_box = QtWidgets.QLineEdit()
        initialize_edit(self.will_base_box, "WillBaseBox", shape=[40, 25])
        save_grid.addWidget(self.will_base_box, 5, 3, 1, 1)
        self.will_ability_box = QtWidgets.QLineEdit()
        initialize_edit(self.will_ability_box, "WillAbilityBox", shape=[40, 25])
        save_grid.addWidget(self.will_ability_box, 5, 5, 1, 1)
        self.will_misc_box = QtWidgets.QLineEdit()
        initialize_edit(self.will_misc_box, "WillMiscBox", shape=[40, 25])
        save_grid.addWidget(self.will_misc_box, 5, 7, 1, 1)

        self.widget.setLayout(save_grid)

    def update_saves(self, skills):
        boxes = [self.fortitude_total_box, self.reflex_total_box, self.will_total_box,
                 self.fortitude_base_box,  self.reflex_base_box, self.will_base_box,
                 self.fortitude_ability_box, self.reflex_ability_box, self.will_ability_box,
                 self.fortitude_misc_box, self.reflex_misc_box, self.will_misc_box]

        for skill, box in zip(skills, boxes):
            box.setText(str(skill))
