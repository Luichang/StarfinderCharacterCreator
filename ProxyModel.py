from PyQt5 import QtCore, QtGui, QtWidgets
from typing import Any

class ProxyModel(QtCore.QAbstractProxyModel):
    def __init__(self, model, placeholderText='---', parent=None):
        super().__init__(parent)
        self._placeholderText = placeholderText
        self.setSourceModel(model)

    def index(self, row: int, column: int, parent: QtCore.QModelIndex = ...) -> QtCore.QModelIndex:
        return self.createIndex(row, column)

    def parent(self, index: QtCore.QModelIndex = ...) -> QtCore.QModelIndex:
        return QtCore.QModelIndex()

    def rowCount(self, parent: QtCore.QModelIndex = ...) -> int:
        return self.sourceModel().rowCount()+1 if self.sourceModel() else 0

    def columnCount(self, parent: QtCore.QModelIndex = ...) -> int:
        return self.sourceModel().columnCount() if self.sourceModel() else 0

    def data(self, index: QtCore.QModelIndex, role: int = QtCore.Qt.DisplayRole) -> Any:
        if index.row() == 0 and role == QtCore.Qt.DisplayRole:
            return self._placeholderText
        elif index.row() == 0 and role == QtCore.Qt.EditRole:
            return None
        else:
            return super().data(index, role)

    def mapFromSource(self, sourceIndex: QtCore.QModelIndex):
        return self.index(sourceIndex.row()+1, sourceIndex.column())

    def mapToSource(self, proxyIndex: QtCore.QModelIndex):
        return self.sourceModel().index(proxyIndex.row()-1, proxyIndex.column())

    def mapSelectionFromSource(self, sourceSelection: QtCore.QItemSelection):
        return super().mapSelection(sourceSelection)

    def mapSelectionToSource(self, proxySelection: QtCore.QItemSelection):
        return super().mapSelectionToSource(proxySelection)

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = QtCore.Qt.DisplayRole):
        if not self.sourceModel():
            return None
        if orientation == QtCore.Qt.Vertical:
            return self.sourceModel().headerData(section-1, orientation, role)
        else:
            return self.sourceModel().headerData(section, orientation, role)

    def removeRows(self, row: int, count: int, parent: QtCore.QModelIndex = ...) -> bool:
        return self.sourceModel().removeRows(row, count -1)
