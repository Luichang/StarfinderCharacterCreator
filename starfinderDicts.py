possibleAttributes = ["str", "strength", "dex", "dexterity", "con", "constitution",
                      "int", "inteligence", "wis", "wisdom", "cha", "charisma"]

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

themes = {
    "ace pilot":     {"strength" : 0, "dexterity" : 1, "constitution" : 0, "intelligence" : 0,
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
                      "wisdom" : 0, "charisma" : 0}
}

classesStatFocus = {
    "envoy": "Charisma or Dexterity and Intelligence",
    "mechanic": "Intelligence or Dexterity",
    "mystic": "Wisdom or Charisma",
    "operative": "Dexterity or Intelligence and Charisma",
    "solarian": "Charisma or Strength",
    "soldier": "Strength or Dexterity or Constitution",
    "technomancer": "Intelligence or Dexterity"
}

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

raceAbilities = {
    "android"            : [["Constructed", "words"],
                            ["Exceptional vision", "words"],
                            ["Flat affect", "stats", [["sense motive", -2]]],
                            ["Upgrade slot", "words"]] ,

     "human"             : [["Bonus feat", "feat"],
                            # Humans select one extra feat at 1st level
                            ["Skilled", "words"]] ,
                            # Humans gain an additional skill rank at 1st level and each level thereafter

     "kasatha"           : [["Desert stride", "words"],
                            ["Four-armed", "words"],
                            ["Historian", "stats", [["culture", 2]]],
                            ["Natural grace", "stats", [["acrobatics", 2], ["athletics", 2]]]] ,

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
                            ["Cultural fascination", "stats", [["culture", 2], ["diplomacy", 2]]],
                            ["Limited telepathy", "words"]] ,

     "vesk"              : [["Armor savant", "words"],
                            ["Fearless", "words"],
                            ["Low-light vision", "words"],
                            ["Natural weapons", "words"]] ,

     "ysoki"             : [["Cheek pouches", "words"],
                            ["Darkvision", "words"],
                            ["Moxie", "words"],
                            ["Scrounger", "stats", [["engineering", 2], ["stealth", 2], ["survival", 2]]]]
}

themeAbilities = {
    "ace pilot":       [["Theme knowledge", "piloting"], # piloting becomes class knowledge or +1 bonus to checks
                        ["Lone wolf", "words"],
                        ["Need for speed", "words"],
                        ["Master pilot", "words"]],

    "bounty hunter":   [["Theme knowledge", "survival"], # survival becomes class knowledge or +1 bonus to checks
                        ["Swift hunter", "words"],
                        ["Relentless", "words"],
                        ["Master hunter", "words"]],

    "icon":            [["Theme knowledge", ["profession", "profession2"]],
                        # chose a profession receive +1 to checks, culture becomes class knowledge or +1 bonus to checks
                        ["Celebrity", "words"],
                        ["Megacelebrity", "words"],
                        ["Master icon", "words"]],

    "mercenary":       [["Theme knowledge", "athletics"], # athletics becomes class knowledge or +1 bonus to checks
                        ["Grunt", "words"], # carrying limit increases
                        ["Squad leader", "words"],
                        ["Commander", "words"]],

    "outlaw":          [["Theme knowledge", "slight of hand"], # slight of hand becomes class knowledge or +1 bonus to checks
                        ["Legal corruption", "words"],
                        ["Black market connections", "words"],
                        ["Master outlaw", "words"]],

    "priest":          [["Theme knowledge", "mysticism"], # mysticism becomes class knowledge or +1 bonus to checks
                        ["Mantle of the clergy", "words"],
                        ["Divine boon", "spell"],
                        # ^ Choose one 1st-level mystic spell with some connection to your deity’s portfolio
                        # (subject to the GM’s approval). If you have levels in the mystic class, you gain 1
                        # additional 1stlevel spell per day and add the chosen spell to your list of mystic
                        # spells known. Otherwise, you can use the chosen spell once per day as a spell-like ability.
                        ["True communion", "words"]],

    "scholar":         [["Theme knowledge", ["life science", "physical science"]],
                        # chose either life or physical science, that becomes class knowledge or +1 bonus to checks
                        ["Tip of the tongue", "words"],
                        ["Research maven", "words"],
                        ["Master scholar", "words"]],

    "spacefarer":      [["Theme knowledge", "physical science"], # physical science becomes class knowledge or +1 bonus to checks
                        ["Eager dabbler", "?"], # +2 bonus to skill checks for skills with 0 ranks in skill
                        ["Jack of all trades", "words"],
                        ["Master explorer", "words"]],

    "xenoseeker":      [["Theme knowledge", "life science"], # life science becomes class knowledge or +1 bonus to checks
                        ["Quick pidgin", "words"],
                        ["First contact", "words"],
                        ["Brilliant discovery", "words"]],

    "themeless":       [["General knowledge", "any"], # chose a skill that becomes class knowledge or +1 bonus to checks
                        ["Certainty", "words"],
                        ["Extensive studies", "words"],
                        ["Steely determination", "words"]]
}

classChoseFeats = {
    "envoy": {
        "improvisation" : [
                            ["Clever Feint", "Dispiriting Taunt", "Don’t Quit", "Expanded Attunement", "Get ’Em",
                            "Inspiring Boost", "Not in the Face", "Universal Expression", "Watch Your Step"],
                            ["Clever Attack", "Duck Under", "Focus", "Hurry", "Long-Range Improvisation",
                            "Quick Dispiriting Taunt", "Quick Inspiring Boost", "Watch Out"],
                            ["Clever Improvisations", "Draw Fire", "Heads Up", "Improved Get ’Em"],
                            ["Desperate Defense", "Expert Attack", "Improved Hurry", "Situational Awareness",
                            "Sustained Determination"]
                        ],
        "talent" : [
                        ["Additional Skill Expertise", "Altered Bearing", "Analyst", "Cautious Expertise",
                        "Convincing Liar", "Cultural Savant", "Cunning Disguise", "Engineering Adept",
                        "Expert Forger", "Fast Hack", "Inspired Medic", "Keen Observer", "Menacing Gaze",
                        "Rattling Presence", "Skilled Linguist", "Slick Customer", "Student of Technology",
                        "Surgeon", "Well Informed"]
                    ],
    },
    "mechanic": {
        "trick" : [
                    ["Distracting Hack", "Energy Shield", "Hack Directory", "Neural Shunt", "Nightvision Processor",
                    "Overcharge", "Overclocking", "Overload Weapon", "Portable Power",
                    "Quick Patch", "Quick Repair", "Repair Drone", "Visual Data Processor"],
                    ["Boost Shield", "Drone Meld", "Engineer’s Eye", "Ghost Intrusion", "Holographic Projector",
                    "Hyperclocking", "Improved Overcharge", "Invisibility Bypass Processor", "Resistant Energy",
                    "Scoutbot"],
                    ["Extra Mod", "Improved Resistant Energy", "Invisibility-Hampering Projector", "Mod Tinkerer",
                    "Saboteur", "Superior Overcharge", "Ultraclocking"]
        ]
    },
    "mystic": [],
    "operative": {
        "exploit" : [
                        ["Alien Archive", "Combat Trick", "Field Treatment", "Holographic Clone", "Inoculation",
                        "Jack of All Trades", "Nightvision", "Quick Disguise", "Uncanny Mobility", "Uncanny Pilot",],
                        ["Bleeding Shot", "Certainty", "Debilitating Sniper", "Enhanced Senses", "Hampering Shot",
                        "Improved Quick Movement", "Interfering Shot", "Mentalist’s Bane", "Speed Hacker",
                        "Staggering Shot", "Stalwart", "Sure-Footed", "Uncanny Shooter"],
                        ["Cloaking Field", "Deactivating Shot", "Elusive Hacker", "Ever Vigilant",
                        "Glimpse the Truth", "Holographic Distraction", "Improved Evasion", "Improved Uncanny Mobility",
                        "Master of Disguise", "Stunning Shot", "Versatile Movement"],
                        ["Efficient Cloaking Field", "Knockout Shot", "Multiattack Mastery", "Uncanny Senses"]
        ]
    },
    "solarian": {
        "revelation" : [
                        ["Dark Matter", "Flare", "Gravity Anchor", "Gravity Boost", "Gravity Hold", "Plasma Sheath",
                        "Radiation", "Stellar Rush"],
                        ["Astrologic Sense", "Blazing Orbit", "Corona", "Crush", "Defy Gravity", "Glow of Life",
                        "Gravity Surge", "Hypnotic Glow", "Reflection"],
                        ["Soul Furnace", "Stealth Warp"],
                        ["Gravity Shield", "Sunbolt"],
                        ["Ultimate Graviton", "Ultimate Photon"]
        ],
        "zenith" : ["Miniature Star", "Ray of Light", "Solar Acceleration", "Starquake", "Time Dilation", "Wormholes"]
    },
    "soldier": {
        "gear" : [
                    ["Armored Advantage", "Brutal Blast", "Bullet Barrage", "Laser Accuracy", "Melee Striker"],
                    ["Anchoring Arcana", "Electric Arc", "Flash Freeze", "Plasma Immolation", "Powerful Explosive",
                    "Sonic Resonance"],
                    ["Heavy Onslaught"]
        ],
        "styles" : {
            "arcane assailant" : ["Rune of the Eldritch Knight", "Secret of the Magi", "Power of Legend",
            "Secret of the Archmagi", "Arcane Attack"],
            "armor storm" : ["Hammer Fist", "Enhanced Tank", "Smash Through", "Mobile Army", "On the Bounce"],
            "blitz" : ["Rapid Response", "Charge Attack", "Keep Fighting", "Perfect Opportunity", "Against the Odds"],
            "bombard" : ["Grenade Expert", "Heavy Fire", "Debilitating Attack", "Explosives Acumen", "Impactful Attack"],
            "guard" : ["Armor Training", "Guard’s Protection", "Rapid Recovery", "Kinetic Resistance",
                        "Impenetrable Defense"],
            "hit-and-run" : ["Opening Volley", "Nimble Fusillade", "Duck and Weave", "Elusive Target", "Harrying Shot"],
            "sharpshoot" : ["Sniper’s Aim", "Focus Fire", "Intense Focus", "Focused Damage", "Prepared Shot", ]
        }
    },
    "technomancer": {
        "hack" : [
                    ["Countertech", "Empowered Weapon", "Energize Spell", "Fabricate Tech", "Harmful Spells",
                    "Quick Scan", "Robot Influence", "Selective Targeting", "Spell Countermeasures",
                    "Technomantic Proficiency"],
                    ["Charging Jolt", "Debug Spell", "Distant Spell", "Extended Spell", "Fabricate Arms",
                    "Magic Negation", "Spell Grenade"],
                    ["Diviner’s Tap", "Flash Teleport", "Mental Mark", "Spellshot", "Tech Countermeasures",
                    "Widened Spell"],
                    ["Countertech Sentinel", "Eternal Spell", "Reboot Mind", "Seeking Shot"],
                    ["Phase Shot", "Quickened Spell", "Rain of Fire", "Spell Library"]
        ]
    }
}

classAbilities = {
    "envoy":  [[["Envoy improvisation", "improvisation"], # one of the classChoseFeats for envoy
                ["Expertise (1d6)", "words"], # maybe worth creating an array with all expertise skills
                ["Skill expertise", "add expertise"]], # any ability, each only once

               [["Envoy improvisation", "improvisation"]],

               [["Expertise talent", "talent"],
                ["Weapon specialization", "weapon"]],
                # You gain the Weapon Specialization feat as a bonus feat for each weapon type with which this
                # class grants you proficiency

               [["Envoy improvisation", "class up"]],

               [["Expertise (1d6+1)", "words"],
                ["Skill expertise", "add expertise"]],

               [["Envoy improvisation", "improvisation"]],

               [["Expertise talent", "talent"]],

               [["Envoy improvisation", "improvisation"]],

               [["Expertise (1d6+2)", "words"],
                ["Skill expertise", "add expertise"]],

               [["Envoy improvisation", "improvisation"]],

               [["Expertise talent", "talent"]],

               [["Envoy improvisation", "improvisation"]],

               [["Expertise (1d8+2)", "words"],
                ["Skill expertise", "add expertise"]],

               [["Envoy improvisation", "improvisation"]],

               [["Expertise talent", "talent"]],

               [["Envoy improvisation", "improvisation"]],

               [["Expertise (1d8+3)", "words"],
                ["Skill expertise", "add expertise"]],

               [["Envoy improvisation", "improvisation"]],

               [["Expertise talent", "talent"]],

               [["Envoy improvisation", "class up"],
                ["Expertise (1d8+4)", "words"],
                ["True expertise", "words"]],
                # maybe add in a selection from the selected envoy improvisation but it really is just words
             ]

    ,
    "mechanic":[[["Artificial intelligence", "words"], # might want a selector between Drone and Exocortex
                 ["Bypass +1", "words"],
                 ["Custom rig", "words"]],

                 ["Mechanic trick", "trick"],

                [["Overload", "words"],
                 ["Weapon specialization", "weapon"]],

                [["Mechanic trick", "trick"]],

                [["Bypass +2", "words"],
                 ["Remote hack", "words"]],

                [["Mechanic trick", "trick"]],

                [["Expert rig", "words"],
                 ["Miracle worker 1/day", "words"]],

                [["Mechanic trick", "trick"]],

                [["Bypass +3", "words"],
                 ["Override", "words"]],

                [["Mechanic trick", "trick"]],

                [["Coordinated assault +1", "words"],
                 ["Miracle worker 2/day", "words"]],

                [["Mechanic trick", "trick"]],

                [["Advanced rig", "words"], # gains a counter measure of firewall as a bonus
                 ["Bypass +4", "words"]],

                [["Mechanic trick", "trick"]],

                [["Miracle worker 3/day", "words"]],

                [["Mechanic trick", "trick"]],

                [["Bypass +5", "words"],
                 ["Control net", "words"],
                 ["Coordinated assault +2", "words"]],

                [["Mechanic trick", "trick"]],

                [["Ghost in the machine", "words"],
                 ["Miracle worker 4/day", "words"],
                 ["Superior rig", "words"]], # gains the counter measures of lock out and wipe as a bonus

                [["Bypass +6", "words"],
                 ["Mechanic trick", "trick"],
                 ["Tech master", "words"]],
             ]
    ,
    "mystic":  [[["Connection"],
                 ["Connection power"],
                 ["Connection spell"],
                 ["Healing touch", "words"]],

                [["Channel skill +1"],
                 ["Mindlink", "words"]],

                [["Connection power"],
                 ["Weapon specialization", "weapon"]],

                [["Connection spell"]],

                [["Channel skill +2"]],

                [["Connection power"]],

                [["Connection spell"]],

                [["Channel skill +3"]],

                [["Connection power"]],

                [["Connection spell"]],

                [["Channel skill +4"],
                 ["Telepathic bond", "words"]],

                [["Connection power"]],

                [["Connection spell"]],

                [["Channel skill +5"]],

                [["Connection power"]],

                [["Connection spell"]],

                [["Channel skill +6"]],

                [["Connection powe"]],

                [["Transcendence", "words"]],

                [["Channel skill +7"],
                 ["Enlightenment", "words"]],
             ]
    ,
    "operative":   [[["Operative’s edge +1"], # +1 insight bonus to initiative checks and to skill checks
                     ["Specialization"],
                     ["Trick attack +1d4", "words"]],

                    [["Evasion", "words"],
                     ["Operative exploit"]],

                    [["Operative’s edge +2"],
                     ["Quick movement (+10 ft.)", "words"],
                     ["Trick attack +1d8", "words"],
                     ["Weapon specialization", "weapon"]],

                    [["Debilitating trick", "words"],
                     ["Operative exploit"]],

                    [["Specialization exploit"],
                     ["Trick attack +3d8", "words"]],

                    [["Operative exploit"]],

                    [["Operative’s edge +3"],
                     ["Specialization skill mastery"],
                     ["Trick attack +4d8", "words"],
                     ["Uncanny agility", "words"]],

                    [["Operative exploit"],
                     ["Triple attack", "words"]],

                    [["Quick movement (+20 ft.)", "words"],
                     ["Trick attack +5d8", "words"]],

                    [["Operative exploit"]],

                    [["Operative’s edge +4"],
                     ["Specialization power"],
                     ["Trick attack +6d8", "words"]],

                    [["Operative exploit"]],

                    [["Quad attack", "words"],
                     ["Trick attack +7d8", "words"]],

                    [["Operative exploit"]],

                    [["Operative’s edge +5"],
                     ["Quick movement (+30 ft.)", "words"],
                     ["Trick attack +8d8", "words"]],

                    [["Operative exploit"]],

                    [["Double debilitation", "words"],
                     ["Trick attack +9d8", "words"]],

                    [["Operative exploit"]],

                    [["Operative’s edge +6"],
                     ["Trick attack +10d8", "words"]],

                    [["Operative exploit"],
                     ["Supreme operative", "words"]],
             ]
    ,
    "solarian": [[["Skill adept", "skills", [["any"], ["any"]]],
                  ["Solar manifestation"],
                  # chose either weapon or armor and chose either glowing star or darkness black hole
                  ["Stellar mode", "words"],
                  ["Stellar revelation (black hole, supernova)", "revelation"]],

                 [["Stellar revelation", "revelation"]],

                 [["Sidereal influence (2 skills)", "influence"],
                  ["Weapon specialization", "weapon"]],

                 [["Stellar revelation", "revelation"]],

                 [[]],

                 [["Stellar revelation", "revelation"]],

                 [["Flashing strikes", "words"]],

                 [["Stellar revelation", "revelation"]],

                 [["Zenith revelations", "zenith"]],

                 [["Stellar revelation", "revelation"]],

                 [["Sidereal influence (4 skills)", "influence"]],

                 [["Stellar revelation", "revelation"]],

                 [["Solarian’s onslaught", "words"]],

                 [["Stellar revelation", "revelation"]],

                 [[]],

                 [["Stellar revelation", "revelation"]],

                 [["Zenith revelations", "zenith"]],

                 [["Stellar revelation", "revelation"]],

                 [["Sidereal influence (6 skills)", "influence"]],

                 [["Stellar paragon", "words"],
                  ["Stellar revelation", "revelation"]],
             ]
    ,
    "soldier": [[["Primary Fighting style", "style"],
                 ["Primary style technique", "technique1"]],

                [["Combat feat", "combat"]],

                [["Gear boost", "gear"],
                 ["Weapon specialization", "weapon"]],

                [["Combat feat", "combat"]],

                [["Primary style technique", "technique1"]],

                [["Combat feat", "combat"]],

                [["Gear boost", "gear"]],

                [["Combat feat", "combat"]],

                [["Primary style technique", "technique1"],
                 ["Secondary fighting style", "style"],
                 ["Secondary style technique", "technique2"]],

                [["Combat feat", "combat"]],

                [["Gear boost", "gear"],
                 ["Soldier’s onslaught", "words"]],

                [["Combat feat", "combat"]],

                [["Primary style technique", "technique1"],
                 ["Secondary style technique", "technique2"]],

                [["Combat feat", "combat"]],

                [["Gear boost", "gear"]],

                [["Combat feat", "combat"]],

                [["Primary style technique", "technique1"],
                 ["Secondary style technique", "technique2"]],

                [["Combat feat", "combat"]],

                [["Gear boost", "gear"]],

                [["Combat feat", "combat"],
                 ["Kill shot", "words"]],
             ]
    ,
    "technomancer": [[["Spell cache", "words"]],

                     [["Magic hack", "hack"]],

                     [["Spell Focus", "feat", "Spell Focus"],
                      ["Techlore +1", "skills", [["computers", 1], ["mysticism", 1]]],
                      ["Weapon specialization", "weapon"]],


                     [[]],

                     [["Magic hack", "hack"]],

                     [["Cache capacitor 1", "words"],
                      ["Techlore +2", "skills", [["computers", 1], ["mysticism", 1]]]],


                     [[]],

                     [["Magic hack", "hack"]],

                     [["Techlore +3", "skills", [["computers", 1], ["mysticism", 1]]]],

                     [[]],

                     [["Magic hack", "hack"]],

                     [["Cache capacitor 2", "words"],
                      ["Techlore +4", "skills", [["computers", 1], ["mysticism", 1]]]],

                     [[]],

                     [["Magic hack", "hack"]],

                     [["Techlore +5", "skills", [["computers", 1], ["mysticism", 1]]]],

                     [[]],

                     [["Magic hack", "hack"]],

                     [["Cache capacitor 3", "words"],
                      ["Techlore +6", "skills", [["computers", 1], ["mysticism", 1]]]],

                     [["Resolve attunement", "words"]],

                     [["Fuse spells", "words"],
                      ["Magic hack", "hack"]],
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
}
