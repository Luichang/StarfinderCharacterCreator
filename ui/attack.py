from PyQt5 import QtCore, QtWidgets

from helpers.helper import initialize_text, initialize_edit, initialize_frame

class Attack:
    def __init__(self) -> None:
        self.widget = QtWidgets.QWidget()

        attack_grid = QtWidgets.QGridLayout()
        attack_grid.setContentsMargins(0, 0, 0, 0)
        attack_grid.setObjectName("AttackGrid")

        self.attack_line1 = QtWidgets.QFrame()
        initialize_frame(self.attack_line1, "AttackLine1", vertical=False)
        self.attack_line2 = QtWidgets.QFrame()
        initialize_frame(self.attack_line2, "AttackLine2", vertical=False)

        melee_attack_text = QtWidgets.QLabel()
        initialize_text(melee_attack_text, "MeleeText", "Melee Attack")
        melee_text_total = QtWidgets.QLabel()
        initialize_text(melee_text_total, "MeleeTotalText", "Total")
        melee_bab_text = QtWidgets.QLabel()
        initialize_text(melee_bab_text, "MeleeBABText", "BAB")
        melee_mod_text = QtWidgets.QLabel()
        initialize_text(melee_mod_text, "MeleeModText", "Str Mod")
        melee_misc_text = QtWidgets.QLabel()
        initialize_text(melee_misc_text, "MeleeMiscText", "Misc Mod")

        ranged_text = QtWidgets.QLabel()
        initialize_text(ranged_text, "RangedText", "Ranged Attack")
        ranged_total_text = QtWidgets.QLabel()
        initialize_text(ranged_total_text, "RangedTotalText", "Total")
        ranged_bab_text = QtWidgets.QLabel()
        initialize_text(ranged_bab_text, "RangedBABText", "BAB")
        ranged_mod_text = QtWidgets.QLabel()
        initialize_text(ranged_mod_text, "RangedModText", "Dex Mod")
        ranged_misc_text = QtWidgets.QLabel()
        initialize_text(ranged_misc_text, "RangedMiscText", "Misc Mod")

        thrown_text = QtWidgets.QLabel()
        initialize_text(thrown_text, "ThrownText", "Thrown Attack")
        thrown_total_text = QtWidgets.QLabel()
        initialize_text(thrown_total_text, "ThrownTotalText", "Total")
        thrown_bab_text = QtWidgets.QLabel()
        initialize_text(thrown_bab_text, "ThrownBABText", "BAB")
        thrown_mod_text = QtWidgets.QLabel()
        initialize_text(thrown_mod_text, "ThrownModText", "Str Mod")
        thrown_misc_text = QtWidgets.QLabel()
        initialize_text(thrown_misc_text, "ThrownMiscText", "Misc Mod")

        attack_equals = QtWidgets.QLabel()
        initialize_text(attack_equals, "AttackEquals", "=", max_size=[10, 25])
        attack_equals_2 = QtWidgets.QLabel()
        initialize_text(attack_equals_2, "AttackEquals_2", "=", max_size=[10, 25])
        attack_equals_3 = QtWidgets.QLabel()
        initialize_text(attack_equals_3, "AttackEquals_3", "=", max_size=[10, 25])
        attack_plus = QtWidgets.QLabel()
        initialize_text(attack_plus, "AttackPlus", "+", max_size=[10, 25])
        attack_plus_2 = QtWidgets.QLabel()
        initialize_text(attack_plus_2, "AttackPlus_2", "+", max_size=[10, 25])
        attack_plus_3 = QtWidgets.QLabel()
        initialize_text(attack_plus_3, "AttackPlus_3", "+", max_size=[10, 25])
        attack_plus_4 = QtWidgets.QLabel()
        initialize_text(attack_plus_4, "AttackPlus_4", "+", max_size=[10, 25])
        attack_plus_5 = QtWidgets.QLabel()
        initialize_text(attack_plus_5, "AttackPlus_5", "+", max_size=[10, 25])
        attack_plus_6 = QtWidgets.QLabel()
        initialize_text(attack_plus_6, "AttackPlus_6", "+", max_size=[10, 25])

        self.melee_total_box = QtWidgets.QLineEdit()
        initialize_edit(self.melee_total_box, "MeleeTotalBox", shape=[40, 25])
        self.melee_bab_box = QtWidgets.QLineEdit()
        initialize_edit(self.melee_bab_box, "MeleeBABBox", shape=[40, 25])
        self.melee_mod_box = QtWidgets.QLineEdit()
        initialize_edit(self.melee_mod_box, "MeleeModBox", shape=[40, 25])
        self.melee_misc_box = QtWidgets.QLineEdit()
        initialize_edit(self.melee_misc_box, "MeleeMiscBox", shape=[40, 25])
        self.ranged_total_box = QtWidgets.QLineEdit()
        initialize_edit(self.ranged_total_box, "RangedTotalBox", shape=[40, 25])
        self.thrown_bab_box = QtWidgets.QLineEdit()
        initialize_edit(self.thrown_bab_box, "ThrownBABBox", shape=[40, 25])
        self.ranged_mod_box = QtWidgets.QLineEdit()
        initialize_edit(self.ranged_mod_box, "RangedModBox", shape=[40, 25])
        self.ranged_misc_box = QtWidgets.QLineEdit()
        initialize_edit(self.ranged_misc_box, "RangedMiscBox", shape=[40, 25])
        self.thrown_total_box = QtWidgets.QLineEdit()
        initialize_edit(self.thrown_total_box, "ThrownTotalBox", shape=[40, 25])
        self.ranged_bab_box = QtWidgets.QLineEdit()
        initialize_edit(self.ranged_bab_box, "RangedBABBox", shape=[40, 25])
        self.thrown_mod_box = QtWidgets.QLineEdit()
        initialize_edit(self.thrown_mod_box, "ThrownModBox", shape=[40, 25])
        self.thrown_misc_box = QtWidgets.QLineEdit()
        initialize_edit(self.thrown_misc_box, "ThrownMiscBox", shape=[40, 25])

        attack_grid.addWidget(melee_text_total, 0, 1, 1, 1)
        attack_grid.addWidget(melee_bab_text, 0, 3, 1, 1)
        attack_grid.addWidget(melee_mod_text, 0, 5, 1, 1)
        attack_grid.addWidget(melee_misc_text, 0, 7, 1, 1)

        attack_grid.addWidget(melee_attack_text,    1, 0, 1, 1)
        attack_grid.addWidget(self.melee_total_box, 1, 1, 1, 1)
        attack_grid.addWidget(attack_equals,   1, 2, 1, 1)
        attack_grid.addWidget(self.melee_bab_box,   1, 3, 1, 1)
        attack_grid.addWidget(attack_plus,     1, 4, 1, 1)
        attack_grid.addWidget(self.melee_mod_box,   1, 5, 1, 1)
        attack_grid.addWidget(attack_plus_2,   1, 6, 1, 1)
        attack_grid.addWidget(self.melee_misc_box,  1, 7, 1, 1)

        attack_grid.addWidget(self.attack_line1, 2, 0, 1, 8)

        attack_grid.addWidget(ranged_total_text, 3, 1, 1, 1)
        attack_grid.addWidget(ranged_bab_text, 3, 3, 1, 1)
        attack_grid.addWidget(ranged_mod_text, 3, 5, 1, 1)
        attack_grid.addWidget(ranged_misc_text, 3, 7, 1, 1)

        attack_grid.addWidget(ranged_text,      4, 0, 1, 1)
        attack_grid.addWidget(self.ranged_total_box, 4, 1, 1, 1)
        attack_grid.addWidget(attack_equals_2,  4, 2, 1, 1)
        attack_grid.addWidget(self.ranged_bab_box,   4, 3, 1, 1)
        attack_grid.addWidget(attack_plus_3,    4, 4, 1, 1)
        attack_grid.addWidget(self.ranged_mod_box,   4, 5, 1, 1)
        attack_grid.addWidget(attack_plus_5,    4, 6, 1, 1)
        attack_grid.addWidget(self.ranged_misc_box,  4, 7, 1, 1)

        attack_grid.addWidget(self.attack_line2, 5, 0, 1, 8)

        attack_grid.addWidget(thrown_total_text, 6, 1, 1, 1)
        attack_grid.addWidget(thrown_bab_text, 6, 3, 1, 1)
        attack_grid.addWidget(thrown_mod_text, 6, 5, 1, 1)
        attack_grid.addWidget(thrown_misc_text, 6, 7, 1, 1)

        attack_grid.addWidget(thrown_text,      7, 0, 1, 1)
        attack_grid.addWidget(self.thrown_total_box, 7, 1, 1, 1)
        attack_grid.addWidget(attack_equals_3,  7, 2, 1, 1)
        attack_grid.addWidget(self.thrown_bab_box,   7, 3, 1, 1)
        attack_grid.addWidget(attack_plus_4,    7, 4, 1, 1)
        attack_grid.addWidget(self.thrown_mod_box,   7, 5, 1, 1)
        attack_grid.addWidget(attack_plus_6,    7, 6, 1, 1)
        attack_grid.addWidget(self.thrown_misc_box,  7, 7, 1, 1)

        self.widget.setLayout(attack_grid)

    def update_attack(self, skills):
        boxes = [self.melee_total_box, self.melee_bab_box, self.melee_mod_box,
                 self.melee_misc_box, self.ranged_total_box, self.ranged_bab_box,
                 self.ranged_mod_box, self.ranged_misc_box, self.thrown_total_box,
                 self.thrown_bab_box, self.thrown_mod_box, self.thrown_misc_box]

        for skill, box in zip(skills, boxes):
            box.setText(str(skill))
