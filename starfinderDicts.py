possibleAttributes = ["str", "strength", "dex", "dexterity", "con", "constitution",
                              "int", "inteligence", "wis", "wisdom", "cha", "charisma"]

raceStatList = {"android"           : {"strength" : 0, "dexterity" : 2, "constitution" : 0,
                                       "intelligence" : 2, "wisdom" : 0, "charisma" : -2, "hp" : 4} ,
                "human"             : {"strength" : 0, "dexterity" : 0, "constitution" : 0,
                                       "intelligence" : 0, "wisdom" : 0, "charisma" : 0, "hp" : 4} ,
                "kasatha"           : {"strength" : 2, "dexterity" : 0, "constitution" : 0,
                                       "intelligence" : -2, "wisdom" : 2, "charisma" : 0, "hp" : 4} ,
                "lashunta(korasha)" : {"strength" : 2, "dexterity" : 0, "constitution" : 0,
                                       "intelligence" : 0, "wisdom" : -2, "charisma" : 2, "hp" : 4} ,
                "lashunta(damaya)"  : {"strength" : 0, "dexterity" : 0, "constitution" : -2,
                                       "intelligence" : 2, "wisdom" : 0, "charisma" : 2, "hp" : 4} ,
                "shirren"           : {"strength" : 0, "dexterity" : 0, "constitution" : 2,
                                       "intelligence" : 0, "wisdom" : 2, "charisma" : -2, "hp" : 6} ,
                "vesk"              : {"strength" : 2, "dexterity" : 0, "constitution" : 2,
                                       "intelligence" : -2, "wisdom" : 0, "charisma" : 0, "hp" : 6} ,
                "ysoki"             : {"strength" : -2, "dexterity" : 2, "constitution" : 0,
                                       "intelligence" : 2, "wisdom" : 0, "charisma" : 0, "hp" : 2} }

themes = {"ace pilot":     {"strength" : 0, "dexterity" : 1, "constitution" : 0, "intelligence" : 0,
                            "wisdom" : 0, "charisma" : 0},
          "bounty hunter": {"strength" : 0, "dexterity" : 0, "constitution" : 1, "intelligence" : 0,
                            "wisdom" : 0, "charisma" : 0},
          "icon":          {"strength" : 0, "dexterity" : 0, "constitution" : 0, "intelligence" : 0,
                            "wisdom" : 0, "charisma" : 1},
          "mercenary":     {"strength" : 1, "dexterity" : 0, "constitution" : 0, "intelligence" : 0,
                            "wisdom" : 0, "charisma" : 0},
          "outlaw":        {"strength" : 0, "dexterity" : 1, "constitution" : 0, "intelligence" : 0,
                            "wisdom" : 0, "charisma" : 0},
          "priest":        {"strength" : 0, "dexterity" : 0, "constitution" : 0, "intelligence" : 0,
                            "wisdom" : 1, "charisma" : 0},
          "scholar":       {"strength" : 0, "dexterity" : 0, "constitution" : 0, "intelligence" : 1,
                            "wisdom" : 0, "charisma" : 0},
          "spacefarer":    {"strength" : 0, "dexterity" : 0, "constitution" : 1, "intelligence" : 0,
                            "wisdom" : 0, "charisma" : 0},
          "xenoseeker":    {"strength" : 0, "dexterity" : 0, "constitution" : 0, "intelligence" : 0,
                            "wisdom" : 0, "charisma" : 1},
          "themeless":     {"strength" : 0, "dexterity" : 0, "constitution" : 0, "intelligence" : 0,
                            "wisdom" : 0, "charisma" : 0}}

classesStatFocus = {"envoy": "Charisma or Dexterity and Intelligence",
                    "mechanic": "Intelligence or Dexterity",
                    "mystic": "Wisdom or Charisma",
                    "operative": "Dexterity or Intelligence and Charisma",
                    "solarian": "Charisma or Strength",
                    "soldier": "Strength or Dexterity or Constitution",
                    "technomancer": "Intelligence or Dexterity"}

attributeShorthand = {
    "strength"     : "strength",
    "str"          : "strength",
    "dexterity"    : "dexterity",
    "dex"          : "dexterity",
    "constitution" : "constitution",
    "con"          : "constitution",
    "intelligence" : "intelligence",
    "int"          : "intelligence",
    "wisdom"       : "wisdom",
    "wis"          : "wisdom",
    "charisma"     : "charisma",
    "cha"          : "charisma"
}

attributeShortener = {
    "strength"      : "Str",
     "dexterity"    : "Dex",
     "constitution" : "Con",
     "intelligence" : "Int",
     "wisdom"       : "Wis",
     "charisma"     : "Cha",
}

raceAbilities = {"android"           : [["Constructed", "words"],
                                        ["Exceptional vision", "words"],
                                        ["Flat affect", "stats", [["sense motive", -2]]],
                                        ["Upgrade slot", "words"]] ,

                 "human"             : [["Bonus feat", "feat"], # Humans select one extra feat at 1st level
                                        ["Skilled", "words"]] , # Humans gain an additional skill rank at 1st level and each level thereafter

                 "kasatha"           : [["Desert stride", "words"],
                                        ["Four-armed", "words"],
                                        ["Historian", "stats", [["culture", 2]]],
                                        ["Natural grace", [["acrobatics", 2], ["athletics", 2]]]] ,

                 "lashunta(korasha)" : [["Dimorphic", "words"],
                                        ["Lashunta magic", "spell", ["daze", "psychokinetic hand", "detect thoughts"]],
                                        ["Limited telepathy", "words"],
                                        ["Student", "stats", [["any", 2], ["any", 2]]]] ,

                 "lashunta(damaya)"  : [["Dimorphic", "words"],
                                        ["Lashunta magic", "spell", ["daze", "psychokinetic hand", "detect thoughts"]],
                                        ["Limited telepathy", "words"],
                                        ["Student", "stats", [["any", 2], ["any", 2]]]] ,

                 "shirren"           : [["Blindsense", "words"],
                                        ["Communalism", "words"],
                                        ["Cultural fascination", [["culture", 2], ["diplomacy", 2]]],
                                        ["Limited telepathy", "words"]] ,

                 "vesk"              : [["Armor savant", "armor"],
                                        ["Fearless", "saveing"],
                                        ["Low-light vision", "words"],
                                        ["Natural weapons", "words"]] ,

                 "ysoki"             : [["Cheek pouches", "words"],
                                        ["Darkvision", "words"],
                                        ["Moxie", "words"],
                                        ["Scrounger", "stats", [["engineering", 2], ["stealth", 2], ["survival", 2]]]] }

themeAbilities = {
    "ace pilot":       [["Theme knowledge", "??"], # piloting becomes class knowledge or +1 bonus to checks
                        ["Lone wolf", "words"],
                        ["Need for speed", "words"],
                        ["Master pilot", "words"]],

    "bounty hunter":   [["Theme knowledge", "??"], # survival becomes class knowledge or +1 bonus to checks
                        ["Swift hunter", "words"],
                        ["Relentless", "words"],
                        ["Master hunter", "words"]],

    "icon":            [["Theme knowledge", "??"], # chose a profession receive +1 to checks, culture becomes class knowledge or +1 bonus to checks
                        ["Celebrity", "words"],
                        ["Megacelebrity", "words"],
                        ["Master icon", "words"]],

    "mercenary":       [["Theme knowledge", "??"], # athletics becomes class knowledge or +1 bonus to checks
                        ["Grunt", "words"], # carrying limit increases
                        ["Squad leader", "words"],
                        ["Commander", "words"]],

    "outlaw":          [["Theme knowledge", "??"], # slight of hand becomes class knowledge or +1 bonus to checks
                        ["Legal corruption", "words"],
                        ["Black market connections", "words"],
                        ["Master outlaw", "words"]],

    "priest":          [["Theme knowledge", "??"], # mysticism becomes class knowledge or +1 bonus to checks
                        ["Mantle of the clergy", "words"],
                        ["Divine boon", "spell"], # Choose one 1st-level mystic spell with some connection to your deity’s portfolio (subject to the GM’s approval). If you have levels in the mystic class, you gain 1 additional 1stlevel spell per day and add the chosen spell to your list of mystic spells known. Otherwise, you can use the chosen spell once per day as a spell-like ability.
                        ["True communion", "words"]],

    "scholar":         [["Theme knowledge", "??"], # chose either life or physical science, that becomes class knowledge or +1 bonus to checks
                        ["Tip of the tongue", "words"],
                        ["Research maven", "words"],
                        ["Master scholar", "words"]],

    "spacefarer":      [["Theme knowledge", "??"], # physical science becomes class knowledge or +1 bonus to checks
                        ["Eager dabbler", "?"], # +2 bonus to skill checks for skills with 0 ranks in skill
                        ["Jack of all trades", "words"],
                        ["Master explorer", "words"]],

    "xenoseeker":      [["Theme knowledge", "??"], # life science becomes class knowledge or +1 bonus to checks
                        ["Quick pidgin", "words"],
                        ["First contact", "words"],
                        ["Brilliant discovery", "words"]],

    "themeless":       [["General knowledge", "??"], # chose a skill that becomes class knowledge or +1 bonus to checks
                        ["Certainty", "words"],
                        ["Extensive studies", "words"],
                        ["Steely determination", "words"]]
}

classAbilities = {
    "envoy":  [[["Envoy improvisation"],
                ["Expertise (1d6)"],
                ["Skill expertise"]],

               [["Envoy improvisation"]],

               [["Expertise talent"],
                ["Weapon specialization"]],

               [["Envoy improvisation"]],

               [["Expertise (1d6+1)"],
                ["Skill expertise"]],

               [["Envoy improvisation"]],

               [["Expertise talent"]],

               [["Envoy improvisation"]],

               [["Expertise (1d6+2)"],
                ["Skill expertise"]],

               [["Envoy improvisation"]],

               [["Expertise talent"]],

               [["Envoy improvisation"]],

               [["Expertise (1d8+2)"], ["Skill expertise"]],

               [["Envoy improvisation"]],

               [["Expertise talent"]],

               [["Envoy improvisation"]],

               [["Expertise (1d8+3)"],
                ["Skill expertise"]],

               [["Envoy improvisation"]],

               [["Expertise talent"]],

               [["Envoy improvisation"],
                ["Expertise (1d8+4)"],
                ["True expertise"]],
             ]

    ,
    "mechanic":[[["Artificial intelligence"],
                 ["Bypass +1"],
                 ["Custom rig"]],

                 ["Mechanic trick"],

                [["Overload"],
                 ["Weapon specialization"]],

                [["Mechanic trick"]],

                [["Bypass +2"],
                 ["Remote hack"]],

                [["Mechanic trick"]],

                [["Expert rig"],
                 ["Miracle worker 1/day"]],

                [["Mechanic trick"]],

                [["Bypass +3"],
                 ["Override"]],

                [["Mechanic trick"]],

                [["Coordinated assault +1"],
                 ["Miracle worker 2/day"]],

                [["Mechanic trick"]],

                [["Advanced rig"],
                 ["Bypass +4"]],

                [["Mechanic trick"]],

                [["Miracle worker 3/day"]],

                [["Mechanic trick"]],

                [["Bypass +5"],
                 ["Control net"],
                 ["Coordinated assault +2"]],

                [["Mechanic trick"]],

                [["Ghost in the machine"],
                 ["Miracle worker 4/day"],
                 ["Superior rig"]],

                [["Bypass +6"],
                 ["Mechanic trick"],
                 ["Tech master"]],
             ]
    ,
    "mystic":  [[["Connection"],
                 ["Connection power"],
                 ["Connection spell"],
                 ["Healing touch"]],

                [["Channel skill +1"],
                 ["Mindlink"]],

                [["Connection power"],
                 ["Weapon specialization"]],

                [["Connection spell"]],

                [["Channel skill +2"]],

                [["Connection power"]],

                [["Connection spell"]],

                [["Channel skill +3"]],

                [["Connection power"]],

                [["Connection spell"]],

                [["Channel skill +4"],
                 ["Telepathic bond"]],

                [["Connection power"]],

                [["Connection spell"]],

                [["Channel skill +5"]],

                [["Connection power"]],

                [["Connection spell"]],

                [["Channel skill +6"]],

                [["Connection powe"]],

                [["Transcendence"]],

                [["Channel skill +7"],
                 ["Enlightenment"]],
             ]
    ,
    "operative":   [[["Operative’s edge +1"],
                     ["Specialization"],
                     ["Trick attack +1d4"]],

                    [["Evasion"],
                     ["Operative exploit"]],

                    [["Operative’s edge +2"],
                     ["Quick movement (+10 ft.)"],
                     ["Trick attack +1d8"],
                     ["Weapon specialization"]],

                    [["Debilitating trick"],
                     ["Operative exploit"]],

                    [["Specialization exploit"],
                     ["Trick attack +3d8"]],

                    [["Operative exploit"]],

                    [["Operative’s edge +3"],
                     ["Specialization skill mastery"],
                     ["Trick attack +4d8"],
                     ["Uncanny agility"]],

                    [["Operative exploit"],
                     ["Triple attack"]],

                    [["Quick movement (+20 ft.)"],
                     ["Trick attack +5d8"]],

                    [["Operative exploit"]],

                    [["Operative’s edge +4"],
                     ["Specialization power"],
                     ["Trick attack +6d8"]],

                    [["Operative exploit"]],

                    [["Quad attack"],
                     ["Trick attack +7d8"]],

                    [["Operative exploit"]],

                    [["Operative’s edge +5"],
                     ["Quick movement (+30 ft.)"],
                     ["Trick attack +8d8"]],

                    [["Operative exploit"]],

                    [["Double debilitation"],
                     ["Trick attack +9d8"]],

                    [["Operative exploit"]],

                    [["Operative’s edge +6"],
                     ["Trick attack +10d8"]],

                    [["Operative exploit"],
                     ["Supreme operative"]],
             ]
    ,
    "solarian": [[["Skill adept"],
                  ["Solar manifestation"],
                  ["Stellar mode"],
                  ["Stellar revelation (black hole, supernova)"]],

                 [["Stellar revelation"]],

                 [["Sidereal influence (2 skills)"],
                  ["Weapon specialization"]],

                 [["Stellar revelation"]],

                 [[]],

                 [["Stellar revelation"]],

                 [["Flashing strikes"]],

                 [["Stellar revelation"]],

                 [["Zenith revelations"]],

                 [["Stellar revelation"]],

                 [["Sidereal influence (4 skills)"]],

                 [["Stellar revelation"]],

                 [["Solarian’s onslaught"]],

                 [["Stellar revelation"]],

                 [[]],

                 [["Stellar revelation"]],

                 [["Zenith revelations"]],

                 [["Stellar revelation"]],

                 [["Sidereal influence (6 skills)"]],

                 [["Stellar paragon"],
                  ["Stellar revelation"]],
             ],
    "soldier": [[["Primary Fighting style"],
                 ["Primary style technique"]],

                [["Combat feat"]],

                [["Gear boost"],
                 ["Weapon specialization"]],

                [["Combat feat"]],

                [["Primary style technique"]],

                [["Combat feat"]],

                [["Gear boost"]],

                [["Combat feat"]],

                [["Primary style technique"],
                 ["Secondary fighting style"],
                 ["Secondary style technique"]],

                [["Combat feat"]],

                [["Gear boost"],
                 ["Soldier’s onslaught"]],

                [["Combat feat"]],

                [["Primary style technique"],
                 ["Secondary style technique"]],

                [["Combat feat"]],

                [["Gear boost"]],

                [["Combat feat"]],

                [["Primary style technique"], ["Secondary style technique"]],

                [["Combat feat"]],

                [["Gear boost"]],

                [["Combat feat"],
                 ["Kill shot"]],
             ],
    "technomancer": [[["Spell cache"]],

                     [["Magic hack"]],

                     [["Spell Focus"],
                      ["Techlore +1"],
                      ["Weapon specialization"]],


                     [[]],

                     [["Magic hack"]],

                     [["Cache capacitor 1"],
                      ["Techlore +2"]],


                     [[]],

                     [["Magic hack"]],

                     [["Techlore +3"]],

                     [[]],

                     [["Magic hack"]],

                     [["Cache capacitor 2"],
                      ["Techlore +4"]],

                     [[]],

                     [["Magic hack"]],

                     [["Techlore +5"]],

                     [[]],

                     [["Magic hack"]],

                     [["Cache capacitor 3"],
                      ["Techlore +6"]],

                     [["Resolve attunement"]],

                     [["Fuse spells"],
                      ["Magic hack"]],
             ]
}

classesStatBonus = {
    "envoy": {
        "bab"       : [0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15],
        "fort"      : [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],
        "reflex"    : [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],
        "will"      : [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],
        "skills"    : 8,
        "sp"        : 6,
        "hp"        : 6,
        "key"       : "cha",
        "classBonus": {
                "acrobatics"       : 3,
                "athletics"        : 3,
                "bluff"            : 3,
                "computers"        : 3,
                "culture"          : 3,
                "diplomacy"        : 3,
                "disguise"         : 3,
                "engineering"      : 3,
                "intimidate"       : 3,
                "life science"     : 0,
                "medicine"         : 3,
                "mysticism"        : 0,
                "perception"       : 3,
                "physical science" : 0,
                "piloting"         : 3,
                "profession"       : 3,
                "profession2"      : 3,
                "sense motive"     : 3,
                "slight of hand"   : 3,
                "stealth"          : 3,
                "survival"         : 0
        }
    },
    "mechanic": {
        "bab"       : [0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15],
        "fort"      : [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],
        "reflex"    : [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],
        "will"      : [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],
        "skills"    : 4,
        "sp"        : 6,
        "hp"        : 6,
        "key"       : "int",
        "classBonus": {
                "acrobatics"       : 0,
                "athletics"        : 3,
                "bluff"            : 0,
                "computers"        : 3,
                "culture"          : 0,
                "diplomacy"        : 0,
                "disguise"         : 0,
                "engineering"      : 3,
                "intimidate"       : 0,
                "life science"     : 0,
                "medicine"         : 3,
                "mysticism"        : 0,
                "perception"       : 3,
                "physical science" : 3,
                "piloting"         : 3,
                "profession"       : 3,
                "profession2"      : 3,
                "sense motive"     : 0,
                "slight of hand"   : 0,
                "stealth"          : 0,
                "survival"         : 0
        }
    },
    "mystic": {
        "bab"       : [0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15],
        "fort"      : [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],
        "reflex"    : [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],
        "will"      : [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],
        "skills"    : 6,
        "sp"        : 6,
        "hp"        : 6,
        "key"       : "wis",
        "classBonus": {
                "acrobatics"       : 0,
                "athletics"        : 0,
                "bluff"            : 3,
                "computers"        : 0,
                "culture"          : 3,
                "diplomacy"        : 3,
                "disguise"         : 3,
                "engineering"      : 0,
                "intimidate"       : 3,
                "life science"     : 3,
                "medicine"         : 3,
                "mysticism"        : 3,
                "perception"       : 3,
                "physical science" : 0,
                "piloting"         : 0,
                "profession"       : 3,
                "profession2"      : 3,
                "sense motive"     : 3,
                "slight of hand"   : 0,
                "stealth"          : 0,
                "survival"         : 3
        }
    },
    "operative": {
        "bab"       : [0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15],
        "fort"      : [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],
        "reflex"    : [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],
        "will"      : [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],
        "skills"    : 8,
        "sp"        : 6,
        "hp"        : 6,
        "key"       : "dex",
        "classBonus": {
                "acrobatics"       : 3,
                "athletics"        : 3,
                "bluff"            : 3,
                "computers"        : 3,
                "culture"          : 3,
                "diplomacy"        : 0,
                "disguise"         : 3,
                "engineering"      : 3,
                "intimidate"       : 3,
                "life science"     : 0,
                "medicine"         : 3,
                "mysticism"        : 0,
                "perception"       : 3,
                "physical science" : 0,
                "piloting"         : 3,
                "profession"       : 3,
                "profession2"      : 3,
                "sense motive"     : 3,
                "slight of hand"   : 3,
                "stealth"          : 3,
                "survival"         : 3
        }
    },
    "solarian": {
        "bab"       : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        "fort"      : [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],
        "reflex"    : [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],
        "will"      : [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],
        "skills"    : 4,
        "sp"        : 7,
        "hp"        : 7,
        "key"       : "cha",
        "classBonus": {
                "acrobatics"       : 3,
                "athletics"        : 3,
                "bluff"            : 0,
                "computers"        : 0,
                "culture"          : 0,
                "diplomacy"        : 3,
                "disguise"         : 0,
                "engineering"      : 0,
                "intimidate"       : 3,
                "life science"     : 0,
                "medicine"         : 0,
                "mysticism"        : 3,
                "perception"       : 3,
                "physical science" : 3,
                "piloting"         : 0,
                "profession"       : 3,
                "profession2"      : 3,
                "sense motive"     : 3,
                "slight of hand"   : 0,
                "stealth"          : 3,
                "survival"         : 0
        }
    },
    "soldier": {
        "bab"       : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        "fort"      : [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],
        "reflex"    : [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],
        "will"      : [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],
        "skills"    : 4,
        "sp"        : 7,
        "hp"        : 7,
        "key"       : "str",
        "classBonus": {
                "acrobatics"       : 3,
                "athletics"        : 3,
                "bluff"            : 0,
                "computers"        : 0,
                "culture"          : 0,
                "diplomacy"        : 0,
                "disguise"         : 0,
                "engineering"      : 3,
                "intimidate"       : 3,
                "life science"     : 0,
                "medicine"         : 3,
                "mysticism"        : 0,
                "perception"       : 0,
                "physical science" : 0,
                "piloting"         : 3,
                "profession"       : 3,
                "profession2"      : 3,
                "sense motive"     : 0,
                "slight of hand"   : 0,
                "stealth"          : 0,
                "survival"         : 3
        }
    },
    "technomancer": {
        "bab"       : [0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15],
        "fort"      : [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],
        "reflex"    : [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],
        "will"      : [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],
        "skills"    : 4,
        "sp"        : 5,
        "hp"        : 5,
        "key"       : "int",
        "classBonus": {
                "acrobatics"       : 0,
                "athletics"        : 0,
                "bluff"            : 0,
                "computers"        : 3,
                "culture"          : 0,
                "diplomacy"        : 0,
                "disguise"         : 0,
                "engineering"      : 3,
                "intimidate"       : 0,
                "life science"     : 3,
                "medicine"         : 0,
                "mysticism"        : 3,
                "perception"       : 0,
                "physical science" : 3,
                "piloting"         : 3,
                "profession"       : 3,
                "profession2"      : 3,
                "sense motive"     : 0,
                "slight of hand"   : 3,
                "stealth"          : 0,
                "survival"         : 0
        }
    }
}

skillMods = {
    "acrobatics"      : 0,
    "athletics"       : 0,
    "bluff"           : 0,
    "computers"       : 0,
    "culture"         : 0,
    "diplomacy"       : 0,
    "disguise"        : 0,
    "engineering"     : 0,
    "intimidate"      : 0,
    "life science"    : 0,
    "medicine"        : 0,
    "mysticism"       : 0,
    "perception"      : 0,
    "physical science": 0,
    "piloting"        : 0,
    "profession"      : 0,
    "sense motive"    : 0,
    "slight of hand"  : 0,
    "stealth"         : 0,
    "survival"        : 0
}

htmlTags = {
    "name" : "character_name",
    "race" : "race",
    "raceStr" : "str_race",
    "raceDex" : "dex_race",
    "raceCon" : "con_race",
    "raceInt" : "int_race",
    "raceWis" : "wis_race",
    "raceCha" : "cha_race",
    "theme" : "theme",
    "themeStr" : "str_theme",
    "themeDex" : "dex_theme",
    "themeCon" : "con_theme",
    "themeInt" : "int_theme",
    "themeWis" : "wis_theme",
    "themeCha" : "cha_theme",
    "attrStr" : "str_score",
    "attrDex" : "dex_score",
    "attrCon" : "con_score",
    "attrInt" : "int_score",
    "attrWis" : "wis_score",
    "attrCha" : "cha_score",
    "attrStrMod" : "str_mod",
    "attrDexMod" : "dex_mod",
    "attrConMod" : "con_mod",
    "attrIntMod" : "int_mod",
    "attrWisMod" : "wis_mod",
    "attrChaMod" : "cha_mod",
    "attrStrPoint" : "str_point",
    "attrDexPoint" : "dex_point",
    "attrConPoint" : "con_point",
    "attrIntPoint" : "int_point",
    "attrWisPoint" : "wis_point",
    "attrChaPoint" : "cha_point",
    "className" : "class_level",
    "init_total" : "init_total",
    "init_dex" : "init_dex",
    "init_misc" : "init_misc",

    "eac" : "ac_eac_total",
    "eac_armor" : "ac_eac_abonus",
    "eac_dex" : "ac_eac_dexmod",
    "eac_misc" : "ac_eac_miscmod",
    "kac" : "ac_kac_total",
    "kac_armor" : "ac_kac_abonus",
    "kac_dex" : "ac_kac_dexmod",
    "kac_misc" : "ac_kac_miscmod",
    "vsCombat" : "ac_acvs_total",

    "sp" : "total_stamina",
    "hp" : "total_hp",
    "rp" : "total_resolve",

    "fortSave" : "save_fort_total",
    "reflexSave" : "save_refl_total",
    "willSave" : "save_will_total",

    "fortSaveBase" : "save_fort_base",
    "reflexSaveBase" : "save_refl_base",
    "willSaveBase" : "save_will_base",

    "fortSaveAbility" : "save_fort_ability",
    "reflexSaveAbility" : "save_refl_ability",
    "willSaveAbility" : "save_will_ability",

    "fortSaveMisc" : "save_fort_misc",
    "reflexSaveMisc" : "save_refl_misc",
    "willSaveMisc" : "save_will_misc",

    "melee" : "attack_melee_total",
    "melee_bab" : "attack_melee_bab",
    "melee_ability" : "attack_melee_ability",
    "melee_misc" : "attack_melee_misc",
    "range" : "attack_range_total",
    "range_bab" : "attack_range_bab",
    "range_ability" : "attack_range_ability",
    "range_misc" : "attack_range_misc",
    "throw" : "attack_throw_total",
    "throw_bab" : "attack_throw_bab",
    "throw_ability" : "attack_throw_ability",
    "throw_misc" : "attack_throw_misc",

    "acrobatics"      : "skills_acrobatics_total",
    "athletics"       : "skills_athletics_total",
    "bluff"           : "skills_bluff_total",
    "computers"       : "skills_computers_total",
    "culture"         : "skills_culture_total",
    "diplomacy"       : "skills_diplomacy_total",
    "disguise"        : "skills_disguise_total",
    "engineering"     : "skills_engineering_total",
    "intimidate"      : "skills_intimidate_total",
    "life science"    : "skills_life_science_total",
    "medicine"        : "skills_medicine_total",
    "mysticism"       : "skills_mysticism_total",
    "perception"      : "skills_perception_total",
    "physical science": "skills_physical_science_total",
    "piloting"        : "skills_piloting_total",
    "profession"      : "skills_profession_total",
    "profession2"     : "skills_profession2_total",
    "sense motive"    : "skills_sense_motive_total",
    "slight of hand"  : "skills_slight_of_hand_total",
    "stealth"         : "skills_stealth_total",
    "survival"        : "skills_survival_total",

    "acrobaticsRank"      : "skills_acrobatics_ranks",
    "athleticsRank"       : "skills_athletics_ranks",
    "bluffRank"           : "skills_bluff_ranks",
    "computersRank"       : "skills_computers_ranks",
    "cultureRank"         : "skills_culture_ranks",
    "diplomacyRank"       : "skills_diplomacy_ranks",
    "disguiseRank"        : "skills_disguise_ranks",
    "engineeringRank"     : "skills_engineering_ranks",
    "intimidateRank"      : "skills_intimidate_ranks",
    "life scienceRank"    : "skills_life_science_ranks",
    "medicineRank"        : "skills_medicine_ranks",
    "mysticismRank"       : "skills_mysticism_ranks",
    "perceptionRank"      : "skills_perception_ranks",
    "physical scienceRank": "skills_physical_science_ranks",
    "pilotingRank"        : "skills_piloting_ranks",
    "professionRank"      : "skills_profession_ranks",
    "profession2Rank"     : "skills_profession2_ranks",
    "sense motiveRank"    : "skills_sense_motive_ranks",
    "slight of handRank"  : "skills_slight_of_hand_ranks",
    "stealthRank"         : "skills_stealth_ranks",
    "survivalRank"        : "skills_survival_ranks",

    "acrobaticsMod"      : "skills_acrobatics_ability",
    "athleticsMod"       : "skills_athletics_ability",
    "bluffMod"           : "skills_bluff_ability",
    "computersMod"       : "skills_computers_ability",
    "cultureMod"         : "skills_culture_ability",
    "diplomacyMod"       : "skills_diplomacy_ability",
    "disguiseMod"        : "skills_disguise_ability",
    "engineeringMod"     : "skills_engineering_ability",
    "intimidateMod"      : "skills_intimidate_ability",
    "life scienceMod"    : "skills_life_science_ability",
    "medicineMod"        : "skills_medicine_ability",
    "mysticismMod"       : "skills_mysticism_ability",
    "perceptionMod"      : "skills_perception_ability",
    "physical scienceMod": "skills_physical_science_ability",
    "pilotingMod"        : "skills_piloting_ability",
    "professionMod"      : "skills_profession_ability",
    "profession2Mod"     : "skills_profession2_ability",
    "sense motiveMod"    : "skills_sense_motive_ability",
    "slight of handMod"  : "skills_slight_of_hand_ability",
    "stealthMod"         : "skills_stealth_ability",
    "survivalMod"        : "skills_survival_ability",

    "acrobaticsClass"      : "skills_acrobatics_class",
    "athleticsClass"       : "skills_athletics_class",
    "bluffClass"           : "skills_bluff_class",
    "computersClass"       : "skills_computers_class",
    "cultureClass"         : "skills_culture_class",
    "diplomacyClass"       : "skills_diplomacy_class",
    "disguiseClass"        : "skills_disguise_class",
    "engineeringClass"     : "skills_engineering_class",
    "intimidateClass"      : "skills_intimidate_class",
    "life scienceClass"    : "skills_life_science_class",
    "medicineClass"        : "skills_medicine_class",
    "mysticismClass"       : "skills_mysticism_class",
    "perceptionClass"      : "skills_perception_class",
    "physical scienceClass": "skills_physical_science_class",
    "pilotingClass"        : "skills_piloting_class",
    "professionClass"      : "skills_profession_class",
    "profession2Class"     : "skills_profession2_class",
    "sense motiveClass"    : "skills_sense_motive_class",
    "slight of handClass"  : "skills_slight_of_hand_class",
    "stealthClass"         : "skills_stealth_class",
    "survivalClass"        : "skills_survival_class",

    "acrobaticsMisc"      : "skills_acrobatics_misc",
    "athleticsMisc"       : "skills_athletics_misc",
    "bluffMisc"           : "skills_bluff_misc",
    "computersMisc"       : "skills_computers_misc",
    "cultureMisc"         : "skills_culture_misc",
    "diplomacyMisc"       : "skills_diplomacy_misc",
    "disguiseMisc"        : "skills_disguise_misc",
    "engineeringMisc"     : "skills_engineering_misc",
    "intimidateMisc"      : "skills_intimidate_misc",
    "life scienceMisc"    : "skills_life_science_misc",
    "medicineMisc"        : "skills_medicine_misc",
    "mysticismMisc"       : "skills_mysticism_misc",
    "perceptionMisc"      : "skills_perception_misc",
    "physical scienceMisc": "skills_physical_science_misc",
    "pilotingMisc"        : "skills_piloting_misc",
    "professionMisc"      : "skills_profession_misc",
    "profession2Misc"     : "skills_profession2_misc",
    "sense motiveMisc"    : "skills_sense_motive_misc",
    "slight of handMisc"  : "skills_slight_of_hand_misc",
    "stealthMisc"         : "skills_stealth_misc",
    "survivalMisc"        : "skills_survival_misc",

    "spendablePoints" : "skills_spendable",
    "perLevelPoints"  : "skills_per_level",

    "raceAbility1" : "c_abilities_51",
    "raceAbility2" : "c_abilities_52",
    "raceAbility3" : "c_abilities_53",
    "raceAbility4" : "c_abilities_54",

    "themeAbility1" : "c_abilities_41",
    "themeAbility2" : "c_abilities_42",
    "themeAbility3" : "c_abilities_43",
    "themeAbility4" : "c_abilities_44",

    "classAbility1" : "c_abilities_01",
    "classAbility2" : "c_abilities_02",
    "classAbility3" : "c_abilities_03",
    "classAbility4" : "c_abilities_04",
    "classAbility5" : "c_abilities_05",
    "classAbility6" : "c_abilities_06",
    "classAbility7" : "c_abilities_07",
    "classAbility8" : "c_abilities_08",
    "classAbility9" : "c_abilities_09",
    "classAbility10" : "c_abilities_10",
    "classAbility11" : "c_abilities_11",
    "classAbility12" : "c_abilities_12",
    "classAbility13" : "c_abilities_13",
    "classAbility14" : "c_abilities_14",
    "classAbility15" : "c_abilities_15",
    "classAbility16" : "c_abilities_16",
    "classAbility17" : "c_abilities_17",
    "classAbility18" : "c_abilities_18",
    "classAbility19" : "c_abilities_19",
    "classAbility20" : "c_abilities_20",
    "classAbility21" : "c_abilities_21",
    "classAbility22" : "c_abilities_22",
    "classAbility23" : "c_abilities_23",
    "classAbility24" : "c_abilities_24",
    "classAbility25" : "c_abilities_25",
    "classAbility26" : "c_abilities_26",
    "classAbility27" : "c_abilities_27",
    "classAbility28" : "c_abilities_28",
    "classAbility29" : "c_abilities_29",
    "classAbility30" : "c_abilities_30",
    "classAbility31" : "c_abilities_31",
    "classAbility32" : "c_abilities_32",
    "classAbility33" : "c_abilities_33",
    "classAbility34" : "c_abilities_34",
    "classAbility35" : "c_abilities_35",
}
