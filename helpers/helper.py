from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets

from helpers.ProxyModel import ProxyModel

def initialize_text(text_widget : QtWidgets.QLabel, name : str, text : str,
                    max_size : list[int]=None) -> None:
    """function to initialize text widgets

    Args:
        text_widget (QtWidgets.QLabel): widget whose text is to be added
        name (str): name of the widget
        text (str): text the widget is to display
        max_size (list[int], optional): the maximum size of the widget. Defaults to None.
    """
    if max_size:
        text_widget.setMaximumSize(QtCore.QSize(*max_size))
    text_widget.setObjectName(name)
    text_widget.setText(text)

def initialize_frame(frame : QtWidgets.QFrame, name : str, shape : list[int] = None,
                     vertical : bool = None) -> None:
    """function to initialize the frame widgets

    Args:
        frame (QtWidgets.QFrame): the frame to be initialized
        name (str): name of the frame
        size (list[int], optional): shape and location of the widget. Defaults to None
        vertical (bool, optional): if the line is vertical. Defaults to None
    """
    if shape:
        frame.setGeometry(QtCore.QRect(*shape))
        frame.setFrameShape(QtWidgets.QFrame.Box)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        frame.setLineWidth(2)
    else:
        if vertical:
            frame.setFrameShape(QtWidgets.QFrame.VLine)
        else:
            frame.setFrameShape(QtWidgets.QFrame.HLine)
        frame.setFrameShadow(QtWidgets.QFrame.Sunken)
    frame.setObjectName(name)

def initialize_model(items : list[str]) -> QtGui.QStandardItemModel:
    """function to initialize combobox widgets

    Args:
        items (list[str]): list of items to be added to the model

    Returns:
        QtGui.QStandardItemModel: created model for the combobox
    """
    model = QtGui.QStandardItemModel()
    for item in items:
        model.appendRow(QtGui.QStandardItem(item))
    return model

def initialize_edit(edit : QtWidgets.QLineEdit, name : str, shape : list[int]) -> None:
    """function to initialize line edit widgets

    Args:
        edit (QtWidgets.QLineEdit): line edit widget to be initialized
        name (str): name of the widget
        size (list[int]): shape and location of the widget
    """
    edit.setMaximumSize(QtCore.QSize(*shape))
    edit.setReadOnly(True)
    edit.setObjectName(name)

def initialize_widget(widget : QtWidgets.QWidget, name : str, shape : list[int]) -> None:
    """function to initialize widget widgets

    Args:
        widget (QtWidgets.QWidget): widget widget to be initialized
        name (str): name of the widget
        size (list[int]): shape and location of the widget
    """
    widget.setGeometry(QtCore.QRect(*shape))
    widget.setObjectName(name)

def initialize_combo(combo : QtWidgets.QComboBox, name : str, items : list[str], size : list[int], func=None) -> None:
    """function to initialize combobox widgets

    Args:
        combo (QtWidgets.QComboBox): combobox widget to be initialized
        name (str): name of the widget
        items (list[str]): list of items to be added to the combobox
        size (list[int]): shape and location of the widget
    """
    combo.setMaximumSize(QtCore.QSize(*size))
    combo.setObjectName(name)
    for item in items:
        combo.addItem(item)

def initialize_combo_model(combo : QtWidgets.QComboBox, items : list[str], model_default : str,
                           index : int=0, size : list[int]=None, connection=None)->None:
    """function to initialize combobox widgets

    Args:
        combo (QtWidgets.QComboBox): combobox widget to be initialized
        items (list[str]): list of items to be added to the combobox
        size (list[int], optional): shape and location of the widget. Defaults to None
        index (int, optional): index the model should be set to. Usually you want either 1 or 0.
                               Defaults to 0
    """
    theme_model = QtGui.QStandardItemModel()
    for item in items:
        theme_model.appendRow(QtGui.QStandardItem(str(item)))
    combo.setModel(ProxyModel(theme_model, model_default))
    combo.setCurrentIndex(index)
    if size:
        combo.setMaximumSize(QtCore.QSize(*size))

def update_combo(combo : QtWidgets.QComboBox, items : list[str]):
    """Function to update the entered combobox with the entered items

    Args:
        combo (QtWidgets.QComboBox): combobox to be updated
        items (list[str]): list of items to be added
    """
    combo.clear()
    combo.addItems(items)

def get_user_response(options : list, text : str="", include : bool=True) -> str:
    """Function to get user response from input options

    Args:
        options (list): list of possible options the user can choose from
        text (str, optional): text to inform the user what they are responding to.
                                Defaults to "".
        include (bool, optional): if include is True the entered text must be in the options
                                    list, False means the input can't be in the options.
                                    Defaults to True.

    Returns:
        str: the entered text that was allowed
    """
    entered = ""
    if include:
        while entered not in options:
            entered = input(text).lower()
    else:
        while entered in options:
            entered = input(text).lower()
    return entered

def write_to_file(name : str, attribute_name : str, attribute_name_value : str) -> None:
    """funtion to write the input to the HTML

    Args:
        name (str): name of the chraracter
        attribute_name (str): either the string "listPass" or the box in which the
                                attribute_name_value is to be entered
        attribute_name_value (str): the string gets entered into the attribute_name box
                                    unless attribute_name was "listPass" in which case it
                                    is a list of lists where the first element of each internal
                                    list is what is here considered the attribute_name and the
                                    second is the attribute_name_value
    """
    try:
        file = open(f"html/{name}.html", mode="r+", encoding='utf-8')
    except FileNotFoundError:
        file = open("html/CharacterSheet.html", mode="r+", encoding='utf-8')

    soup = BeautifulSoup(file, 'html.parser')
    if attribute_name == "listPass":
        for a_name, a_name_value in attribute_name_value:
            try:
                soup.find(attrs={"id": a_name})["value"] = a_name_value
            except TypeError:
                print("------------------")
                print(a_name)
                print(a_name_value)
                print(soup.find(attrs={"id": a_name}))
                print("------------------")
    else:
        try:
            soup.find(attrs={"id": attribute_name})["value"] = attribute_name_value
        except TypeError:
            print("------------------")
            print(attribute_name)
            print(attribute_name_value)
            print(soup.find(attrs={"id": attribute_name}))
            print("------------------")

    with open(f"html/{name}.html", "w", encoding='utf-8') as out:
        out.write(str(soup))
    file.close()
