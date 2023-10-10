from typing import Protocol
from PyQt5 import QtCore, QtWidgets


from helpers.helper import initialize_text, initialize_edit, initialize_frame

class Character(Protocol):
    stamina_points: str
    hit_points: str
    resolve_points: str

class Health:
    def __init__(self) -> None:
        self.widget = QtWidgets.QWidget()

        hp_grid = QtWidgets.QGridLayout()
        hp_grid.setContentsMargins(0, 0, 0, 0)
        hp_grid.setObjectName("HPGrid")

        self.hp_line1 = QtWidgets.QFrame()
        initialize_frame(self.hp_line1, "HPLine1", vertical=True)
        hp_grid.addWidget(self.hp_line1, 2, 2, 1, 1)
        self.hp_line2 = QtWidgets.QFrame()
        initialize_frame(self.hp_line2, "HPLine2", vertical=True)
        hp_grid.addWidget(self.hp_line2, 2, 4, 1, 1)
        self.hp_line3 = QtWidgets.QFrame()
        initialize_frame(self.hp_line3, "HPLine3", vertical=False)
        hp_grid.addWidget(self.hp_line3, 1, 0, 1, 6)

        self.hp_total_text = QtWidgets.QLabel()
        initialize_text(self.hp_total_text, "HPTotalText", "Total")
        hp_grid.addWidget(self.hp_total_text, 2, 0, 1, 1)
        self.sp_stamina_text = QtWidgets.QLabel()
        initialize_text(self.sp_stamina_text, "HPStaminaText", "Stamina Points")
        self.sp_stamina_text.setObjectName("HPStaminaText")
        self.sp_stamina_text.setText("Stamina Points")
        hp_grid.addWidget(self.sp_stamina_text, 0, 1, 1, 1)
        self.hp_hit_text = QtWidgets.QLabel()
        initialize_text(self.hp_hit_text, "HPHitText", "Hit Points")
        hp_grid.addWidget(self.hp_hit_text, 0, 3, 1, 1)
        self.hp_resolve_text = QtWidgets.QLabel()
        initialize_text(self.hp_resolve_text, "HPResolveText", "Resolve")
        hp_grid.addWidget(self.hp_resolve_text, 0, 5, 1, 1)

        self.hp_hit_box = QtWidgets.QLineEdit()
        initialize_edit(self.hp_hit_box, "HPHitBox", shape=[40, 25])
        hp_grid.addWidget(self.hp_hit_box, 2, 3, 1, 1)

        self.hp_resolve_box = QtWidgets.QLineEdit()
        initialize_edit(self.hp_resolve_box, "HPResolveBox", shape=[40, 25])
        hp_grid.addWidget(self.hp_resolve_box, 2, 5, 1, 1)
        self.hp_stamina_box = QtWidgets.QLineEdit()
        initialize_edit(self.hp_stamina_box, "HPStaminaBox", shape=[40, 25])
        hp_grid.addWidget(self.hp_stamina_box, 2, 1, 1, 1)

        self.widget.setLayout(hp_grid)

    def update_hp(self, stamina_points: int, hit_points: int, resolve_points: int):
        self.hp_stamina_box.setText(str(stamina_points))
        self.hp_hit_box.setText(str(hit_points))
        self.hp_resolve_box.setText(str(resolve_points))
