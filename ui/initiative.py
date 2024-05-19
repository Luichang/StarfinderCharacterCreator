from PyQt5 import QtCore, QtWidgets


from helpers.helper import initialize_text, initialize_edit


class Initiative:
    def __init__(self) -> None:
        self.widget = QtWidgets.QWidget()

        initiative_grid = QtWidgets.QHBoxLayout()
        initiative_grid.setContentsMargins(0, 0, 0, 0)
        initiative_grid.setObjectName("InitiativeGrid")

        self.initiative_text = QtWidgets.QLabel()
        initialize_text(self.initiative_text, "InitiativeText", "Initiative", max_size=[50, 20])
        initiative_grid.addWidget(self.initiative_text)

        self.initiative_total = QtWidgets.QLineEdit()
        initialize_edit(self.initiative_total, "InitiativeTotal", shape=[40, 20])
        initiative_grid.addWidget(self.initiative_total)

        self.initiative_equals = QtWidgets.QLabel()
        initialize_text(self.initiative_equals, "InitiativeEquals", "=", max_size=[10, 25])
        initiative_grid.addWidget(self.initiative_equals)

        self.initiative_dex_mod = QtWidgets.QLineEdit()
        initialize_edit(self.initiative_dex_mod, "InitiativeDexMod", shape=[40, 20])
        initiative_grid.addWidget(self.initiative_dex_mod)

        self.initiative_plus = QtWidgets.QLabel()
        initialize_text(self.initiative_plus, "InitiativePlus", "+", max_size=[10, 25])
        initiative_grid.addWidget(self.initiative_plus)

        self.initiative_misc_mod = QtWidgets.QLineEdit()
        initialize_edit(self.initiative_misc_mod, "InitiativeMiscMod", shape=[40, 20])
        initiative_grid.addWidget(self.initiative_misc_mod)

        self.widget.setLayout(initiative_grid)

    def update_initiative(self, skills: list[int]):
        boxes = [self.initiative_total, self.initiative_dex_mod, self.initiative_misc_mod]
        for skill, box in zip(skills, boxes):
            box.setText(str(skill))
