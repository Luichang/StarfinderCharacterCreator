classesStatFocus = {
    "envoy": "Charisma or Dexterity and Intelligence",
    "mechanic": "Intelligence or Dexterity",
    "mystic": "Wisdom or Charisma",
    "operative": "Dexterity or Intelligence and Charisma",
    "solarian": "Charisma or Strength",
    "soldier": "Strength or Dexterity or Constitution",
    "technomancer": "Intelligence or Dexterity"
}

classChoseFeats = {
    "envoy": {
        "improvisation" : [
                            # 1
                            [1, "Clever Feint", "Dispiriting Taunt", "Don't Quit",
                            "Expanded Attunement", "Get 'Em", "Inspiring Boost", "Not in the Face",
                            "Universal Expression", "Watch Your Step"],
                            # 4
                            [4, "Clever Attack", "Duck Under", "Focus", "Hurry",
                            "Long-Range Improvisation", "Quick Dispiriting Taunt",
                            "Quick Inspiring Boost", "Watch Out"],
                            #6
                            [6, "Clever Improvisations", "Draw Fire", "Heads Up",
                            "Improved Get 'Em"],
                            #8
                            [8, "Desperate Defense", "Expert Attack", "Improved Hurry",
                            "Situational Awareness", "Sustained Determination"]
                        ],
        "talent" : [
                        [1, "Additional Skill Expertise", "Altered Bearing", "Analyst",
                        "Cautious Expertise", "Convincing Liar", "Cultural Savant",
                        "Cunning Disguise", "Engineering Adept", "Expert Forger", "Fast Hack",
                        "Inspired Medic", "Keen Observer", "Menacing Gaze", "Rattling Presence",
                        "Skilled Linguist", "Slick Customer", "Student of Technology", "Surgeon",
                        "Well Informed"]
                    ],
    },
    "mechanic": {
        "trick" : [
                    #2
                    [2, "Distracting Hack", "Energy Shield", "Hack Directory", "Neural Shunt",
                    "Nightvision Processor", "Overcharge", "Overclocking", "Overload Weapon",
                    "Portable Power", "Quick Patch", "Quick Repair", "Repair Drone",
                    "Visual Data Processor"],
                    #8
                    [8, "Boost Shield", "Drone Meld", "Engineer's Eye", "Ghost Intrusion",
                    "Holographic Projector", "Hyperclocking", "Improved Overcharge",
                    "Invisibility Bypass Processor", "Resistant Energy", "Scoutbot"],
                    #14
                    [14, "Extra Mod", "Improved Resistant Energy",
                    "Invisibility-Hampering Projector", "Mod Tinkerer", "Saboteur",
                    "Superior Overcharge", "Ultraclocking"]
        ]
    },
    "mystic": {
        "connection" : {
            "Akashic" : {
                "spell" : ["Identify", "Augury", "Tongues", "Divination", "Contact Other Plane",
                           "Vision"],
                "skill" : ["culture", "mysticism"],
                "feat"  : [["Akashic Knowledge"],
                           ["Access Akashic Record"],
                           ["Peer into the Future"],
                           ["Mind Probe"],
                           ["Telepathic Memories"],
                           ["Memory Palace"],
                           ["Glean Spell"]]
                },
            "Empath" :  {
                "spell" : ["Detect Thoughts", "Zone of Truth", "Clairaudience/Clairvoyance",
                           "Mind Probe", "Telepathy", "True Seeing"],
                "skill" : ["perception", "sense motive"],
                "feat"  : [["Empathy"],
                           ["Greater Mindlink"],
                           ["Emotionsense"],
                           ["Discern Lies"],
                           ["Greater Emotionsense"],
                           ["Retrocognition"],
                           ["Empathic Mastery"]]
                },
            "Healer" : {
                "spell" : ["ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR"],
                "skill" : ["medicine", "mysticism"],
                "feat"  : [["Healing Channe"],
                           ["Lifelink"],
                           ["Healer's Bond"],
                           ["Steal Life"],
                           ["Channel Bond"],
                           ["Channel Life"],
                           ["Deny Death"]]
                },
            "Mindbreaker" : {
                "spell" : ["ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR"],
                "skill" : ["bluff", "intimidate"],
                "feat"  : [["Share Pain"],
                           ["Backlash"],
                           ["Sow Doubt"],
                           ["Mental Anguish"],
                           ["Mindbreaking Link"],
                           ["Mindkiller"],
                           ["Explode Head"]]
                },
            "Overlord" : {
                "spell" : ["Command", "Hold Person", "Suggestion", "Confusion", "Dominate Person",
                           "Mass Suggestion"],
                "skill" : ["diplomacy", "intimidate"],
                "feat"  : [["Inexplicable Commands"],
                           ["Forced Amity"],
                           ["Echoes of Obedience"],
                           ["Greater Forced Amity"],
                           ["Jealous Overlord"],
                           ["Forceful Commands"],
                           ["Absolute Control"]]
                },
            "Star Shaman" : {
                "spell" : ["Shooting Stars", "Darkvision", "Irradiate", "Remove Radioactivity",
                           "Telekinesis", "Control Gravity"],
                "skill" : ["perception", "piloting"],
                "feat"  : [["Walk the Void"],
                           ["Starlight Form"],
                           ["Stargazer"],
                           ["Starflight"],
                           ["Starry Bond"],
                           ["Meteor Shower"],
                           ["Interplanetary Teleport"]]
                },
            "Xenodruid" : {
                "spell" : ["Life Bubble", "Fog Cloud", "Entropic Grasp", "Reincarnate",
                           "Commune with Nature", "Terraform"],
                "skill" : ["life science", "survival"],
                "feat"  : [["Speak with Animals"],
                           ["Grasping Vines"],
                           ["Animal Adaptation"],
                           ["Reactive Resistance"],
                           ["Share Resistance"],
                           ["Plant Transport"],
                           ["Guided Rebirth"]]
                    }
        }
    },
    "operative": {
        "exploit" : [
                        #2
                        [2, "Alien Archive", "Combat Trick", "Field Treatment",
                         "Holographic Clone", "Inoculation", "Jack of All Trades", "Nightvision",
                         "Quick Disguise", "Uncanny Mobility", "Uncanny Pilot"],
                        #6
                        [6, "Bleeding Shot", "Certainty", "Debilitating Sniper", "Enhanced Senses",
                         "Hampering Shot", "Improved Quick Movement", "Interfering Shot",
                         "Mentalist's Bane", "Speed Hacker", "Staggering Shot", "Stalwart",
                         "Sure-Footed", "Uncanny Shooter"],
                        #10
                        [10, "Cloaking Field", "Deactivating Shot", "Elusive Hacker",
                         "Ever Vigilant", "Glimpse the Truth", "Holographic Distraction",
                         "Improved Evasion", "Improved Uncanny Mobility", "Master of Disguise",
                         "Stunning Shot", "Versatile Movement"],
                        #14
                        [14, "Efficient Cloaking Field", "Knockout Shot", "Multiattack Mastery",
                         "Uncanny Senses"]
        ],
        "specialization" : {
            "Daredevil" : [["acrobatics", "athletics"], "Versatile movement", "Terrain Attack"],
            "Detective" : [["culture", "sense motive"], "Glimpse the truth","Detective's Insight"],
            "Explorer"  : [["culture", "survival"], "Ever vigilant", "Into the Unknown"],
            # Explorer: you gain a +4 bonus to Culture and Survival checks
            "Ghost"     : [["acrobatics", "stealth"], "Cloaking field", "Phase Shift Escape"],
            "Hacker"    : [["computers", "engineering"], "Elusive hacker", "Control Hack"],
            "Spy"       : [["bluff", "disguise"], "Master of disguise", "Fool Detection"],
            "Thief"     : [["perception", "sleight of hand"], "Holographic distraction",
                            "Contingency Plan"]
        }
    },
    "solarian": {
        "revelation" : [
                        #2
                        [2, "Dark Matter", "Flare", "Gravity Anchor", "Gravity Boost",
                         "Gravity Hold", "Plasma Sheath", "Radiation", "Stellar Rush"],
                        #6
                        [6, "Astrologic Sense", "Blazing Orbit", "Corona", "Crush", "Defy Gravity",
                         "Glow of Life", "Gravity Surge", "Hypnotic Glow", "Reflection"],
                        #10
                        [10, "Soul Furnace", "Stealth Warp"],
                        #14
                        [14, "Gravity Shield", "Sunbolt"],
                        #16
                        [16, "Ultimate Graviton", "Ultimate Photon"]
        ],
        "graviton" : ["bluff", "disguise", "mysticism", "sense motive", "stealth"],
        "photon" : ["culture", "diplomacy", "intimidate", "medicine", "survival"],
        "zenith" : [[1, "Miniature Star", "Ray of Light", "Solar Acceleration", "Starquake",
                    "Time Dilation", "Wormholes"]]
    },
    "soldier": {
        "gear" : [
                    #1
                    [1, "Armored Advantage", "Brutal Blast", "Bullet Barrage", "Laser Accuracy",
                        "Melee Striker"],
                    #7
                    [7, "Anchoring Arcana", "Electric Arc", "Flash Freeze", "Plasma Immolation",
                        "Powerful Explosive", "Sonic Resonance"],
                    #11
                    [11, "Heavy Onslaught"]
        ],
        "styles" : {
            # name                  1, 5, 9, 13, 17
            "arcane assailant" : ["Rune of the Eldritch Knight", "Secret of the Magi",
                                  "Power of Legend", "Secret of the Archmagi", "Arcane Attack"],
            "armor storm" : ["Hammer Fist", "Enhanced Tank", "Smash Through", "Mobile Army",
                             "On the Bounce"],
            "blitz" : ["Rapid Response", "Charge Attack", "Keep Fighting", "Perfect Opportunity",
                       "Against the Odds"],
            "bombard" : ["Grenade Expert", "Heavy Fire", "Debilitating Attack",
                         "Explosives Acumen", "Impactful Attack"],
            "guard" : ["Armor Training", "Guard's Protection", "Rapid Recovery",
                       "Kinetic Resistance", "Impenetrable Defense"],
            "hit-and-run" : ["Opening Volley", "Nimble Fusillade", "Duck and Weave",
                             "Elusive Target", "Harrying Shot"],
            "sharpshoot" : ["Sniper's Aim", "Focus Fire", "Intense Focus", "Focused Damage",
                            "Prepared Shot"]
        }
    },
    "technomancer": {
        "hack" : [
                    #2
                    [2, "Countertech", "Empowered Weapon", "Energize Spell", "Fabricate Tech",
                        "Harmful Spells", "Quick Scan", "Robot Influence", "Selective Targeting",
                        "Spell Countermeasures", "Technomantic Proficiency"],
                    #5
                    [5, "Charging Jolt", "Debug Spell", "Distant Spell", "Extended Spell",
                        "Fabricate Arms", "Magic Negation", "Spell Grenade"],
                    #8
                    [8, "Diviner's Tap", "Flash Teleport", "Mental Mark", "Spellshot",
                        "Tech Countermeasures", "Widened Spell"],
                    #11
                    [11, "Countertech Sentinel", "Eternal Spell", "Reboot Mind", "Seeking Shot"],
                    #14
                    [14, "Phase Shot", "Quickened Spell", "Rain of Fire", "Spell Library"]
        ]
    }
}

classAbilities = {
    "envoy":  [[["Envoy improvisation", "improvisation"], # one of the classChoseFeats for envoy
                ["Expertise (1d6)", "expertise"],
                ["Skill expertise (1)", "add expertise"]], # any ability, each only once

               [["Envoy improvisation", "improvisation"]],

               [["Expertise talent", "talent"],
                ["Weapon specialization", "weapon"]],
                # You gain the Weapon Specialization feat as a bonus feat for each weapon type with
                # which this class grants you proficiency

               [["Envoy improvisation", "improvisation"]],

               [["Expertise (1d6+1)", "words"],
                ["Skill expertise (2)", "add expertise"]],

               [["Envoy improvisation", "improvisation"]],

               [["Expertise talent", "talent"]],

               [["Envoy improvisation", "improvisation"]],

               [["Expertise (1d6+2)", "words"],
                ["Skill expertise (3)", "add expertise"]],

               [["Envoy improvisation", "improvisation"]],

               [["Expertise talent", "talent"]],

               [["Envoy improvisation", "improvisation"]],

               [["Expertise (1d8+2)", "words"],
                ["Skill expertise (4)", "add expertise"]],

               [["Envoy improvisation", "improvisation"]],

               [["Expertise talent", "talent"]],

               [["Envoy improvisation", "improvisation"]],

               [["Expertise (1d8+3)", "words"],
                ["Skill expertise (5)", "add expertise"]],

               [["Envoy improvisation", "improvisation"]],

               [["Expertise talent", "talent"]],

               [["Envoy improvisation", "improvisation"],
                ["Expertise (1d8+4)", "words"],
                ["True expertise", "words"]],
                # maybe add in a selection from the selected envoy improvisation but it really is
                # just words
             ]

    ,
    "mechanic":[[["Artificial intelligence", "words"],
                # might want a selector between Drone and Exocortex
                 ["Bypass +1", "words"],
                 ["Custom rig", "words"]],

                [["Mechanic trick", "trick"]], # TODO

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
                 ["Superior rig", "words"]],
                 # gains the counter measures of lock out and wipe as a bonus

                [["Bypass +6", "words"],
                 ["Mechanic trick", "trick"],
                 ["Tech master", "words"]],
             ]
    ,
    "mystic":  [[["Connection", "connection"],
                 ["Connection power", "cpower", 0], # 1
                 ["Connection spell", "spell", 0],
                 ["Healing touch", "words"]],

                [["Channel skill +1", "channel"],
                 ["Mindlink", "words"]],

                [["Connection power", "cpower", 1], # 3
                 ["Weapon specialization", "weapon"]],

                [["Connection spell", "spell", 1]],

                [["Channel skill +2", "channel"]],

                [["Connection power", "cpower", 2]], # 6

                [["Connection spell", "spell", 2]],

                [["Channel skill +3", "channel"]],

                [["Connection power", "cpower", 3]], # 9

                [["Connection spell", "spell", 3]],

                [["Channel skill +4", "channel"],
                 ["Telepathic bond", "words"]],

                [["Connection power", "cpower", 4]], # 12

                [["Connection spell", "spell", 4]],

                [["Channel skill +5", "channel"]],

                [["Connection power", "cpower", 5]], # 15

                [["Connection spell", "spell", 5]],

                [["Channel skill +6", "channel"]],

                [["Connection power", "cpower", 6]], # 18

                [["Transcendence", "words"]],

                [["Channel skill +7", "channel"],
                 ["Enlightenment", "words"]],
             ]
    ,
    "operative":   [[["Operative's edge +1", "edge"], # edge, specialization, exploit
                     ["Specialization", "specialization", ["feat", "Skill Focus"]],
                     ["Trick attack +1d4", "words"]],

                    [["Evasion", "words"],
                     ["Operative exploit", "exploit"]],

                    [["Operative's edge +2", "edge"],
                     ["Quick movement (+10 ft.)", "words"],
                     ["Trick attack +1d8", "words"],
                     ["Weapon specialization", "weapon"]],

                    [["Debilitating trick", "words"],
                     ["Operative exploit", "exploit"]],

                    [["Specialization exploit", "specialization", ["exploit"]],
                     ["Trick attack +3d8", "words"]],

                    [["Operative exploit", "exploit"]],

                    [["Operative's edge +3", "edge"],
                     ["Specialization skill mastery", "words"],
                     ["Trick attack +4d8", "words"],
                     ["Uncanny agility", "words"]],

                    [["Operative exploit", "exploit"],
                     ["Triple attack", "words"]],

                    [["Quick movement (+20 ft.)", "words"],
                     ["Trick attack +5d8", "words"]],

                    [["Operative exploit", "exploit"]],

                    [["Operative's edge +4", "edge"],
                     ["Specialization power", "specialization", ["power"]],
                     ["Trick attack +6d8", "words"]],

                    [["Operative exploit", "exploit"]],

                    [["Quad attack", "words"],
                     ["Trick attack +7d8", "words"]],

                    [["Operative exploit", "exploit"]],

                    [["Operative's edge +5", "edge"],
                     ["Quick movement (+30 ft.)", "words"],
                     ["Trick attack +8d8", "words"]],

                    [["Operative exploit", "exploit"]],

                    [["Double debilitation", "words"],
                     ["Trick attack +9d8", "words"]],

                    [["Operative exploit", "exploit"]],

                    [["Operative's edge +6", "edge"],
                     ["Trick attack +10d8", "words"]],

                    [["Operative exploit", "exploit"],
                     ["Supreme operative", "words"]],
             ]
    ,
    "solarian": [[["Skill adept", "class", [["any"], ["any"]]], # class, revelation, influence, zenith, None
                  ["Solar manifestation", "words"],
                  # chose either weapon or armor and chose either glowing star or
                  # darkness black hole
                  ["Stellar mode", "words"],
                  ["Stellar revelation (black hole, supernova)", "revelation"]],

                 [["Stellar revelation", "revelation"]],

                 [["Sidereal influence (2 skills)", "influence"],
                  ["Weapon specialization", "weapon"]],

                 [["Stellar revelation", "revelation"]],

                 [["None", "None"]],

                 [["Stellar revelation", "revelation"]],

                 [["Flashing strikes", "words"]],

                 [["Stellar revelation", "revelation"]],

                 [["Zenith revelations", "zenith"]],

                 [["Stellar revelation", "revelation"]],

                 [["Sidereal influence (4 skills)", "influence"]],

                 [["Stellar revelation", "revelation"]],

                 [["Solarian's onslaught", "words"]],

                 [["Stellar revelation", "revelation"]],

                 [["None", "None"]],

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
                 ["Soldier's onslaught", "words"]],

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
    "technomancer": [[["Spell cache", "words"]], # hack, feat, skills

                     [["Magic hack", "hack"]],

                     [["Spell Focus", "feat", "Spell Focus"],
                      ["Techlore +1", "skills", [["computers", 1], ["mysticism", 1]]],
                      ["Weapon specialization", "weapon"]],


                     [["None", "None"]],

                     [["Magic hack", "hack"]],

                     [["Cache capacitor 1", "words"],
                      ["Techlore +2", "skills", [["computers", 1], ["mysticism", 1]]]],


                     [["None", "None"]],

                     [["Magic hack", "hack"]],

                     [["Techlore +3", "skills", [["computers", 1], ["mysticism", 1]]]],

                     [["None", "None"]],

                     [["Magic hack", "hack"]],

                     [["Cache capacitor 2", "words"],
                      ["Techlore +4", "skills", [["computers", 1], ["mysticism", 1]]]],

                     [["None", "None"]],

                     [["Magic hack", "hack"]],

                     [["Techlore +5", "skills", [["computers", 1], ["mysticism", 1]]]],

                     [["None", "None"]],

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
        "proficiencies" : ["Light Armor Proficiency", "Basic Melee Weapon Proficiency",
                           "Grenade Proficiency", "Small Arm Proficiency"],
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
                "sleight of hand"  : 3,
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
        "proficiencies" : ["Light Armor Proficiency", "Basic Melee Weapon Proficiency",
                           "Grenade Proficiency", "Small Arm Proficiency"],
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
                "sleight of hand"  : 0,
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
        "proficiencies" : ["Light Armor Proficiency", "Basic Melee Weapon Proficiency",
                           "Small Arm Proficiency"],
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
                "sleight of hand"  : 0,
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
        "proficiencies" : ["Light Armor Proficiency", "Basic Melee Weapon Proficiency",
                           "Small Arm Proficiency", "Sniper Weapon Proficiency"],
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
                "sleight of hand"  : 3,
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
        "proficiencies" : ["Light Armor Proficiency", "Basic Melee Weapon Proficiency",
                           "Advanced Melee Weapon Proficiency", "Small Arm Proficiency"],
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
                "sleight of hand"  : 0,
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
        "proficiencies" : ["Light Armor Proficiency", "Heavy Armor Proficiency",
                           "Basic Melee Weapon Proficiency", "Advanced Melee Weapon Proficiency",
                           "Small Arm Proficiency", "Longarm Proficiency",
                           "Heavy Weapon Proficiency", "Sniper Weapon Proficiency",
                           "Grenade Proficiency"],
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
                "sleight of hand"  : 0,
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
        "proficiencies" : ["Light Armor Proficiency", "Basic Melee Weapon Proficiency",
                           "Small Arm Proficiency"],
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
                "sleight of hand"  : 3,
                "stealth"          : 0,
                "survival"         : 0
        }
    }
}

class_feat_replacables = ["Expertise", "Skill expertise", "Bypass", "Miracle worker",
                          "Coordinated assault", "Channel skill", "Operative's edge",
                          "Trick attack", "Sidereal influence", "Techlore", "Cache capacitor",
                          "Quick movement"]
