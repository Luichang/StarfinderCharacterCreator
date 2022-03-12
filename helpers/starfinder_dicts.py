possible_attributes = ["str", "strength", "dex", "dexterity", "con", "constitution",
                      "int", "inteligence", "wis", "wisdom", "cha", "charisma"]

attribute_shorthand = {
    "strength"     : "strength",
    "str"          : "strength",
    "Str"          : "strength",
    "dexterity"    : "dexterity",
    "dex"          : "dexterity",
    "Dex"          : "dexterity",
    "constitution" : "constitution",
    "con"          : "constitution",
    "Con"          : "constitution",
    "intelligence" : "intelligence",
    "int"          : "intelligence",
    "Int"          : "intelligence",
    "wisdom"       : "wisdom",
    "wis"          : "wisdom",
    "Wis"          : "wisdom",
    "charisma"     : "charisma",
    "cha"          : "charisma",
    "Cha"          : "charisma"
}

attribute_shortener = {
    "strength"      : "Str",
     "dexterity"    : "Dex",
     "constitution" : "Con",
     "intelligence" : "Int",
     "wisdom"       : "Wis",
     "charisma"     : "Cha",
}

spells_known = [
    [4, 2, 0, 0, 0, 0, 0], # 1
    [5, 3, 0, 0, 0, 0, 0], # 2
    [6, 4, 0, 0, 0, 0, 0], # 3
    [6, 4, 2, 0, 0, 0, 0], # 4
    [6, 4, 3, 0, 0, 0, 0], # 5
    [6, 4, 4, 0, 0, 0, 0], # 6
    [6, 5, 4, 2, 0, 0, 0], # 7
    [6, 5, 4, 3, 0, 0, 0], # 8
    [6, 5, 4, 4, 0, 0, 0], # 9
    [6, 5, 5, 4, 2, 0, 0], # 10
    [6, 6, 5, 4, 3, 0, 0], # 11
    [6, 6, 5, 4, 4, 0, 0], # 12
    [6, 6, 5, 5, 4, 2, 0], # 13
    [6, 6, 6, 5, 4, 3, 0], # 14
    [6, 6, 6, 5, 4, 4, 0], # 15
    [6, 6, 6, 5, 5, 4, 2], # 16
    [6, 6, 6, 6, 5, 4, 3], # 17
    [6, 6, 6, 6, 5, 4, 4], # 18
    [6, 6, 6, 6, 5, 5, 4], # 19
    [6, 6, 6, 6, 6, 5, 5], # 20
]

spells_day = [
    [2, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0],
    [3, 2, 0, 0, 0, 0],
    [4, 2, 0, 0, 0, 0],
    [4, 3, 0, 0, 0, 0],
    [4, 3, 2, 0, 0, 0],
    [4, 4, 2, 0, 0, 0],
    [5, 4, 3, 0, 0, 0],
    [5, 4, 3, 2, 0, 0],
    [5, 4, 4, 2, 0, 0],
    [5, 5, 4, 3, 0, 0],
    [5, 5, 4, 3, 2, 0],
    [5, 5, 4, 4, 2, 0],
    [5, 5, 5, 4, 3, 0],
    [5, 5, 5, 4, 3, 2],
    [5, 5, 5, 4, 4, 2],
    [5, 5, 5, 5, 4, 3],
    [5, 5, 5, 5, 5, 4],
    [5, 5, 5, 5, 5, 5]
]

spells_bonus = [
    [ 0, 0, 0, 0, 0, 0, 0, 0], # 1-11
    [11, 0, 1, 0, 0, 0, 0, 0], # 12-13
    [13, 0, 1, 1, 0, 0, 0, 0], # 14-15
    [15, 0, 1, 1, 1, 0, 0, 0], # 16-17
    [17, 0, 1, 1, 1, 1, 0, 0], # 18-19
    [19, 0, 2, 1, 1, 1, 1, 0], # 20-21
    [21, 0, 2, 2, 1, 1, 1, 1], # 22-23
    [23, 0, 2, 2, 2, 1, 1, 1], # 24-25
    [25, 0, 2, 2, 2, 2, 1, 1], # 26-27
    [27, 0, 3, 2, 2, 2, 2, 1], # 28-29
    [29, 0, 3, 3, 2, 2, 2, 2], # 30-31
]

skills = {
            "acrobatics"       : 0,
            "athletics"        : 0,
            "bluff"            : 0,
            "computers"        : 0,
            "culture"          : 0,
            "diplomacy"        : 0,
            "disguise"         : 0,
            "engineering"      : 0,
            "intimidate"       : 0,
            "life science"     : 0,
            "medicine"         : 0,
            "mysticism"        : 0,
            "perception"       : 0,
            "physical science" : 0,
            "piloting"         : 0,
            "profession"       : 0,
            "profession2"      : 0,
            "sense motive"     : 0,
            "sleight of hand"  : 0,
            "stealth"          : 0,
            "survival"         : 0,
        }
