raceStatList = {
    "android"           : {"strength" : 0, "dexterity" : 2, "constitution" : 0,
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
                           "intelligence" : 2, "wisdom" : 0, "charisma" : 0, "hp" : 2}
}

raceAbilities = {
    "android"            : [["Constructed", "words"],
                            ["Exceptional vision", "words"],
                            ["Flat affect", "stats", [["sense motive", -2]]],
                            ["Upgrade slot", "words"]] ,

     "human"             : [["Bonus feat", "feat"],
                            # Humans select one extra feat at 1st level
                            ["Skilled", "words"]] ,
                            # Humans gain an additional skill rank at 1st level and
                            # each level thereafter

     "kasatha"           : [["Desert stride", "words"],
                            ["Four-armed", "words"],
                            ["Historian", "stats", [["culture", 2]]],
                            ["Natural grace", "stats", [["acrobatics", 2], ["athletics", 2]]]] ,

     "lashunta(korasha)" : [["Dimorphic", "words"],
                            ["Lashunta magic", "spell", [["Daze", "Psychokinetic Hand"],
                                                         ["Detect Thoughts"]]],
                            ["Limited telepathy", "words"],
                            ["Student", "stats", [["any", 2], ["any", 2]]]] ,

     "lashunta(damaya)"  : [["Dimorphic", "words"],
                            ["Lashunta magic", "spell", [["Daze", "Psychokinetic Hand"],
                                                         ["Detect Thoughts"]]],
                            ["Limited telepathy", "words"],
                            ["Student", "stats", [["any", 2], ["any", 2]]]] ,

     "shirren"           : [["Blindsense", "words"],
                            ["Communalism", "words"],
                            ["Cultural fascination", "stats", [["culture", 2], ["diplomacy", 2]]],
                            ["Limited telepathy", "words"]] ,

     "vesk"              : [["Armor savant", "words"],
                            ["Fearless", "words"],
                            ["Low-light vision", "words"],
                            ["Natural weapons", "words"]] ,

     "ysoki"             : [["Cheek pouches", "words"],
                            ["Darkvision", "words"],
                            ["Moxie", "words"],
                            ["Scrounger", "stats", [["engineering", 2], ["stealth", 2],
                                                    ["survival", 2]]]]
}
