from PyQt5 import QtCore, QtGui, QtWidgets

import os
import sys


sys.path.append(os.path.abspath("."))

from helpers.helper import (initialize_combo, initialize_combo_model,
                            initialize_edit, initialize_frame, initialize_text,
                            initialize_widget)
from character_classes.character import Character
from helpers.ProxyModel import ProxyModel
from helpers.starfinder_dicts import spells_day, spells_known
from starfinder_feats.starfinder_spell import Spell
from starfinder_feats.starfinder_spells import (spells, spells_by_class,
                                                spells_by_level)


class Spells0(QtWidgets.QFrame):
    def __init__(self, centralwidget):
        super().__init__(centralwidget)
        initialize_frame(self, "frame", [10, 30, 1000, 120])
        self.grid_layout_widget = QtWidgets.QWidget(self)
        initialize_widget(self.grid_layout_widget, "gridLayoutWidget", [5, 0, 990, 120])
        self.grid_layout = QtWidgets.QGridLayout(self.grid_layout_widget)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setObjectName("gridLayout")

        self.level_0_known_text = QtWidgets.QLabel(self.grid_layout_widget)
        self.level_0_known_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget)

        initialize_text(self.level_0_known_text, "level_0_known_text", "0 - Level Spells Known")
        initialize_edit(self.level_0_known_box, "level_0_known_box", [25, 25])

        self.grid_layout.addWidget(self.level_0_known_text, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.level_0_known_box, 1, 1, 1, 1)

        self.level_0_box1 = QtWidgets.QComboBox(self.grid_layout_widget)
        self.level_0_box2 = QtWidgets.QComboBox(self.grid_layout_widget)
        self.level_0_box3 = QtWidgets.QComboBox(self.grid_layout_widget)
        self.level_0_box4 = QtWidgets.QComboBox(self.grid_layout_widget)
        self.level_0_box5 = QtWidgets.QComboBox(self.grid_layout_widget)
        self.level_0_box6 = QtWidgets.QComboBox(self.grid_layout_widget)
        self.level_0_box7 = QtWidgets.QComboBox(self.grid_layout_widget)
        self.level_0_box8 = QtWidgets.QComboBox(self.grid_layout_widget)
        self.level_0_box9 = QtWidgets.QComboBox(self.grid_layout_widget)
        self.level_0_box10 = QtWidgets.QComboBox(self.grid_layout_widget)
        self.level_0_box11 = QtWidgets.QComboBox(self.grid_layout_widget)
        self.level_0_box12 = QtWidgets.QComboBox(self.grid_layout_widget)
        self.level_0_box13 = QtWidgets.QComboBox(self.grid_layout_widget)
        self.level_0_box14 = QtWidgets.QComboBox(self.grid_layout_widget)

        comboboxes = [self.level_0_box1, self.level_0_box2, self.level_0_box3, self.level_0_box4,
                      self.level_0_box5, self.level_0_box6, self.level_0_box7, self.level_0_box8,
                      self.level_0_box9, self.level_0_box10, self.level_0_box11, self.level_0_box12,
                      self.level_0_box13, self.level_0_box14]

        
        j = 2
        k = 0
        l = 2
        for i, combobox in enumerate(comboboxes):
            initialize_combo(combobox, f"level_0_box{i}", [], [184, 20])
            self.grid_layout.addWidget(combobox, j, k, 1, l)
            k = (k + 1) % 7
            l = 1
            if k == 0:
                j += 1
                l = 2
            if k == 1:
                k = (k + 1)

class Spells1(QtWidgets.QFrame):
    def __init__(self, centralwidget):
        super().__init__(centralwidget)
        self.grid_layout_widget_2 = QtWidgets.QWidget(self)
        self.grid_layout_2 = QtWidgets.QGridLayout(self.grid_layout_widget_2)
        self.grid_layout_2.setContentsMargins(0, 0, 0, 0)
        self.grid_layout_2.setObjectName("gridLayout_2")
        self.level_1_known_text = QtWidgets.QLabel(self.grid_layout_widget_2)
        self.level_1_known_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_2)
        self.level_1_per_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_2)
        self.level_1_per_text = QtWidgets.QLabel(self.grid_layout_widget_2)

        initialize_frame(self, "frame_2", [10, 150, 1000, 100])
        initialize_widget(self.grid_layout_widget_2, "gridLayoutWidget_2", [5, 0, 990, 100])
        initialize_text(self.level_1_known_text, "level_1_known_text", "1st - Level Spells Known")
        initialize_edit(self.level_1_known_box, "level_1_known_box", [25, 25])
        initialize_text(self.level_1_per_text, "level_1_per_text", "1st - Level Spells Per Day")
        initialize_edit(self.level_1_per_box, "level_1_per_box", [25, 25])

        self.grid_layout_2.addWidget(self.level_1_known_text, 1, 0, 1, 1)
        self.grid_layout_2.addWidget(self.level_1_known_box, 1, 1, 1, 1)
        self.grid_layout_2.addWidget(self.level_1_per_text, 1, 2, 1, 1)
        self.grid_layout_2.addWidget(self.level_1_per_box, 1, 3, 1, 1)

        self.level_1_box1 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.level_1_box2 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.level_1_box3 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.level_1_box4 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.level_1_box5 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.level_1_box6 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.level_1_box7 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.level_1_box8 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.level_1_box9 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.level_1_box10 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.level_1_box11 = QtWidgets.QComboBox(self.grid_layout_widget_2)
        self.level_1_box12 = QtWidgets.QComboBox(self.grid_layout_widget_2)

        comboboxes = [self.level_1_box1, self.level_1_box2, self.level_1_box3, self.level_1_box4,
                      self.level_1_box5, self.level_1_box6, self.level_1_box7, self.level_1_box8,
                      self.level_1_box9, self.level_1_box10, self.level_1_box11, self.level_1_box12]

        j = 2
        k = 0
        l = 2
        for i, combobox in enumerate(comboboxes):
            initialize_combo(combobox, f"level_1_box{i}", [], [184, 20])
            self.grid_layout_2.addWidget(combobox, j, k, 1, l)
            k = (k + 1) % 8
            l = 1
            if k == 0:
                j += 1
            if k in (0, 1):
                l = 2
            if k in (1, 3):
                k = (k + 1)

class Spells2(QtWidgets.QFrame):
    def __init__(self, centralwidget):
        super().__init__(centralwidget)
        initialize_frame(self, "frame_3", [10, 250, 1000, 100])
        self.grid_layout_widget_4 = QtWidgets.QWidget(self)
        initialize_widget(self.grid_layout_widget_4, "gridLayoutWidget_4", [5, 0, 990, 100])
        self.grid_layout_4 = QtWidgets.QGridLayout(self.grid_layout_widget_4)
        self.grid_layout_4.setContentsMargins(0, 0, 0, 0)
        self.grid_layout_4.setObjectName("gridLayout_4")

        self.level_2_known_text = QtWidgets.QLabel(self.grid_layout_widget_4)
        self.level_2_known_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_4)
        self.level_2_per_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_4)
        self.level_2_per_text = QtWidgets.QLabel(self.grid_layout_widget_4)

        initialize_text(self.level_2_known_text, "level_2_known_text", "2nd - Level Spells Known")
        initialize_edit(self.level_2_known_box, "level_2_known_box", [25, 25])
        initialize_text(self.level_2_per_text, "level_2_per_text", "2nd - Level Spells Known")
        initialize_edit(self.level_2_per_box, "level_2_per_box", [25, 25])

        self.grid_layout_4.addWidget(self.level_2_known_text, 1, 0, 1, 1)
        self.grid_layout_4.addWidget(self.level_2_known_box, 1, 1, 1, 1)
        self.grid_layout_4.addWidget(self.level_2_per_text, 1, 2, 1, 1)
        self.grid_layout_4.addWidget(self.level_2_per_box, 1, 3, 1, 1)

        self.level_2_box1 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        self.level_2_box2 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        self.level_2_box3 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        self.level_2_box4 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        self.level_2_box5 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        self.level_2_box6 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        self.level_2_box7 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        self.level_2_box8 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        self.level_2_box9 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        self.level_2_box10 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        self.level_2_box11 = QtWidgets.QComboBox(self.grid_layout_widget_4)
        self.level_2_box12 = QtWidgets.QComboBox(self.grid_layout_widget_4)

        comboboxes = [self.level_2_box1, self.level_2_box2, self.level_2_box3, self.level_2_box4,
                      self.level_2_box5, self.level_2_box6, self.level_2_box7, self.level_2_box8,
                      self.level_2_box9, self.level_2_box10, self.level_2_box11, self.level_2_box12]

        j = 2
        k = 0
        l = 2
        for i, combobox in enumerate(comboboxes):
            initialize_combo(combobox, f"level_2_box{i}", [], [184, 20])
            self.grid_layout_4.addWidget(combobox, j, k, 1, l)
            k = (k + 1) % 8
            l = 1
            if k == 0:
                j += 1
            if k in (0, 1):
                l = 2
            if k in (1, 3):
                k = (k + 1)

class Spells3(QtWidgets.QFrame):
    def __init__(self, centralwidget):
        super().__init__(centralwidget)
        initialize_frame(self, "frame_4", [10, 350, 1000, 100])
        self.grid_layout_widget_5 = QtWidgets.QWidget(self)
        initialize_widget(self.grid_layout_widget_5, "gridLayoutWidget_5", [5, 0, 990, 100])
        self.grid_layout_5 = QtWidgets.QGridLayout(self.grid_layout_widget_5)
        self.grid_layout_5.setContentsMargins(0, 0, 0, 0)
        self.grid_layout_5.setObjectName("gridLayout_5")

        self.level_3_known_text = QtWidgets.QLabel(self.grid_layout_widget_5)
        self.level_3_known_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_5)
        self.level_3_per_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_5)
        self.level_3_per_text = QtWidgets.QLabel(self.grid_layout_widget_5)

        initialize_text(self.level_3_known_text, "level_3_known_text", "3rd - Level Spells Known")
        initialize_edit(self.level_3_known_box, "level_3_known_box", [25, 25])
        initialize_text(self.level_3_per_text, "level_3_per_text", "3rd - Level Spells Known")
        initialize_edit(self.level_3_per_box, "level_3_per_box", [25, 25])

        self.grid_layout_5.addWidget(self.level_3_known_text, 1, 0, 1, 1)
        self.grid_layout_5.addWidget(self.level_3_known_box, 1, 1, 1, 1)
        self.grid_layout_5.addWidget(self.level_3_per_text, 1, 2, 1, 1)
        self.grid_layout_5.addWidget(self.level_3_per_box, 1, 3, 1, 1)

        self.level_3_box1 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.level_3_box2 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.level_3_box3 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.level_3_box4 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.level_3_box5 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.level_3_box6 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.level_3_box7 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.level_3_box8 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.level_3_box9 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.level_3_box10 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.level_3_box11 = QtWidgets.QComboBox(self.grid_layout_widget_5)
        self.level_3_box12 = QtWidgets.QComboBox(self.grid_layout_widget_5)

        comboboxes = [self.level_3_box1, self.level_3_box2, self.level_3_box3, self.level_3_box4,
                      self.level_3_box5, self.level_3_box6, self.level_3_box7, self.level_3_box8,
                      self.level_3_box9, self.level_3_box10, self.level_3_box11, self.level_3_box12]

        j = 2
        k = 0
        l = 2
        for i, combobox in enumerate(comboboxes):
            initialize_combo(combobox, f"level_2_box{i}", [], [184, 20])
            self.grid_layout_5.addWidget(combobox, j, k, 1, l)
            k = (k + 1) % 8
            l = 1
            if k == 0:
                j += 1
            if k in (0, 1):
                l = 2
            if k in (1, 3):
                k = (k + 1)

class Spells4(QtWidgets.QFrame):
    def __init__(self, centralwidget):
        super().__init__(centralwidget)
        initialize_frame(self, "frame_5", [10, 450, 1000, 100])
        self.grid_layout_widget_6 = QtWidgets.QWidget(self)
        initialize_widget(self.grid_layout_widget_6, "gridLayoutWidget_6", [5, 0, 990, 100])
        self.grid_layout_6 = QtWidgets.QGridLayout(self.grid_layout_widget_6)
        self.grid_layout_6.setContentsMargins(0, 0, 0, 0)
        self.grid_layout_6.setObjectName("gridLayout_6")

        self.level_4_known_text = QtWidgets.QLabel(self.grid_layout_widget_6)
        self.level_4_known_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_6)
        self.level_4_per_text = QtWidgets.QLabel(self.grid_layout_widget_6)
        self.level_4_per_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_6)

        initialize_text(self.level_4_known_text, "level_4_known_text", "4th - Level Spells Known")
        initialize_edit(self.level_4_known_box, "level_4_known_box", [25, 25])
        initialize_text(self.level_4_per_text, "level_4_per_text", "4th - Level Spells Known")
        initialize_edit(self.level_4_per_box, "level_4_per_box", [25, 25])

        self.grid_layout_6.addWidget(self.level_4_known_text, 1, 0, 1, 1)
        self.grid_layout_6.addWidget(self.level_4_known_box, 1, 1, 1, 1)
        self.grid_layout_6.addWidget(self.level_4_per_text, 1, 2, 1, 1)
        self.grid_layout_6.addWidget(self.level_4_per_box, 1, 3, 1, 1)

        self.level_4_box1 = QtWidgets.QComboBox(self.grid_layout_widget_6)
        self.level_4_box2 = QtWidgets.QComboBox(self.grid_layout_widget_6)
        self.level_4_box3 = QtWidgets.QComboBox(self.grid_layout_widget_6)
        self.level_4_box4 = QtWidgets.QComboBox(self.grid_layout_widget_6)
        self.level_4_box5 = QtWidgets.QComboBox(self.grid_layout_widget_6)
        self.level_4_box6 = QtWidgets.QComboBox(self.grid_layout_widget_6)
        self.level_4_box7 = QtWidgets.QComboBox(self.grid_layout_widget_6)
        self.level_4_box8 = QtWidgets.QComboBox(self.grid_layout_widget_6)
        self.level_4_box9 = QtWidgets.QComboBox(self.grid_layout_widget_6)
        self.level_4_box10 = QtWidgets.QComboBox(self.grid_layout_widget_6)

        comboboxes = [self.level_4_box1, self.level_4_box2, self.level_4_box3, self.level_4_box4,
                      self.level_4_box5, self.level_4_box6, self.level_4_box7, self.level_4_box8,
                      self.level_4_box9, self.level_4_box10]

        j = 2
        k = 0
        l = 2
        for i, combobox in enumerate(comboboxes):
            initialize_combo(combobox, f"level_2_box{i}", [], [184, 20])
            self.grid_layout_6.addWidget(combobox, j, k, 1, l)
            k = (k + 1) % 8
            l = 1
            if k == 0:
                j += 1
            if k in (0, 1):
                l = 2
            if k in (1, 3):
                k = (k + 1)

class Spells5(QtWidgets.QFrame):
    def __init__(self, centralwidget):
        super().__init__(centralwidget)
        initialize_frame(self, "frame_6", [10, 550, 500, 120])
        self.grid_layout_widget_7 = QtWidgets.QWidget(self)
        initialize_widget(self.grid_layout_widget_7, "gridLayoutWidget_7", [5, 0, 490, 120])
        self.grid_layout_7 = QtWidgets.QGridLayout(self.grid_layout_widget_7)
        self.grid_layout_7.setContentsMargins(0, 0, 0, 0)
        self.grid_layout_7.setObjectName("gridLayout_7")

        self.level_5_known_text = QtWidgets.QLabel(self.grid_layout_widget_7)
        self.level_5_known_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_7)
        self.level_5_per_text = QtWidgets.QLabel(self.grid_layout_widget_7)
        self.level_5_per_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_7)

        initialize_text(self.level_5_known_text, "level_5_known_text", "5th - Level Spells Known")
        initialize_edit(self.level_5_known_box, "level_5_known_box", [25, 25])
        initialize_text(self.level_5_per_text, "level_5_per_text", "5th - Level Spells Known")
        initialize_edit(self.level_5_per_box, "level_5_per_box", [25, 25])

        self.grid_layout_7.addWidget(self.level_5_known_text, 1, 0, 1, 1)
        self.grid_layout_7.addWidget(self.level_5_known_box, 1, 1, 1, 1)
        self.grid_layout_7.addWidget(self.level_5_per_text, 1, 2, 1, 1)
        self.grid_layout_7.addWidget(self.level_5_per_box, 1, 3, 1, 1)

        self.level_5_box1 = QtWidgets.QComboBox(self.grid_layout_widget_7)
        self.level_5_box2 = QtWidgets.QComboBox(self.grid_layout_widget_7)
        self.level_5_box3 = QtWidgets.QComboBox(self.grid_layout_widget_7)
        self.level_5_box4 = QtWidgets.QComboBox(self.grid_layout_widget_7)
        self.level_5_box5 = QtWidgets.QComboBox(self.grid_layout_widget_7)
        self.level_5_box6 = QtWidgets.QComboBox(self.grid_layout_widget_7)
        self.level_5_box7 = QtWidgets.QComboBox(self.grid_layout_widget_7)
        self.level_5_box8 = QtWidgets.QComboBox(self.grid_layout_widget_7)

        comboboxes = [self.level_5_box1, self.level_5_box2, self.level_5_box3, self.level_5_box4,
                      self.level_5_box5, self.level_5_box6, self.level_5_box7, self.level_5_box8]

        j = 2
        k = 0
        l = 2
        for i, combobox in enumerate(comboboxes):
            initialize_combo(combobox, f"level_2_box{i}", [], [184, 20])
            self.grid_layout_7.addWidget(combobox, j, k, 1, l)
            k = (k + 2) % 6
            l = 2
            if k == 0:
                j += 1
            if k == 4:
                l = 1

class Spells6(QtWidgets.QFrame):
    def __init__(self, centralwidget):
        super().__init__(centralwidget)
        initialize_frame(self, "frame_7", [510, 550, 500, 120])
        self.grid_layout_widget_8 = QtWidgets.QWidget(self)
        initialize_widget(self.grid_layout_widget_8, "gridLayoutWidget_8", [5, 0, 490, 120])
        self.grid_layout_9 = QtWidgets.QGridLayout(self.grid_layout_widget_8)
        self.grid_layout_9.setContentsMargins(0, 0, 0, 0)
        self.grid_layout_9.setObjectName("gridLayout_9")

        self.level_6_known_text = QtWidgets.QLabel(self.grid_layout_widget_8)
        self.level_6_known_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_8)
        self.level_6_per_text = QtWidgets.QLabel(self.grid_layout_widget_8)
        self.level_6_per_box = QtWidgets.QPlainTextEdit(self.grid_layout_widget_8)

        initialize_text(self.level_6_known_text, "level_6_known_text", "6th - Level Spells Known")
        initialize_edit(self.level_6_known_box, "level_6_known_box", [25, 25])
        initialize_text(self.level_6_per_text, "level_6_per_text", "6th - Level Spells Known")
        initialize_edit(self.level_6_per_box, "level_6_per_box", [25, 25])

        self.grid_layout_9.addWidget(self.level_6_known_text, 1, 0, 1, 1)
        self.grid_layout_9.addWidget(self.level_6_known_box, 1, 1, 1, 1)
        self.grid_layout_9.addWidget(self.level_6_per_text, 1, 2, 1, 1)
        self.grid_layout_9.addWidget(self.level_6_per_box, 1, 3, 1, 1)

        self.level_6_box1 = QtWidgets.QComboBox(self.grid_layout_widget_8)
        self.level_6_box2 = QtWidgets.QComboBox(self.grid_layout_widget_8)
        self.level_6_box3 = QtWidgets.QComboBox(self.grid_layout_widget_8)
        self.level_6_box4 = QtWidgets.QComboBox(self.grid_layout_widget_8)
        self.level_6_box5 = QtWidgets.QComboBox(self.grid_layout_widget_8)
        self.level_6_box6 = QtWidgets.QComboBox(self.grid_layout_widget_8)
        self.level_6_box7 = QtWidgets.QComboBox(self.grid_layout_widget_8)
        self.level_6_box8 = QtWidgets.QComboBox(self.grid_layout_widget_8)

        comboboxes = [self.level_6_box1, self.level_6_box2, self.level_6_box3, self.level_6_box4,
                      self.level_6_box5, self.level_6_box6, self.level_6_box7, self.level_6_box8]

        j = 2
        k = 0
        l = 2
        for i, combobox in enumerate(comboboxes):
            initialize_combo(combobox, f"level_2_box{i}", [], [184, 20])
            self.grid_layout_9.addWidget(combobox, j, k, 1, l)
            k = (k + 2) % 6
            l = 2
            if k == 0:
                j += 1
            if k == 4:
                l = 1

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

        self.frame = Spells0(self.centralwidget)
        self.frame_2 = Spells1(self.centralwidget)
        self.frame_3 = Spells2(self.centralwidget)
        self.frame_4 = Spells3(self.centralwidget)
        self.frame_5 = Spells4(self.centralwidget)
        self.frame_6 = Spells5(self.centralwidget)
        self.frame_7 = Spells6(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(self.centralwidget)
        self.choose_level0 = []
        self.choose_level1 = []
        self.choose_level2 = []
        self.choose_level3 = []
        self.choose_level4 = []
        self.choose_level5 = []
        self.choose_level6 = []

    #     if self.character.spell_level > -1:
    #         self.initialize_spells()
    #         self.spell_dict = {}
    #         self.update_spell_dict(spells)

    # def update_spell_dict(self, new_spell : list[Spell]) -> None:
    #     """Function to keep the spell dict updated

    #     Args:
    #         new_spell (Ability): Spell that is to be checked if it already is in the dict
    #     """
    #     if not isinstance(new_spell, list):
    #         new_spell = [new_spell]

    #     for spell in new_spell:
    #         try:
    #             self.spell_dict[str(spell)]
    #         except KeyError:
    #             self.spell_dict[str(spell)] = spell

    # def initialize_spells(self):
    #     """function to initialize the level 0 spell boxes
    #     """
    #     boxes = [[self.level_0_box1, self.level_0_box2, self.level_0_box3, self.level_0_box4,
    #                   self.level_0_box5, self.level_0_box6, self.level_0_box7, self.level_0_box8,
    #                   self.level_0_box9, self.level_0_box10, self.level_0_box11,self.level_0_box12,
    #                   self.level_0_box13, self.level_0_box14
    #                  ],
    #                  [self.level_1_box1, self.level_1_box2, self.level_1_box3, self.level_1_box4,
    #                   self.level_1_box5, self.level_1_box6, self.level_1_box7, self.level_1_box8,
    #                   self.level_1_box9, self.level_1_box10, self.level_1_box11,self.level_1_box12
    #                  ],
    #                  [self.level_2_box1, self.level_2_box2, self.level_2_box3, self.level_2_box4,
    #                   self.level_2_box5, self.level_2_box6, self.level_2_box7, self.level_2_box8,
    #                   self.level_2_box9, self.level_2_box10, self.level_2_box11,self.level_2_box12
    #                  ],
    #                  [self.level_3_box1, self.level_3_box2, self.level_3_box3, self.level_3_box4,
    #                   self.level_3_box5, self.level_3_box6, self.level_3_box7, self.level_3_box8,
    #                   self.level_3_box9, self.level_3_box10, self.level_3_box11,self.level_3_box12
    #                  ],
    #                  [self.level_4_box1, self.level_4_box2, self.level_4_box3, self.level_4_box4,
    #                   self.level_4_box5, self.level_4_box6, self.level_4_box7, self.level_4_box8,
    #                   self.level_4_box9, self.level_4_box10
    #                  ],
    #                  [self.level_5_box1, self.level_5_box2, self.level_5_box3, self.level_5_box4,
    #                   self.level_5_box5, self.level_5_box6, self.level_5_box7, self.level_5_box8
    #                  ],
    #                  [self.level_6_box1, self.level_6_box2, self.level_6_box3, self.level_6_box4,
    #                   self.level_6_box5, self.level_6_box6, self.level_6_box7, self.level_6_box8
    #                  ]]

    #     chosen = [self.choose_level0, self.choose_level1, self.choose_level2, self.choose_level3,
    #               self.choose_level4, self.choose_level5, self.choose_level6]


    #     for i in range(7):
    #         boxcount = 0

    #         for spell in self.character.additional_spells[i]:
    #             # if we look at additional_spells[1] we need to check if spell name is MYSTICSPELL
    #             if not isinstance(spell, list):
    #                 initialize_combo_model(boxes[i][boxcount], [spell], "<<Fixed Spell>>",
    #                                         index=1)
    #             else:
    #                 model_default = "<<Select Priest Spell>>"
    #                 mystic_spells = spells_by_class(spells, "Mystic")
    #                 possible_spells = spells_by_level(mystic_spells, 1)
    #                 self.initialize_combobox(boxes[i][boxcount],
    #                                          model_default,
    #                                          possible_spells,
    #                                          "additional")
    #                 index = self.character.additional_spells[i].index(spell)
    #                 self.character.additional_spells[i][index] = possible_spells[0]
    #                 chosen[i].append(boxes[i][boxcount])
    #                 self.update_spell_boxes(i, chosen[i])
    #                 boxes[i][boxcount].setProperty("model_default", model_default)
    #             boxcount += 1


    #     known_boxes = [self.level_0_known_box, self.level_1_known_box, self.level_2_known_box,
    #                    self.level_3_known_box, self.level_4_known_box, self.level_5_known_box,
    #                    self.level_6_known_box]
    #     for box, num in zip(known_boxes, spells_known[self.character.class_level - 1]):
    #         box.setPlainText(str(num))

    #     day_boxes = [self.level_1_per_box, self.level_2_per_box, self.level_3_per_box,
    #                  self.level_4_per_box, self.level_5_per_box, self.level_6_per_box]
    #     for box, num in zip(day_boxes, spells_day[self.character.class_level - 1]):
    #         box.setPlainText(str(num))

    #     list_of_pickable_spells = self.character.add_spells(gui=True)
    #     if list_of_pickable_spells:
    #         for i in range(7):
    #             boxcount = len(self.character.additional_spells[i])

    #             num_to_add = spells_known[self.character.class_level - 1][i]
    #             for _ in range(num_to_add):
    #                 model_default = f"<<Select Level {i} Spell>>"
    #                 self.initialize_combobox(boxes[i][boxcount],
    #                                          model_default,
    #                                         list_of_pickable_spells[i],
    #                                         "spells")
    #                 self.character.spells[i].append(list_of_pickable_spells[i].pop(0))
    #                 chosen[i].append(boxes[i][boxcount])
    #                 self.update_spell_boxes(i, chosen[i])
    #                 boxes[i][boxcount].setProperty("model_default", model_default)
    #                 boxcount += 1

    #             self.update_boxes(i, chosen[i], list_of_pickable_spells)

    # def initialize_combobox(self, box : QtWidgets.QComboBox, model_default : str,
    #                         possible_spells : list, property_name : str) -> None:
    #     """Initialize the entered combobox

    #     Args:
    #         box (QtWidgets.QComboBox): combobox that is to initialized
    #         spell_type (str): Text that indicates the spell grouping
    #         possible_spells (list): list of possible spells
    #     """
    #     spell_model = QtGui.QStandardItemModel()
    #     for spell in possible_spells:
    #         spell_model.appendRow(QtGui.QStandardItem(str(spell)))
    #     box.setModel(ProxyModel(spell_model, model_default))
    #     box.setCurrentIndex(1)
    #     box.activated[str].connect(self.update_spells)
    #     box.setProperty("spell_list", [property_name, possible_spells[0]])

    # def update_spell_boxes(self, key : str, spell_list : list) -> None:
    #     """update the level 0 spell boxes

    #     Args:
    #         key (str): key for the select_new_class_feat function
    #     """
    #     for box in spell_list:
    #         box.setProperty("level", [key, spell_list])

    # def update_spells(self, selected_spell : str) -> None:
    #     """replace the class feat with the newly selected class feat

    #     level0 combobox got updated -> come in here
    #     replace the spell in the spell list. can be either spells or additional_spells
    #     update the text in all level0 boxes

    #     Args:
    #         selected_spell (str): feat selected in the combobox
    #     """
    #     combo = self.sender()
    #     spell_list = combo.property("spell_list")
    #     spell_function = combo.property("level")
    #     level = spell_function[0]

    #     # update spell in appropriate spell list
    #     if spell_list[0] == "spells":
    #         index = self.character.spells[level].index(spell_list[1])
    #         self.character.spells[level][index] = self.spell_dict[selected_spell]
    #     elif spell_list[0] == "additional":
    #         index = self.character.additional_spells[level].index(spell_list[1])
    #         self.character.additional_spells[level][index] = self.spell_dict[selected_spell]

    #     combo.setProperty("spell_list", [spell_list[0], selected_spell])
    #     # update all related comboboxes

    #     list_of_pickable_spells = self.character.add_spells(gui=True)
    #     self.update_boxes(*spell_function, list_of_pickable_spells)

    # def update_boxes(self, spell_level : int, spell_list : list, possible_spells : list) -> None:
    #     """update all selectable spell comboboxes

    #     Args:
    #         spell_level (int): the type of spell that should be checked in the select_new_spell
    #         spell_list (list): list of comboboxes that are to be updated
    #         possible_spells (list): list of options that can be entered
    #     """
    #     for box in spell_list:
    #         model_default = box.property("model_default")
    #         model = QtGui.QStandardItemModel()
    #         current_item = box.currentText()
    #         model.appendRow(QtGui.QStandardItem(current_item))
    #         if not possible_spells:
    #             mystic_spells = spells_by_class(spells, "Mystic")
    #             possible_spells = spells_by_level(mystic_spells, 1)
    #             possible_spells = [[], possible_spells]
    #             possible_spells[1].remove(self.spell_dict[str(current_item)])
    #         for spell in possible_spells[spell_level]:
    #             model.appendRow(QtGui.QStandardItem(str(spell)))
    #         box.setModel(ProxyModel(model, model_default))
    #         box.setCurrentIndex(1)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    characte = Character()
    characte.choose_class("Envoy", None)
    characte.update_level(2)
    window = SpellForm(characte)
    window.show()
    sys.exit(app.exec_())
