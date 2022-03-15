from PyQt5 import QtCore, QtGui, QtWidgets

from helpers.helper import (initialize_combo, initialize_combo_model,
                            initialize_edit, initialize_frame, initialize_text,
                            initialize_widget)


class SpellForm(QtWidgets.QWidget):
    """UI Class to display the character spells

    Args:
        QtWidgets (???): whatever this is
    """
    def __init__(self, character, parent=None):

        QtWidgets.QWidget.__init__(self, parent)
        self.setGeometry(0,0,1045,785)

        self.centralwidget = QtWidgets.QFrame()
        self.centralwidget.resize(821, 635)

        layout=QtWidgets.QVBoxLayout()
        layout.addWidget(self.centralwidget)
        self.setLayout(layout)
        self.setWindowTitle("Character Spells")

        self.character = character

        self.known_spells_text = QtWidgets.QLabel(self.centralwidget)
        self.known_spells_text.setGeometry(QtCore.QRect(210, 10, 77, 29))
        self.known_spells_text.setObjectName("known_spells_text")
        self.known_spells_text.setText("All Known Spells")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.frame, "frame", [10, 30, 1000, 120])
        self.grid_layout_widget = QtWidgets.QWidget(self.frame)
        initialize_widget(self.grid_layout_widget, "gridLayoutWidget", [5, 0, 990, 120])
        self.grid_layout = QtWidgets.QGridLayout(self.grid_layout_widget)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setObjectName("gridLayout")

        self.level_0_known_text = QtWidgets.QLabel(self.grid_layout_widget)
        initialize_text(self.level_0_known_text, "level_0_known_text", "0 - Level Spells Known")
        self.grid_layout.addWidget(self.level_0_known_text, 1, 0, 1, 1)
        self.level_0_known_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget)
        initialize_edit(self.level_0_known_box, "level_0_known_box", [25, 25])
        self.grid_layout.addWidget(self.level_0_known_box, 1, 1, 1, 1)
        self.level_0_box1 = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.level_0_box1, "level_0_box1", [], [184, 20])
        self.grid_layout.addWidget(self.level_0_box1, 2, 0, 1, 2)
        self.level_0_box2 = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.level_0_box2, "level_0_box2", [], [184, 20])
        self.grid_layout.addWidget(self.level_0_box2, 2, 2, 1, 1)
        self.level_0_box3 = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.level_0_box3, "level_0_box3", [], [184, 20])
        self.grid_layout.addWidget(self.level_0_box3, 2, 3, 1, 1)
        self.level_0_box4 = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.level_0_box4, "level_0_box4", [], [184, 20])
        self.grid_layout.addWidget(self.level_0_box4, 2, 4, 1, 1)
        self.level_0_box5 = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.level_0_box5, "level_0_box5", [], [184, 20])
        self.grid_layout.addWidget(self.level_0_box5, 2, 5, 1, 1)
        self.level_0_box6 = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.level_0_box6, "level_0_box6", [], [184, 20])
        self.grid_layout.addWidget(self.level_0_box6, 2, 6, 1, 1)
        self.level_0_box7 = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.level_0_box7, "level_0_box7", [], [184, 20])
        self.grid_layout.addWidget(self.level_0_box7, 3, 0, 1, 2)
        self.level_0_box8 = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.level_0_box8, "level_0_box8", [], [184, 20])
        self.grid_layout.addWidget(self.level_0_box8, 3, 2, 1, 1)
        self.level_0_box9 = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.level_0_box9, "level_0_box9", [], [184, 20])
        self.grid_layout.addWidget(self.level_0_box9, 3, 3, 1, 1)
        self.level_0_box10 = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.level_0_box10, "level_0_box10", [], [184, 20])
        self.grid_layout.addWidget(self.level_0_box10, 3, 4, 1, 1)
        self.level_0_box11 = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.level_0_box11, "level_0_box11", [], [184, 20])
        self.grid_layout.addWidget(self.level_0_box11, 3, 5, 1, 1)
        self.level_0_box12 = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.level_0_box12, "level_0_box12", [], [184, 20])
        self.grid_layout.addWidget(self.level_0_box12, 3, 6, 1, 1)
        self.level_0_box13 = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.level_0_box13, "level_0_box13", [], [184, 20])
        self.grid_layout.addWidget(self.level_0_box13, 4, 0, 1, 2)
        self.level_0_box14 = QtWidgets.QComboBox(self.grid_layout_widget)
        initialize_combo(self.level_0_box14, "level_0_box14", [], [184, 20])
        self.grid_layout.addWidget(self.level_0_box14, 4, 2, 1, 1)

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.frame_2, "frame_2", [10, 150, 1000, 100])
        self.grid_layout_widget_2 = QtWidgets.QWidget(self.frame_2)
        initialize_widget(self.grid_layout_widget_2, "gridLayoutWidget_2", [5, 0, 990, 100])
        self.grid_layout_2 = QtWidgets.QGridLayout(self.grid_layout_widget_2)
        self.grid_layout_2.setContentsMargins(0, 0, 0, 0)
        self.grid_layout_2.setObjectName("gridLayout_2")
        self.level_1_known_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.level_1_known_text, "level_1_known_text", "1st - Level Spells Known")
        self.grid_layout_2.addWidget(self.level_1_known_text, 1, 0, 1, 1)
        self.level_1_known_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_2)
        initialize_edit(self.level_1_known_box, "level_1_known_box", [25, 25])
        self.grid_layout_2.addWidget(self.level_1_known_box, 1, 1, 1, 1)
        self.level_1_per_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_2)
        initialize_edit(self.level_1_per_box, "level_1_per_box", [25, 25])
        self.grid_layout_2.addWidget(self.level_1_per_box, 1, 3, 1, 1)
        self.level_1_per_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        initialize_text(self.level_1_per_text, "level_1_per_text", "1st - Level Spells Per Day")
        self.grid_layout_2.addWidget(self.level_1_per_text, 1, 2, 1, 1)

        self.level_1_box1 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.level_1_box1, "level_1_box1", [], [184, 20])
        self.grid_layout_2.addWidget(self.level_1_box1, 2, 0, 1, 2)
        self.level_1_box2 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.level_1_box2, "level_1_box2", [], [184, 20])
        self.grid_layout_2.addWidget(self.level_1_box2, 2, 2, 1, 2)
        self.level_1_box3 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.level_0_box1, "level_1_box3", [], [184, 20])
        self.grid_layout_2.addWidget(self.level_1_box3, 2, 4, 1, 1)
        self.level_1_box4 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.level_1_box4, "level_1_box4", [], [184, 20])
        self.grid_layout_2.addWidget(self.level_1_box4, 2, 5, 1, 1)
        self.level_1_box5 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.level_1_box5, "level_1_box5", [], [184, 20])
        self.grid_layout_2.addWidget(self.level_1_box5, 2, 6, 1, 1)
        self.level_1_box6 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.level_1_box6, "level_1_box6", [], [184, 20])
        self.grid_layout_2.addWidget(self.level_1_box6, 2, 7, 1, 1)
        self.level_1_box7 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.level_1_box7, "level_1_box7", [], [184, 20])
        self.grid_layout_2.addWidget(self.level_1_box7, 3, 0, 1, 2)
        self.level_1_box8 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.level_1_box8, "level_1_box8", [], [184, 20])
        self.grid_layout_2.addWidget(self.level_1_box8, 3, 2, 1, 2)
        self.level_1_box9 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.level_1_box9, "level_1_box9", [], [184, 20])
        self.grid_layout_2.addWidget(self.level_1_box9, 3, 4, 1, 1)
        self.level_1_box10 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.level_1_box10, "level_1_box10", [], [184, 20])
        self.grid_layout_2.addWidget(self.level_1_box10, 3, 5, 1, 1)
        self.level_1_box11 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.level_1_box11, "level_1_box11", [], [184, 20])
        self.grid_layout_2.addWidget(self.level_1_box11, 3, 6, 1, 1)
        self.level_1_box12 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        initialize_combo(self.level_1_box12, "level_1_box12", [], [184, 20])
        self.grid_layout_2.addWidget(self.level_1_box12, 3, 7, 1, 1)

        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.frame_3, "frame_3", [10, 250, 1000, 100])
        self.grid_layout_widget_4 = QtWidgets.QWidget(self.frame_3)
        initialize_widget(self.grid_layout_widget_4, "gridLayoutWidget_4", [5, 0, 990, 100])
        self.grid_layout_4 = QtWidgets.QGridLayout(self.grid_layout_widget_4)
        self.grid_layout_4.setContentsMargins(0, 0, 0, 0)
        self.grid_layout_4.setObjectName("gridLayout_4")
        self.level_2_known_text = QtWidgets.QLabel(self.grid_layout_widget_4)
        initialize_text(self.level_2_known_text, "level_2_known_text", "2nd - Level Spells Known")
        self.grid_layout_4.addWidget(self.level_2_known_text, 1, 0, 1, 1)
        self.level_2_known_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_4)
        initialize_edit(self.level_2_known_box, "level_2_known_box", [25, 25])
        self.grid_layout_4.addWidget(self.level_2_known_box, 1, 1, 1, 1)
        self.level_2_per_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_4)
        initialize_edit(self.level_2_per_box, "level_2_per_box", [25, 25])
        self.grid_layout_4.addWidget(self.level_2_per_box, 1, 3, 1, 1)
        self.level_2_per_text = QtWidgets.QLabel(self.grid_layout_widget_4)
        initialize_text(self.level_2_per_text, "level_2_per_text", "2nd - Level Spells Known")
        self.grid_layout_4.addWidget(self.level_2_per_text, 1, 2, 1, 1)
        self.level_2_box1 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        initialize_combo(self.level_2_box1, "level_2_box1", [], [184, 20])
        self.grid_layout_4.addWidget(self.level_2_box1, 2, 0, 1, 2)
        self.level_2_box2 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        initialize_combo(self.level_2_box2, "level_2_box2", [], [184, 20])
        self.grid_layout_4.addWidget(self.level_2_box2, 2, 2, 1, 2)
        self.level_2_box3 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        initialize_combo(self.level_2_box3, "level_2_box3", [], [184, 20])
        self.grid_layout_4.addWidget(self.level_2_box3, 2, 4, 1, 1)
        self.level_2_box4 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        initialize_combo(self.level_2_box4, "level_2_box4", [], [184, 20])
        self.grid_layout_4.addWidget(self.level_2_box4, 2, 5, 1, 1)
        self.level_2_box5 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        initialize_combo(self.level_2_box5, "level_2_box5", [], [184, 20])
        self.grid_layout_4.addWidget(self.level_2_box5, 2, 6, 1, 1)
        self.level_2_box6 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        initialize_combo(self.level_2_box6, "level_2_box6", [], [184, 20])
        self.grid_layout_4.addWidget(self.level_2_box6, 2, 7, 1, 1)
        self.level_2_box7 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        initialize_combo(self.level_2_box7, "level_2_box7", [], [184, 20])
        self.grid_layout_4.addWidget(self.level_2_box7, 3, 0, 1, 2)
        self.level_2_box8 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        initialize_combo(self.level_2_box8, "level_2_box8", [], [184, 20])
        self.grid_layout_4.addWidget(self.level_2_box8, 3, 2, 1, 2)
        self.level_2_box9 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        initialize_combo(self.level_2_box9, "level_2_box9", [], [184, 20])
        self.grid_layout_4.addWidget(self.level_2_box9, 3, 4, 1, 1)
        self.level_2_box10 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        initialize_combo(self.level_2_box10, "level_2_box10", [], [184, 20])
        self.grid_layout_4.addWidget(self.level_2_box10, 3, 5, 1, 1)
        self.level_2_box11 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        initialize_combo(self.level_2_box11, "level_2_box11", [], [184, 20])
        self.grid_layout_4.addWidget(self.level_2_box11, 3, 6, 1, 1)
        self.level_2_box12 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        initialize_combo(self.level_2_box12, "level_2_box12", [], [184, 20])
        self.grid_layout_4.addWidget(self.level_2_box12, 3, 7, 1, 1)

        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.frame_4, "frame_4", [10, 350, 1000, 100])
        self.grid_layout_widget_5 = QtWidgets.QWidget(self.frame_4)
        initialize_widget(self.grid_layout_widget_5, "gridLayoutWidget_5", [5, 0, 990, 100])
        self.grid_layout_5 = QtWidgets.QGridLayout(self.grid_layout_widget_5)
        self.grid_layout_5.setContentsMargins(0, 0, 0, 0)
        self.grid_layout_5.setObjectName("gridLayout_5")
        self.level_3_known_text = QtWidgets.QLabel(self.grid_layout_widget_5)
        initialize_text(self.level_3_known_text, "level_3_known_text", "3rd - Level Spells Known")
        self.grid_layout_5.addWidget(self.level_3_known_text, 1, 0, 1, 1)
        self.level_3_known_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_5)
        initialize_edit(self.level_3_known_box, "level_3_known_box", [25, 25])
        self.grid_layout_5.addWidget(self.level_3_known_box, 1, 1, 1, 1)
        self.level_3_per_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_5)
        initialize_edit(self.level_3_per_box, "level_3_per_box", [25, 25])
        self.grid_layout_5.addWidget(self.level_3_per_box, 1, 3, 1, 1)
        self.level_3_per_text = QtWidgets.QLabel(self.grid_layout_widget_5)
        initialize_text(self.level_3_per_text, "level_3_per_text", "3rd - Level Spells Known")
        self.grid_layout_5.addWidget(self.level_3_per_text, 1, 2, 1, 1)
        self.level_3_box1 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.level_3_box1, "level_3_box1", [], [184, 20])
        self.grid_layout_5.addWidget(self.level_3_box1, 2, 0, 1, 2)
        self.level_3_box2 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.level_3_box2, "level_3_box2", [], [184, 20])
        self.grid_layout_5.addWidget(self.level_3_box2, 2, 2, 1, 2)
        self.level_3_box3 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.level_3_box3, "level_3_box3", [], [184, 20])
        self.grid_layout_5.addWidget(self.level_3_box3, 2, 4, 1, 1)
        self.level_3_box4 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.level_3_box4, "level_3_box4", [], [184, 20])
        self.grid_layout_5.addWidget(self.level_3_box4, 2, 5, 1, 1)
        self.level_3_box5 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.level_3_box5, "level_3_box5", [], [184, 20])
        self.grid_layout_5.addWidget(self.level_3_box5, 2, 6, 1, 1)
        self.level_3_box6 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.level_3_box6, "level_3_box6", [], [184, 20])
        self.grid_layout_5.addWidget(self.level_3_box6, 2, 7, 1, 1)
        self.level_3_box7 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.level_3_box7, "level_3_box7", [], [184, 20])
        self.grid_layout_5.addWidget(self.level_3_box7, 3, 0, 1, 2)
        self.level_3_box8 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.level_3_box8, "level_3_box8", [], [184, 20])
        self.grid_layout_5.addWidget(self.level_3_box8, 3, 2, 1, 2)
        self.level_3_box9 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.level_3_box9, "level_3_box9", [], [184, 20])
        self.grid_layout_5.addWidget(self.level_3_box9, 3, 4, 1, 1)
        self.level_3_box10 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.level_3_box10, "level_3_box10", [], [184, 20])
        self.grid_layout_5.addWidget(self.level_3_box10, 3, 5, 1, 1)
        self.level_3_box11 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.level_3_box11, "level_3_box11", [], [184, 20])
        self.grid_layout_5.addWidget(self.level_3_box11, 3, 6, 1, 1)
        self.level_3_box12 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        initialize_combo(self.level_3_box12, "level_3_box12", [], [184, 20])
        self.grid_layout_5.addWidget(self.level_3_box12, 3, 7, 1, 1)

        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.frame_5, "frame_5", [10, 450, 1000, 100])
        self.grid_layout_widget_6 = QtWidgets.QWidget(self.frame_5)
        initialize_widget(self.grid_layout_widget_6, "gridLayoutWidget_6", [5, 0, 990, 100])
        self.grid_layout_6 = QtWidgets.QGridLayout(self.grid_layout_widget_6)
        self.grid_layout_6.setContentsMargins(0, 0, 0, 0)
        self.grid_layout_6.setObjectName("gridLayout_6")
        self.level_4_known_text = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.level_4_known_text, "level_4_known_text", "4th - Level Spells Known")
        self.grid_layout_6.addWidget(self.level_4_known_text, 1, 0, 1, 1)
        self.level_4_known_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_6)
        initialize_edit(self.level_4_known_box, "level_4_known_box", [25, 25])
        self.grid_layout_6.addWidget(self.level_4_known_box, 1, 1, 1, 1)
        self.level_4_per_text = QtWidgets.QLabel(self.grid_layout_widget_6)
        initialize_text(self.level_4_per_text, "level_4_per_text", "4th - Level Spells Known")
        self.grid_layout_6.addWidget(self.level_4_per_text, 1, 2, 1, 1)
        self.level_4_per_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_6)
        initialize_edit(self.level_4_per_box, "level_4_per_box", [25, 25])
        self.grid_layout_6.addWidget(self.level_4_per_box, 1, 3, 1, 1)
        self.level_4_box1 = QtWidgets.QComboBox(self.grid_layout_widget_6)
        initialize_combo(self.level_4_box1, "level_4_box1", [], [184, 20])
        self.grid_layout_6.addWidget(self.level_4_box1, 2, 0, 1, 2)
        self.level_4_box2 = QtWidgets.QComboBox(self.grid_layout_widget_6)
        initialize_combo(self.level_4_box2, "level_4_box2", [], [184, 20])
        self.grid_layout_6.addWidget(self.level_4_box2, 2, 2, 1, 2)
        self.level_4_box3 = QtWidgets.QComboBox(self.grid_layout_widget_6)
        initialize_combo(self.level_4_box3, "level_4_box3", [], [184, 20])
        self.grid_layout_6.addWidget(self.level_4_box3, 2, 4, 1, 1)
        self.level_4_box4 = QtWidgets.QComboBox(self.grid_layout_widget_6)
        initialize_combo(self.level_4_box4, "level_4_box4", [], [184, 20])
        self.grid_layout_6.addWidget(self.level_4_box4, 2, 5, 1, 1)
        self.level_4_box5 = QtWidgets.QComboBox(self.grid_layout_widget_6)
        initialize_combo(self.level_4_box5, "level_4_box5", [], [184, 20])
        self.grid_layout_6.addWidget(self.level_4_box5, 2, 6, 1, 1)
        self.level_4_box6 = QtWidgets.QComboBox(self.grid_layout_widget_6)
        initialize_combo(self.level_4_box6, "level_4_box6", [], [184, 20])
        self.grid_layout_6.addWidget(self.level_4_box6, 2, 7, 1, 1)
        self.level_4_box7 = QtWidgets.QComboBox(self.grid_layout_widget_6)
        initialize_combo(self.level_4_box7, "level_4_box7", [], [184, 20])
        self.grid_layout_6.addWidget(self.level_4_box7, 3, 0, 1, 2)
        self.level_4_box8 = QtWidgets.QComboBox(self.grid_layout_widget_6)
        initialize_combo(self.level_4_box8, "level_4_box8", [], [184, 20])
        self.grid_layout_6.addWidget(self.level_4_box8, 3, 2, 1, 2)
        self.level_4_box9 = QtWidgets.QComboBox(self.grid_layout_widget_6)
        initialize_combo(self.level_4_box9, "level_4_box9", [], [184, 20])
        self.grid_layout_6.addWidget(self.level_4_box9, 3, 4, 1, 1)
        self.level_4_box10 = QtWidgets.QComboBox(self.grid_layout_widget_6)
        initialize_combo(self.level_4_box10, "level_4_box10", [], [184, 20])
        self.grid_layout_6.addWidget(self.level_4_box10, 3, 5, 1, 1)

        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.frame_6, "frame_6", [10, 550, 500, 120])
        self.grid_layout_widget_7 = QtWidgets.QWidget(self.frame_6)
        initialize_widget(self.grid_layout_widget_7, "gridLayoutWidget_7", [5, 0, 490, 120])
        self.grid_layout_7 = QtWidgets.QGridLayout(self.grid_layout_widget_7)
        self.grid_layout_7.setContentsMargins(0, 0, 0, 0)
        self.grid_layout_7.setObjectName("gridLayout_7")
        self.level_5_known_text = QtWidgets.QLabel(self.grid_layout_widget_7)
        initialize_text(self.level_5_known_text, "level_5_known_text", "5th - Level Spells Known")
        self.grid_layout_7.addWidget(self.level_5_known_text, 1, 0, 1, 1)
        self.level_5_known_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_7)
        initialize_edit(self.level_5_known_box, "level_5_known_box", [25, 25])
        self.grid_layout_7.addWidget(self.level_5_known_box, 1, 1, 1, 1)
        self.level_5_per_text = QtWidgets.QLabel(self.grid_layout_widget_7)
        initialize_text(self.level_5_per_text, "level_5_per_text", "5th - Level Spells Known")
        self.grid_layout_7.addWidget(self.level_5_per_text, 1, 2, 1, 1)
        self.level_5_per_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_7)
        initialize_edit(self.level_5_per_box, "level_5_per_box", [25, 25])
        self.grid_layout_7.addWidget(self.level_5_per_box, 1, 3, 1, 1)
        self.level_5_box1 = QtWidgets.QComboBox(self.grid_layout_widget_7)
        initialize_combo(self.level_5_box1, "level_5_box1", [], [184, 20])
        self.grid_layout_7.addWidget(self.level_5_box1, 2, 0, 1, 2)
        self.level_5_box2 = QtWidgets.QComboBox(self.grid_layout_widget_7)
        initialize_combo(self.level_5_box2, "level_5_box2", [], [184, 20])
        self.grid_layout_7.addWidget(self.level_5_box2, 2, 2, 1, 2)
        self.level_5_box3 = QtWidgets.QComboBox(self.grid_layout_widget_7)
        initialize_combo(self.level_5_box3, "level_5_box3", [], [184, 20])
        self.grid_layout_7.addWidget(self.level_5_box3, 2, 4, 1, 1)
        self.level_5_box4 = QtWidgets.QComboBox(self.grid_layout_widget_7)
        initialize_combo(self.level_5_box4, "level_5_box4", [], [184, 20])
        self.grid_layout_7.addWidget(self.level_5_box4, 3, 0, 1, 2)
        self.level_5_box5 = QtWidgets.QComboBox(self.grid_layout_widget_7)
        initialize_combo(self.level_5_box5, "level_5_box5", [], [184, 20])
        self.grid_layout_7.addWidget(self.level_5_box5, 3, 2, 1, 2)
        self.level_5_box6 = QtWidgets.QComboBox(self.grid_layout_widget_7)
        initialize_combo(self.level_5_box6, "level_5_box6", [], [184, 20])
        self.grid_layout_7.addWidget(self.level_5_box6, 3, 4, 1, 1)
        self.level_5_box7 = QtWidgets.QComboBox(self.grid_layout_widget_7)
        initialize_combo(self.level_5_box7, "level_5_box7", [], [184, 20])
        self.grid_layout_7.addWidget(self.level_5_box7, 4, 0, 1, 2)
        self.level_5_box8 = QtWidgets.QComboBox(self.grid_layout_widget_7)
        initialize_combo(self.level_5_box8, "level_5_box8", [], [184, 20])
        self.grid_layout_7.addWidget(self.level_5_box8, 4, 2, 1, 2)

        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        initialize_frame(self.frame_7, "frame_7", [510, 550, 500, 120])
        self.grid_layout_widget_8 = QtWidgets.QWidget(self.frame_7)
        initialize_widget(self.grid_layout_widget_8, "gridLayoutWidget_8", [5, 0, 490, 120])
        self.grid_layout_9 = QtWidgets.QGridLayout(self.grid_layout_widget_8)
        self.grid_layout_9.setContentsMargins(0, 0, 0, 0)
        self.grid_layout_9.setObjectName("gridLayout_9")

        self.level_6_known_text = QtWidgets.QLabel(self.grid_layout_widget_8)
        initialize_text(self.level_6_known_text, "level_6_known_text", "6th - Level Spells Known")
        self.grid_layout_9.addWidget(self.level_6_known_text, 1, 0, 1, 1)
        self.level_6_known_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_8)
        initialize_edit(self.level_6_known_box, "level_6_known_box", [25, 25])
        self.grid_layout_9.addWidget(self.level_6_known_box, 1, 1, 1, 1)
        self.level_6_per_text = QtWidgets.QLabel(self.grid_layout_widget_8)
        initialize_text(self.level_6_per_text, "level_6_per_text", "6th - Level Spells Known")
        self.grid_layout_9.addWidget(self.level_6_per_text, 1, 2, 1, 1)
        self.level_6_per_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_8)
        initialize_edit(self.level_6_per_box, "level_6_per_box", [25, 25])
        self.grid_layout_9.addWidget(self.level_6_per_box, 1, 3, 1, 1)
        self.level_6_box1 = QtWidgets.QComboBox(self.grid_layout_widget_8)
        initialize_combo(self.level_6_box1, "level_6_box1", [], [184, 20])
        self.grid_layout_9.addWidget(self.level_6_box1, 2, 0, 1, 2)
        self.level_6_box2 = QtWidgets.QComboBox(self.grid_layout_widget_8)
        initialize_combo(self.level_6_box2, "level_6_box2", [], [184, 20])
        self.grid_layout_9.addWidget(self.level_6_box2, 2, 2, 1, 2)
        self.level_6_box3 = QtWidgets.QComboBox(self.grid_layout_widget_8)
        initialize_combo(self.level_6_box3, "level_6_box3", [], [184, 20])
        self.grid_layout_9.addWidget(self.level_6_box3, 2, 4, 1, 1)
        self.level_6_box4 = QtWidgets.QComboBox(self.grid_layout_widget_8)
        initialize_combo(self.level_6_box4, "level_6_box4", [], [184, 20])
        self.grid_layout_9.addWidget(self.level_6_box4, 3, 0, 1, 2)
        self.level_6_box5 = QtWidgets.QComboBox(self.grid_layout_widget_8)
        initialize_combo(self.level_6_box5, "level_6_box5", [], [184, 20])
        self.grid_layout_9.addWidget(self.level_6_box5, 3, 2, 1, 2)
        self.level_6_box6 = QtWidgets.QComboBox(self.grid_layout_widget_8)
        initialize_combo(self.level_6_box6, "level_6_box6", [], [184, 20])
        self.grid_layout_9.addWidget(self.level_6_box6, 3, 4, 1, 1)
        self.level_6_box7 = QtWidgets.QComboBox(self.grid_layout_widget_8)
        initialize_combo(self.level_6_box7, "level_6_box7", [], [184, 20])
        self.grid_layout_9.addWidget(self.level_6_box7, 4, 0, 1, 2)
        self.level_6_box8 = QtWidgets.QComboBox(self.grid_layout_widget_8)
        initialize_combo(self.level_6_box8, "level_6_box8", [], [184, 20])
        self.grid_layout_9.addWidget(self.level_6_box8, 4, 2, 1, 2)

        QtCore.QMetaObject.connectSlotsByName(self.centralwidget)

    def update_level0_spells(self):
        pass
