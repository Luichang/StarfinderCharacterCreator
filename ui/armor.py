from PyQt5 import QtWidgets

from helpers.helper import initialize_text, initialize_edit, initialize_frame

class Armor:
    def __init__(self) -> None:
        self.widget = QtWidgets.QWidget()

        ac_grid = QtWidgets.QGridLayout()
        ac_grid.setContentsMargins(0, 0, 0, 0)
        ac_grid.setObjectName("ACGrid")

        self.armor_line1 = QtWidgets.QFrame()
        initialize_frame(self.armor_line1, "ArmorLine1", vertical=False)
        self.armor_line2 = QtWidgets.QFrame()
        initialize_frame(self.armor_line2, "ArmorLine2", vertical=False)

        self.eac_text = QtWidgets.QLabel()
        initialize_text(self.eac_text, "EACText", "Energy Armor Class (EAC)")
        self.kac_text = QtWidgets.QLabel()
        initialize_text(self.kac_text, "KACText", "Kinetic Armor Class (KAC)")
        self.acvs_text = QtWidgets.QLabel()
        initialize_text(self.acvs_text, "ACVSText", "AC VS Combat Maneuvers")
        self.ac_total_text = QtWidgets.QLabel()
        initialize_text(self.ac_total_text, "ACTotalText", "Total")
        self.ac_armor_text = QtWidgets.QLabel()
        initialize_text(self.ac_armor_text, "ACArmorText", "Armor Bonus")
        self.ac_dex_text = QtWidgets.QLabel()
        initialize_text(self.ac_dex_text, "ACDexText", "Dex Mod")
        self.ac_misc_text = QtWidgets.QLabel()
        initialize_text(self.ac_misc_text, "ACMiscText", "MiscMod")

        self.eac_plus = QtWidgets.QLabel()
        initialize_text(self.eac_plus, "EACPlus", "+", max_size=[10, 25])
        self.eac_plus_2 = QtWidgets.QLabel()
        initialize_text(self.eac_plus_2, "EACPlus_2", "+", max_size=[10, 25])
        self.eac_equals = QtWidgets.QLabel()
        initialize_text(self.eac_equals, "EACEquals", "= 10 +", max_size=[40, 25])
        self.kac_plus = QtWidgets.QLabel()
        initialize_text(self.kac_plus, "KACPlus", "+", max_size=[10, 25])
        self.kac_plus_2 = QtWidgets.QLabel()
        initialize_text(self.kac_plus_2, "KACPlus_2", "+", max_size=[10, 25])
        self.kac_equals = QtWidgets.QLabel()
        initialize_text(self.kac_equals, "KACEquals", "= 10 +", max_size=[40, 25])
        self.acvs_equals = QtWidgets.QLabel()
        initialize_text(self.acvs_equals, "ACVSEquals", "= 8 +", max_size=[40, 25])

        self.eac_total_box = QtWidgets.QLineEdit()
        initialize_edit(self.eac_total_box, "EACTotalBox", shape=[40, 25])
        self.eac_armor_box = QtWidgets.QLineEdit()
        initialize_edit(self.eac_armor_box, "EACArmorBox", shape=[40, 25])
        self.eac_dex_box = QtWidgets.QLineEdit()
        initialize_edit(self.eac_dex_box, "EACDexBox", shape=[40, 25])
        self.eac_misc_box = QtWidgets.QLineEdit()
        initialize_edit(self.eac_misc_box, "EACMiscBox", shape=[40, 25])
        self.kac_total_box = QtWidgets.QLineEdit()
        initialize_edit(self.kac_total_box, "KACTotalBox", shape=[40, 25])
        self.kac_armor_box = QtWidgets.QLineEdit()
        initialize_edit(self.kac_armor_box, "KACArmorBox", shape=[40, 25])
        self.kac_dex_box = QtWidgets.QLineEdit()
        initialize_edit(self.kac_dex_box, "KACDexBox", shape=[40, 25])
        self.kac_misc_box = QtWidgets.QLineEdit()
        initialize_edit(self.kac_misc_box, "KACMiscBox", shape=[40, 25])
        self.acvs_total_box = QtWidgets.QLineEdit()
        initialize_edit(self.acvs_total_box, "ACVSTotalBox", shape=[40, 25])
        self.acvs_kac_box = QtWidgets.QLineEdit()
        initialize_edit(self.acvs_kac_box, "ACVSKACBox", shape=[40, 25])

        ac_grid.addWidget(self.armor_line1, 3, 0, 1, 8)
        ac_grid.addWidget(self.armor_line2, 5, 0, 1, 8)

        ac_grid.addWidget(self.eac_text, 2, 0, 1, 1)
        ac_grid.addWidget(self.kac_text, 4, 0, 1, 1)
        ac_grid.addWidget(self.acvs_text, 6, 0, 1, 1)
        ac_grid.addWidget(self.ac_total_text, 0, 1, 1, 1)
        ac_grid.addWidget(self.ac_armor_text, 0, 3, 1, 1)
        ac_grid.addWidget(self.ac_dex_text, 0, 5, 1, 1)
        ac_grid.addWidget(self.ac_misc_text, 0, 7, 1, 1)

        ac_grid.addWidget(self.eac_plus, 2, 4, 1, 1)
        ac_grid.addWidget(self.eac_plus_2, 2, 6, 1, 1)
        ac_grid.addWidget(self.eac_equals, 2, 2, 1, 1)
        ac_grid.addWidget(self.kac_plus, 4, 4, 1, 1)
        ac_grid.addWidget(self.kac_plus_2, 4, 6, 1, 1)
        ac_grid.addWidget(self.kac_equals, 4, 2, 1, 1)
        ac_grid.addWidget(self.acvs_equals, 6, 2, 1, 1)

        ac_grid.addWidget(self.eac_total_box, 2, 1, 1, 1)
        ac_grid.addWidget(self.eac_armor_box, 2, 3, 1, 1)
        ac_grid.addWidget(self.eac_dex_box, 2, 5, 1, 1)
        ac_grid.addWidget(self.eac_misc_box, 2, 7, 1, 1)
        ac_grid.addWidget(self.kac_total_box, 4, 1, 1, 1)
        ac_grid.addWidget(self.kac_armor_box, 4, 3, 1, 1)
        ac_grid.addWidget(self.kac_dex_box, 4, 5, 1, 1)
        ac_grid.addWidget(self.kac_misc_box, 4, 7, 1, 1)
        ac_grid.addWidget(self.acvs_total_box, 6, 1, 1, 1)
        ac_grid.addWidget(self.acvs_kac_box, 6, 3, 1, 1)

        self.widget.setLayout(ac_grid)

    def update_ac(self, skills):
        """update ac tab related boxes
        """
        boxes = [self.eac_total_box, self.eac_armor_box, self.eac_dex_box, self.eac_misc_box,
                 self.kac_total_box, self.kac_armor_box, self.kac_dex_box, self.kac_misc_box,
                 self.acvs_total_box, self.acvs_kac_box]
        for skill, box in zip(skills, boxes):
            box.setText(str(skill))
