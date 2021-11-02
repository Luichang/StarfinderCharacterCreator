feats = {
    "Adaptive Fighting" :                 ["combat", [["combat", ["any", "any", "any"]]],                                                                                      "words"],
    "Advanced Melee Weapon Proficiency" : ["combat", [["feat", ["Basic Melee Weapon Proficiency"]]],                                                                           "words"],
    "Amplified Glitch" :                  ["combat", [["skills", [["computers", 3], ["intimidate", 3]]]],                                                                      "words"],
    "Antagonize" :                        ["normal", [["skills", [["diplomacy", 5], ["intimidate", 5]]]],                                                                      "words"],
    "Barricade" :                         ["combat", [["skills", [["engineering", 1]]]],                                                                                       "words"],
    "Basic Melee Weapon Proficiency" :    ["combat", [[]],                                                                                                                     "words"],
    "Blind-Fight" :                       ["combat", [[]],                                                                                                                     "words"],
    "Bodyguard" :                         ["combat", [[]],                                                                                                                     "words"],
    "In Harm's Way" :                     ["combat", [["feat", ["Bodyguard"]]],                                                                                                "words"],
    "Cleave" :                            ["combat", [["ability", ["str", 13]], ["bab", 1]],                                                                                   "words"],
    "Great Cleave" :                      ["combat", [["ability", ["str", 13]], ["feat", ["Cleave"]], ["bab", 4]],                                                              "words"],
    "Climbing Master" :                   ["normal", [["skills", [["athletics", 5]]]],                                                                                         "words"], # speed effected
    "Combat Casting" :                    ["combat", [["spellLevel", 2]],                                                                                                      "words"],
    "Connection Inkling" :                ["normal", [["ability", ["wis", 15]], ["level", 5], ["skills", [["mysticism", 0, "less"]]]],                                              "words"], # Gain the ability to cast minor mystic spells
    "Coordinated Shot" :                  ["combat", [["bab", 1]],                                                                                                             "words"],
    "Deadly Aim" :                        ["combat", [["bab", 1]],                                                                                                             "words"],
    "Deflect Projectiles" :               ["combat", [["bab", 8]],                                                                                                             "words"],
    "Reflect Projectiles" :               ["combat", [["feat", ["Deflect Projectiles"]], ["bab", 16]],                                                                         "words"],
    "Diehard" :                           ["normal", [[]],                                                                                                                     "words"],
    "Dive for Cover" :                    ["combat", [["save", ["reflex", 2]]],                                                                                                "words"], #  base reflex +2
    "Diversion" :                         ["normal", [[]],                                                                                                                     "words"],
    "Drag Down" :                         ["combat", [[]],                                                                                                                     "words"],
    "Enhanced Resistance" :               ["normal", [["bab", 4]],                                                                                                             "words"],
    "Extra Resolve" :                     ["normal", [["level", 5]],                                                                                                           "resolve", 2],
    "Far Shot" :                          ["combat", [["bab", 1]],                                                                                                             "words"],
    "Fast Talk" :                         ["normal", [["skills", [["bluff", 5]]]],                                                                                             "words"],
    "Fleet" :                             ["combat", [[]],                                                                                                                     "words"], # speed effected
    "Fusillade" :                         ["combat", [["bab", 1], ["race", "kasatha"]],                                                                                        "words"],
    "Great Fortitude" :                   ["normal", [[]],                                                                                                                     "save", ["Fortitude", 2]],
    "Improved Great Fortitude" :          ["normal", [["feat", ["Great Fortitude"]], ["level", 5]],                                                                            "words"],
    "Grenade Proficiency" :               ["combat", [[]],                                                                                                                     "words"],
    "Harm Undead" :                       ["normal", [["class", "mystic"], ["style", "Healer"]],                                                                               "words"],
    "Heavy Armor Proficiency" :           ["combat", [["ability", ["str", 13]], ["feat", ["Light Armor Proficiency"]]],                                                        "words"],
    "Heavy Weapon Proficiency" :          ["combat", [["ability", ["str", 13]], ["feat", ["Small Arm Proficiency", "Longarm Proficiency"]]],                                   "words"],
    "Improved Combat Maneuver" :          ["combat", [["bab", 1]],                                                                                                             "words"], # +4 bonus to perform one combat maneuver
    "Pull the Pin" :                      ["combat", [["feat", ["Improved Combat Maneuver"]]],                                                                                 "words"],
    "Improved Critical" :                 ["combat", [["bab", 8]],                                                                                                             "words"],
    "Improved Feint" :                    ["combat", [[]],                                                                                                                     "words"],
    "Greater Feint" :                     ["combat", [["feat", ["Improved Feint"]], ["bab", 6]],                                                                               "words"],
    "Improved Initiative" :               ["combat", [[]],                                                                                                                     "initiative", 4],
    "Improved Unarmed Strike" :           ["combat", [[]],                                                                                                                     "words"],
    "Iron Will" :                         ["normal", [[]],                                                                                                                     "save", ["Will", 2]],
    "Improved Iron Will" :                ["normal", [["feat", ["Iron Will"]], ["level", 5]],                                                                                  "words"],
    "Jet Dash" :                          ["normal", [[]],                                                                                                                     "words"],
    "Kip Up" :                            ["combat", [["skills", [["acrobatics", 1]]]],                                                                                        "words"],
    "Light Armor Proficiency" :           ["combat", [[]],                                                                                                                     "words"],
    "Lightning Reflexes" :                ["normal", [[]],                                                                                                                     "save", ["Reflex", 2]],
    "Improved Lightning Reflexes" :       ["normal", [["feat", ["Lightning Reflexes"]], ["level", 5]],                                                                         "words"],
    "Longarm Proficiency" :               ["combat", [["feat", ["Small Arm Proficiency"]]],                                                                                    "words"],
    "Lunge" :                             ["combat", [["bab", 6]],                                                                                                             "words"],
    "Master Crafter" :                    ["normal", [["skills", [["from", ["computers", "engineering", "life science", "mysticism", "physical science", "profession"], 5]]]], "words"],
    "Medical Expert" :                    ["normal", [["skills", [["life science", 1], ["medicine", 1], ["physical science", 1]]]],                                            "words"],
    "Minor Psychic Power" :               ["normal", [["ability", ["cha", 11]]],                                                                                               "words"], # Cast a 0-level spell as a spell-like ability 3/day
    "Psychic Power" :                     ["normal", [["ability", ["cha", 13]], ["feat", ["Minor Psychic Power"]], ["level", 4]],                                              "words"], # Cast a 1st-level spell as a spell-like ability 1/day
    "Major Psychic Power" :               ["normal", [["ability", ["cha", 15]], ["feat", ["Minor Psychic Power", "Psychic Power"]], ["level", 4]],                             "words"], # Cast a 2nd-level spell as a spell-like ability 1/day
    "Mobility" :                          ["combat", [["ability", ["dex", 13]]],                                                                                               "words"],
    "Agile Casting" :                     ["normal", [["ability", ["key", 15]], ["ability", ["dex", 15]], ["feat", ["Mobility"]], ["from", [["class", "mystic"], ["class", "technomancer"]]], ["level", 4]],      "words"],
    "Shot on the Run" :                   ["combat", [["ability", ["dex", 15]], ["feat", ["Mobility"]], ["bab", 4]],                                                           "words"],
    "Parting Shot" :                      ["combat", [["ability", ["dex", 15]], ["feat", ["Mobility", "Shot on the Run"]], ["bab", 6]],                                        "words"],
    "Sidestep" :                          ["combat", [["ability", ["dex", 15]], ["from", [["feat", ["Mobility"]], ["class", "operative"]]]],                                     "words"],
    "Improved Sidestep" :                 ["combat", [["ability", ["dex", 15]], ["from", [["feat", ["Mobility"]], ["class", "operative"]]], ["feat", ["Sidestep"]]],             "words"],
    "Spring Attack" :                     ["combat", [["ability", ["dex", 15]], ["feat", ["Mobility"]], ["bab", 4]],                                                           "words"],
    "Multi-Weapon Fighting" :             ["combat", [[]],                                                                                                                     "words"],
    "Mystic Strike" :                     ["combat", [["spellLevel", 1]],                                                                                                      "words"],
    "Nimble Moves" :                      ["combat", [["ability", ["dex", 15]]],                                                                                               "words"],
    "Opening Volley" :                    ["combat", [[]],                                                                                                                     "words"],
    "Penetrating Attack" :                ["combat", [["bab", 12]],                                                                                                            "words"],
    "Penetrating Spell" :                 ["normal", [["spellLevel", 4]],                                                                                                      "words"],
    "Powered Armor Proficiency" :         ["combat", [["ability", ["str", 13]], ["feat", ["Light Armor Proficiency"]], ["bab", 5]],                                            "words"],
    "Quick Draw" :                        ["combat", [["bab", 1]],                                                                                                             "words"],
    "Skill Focus" :                       ["normal", [[]],                                                                                                                     "choose", ["skill", ["any", 3]]],
    "Skill Synergy" :                     ["normal", [[]],                                                                                                                     "classSkill", [["any"], ["any"]]], # or a +2 bonus to it
    "Sky Jockey" :                        ["normal", [["skills", [["piloting", 5]]]],                                                                                          "words"],
    "Slippery Shooter" :                  ["combat", [["ability", ["dex", 15]], ["bab", 6]],                                                                                   "words"],
    "Small Arm Proficiency" :             ["combat", [[]],                                                                                                                     "words"],
    "Sniper Weapon Proficiency" :         ["combat", [[]],                                                                                                                     "words"],
    "Special Weapon Proficiency" :        ["combat", [["from", [["feat", ["Small Arm Proficiency", "Basic Melee Weapon Proficiency"]]]]],                                      "words"],
    "Spell Focus" :                       ["normal", [["spellLevel", 1], ["level", 3]],                                                                                        "words"],
    "Spell Penetration" :                 ["normal", [[]],                                                                                                                     "words"], # +2 bonus to caster level checks to overcome SR
    "Greater Spell Penetration" :         ["normal", [["feat", ["Spell Penetration"]]],                                                                                        "words"], # Additional +2 bonus to caster level checks to overcome SR
    "Spellbane" :                         ["normal", [["spellLevel", -1]],                                                                                                     "words"],
    "Spry Cover" :                        ["combat", [["bab", 1]],                                                                                                             "words"],
    "Stand Still" :                       ["combat", [[]],                                                                                                                     "words"],
    "Improved Stand Still" :              ["combat", [["feat", ["Stand Still"]]],                                                                                              "words"],
    "Step Up" :                           ["combat", [["bab", 1]],                                                                                                             "words"],
    "Step Up and Strike" :                ["combat", [["ability", ["dex", 13]], ["feat", ["Step Up"]], ["bab", 6]],                                                            "words"],
    "Strike Back" :                       ["combat", [["bab", 1]],                                                                                                             "words"],
    "Suppressive Fire" :                  ["combat", [["bab", 1], ["feat", ["Heavy Weapon Proficiency"]]],                                                                     "words"],
    "Swimming Master" :                   ["normal", [["skills", [["athletics", 5]]]],                                                                                         "words"], # effects speed
    "Technomantic Dabbler" :              ["normal", [["ability", ["int", 15]], ["level", 5], ["class", "technomancer", "not"]],                                               "words"], # Gain the ability to cast minor technomancer spells
    "Toughness" :                         ["normal", [[]],                                                                                                                     "stamina"], # +1 Stamina Point per character level and other bonuses
    "Unfriendly Fire" :                   ["combat", [["skills", [["bluff", 5]]]],                                                                                             "words"],
    "Veiled Threat" :                     ["normal", [["ability", ["cha", 15]], ["skills", [["intimidate", 1]]]],                                                                "words"],
    "Weapon Focus" :                      ["combat", [[]],                                                               "choose"],
    "Versatile Focus" :                   ["combat", [["feat", ["Weapon Focus"]]],                                                                                             "words"],
    "Weapon Specialization" :             ["combat", [["level", 3]],                                                 "words"],
    "Versatile Specialization" :          ["combat", [["feat", ["Weapon Specialization"]], ["level", 3]],                                                                      "words"]
}
