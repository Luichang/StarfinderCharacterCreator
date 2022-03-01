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

themeAbilities = {
    "ace pilot":       [["Theme knowledge", "piloting"],
                        # piloting becomes class knowledge or +1 bonus to checks
                        ["Lone wolf", "words"],
                        ["Need for speed", "words"],
                        ["Master pilot", "words"]],

    "bounty hunter":   [["Theme knowledge", "survival"],
                        # survival becomes class knowledge or +1 bonus to checks
                        ["Swift hunter", "words"],
                        ["Relentless", "words"],
                        ["Master hunter", "words"]],

    "icon":            [["Theme knowledge", ["profession", "profession2"]],
                        # chose a profession receive +1 to checks, culture becomes class knowledge
                        # or +1 bonus to checks
                        ["Celebrity", "words"],
                        ["Megacelebrity", "words"],
                        ["Master icon", "words"]],

    "mercenary":       [["Theme knowledge", "athletics"],
                        # athletics becomes class knowledge or +1 bonus to checks
                        ["Grunt", "words"], # carrying limit increases
                        ["Squad leader", "words"],
                        ["Commander", "words"]],

    "outlaw":          [["Theme knowledge", "sleight of hand"],
                        # sleight of hand becomes class knowledge or +1 bonus to checks
                        ["Legal corruption", "words"],
                        ["Black market connections", "words"],
                        ["Master outlaw", "words"]],

    "priest":          [["Theme knowledge", "mysticism"],
                        # mysticism becomes class knowledge or +1 bonus to checks
                        ["Mantle of the clergy", "words"],
                        ["Divine boon", "spell"],
                        # ^ Choose one 1st-level mystic spell with some connection to your deity's
                        # portfolio (subject to the GM's approval). If you have levels in the
                        # mystic class, you gain 1 additional 1stlevel spell per day and add the
                        # chosen spell to your list of mystic spells known. Otherwise, you can use
                        # the chosen spell once per day as a spell-like ability.
                        ["True communion", "words"]],

    "scholar":         [["Theme knowledge", ["life science", "physical science"]],
                        # chose either life or physical science, that becomes class knowledge or
                        # +1 bonus to checks
                        ["Tip of the tongue", "words"],
                        ["Research maven", "words"],
                        ["Master scholar", "words"]],

    "spacefarer":      [["Theme knowledge", "physical science"],
                        # physical science becomes class knowledge or +1 bonus to checks
                        ["Eager dabbler", "dabbler"],
                        # +2 bonus to skill checks for skills with 0 ranks in skill
                        ["Jack of all trades", "words"],
                        ["Master explorer", "words"]],

    "xenoseeker":      [["Theme knowledge", "life science"],
                        # life science becomes class knowledge or +1 bonus to checks
                        ["Quick pidgin", "words"],
                        ["First contact", "words"],
                        ["Brilliant discovery", "words"]],

    "themeless":       [["General knowledge", "any"],
                        # chose a skill that becomes class knowledge or +1 bonus to checks
                        ["Certainty", "words"],
                        ["Extensive studies", "words"],
                        ["Steely determination", "words"]]
}
