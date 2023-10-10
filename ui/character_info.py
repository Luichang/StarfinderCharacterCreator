from typing import Protocol

from PyQt5 import QtGui, QtWidgets

from helpers.ProxyModel import ProxyModel


class UIWindow(Protocol):
    def character_name_changed(self, text: str) -> None:
        ...

    def update_level(self, text: str) -> None:
        ...

class CharacterInfo:

    def __init__(self, parent: UIWindow) -> None:
        self.parent = parent
        self.widget = QtWidgets.QWidget()
        character_name_grid = QtWidgets.QHBoxLayout()
        character_name_grid.setContentsMargins(0, 0, 0, 0)
        character_name_grid.setObjectName("CharacterNameGrid")

        character_name_text = QtWidgets.QLabel("Character Name")
        self.character_name_box = QtWidgets.QTextEdit()
        self.character_level_box = QtWidgets.QComboBox()

        self.character_name_box.textChanged.connect(self.emit_text_changed)

        level_model = QtGui.QStandardItemModel()
        for item in range(1, 21):
            level_model.appendRow(QtGui.QStandardItem(str(item)))
        self.character_level_box.setModel(ProxyModel(level_model, "0"))
        self.character_level_box.setCurrentIndex(0)
        # self.update_level
        self.character_level_box.currentTextChanged.connect(self.emit_combo_box_changed)

        character_name_grid.addWidget(character_name_text)
        character_name_grid.addWidget(self.character_name_box)
        character_name_grid.addWidget(self.character_level_box)

        self.widget.setLayout(character_name_grid)

    def emit_text_changed(self):
        text = self.character_name_box.toPlainText()
        self.parent.character_name_changed(text)

    def emit_combo_box_changed(self):
        selected_item = self.character_level_box.currentText()
        self.parent.update_level(selected_item)
