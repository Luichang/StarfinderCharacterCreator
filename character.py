import math
from bs4 import BeautifulSoup
from starfinderDicts import *
from feats import feats

class character:
    def __init__(self, fileName=""):

        self.spellLevel = -1

        self.chosenFeats = []
        self.classFeats = []
        self.styles = [] # this is soldier exclusive

        self.mods = {
            "str" : 0,
            "dex" : 0,
            "con" : 0,
            "int" : 0,
            "cha" : 0
        }

        self.attributes = {
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10
        }

        self.abilityIncreases = {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0
        }

        self.skills = {
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
            "profession"       : 0, #?????????????????
            "profession2"      : 0, #?????????????????
            "sense motive"     : 0,
            "sleight of hand"   : 0,
            "stealth"          : 0,
            "survival"         : 0,
        }

        self.skillRanks = {
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
            "profession2"     : 0,
            "sense motive"    : 0,
            "sleight of hand"  : 0,
            "stealth"         : 0,
            "survival"        : 0
        }

        self.skillClass = {
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
            "profession2"     : 0,
            "sense motive"    : 0,
            "sleight of hand"  : 0,
            "stealth"         : 0,
            "survival"        : 0
        }

        self.skillMisc = {
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
            "profession2"     : 0,
            "sense motive"    : 0,
            "sleight of hand"  : 0,
            "stealth"         : 0,
            "survival"        : 0
        }

        self.spentPoints = {"Str" : 0, "Dex" : 0, "Con" : 0, "Int" : 0, "Wis": 0, "Cha" : 0}
        self.themeAttributes = themes["themeless"]

        self.classLevel = 1

        if fileName == "":
            self.createNew()
        else:
            self.readFromHTML(fileName)


    def createNew(self):
        self.name = self.getUserResponse([""], "Enter a Character Name", False)

        self.writeToFile(htmlTags["name"], self.name)

        self.raceName = self.getUserResponse(["android", "human", "kasatha", "lashunta(korasha)",
                                              "lashunta(damaya)", "shirren", "vesk", "ysoki"],
                                              """Please chose a race, options are: android, human, kasatha, lashunta(korasha), lashunta(damaya), shirren, vesk, ysoki"""
                                            )

        listToWriteToFile = []
        listToWriteToFile.append([htmlTags["race"], self.raceName])
        listToWriteToFile.append([htmlTags["raceStr"], raceStatList[self.raceName]["strength"]])
        listToWriteToFile.append([htmlTags["raceDex"], raceStatList[self.raceName]["dexterity"]])
        listToWriteToFile.append([htmlTags["raceCon"], raceStatList[self.raceName]["constitution"]])
        listToWriteToFile.append([htmlTags["raceInt"], raceStatList[self.raceName]["intelligence"]])
        listToWriteToFile.append([htmlTags["raceWis"], raceStatList[self.raceName]["wisdom"]])
        listToWriteToFile.append([htmlTags["raceCha"], raceStatList[self.raceName]["charisma"]])

        self.writeToFile("listPass", listToWriteToFile)

        raceAttributes = raceStatList[self.raceName]

        if self.raceName == "human":
            entered = self.getUserResponse(possibleAttributes,
                                           """Humans get to increase one stat by 2. Possible attributes: (str)ength, (dex)terity, (con)stitution, (int)elligence, (wis)dom, (cha)risma""")

            raceAttributes[attributeShorthand[entered]] = 2

            htmlEnteredTag = "race" + attributeShortener[attributeShorthand[entered]]

            self.raceName += " (" + entered + ")"

            listToWriteToFile = []
            listToWriteToFile.append([htmlTags["race"], self.raceName])
            listToWriteToFile.append([htmlTags[htmlEnteredTag], 2])
            self.writeToFile("listPass", listToWriteToFile)

        self.theme = self.getUserResponse(["ace pilot", "bounty hunter", "icon", "mercenary", "outlaw", "priest",
                                        "scholar", "spacefarer", "xenoseeker", "themeless"],
                                          """Chose a theme. Possible themes are: "ace pilot, bounty hunter, icon, mercenary, outlaw, priest, scholar, spacefarer, xenoseeker, themeless""")

        self.writeToFile(htmlTags["theme"], self.theme)

        self.themeAttributes = themes[self.theme]
        if self.theme == "themeless":
            entered = self.getUserResponse(possibleAttributes,
                                           """Themeless get to increase one stat by 1. Possible attributes: (str)ength, (dex)terity, (con)stitution, (int)elligence, (wis)dom, (cha)risma""")

            self.themeAttributes[attributeShorthand[entered]] = 1
            self.theme += " (" + entered + ")"
            self.writeToFile(htmlTags["theme"], self.theme)

        listToWriteToFile = []
        listToWriteToFile.append([htmlTags["themeStr"], self.themeAttributes["strength"]])
        listToWriteToFile.append([htmlTags["themeDex"], self.themeAttributes["dexterity"]])
        listToWriteToFile.append([htmlTags["themeCon"], self.themeAttributes["constitution"]])
        listToWriteToFile.append([htmlTags["themeInt"], self.themeAttributes["intelligence"]])
        listToWriteToFile.append([htmlTags["themeWis"], self.themeAttributes["wisdom"]])
        listToWriteToFile.append([htmlTags["themeCha"], self.themeAttributes["charisma"]])
        self.writeToFile("listPass", listToWriteToFile)

        self.attributes["strength"]     = 10 + raceAttributes["strength"]     + self.themeAttributes["strength"]
        self.attributes["dexterity"]    = 10 + raceAttributes["dexterity"]    + self.themeAttributes["dexterity"]
        self.attributes["constitution"] = 10 + raceAttributes["constitution"] + self.themeAttributes["constitution"]
        self.attributes["intelligence"] = 10 + raceAttributes["intelligence"] + self.themeAttributes["intelligence"]
        self.attributes["wisdom"]       = 10 + raceAttributes["wisdom"]       + self.themeAttributes["wisdom"]
        self.attributes["charisma"]     = 10 + raceAttributes["charisma"]     + self.themeAttributes["charisma"]

        listToWriteToFile = []
        listToWriteToFile.append([htmlTags["attrStr"], self.attributes["strength"]])
        listToWriteToFile.append([htmlTags["attrDex"], self.attributes["dexterity"]])
        listToWriteToFile.append([htmlTags["attrCon"], self.attributes["constitution"]])
        listToWriteToFile.append([htmlTags["attrInt"], self.attributes["intelligence"]])
        listToWriteToFile.append([htmlTags["attrWis"], self.attributes["wisdom"]])
        listToWriteToFile.append([htmlTags["attrCha"], self.attributes["charisma"]])

        listToWriteToFile.append([htmlTags["abilityStr"], self.abilityIncreases["strength"]])
        listToWriteToFile.append([htmlTags["abilityDex"], self.abilityIncreases["dexterity"]])
        listToWriteToFile.append([htmlTags["abilityCon"], self.abilityIncreases["constitution"]])
        listToWriteToFile.append([htmlTags["abilityInt"], self.abilityIncreases["intelligence"]])
        listToWriteToFile.append([htmlTags["abilityWis"], self.abilityIncreases["wisdom"]])
        listToWriteToFile.append([htmlTags["abilityCha"], self.abilityIncreases["charisma"]])

        self.className = self.getUserResponse(["envoy", "mechanic", "mystic", "operative", "solarian", "soldier",
                                               "technomancer"],
                                              """Chose a Class. Possible Classes are: envoy, mechanic, mystic, operative, solarian, soldier, technomancer""")

        if self.className == "soldier":
            self.key = self.getUserResponse(["str", "dex"], """Soldier has to chose the key ability. Possible
                                            are str and dex""")
        else:
            self.key = classesStatBonus[self.className]["key"]

        listToWriteToFile.append([htmlTags["className"], self.className + " (" + str(self.classLevel) + ")"])

        for skill in classesStatBonus[self.className]["classBonus"]:
            self.skillClass[skill] = classesStatBonus[self.className]["classBonus"][skill]
            listToWriteToFile.append([htmlTags[skill + "Class"], self.skillClass[skill]])

        for feat in classesStatBonus[self.className]["proficiencies"]:
            self.chosenFeats.append(feat)

        print("""Currently only point buy system is implemented, if you want to use another system figure
                out the conversion yourself.""")
        print("{} tend to want more points in {}".format(self.className, classesStatFocus[self.className]))

        spendablePoints = 10

        listToWriteToFile.append([htmlTags["attrStrPoint"], 0])
        listToWriteToFile.append([htmlTags["attrDexPoint"], 0])
        listToWriteToFile.append([htmlTags["attrConPoint"], 0])
        listToWriteToFile.append([htmlTags["attrIntPoint"], 0])
        listToWriteToFile.append([htmlTags["attrWisPoint"], 0])
        listToWriteToFile.append([htmlTags["attrChaPoint"], 0])
        self.writeToFile("listPass", listToWriteToFile)

        while spendablePoints > 0:
            entered = self.getUserResponse(possibleAttributes,
                                           """You have {} points left to spend. Chose one from (str)ength, (dex)terity, (con)stitution, (int)elligence, (wis)dom, (cha)risma""".format(spendablePoints))
            if self.attributes[attributeShorthand[entered]] == 18:
                print("""Sorry try again {} is already at 18 which is the maximum when setting up a
                        character""".format(attributeShorthand[entered]))
                continue
            currAttr = attributeShorthand[entered]
            self.attributes[currAttr] += 1
            self.spentPoints[attributeShortener[currAttr]] += 1

            self.writeToFile(htmlTags["attr" + attributeShortener[currAttr] + "Point"], self.spentPoints[attributeShortener[currAttr]])

            spendablePoints -= 1

            listToWriteToFile = []
            listToWriteToFile.append([htmlTags["attrStr"], self.attributes["strength"]])
            listToWriteToFile.append([htmlTags["attrDex"], self.attributes["dexterity"]])
            listToWriteToFile.append([htmlTags["attrCon"], self.attributes["constitution"]])
            listToWriteToFile.append([htmlTags["attrInt"], self.attributes["intelligence"]])
            listToWriteToFile.append([htmlTags["attrWis"], self.attributes["wisdom"]])
            listToWriteToFile.append([htmlTags["attrCha"], self.attributes["charisma"]])

        self.calcAtributMod()

        listToWriteToFile.append([htmlTags["attrStrMod"], self.mods["str"]])
        listToWriteToFile.append([htmlTags["attrDexMod"], self.mods["dex"]])
        listToWriteToFile.append([htmlTags["attrConMod"], self.mods["con"]])
        listToWriteToFile.append([htmlTags["attrIntMod"], self.mods["int"]])
        listToWriteToFile.append([htmlTags["attrWisMod"], self.mods["wis"]])
        listToWriteToFile.append([htmlTags["attrChaMod"], self.mods["cha"]])

        self.initiative = self.mods["dex"]
        self.initiative_misc = 0

        listToWriteToFile.append([htmlTags["init_total"], self.initiative])
        listToWriteToFile.append([htmlTags["init_dex"], self.mods["dex"]])
        listToWriteToFile.append([htmlTags["init_misc"], self.initiative_misc])

        self.eac = 10 + 0 + self.mods["dex"] + 0
        listToWriteToFile.append([htmlTags["eac"], self.eac])
        listToWriteToFile.append([htmlTags["eac_armor"], 0])
        listToWriteToFile.append([htmlTags["eac_dex"], self.mods["dex"]])
        listToWriteToFile.append([htmlTags["eac_misc"], 0])
        self.kac = 10 + 0 + self.mods["dex"] + 0
        listToWriteToFile.append([htmlTags["kac"], self.kac])
        listToWriteToFile.append([htmlTags["kac_armor"], 0])
        listToWriteToFile.append([htmlTags["kac_dex"], self.mods["dex"]])
        listToWriteToFile.append([htmlTags["kac_misc"], 0])

        self.vsCombat = 8 + self.kac
        listToWriteToFile.append([htmlTags["vsCombat"], self.vsCombat])

        self.calcHP()

        listToWriteToFile.append([htmlTags["sp"], self.SP])
        listToWriteToFile.append([htmlTags["hp"], self.HP])
        listToWriteToFile.append([htmlTags["rp"], self.RP])

        self.fortSave = classesStatBonus[self.className]["fort"][self.classLevel - 1] + self.mods["con"] + 0
        self.reflexSave = classesStatBonus[self.className]["reflex"][self.classLevel - 1] + self.mods["dex"] + 0
        self.willSave = classesStatBonus[self.className]["will"][self.classLevel - 1] + self.mods["wis"] + 0

        listToWriteToFile.append([htmlTags["fortSave"], self.fortSave])
        listToWriteToFile.append([htmlTags["reflexSave"], self.reflexSave])
        listToWriteToFile.append([htmlTags["willSave"], self.willSave])

        listToWriteToFile.append([htmlTags["fortSaveBase"], classesStatBonus[self.className]["fort"][self.classLevel - 1]])
        listToWriteToFile.append([htmlTags["reflexSaveBase"], classesStatBonus[self.className]["reflex"][self.classLevel - 1]])
        listToWriteToFile.append([htmlTags["willSaveBase"], classesStatBonus[self.className]["will"][self.classLevel - 1]])

        listToWriteToFile.append([htmlTags["fortSaveAbility"], self.mods["con"]])
        listToWriteToFile.append([htmlTags["reflexSaveAbility"], self.mods["dex"]])
        listToWriteToFile.append([htmlTags["willSaveAbility"], self.mods["wis"]])

        listToWriteToFile.append([htmlTags["fortSaveMisc"], 0])
        listToWriteToFile.append([htmlTags["reflexSaveMisc"], 0])
        listToWriteToFile.append([htmlTags["willSaveMisc"], 0])

        self.melee = classesStatBonus[self.className]["bab"][self.classLevel - 1] + self.mods["str"] + 0
        self.range = classesStatBonus[self.className]["bab"][self.classLevel - 1] + self.mods["dex"] + 0
        self.throw = classesStatBonus[self.className]["bab"][self.classLevel - 1] + self.mods["str"] + 0

        listToWriteToFile.append([htmlTags["melee"], self.melee])
        listToWriteToFile.append([htmlTags["melee_bab"], classesStatBonus[self.className]["bab"][self.classLevel - 1]])
        listToWriteToFile.append([htmlTags["melee_ability"], self.mods["str"]])
        listToWriteToFile.append([htmlTags["melee_misc"], 0])

        listToWriteToFile.append([htmlTags["range"], self.range])
        listToWriteToFile.append([htmlTags["range_bab"], classesStatBonus[self.className]["bab"][self.classLevel - 1]])
        listToWriteToFile.append([htmlTags["range_ability"], self.mods["dex"]])
        listToWriteToFile.append([htmlTags["range_misc"], 0])

        listToWriteToFile.append([htmlTags["throw"], self.range])
        listToWriteToFile.append([htmlTags["throw_bab"], classesStatBonus[self.className]["bab"][self.classLevel - 1]])
        listToWriteToFile.append([htmlTags["throw_ability"], self.mods["str"]])
        listToWriteToFile.append([htmlTags["throw_misc"], 0])

        listToWriteToFile.append([htmlTags["spendablePoints"], 0])
        listToWriteToFile.append([htmlTags["perLevelPoints"], classesStatBonus[self.className]["skills"] + self.mods["int"]])

        self.writeToFile("listPass", listToWriteToFile)

        self.addSkillPoints()

        listToWriteToFile = []
        listToWriteToFile.append([htmlTags["acrobaticsMod"], self.mods["dex"]])
        listToWriteToFile.append([htmlTags["athleticsMod"], self.mods["str"]])
        listToWriteToFile.append([htmlTags["bluffMod"], self.mods["cha"]])
        listToWriteToFile.append([htmlTags["computersMod"], self.mods["int"]])
        listToWriteToFile.append([htmlTags["cultureMod"], self.mods["int"]])
        listToWriteToFile.append([htmlTags["diplomacyMod"], self.mods["cha"]])
        listToWriteToFile.append([htmlTags["disguiseMod"], self.mods["cha"]])
        listToWriteToFile.append([htmlTags["engineeringMod"], self.mods["int"]])
        listToWriteToFile.append([htmlTags["intimidateMod"], self.mods["cha"]])
        listToWriteToFile.append([htmlTags["life scienceMod"], self.mods["int"]])
        listToWriteToFile.append([htmlTags["medicineMod"], self.mods["int"]])
        listToWriteToFile.append([htmlTags["mysticismMod"], self.mods["wis"]])
        listToWriteToFile.append([htmlTags["perceptionMod"], self.mods["wis"]])
        listToWriteToFile.append([htmlTags["physical scienceMod"], self.mods["int"]])
        listToWriteToFile.append([htmlTags["pilotingMod"], self.mods["dex"]])
        listToWriteToFile.append([htmlTags["professionMod"], -1])
        listToWriteToFile.append([htmlTags["profession2Mod"], -1])
        listToWriteToFile.append([htmlTags["sense motiveMod"], self.mods["wis"]])
        listToWriteToFile.append([htmlTags["sleight of handMod"], self.mods["dex"]])
        listToWriteToFile.append([htmlTags["stealthMod"], self.mods["dex"]])
        listToWriteToFile.append([htmlTags["survivalMod"], self.mods["wis"]])
        self.skills = {
            "acrobatics"       : self.mods["dex"],
            "athletics"        : self.mods["str"],
            "bluff"            : self.mods["cha"],
            "computers"        : self.mods["int"],
            "culture"          : self.mods["int"],
            "diplomacy"        : self.mods["cha"],
            "disguise"         : self.mods["cha"],
            "engineering"      : self.mods["int"],
            "intimidate"       : self.mods["cha"],
            "life science"     : self.mods["int"],
            "medicine"         : self.mods["int"],
            "mysticism"        : self.mods["wis"],
            "perception"       : self.mods["wis"],
            "physical science" : self.mods["int"],
            "piloting"         : self.mods["dex"],
            "profession"       : self.mods["wis"], #?????????????????
            "profession2"      : self.mods["wis"], #?????????????????
            "sense motive"     : self.mods["wis"],
            "sleight of hand"  : self.mods["dex"],
            "stealth"          : self.mods["dex"],
            "survival"         : self.mods["wis"],
        }

        for skill in self.skillRanks:
            self.skills[skill] += self.skillRanks[skill] + min(1, self.skillRanks[skill]) * self.skillClass[skill]
            listToWriteToFile.append([htmlTags[skill], self.skills[skill]])
            listToWriteToFile.append([htmlTags[skill + "Rank"], self.skillRanks[skill]])
            listToWriteToFile.append([htmlTags[skill + "Misc"], self.skillMisc[skill]])
        self.writeToFile("listPass", listToWriteToFile)
        self.featsAndAbilities()

    def calcHP(self):
        self.SP = max(1, (max(0, classesStatBonus[self.className]["sp"] + self.mods["con"])) * self.classLevel)
        self.HP = max(1, (classesStatBonus[self.className]["hp"] * self.classLevel) + raceStatList[self.raceName.split()[0]]["hp"])
        self.RP = max(1, max(1, self.classLevel // 2) + self.mods[self.key])

    def addSkillPoints(self):
        skillpoints = classesStatBonus[self.className]["skills"] + self.mods["int"]
        possibleSkill = ["acrobatics", "athletics", "bluff", "computers", "culture", "diplomacy", "disguise", "engineering",
                         "intimidate", "life science", "medicine", "mysticism", "perception", "physical science", "piloting",
                         "sense motive", "sleight of hand", "stealth", "survival"]

        while skillpoints > 0:
            entered = self.getUserResponse(possibleSkill,
                                           "please enter skill name to add a point to. Possible skills are: {}".format(", ".join(possibleSkill)))
            possibleSkill.remove(entered)
            self.skillRanks[entered] += 1
            skillpoints -= 1
            self.writeToFile(htmlTags["spendablePoints"], skillpoints)


    def calcAtributMod(self):
        self.mods["str"] = ((self.attributes["strength"] // 2) - 5)
        self.mods["dex"] = ((self.attributes["dexterity"] // 2) - 5)
        self.mods["con"] = ((self.attributes["constitution"] // 2) - 5)
        self.mods["int"] = ((self.attributes["intelligence"] // 2) - 5)
        self.mods["wis"] = ((self.attributes["wisdom"] // 2) - 5)
        self.mods["cha"] = ((self.attributes["charisma"] // 2) - 5)

    def checkCombatFeats(self, checkFeat):
        # need a combat list to track how many combat feats have been selected
        anyCounter = 0
        toAdd = True
        combat = []

        for feat in self.chosenFeats:
            if feats[feat][0] == "combat":
                combat.append(feat)
        for feat in checkFeat:
            if feat == "any":
                anyCounter += 1
            else:
                if feat not in combat:
                    toAdd = False
                    break

        if anyCounter > len(combat):
            toAdd = False
        return toAdd

    def checkForFeat(self, checkFeat):
        # need a list to track how many feats have been selected
        toAdd = True
        for feat in checkFeat:
            if feat not in self.chosenFeats:
                toAdd = False
                break
        return toAdd

    def checkForSkills(self, checkSkills):
        toAdd = True
        for checkSkill in checkSkills:
            if not toAdd:
                break
            if checkSkill[0] == "from":
                toAdd = False
                for fromCheckSkill in checkSkill[1]:
                    if self.skills[fromCheckSkill] >= checkSkill[2]:
                        toAdd = True
                        break
            elif len(checkSkill) > 2:
                if self.skills[checkSkill[0]] != checkSkill[1]:
                    toAdd = False
            else:
                if self.skills[checkSkill[0]] < checkSkill[1]:
                    toAdd = False
        return toAdd

    def checkForAttribute(self, checkAttribute):
        checkAbility = checkAttribute[0]
        if checkAttribute[0] == "key":
            checkAbility = self.key
        if self.attributes[attributeShorthand[checkAbility]] >= checkAttribute[1]:
            return True
        return False

    def checkForSpellLevel(self, checkSpellLevel):
        if checkSpellLevel == -1:
            if self.spellLevel == -1:
                return True
        elif self.spellLevel >= checkSpellLevel:
            return True
        return False

    def checkForBab(self, checkBab):
        if classesStatBonus[self.className]["bab"][self.classLevel - 1] >= checkBab:
            return True
        return False

    def checkForLevel(self, checkLevel):
        if self.classLevel >= checkLevel:
            return True
        return False

    def checkForSaves(self, checkSaves):
        if classesStatBonus[self.className][checkSaves[0]][self.classLevel - 1] >= checkSaves[1]:
            return True
        return False

    def checkForRace(self, checkRace):
        if self.raceName == checkRace:
            return True
        return False

    def checkForText(self, printText):
        # TODO figure out more elegant way to check these
        affirm = ['true', '1', 't', 'y', 'yes']
        deny = ['false', '0', 'f', 'n', 'no']
        possible = affirm + deny
        entered = ""
        while entered not in possible:
            entered = input(printText)
        return entered in affirm

    def checkFrom(self, fromList):
        featTrue = False
        classTrue = False
        for fromCheck in fromList:
            if fromCheck[0] == "feat":
                for feat in fromCheck[1]:
                    if feat in self.chosenFeats:
                        featTrue = True
                        break
            elif fromCheck[0] == "class":
                classTrue = fromCheck[1] == self.className

            else:
                print("from", fromCheck[0], "not implemented", fromList)
        return featTrue or classTrue

    def filterFeats(self, combat=False):
        selected = []
        for feat in feats:
            tmp = feats[feat]
            if not combat or tmp[0] == "combat":
                toAdd = True
                for check in tmp[1]:
                    if len(check) > 0:
                        if check[0] == "combat":
                            if not self.checkCombatFeats(check[1]):
                                toAdd = False
                        elif check[0] == "feat":
                            if not self.checkForFeat(check[1]):
                                toAdd = False
                        elif check[0] == "skills":
                            if not self.checkForSkills(check[1]):
                                toAdd = False
                        elif check[0] == "ability":
                            if not self.checkForAttribute(check[1]):
                                toAdd = False
                        elif check[0] == "spellLevel":
                            if not self.checkForSpellLevel(check[1]):
                                toAdd = False
                        elif check[0] == "bab":
                            if not self.checkForBab(check[1]):
                                toAdd = False
                        elif check[0] == "level":
                            if not self.checkForLevel(check[1]):
                                toAdd = False
                        elif check[0] == "save":
                            if not self.checkForSaves(check[1]):
                                toAdd = False
                        elif check[0] == "race":
                            if not self.checkForRace(check[1]):
                                toAdd = False
                        # casterLevel check: check if lashunta and greater than level required, or class of technomancer or mystic
                        elif check[0] == "text":
                            if not self.checkForText(check[1]):
                                toAdd = False
                        elif check[0] == "from":
                            if not self.checkFrom(check[1]):
                                toAdd = False
                if toAdd:
                    selected.append(feat)
        return selected

    def selectNewFeat(self, combat=False):
        possibleFeats = self.filterFeats(combat)
        for feat in self.chosenFeats:
            if feat in possibleFeats:
                possibleFeats.remove(feat)

        printText = "please enter feat name you would like to add. Possible feats are: {}".format(", ".join(possibleFeats))
        lowerChosenFeats = [x.lower() for x in possibleFeats]
        entered = self.getUserResponse(lowerChosenFeats, printText)
        enteredFeatIndex = lowerChosenFeats.index(entered)
        self.chosenFeats.append(possibleFeats[enteredFeatIndex])

        # entered = self.getUserResponse([x.lower() for x in possibleFeats], printText)
        # self.chosenFeats.append(entered)

    def selectNewClassFeat(self, featType, level):
        possibleClassFeats = []
        for featList in classChoseFeats[self.className][featType]:
            if level >= featList[0]:
                possibleClassFeats += featList[1:]
        for feat in self.classFeats:
            if feat in possibleClassFeats:
                possibleClassFeats.remove(feat)
        printText = "please enter feat name you would like to add. Possible feats are: {}".format(", ".join(possibleClassFeats))
        lowerClassFeats = [x.lower() for x in possibleClassFeats]
        entered = self.getUserResponse(lowerClassFeats, printText)
        enteredFeatIndex = lowerClassFeats.index(entered)
        self.classFeats.append(possibleClassFeats[enteredFeatIndex])

    def featsAndAbilities(self):
        raceBoxes = [htmlTags["raceAbility1"], htmlTags["raceAbility2"], htmlTags["raceAbility3"],
                     htmlTags["raceAbility4"]]
        themeBoxes = [htmlTags["themeAbility1"], htmlTags["themeAbility2"], htmlTags["themeAbility3"],
                     htmlTags["themeAbility4"]]
        classBoxes = [htmlTags["classAbility1"], htmlTags["classAbility2"], htmlTags["classAbility3"], htmlTags["classAbility4"],
                        htmlTags["classAbility5"], htmlTags["classAbility6"], htmlTags["classAbility7"], htmlTags["classAbility8"],
                        htmlTags["classAbility9"], htmlTags["classAbility10"], htmlTags["classAbility11"], htmlTags["classAbility12"],
                        htmlTags["classAbility13"], htmlTags["classAbility14"], htmlTags["classAbility15"], htmlTags["classAbility16"],
                        htmlTags["classAbility17"], htmlTags["classAbility18"], htmlTags["classAbility19"], htmlTags["classAbility20"],
                        htmlTags["classAbility21"], htmlTags["classAbility22"], htmlTags["classAbility23"], htmlTags["classAbility24"],
                        htmlTags["classAbility25"], htmlTags["classAbility26"], htmlTags["classAbility27"], htmlTags["classAbility28"]]
        otherBoxes = [htmlTags["otherAbility1"], htmlTags["otherAbility2"], htmlTags["otherAbility3"], htmlTags["otherAbility4"],
                       htmlTags["otherAbility5"], htmlTags["otherAbility6"], htmlTags["otherAbility7"], htmlTags["otherAbility8"],
                       htmlTags["otherAbility9"], htmlTags["otherAbility10"], htmlTags["otherAbility11"], htmlTags["otherAbility12"],
                       htmlTags["otherAbility13"], htmlTags["otherAbility14"], htmlTags["otherAbility15"], htmlTags["otherAbility16"]]
        featBoxes = [htmlTags["feat1"], htmlTags["feat2"], htmlTags["feat3"], htmlTags["feat4"], htmlTags["feat5"], htmlTags["feat6"],
                     htmlTags["feat7"], htmlTags["feat8"], htmlTags["feat9"], htmlTags["feat10"], htmlTags["feat11"], htmlTags["feat12"],
                     htmlTags["feat13"], htmlTags["feat14"], htmlTags["feat15"], htmlTags["feat16"], htmlTags["feat17"], htmlTags["feat18"],
                     htmlTags["feat19"], htmlTags["feat20"], htmlTags["feat21"], htmlTags["feat22"], htmlTags["feat23"], htmlTags["feat24"],
                     htmlTags["feat25"], htmlTags["feat26"], htmlTags["feat27"], htmlTags["feat28"]]

        possibleSkill = ["acrobatics", "athletics", "bluff", "computers", "culture", "diplomacy", "disguise", "engineering",
                         "intimidate", "life science", "medicine", "mysticism", "perception", "physical science", "piloting",
                         "sense motive", "sleight of hand", "stealth", "survival"]

        listWriteToFile = []
        for i in range(len(raceAbilities[self.raceName.split()[0]])):
            raceAbilityBlock = raceAbilities[self.raceName.split()[0]][i]
            listWriteToFile.append([raceBoxes[i], raceAbilityBlock[0]])
            if raceAbilityBlock[1] == "stats":
                for block in raceAbilityBlock[2]:
                    if block[0] == "any":
                        printText = "please enter skill name to add {} point(s) to. Possible skills are: {}".format(block[1], ", ".join(possibleSkill))
                        block[0] = self.getUserResponse(possibleSkill, printText)
                    self.skillMisc[block[0]] += block[1]
                    self.skills[block[0]] += block[1]
                    listWriteToFile.append([htmlTags[block[0]], self.skills[block[0]]])
                    listWriteToFile.append([htmlTags[block[0] + "Misc"], self.skillMisc[block[0]]])
            elif raceAbilityBlock[1] == "spell": # TODO
                pass
            elif raceAbilityBlock[1] == "feat":
                self.selectNewFeat()
            elif raceAbilityBlock[1] == "words":
                pass
            else:
                print("The race Ability", raceAbilityBlock[1], "has not yet been implemented")

        themeName = self.theme.split("(")[0].rstrip()
        if self.classLevel == 1:
            listWriteToFile.append([themeBoxes[0], themeAbilities[themeName][0][0]])
            if type(themeAbilities[themeName][0][1]) == type(""):
                newClassSkill = themeAbilities[themeName][0][1]
                if newClassSkill == "any":
                    newClassSkill = self.getUserResponse(possibleSkill, "You get to select a Skill to be turned into a class skill. Options are {}".format(", ".join(possibleSkill)))
                self.makeClassSkill(newClassSkill)
            elif type(themeAbilities[themeName][0][1]) == type([]):
                newClassSkill = self.getUserResponse(themeAbilities[themeName][0][1], "You get to select a Skill to be turned into a class skill. Options are {}".format(", ".join(themeAbilities[themeName][0][1])))
                self.makeClassSkill(newClassSkill)
            else:
                print("themeAbility", themeAbilities[themeName][0][1], "has not yet been implemented")
        if self.classLevel == 6:
            listWriteToFile.append([themeBoxes[1], themeAbilities[themeName][1][0]]) # TODO
            if themeAbilities[themeName][1][1] != "words": # not sure what this is yet only spacefarer will have this
                # +2 bonus to skill checks for skills with 0 ranks in skill
                pass
        if self.classLevel == 12:
            listWriteToFile.append([themeBoxes[2], themeAbilities[themeName][2][0]])
            if themeAbilities[themeName][2][1] != "words": # the alternative is spell and needs to add a spell, only priest will have this
                # ^ Choose one 1st-level mystic spell with some connection to your deity’s portfolio
                # (subject to the GM’s approval). If you have levels in the mystic class, you gain 1
                # additional 1stlevel spell per day and add the chosen spell to your list of mystic
                # spells known. Otherwise, you can use the chosen spell once per day as a spell-like ability.
                pass
        if self.classLevel == 18:
            listWriteToFile.append([themeBoxes[3], themeAbilities[themeName][3][0]])


        listReplaceables = ["Expertise", "Bypass", "Miracle", "Coordinated", "Channel", "Operative’s", # Operative’s might not be just words
                            "Trick", "Quick", "Sidereal", "Techlore", "Cache", "Skill"] # Sidereal is not just words, Techlore is not just words
        listClassAbilities = []
        #for level in range(1, self.classLevel + 1):
        for ability in classAbilities[self.className][self.classLevel - 1]:
            if ability[1] == "improvisation": # classChoseFeats, lists with levels
                self.selectNewClassFeat("improvisation", self.classLevel - 1)
            elif ability[1] == "talent": # classChoseFeats, lists with levels
                self.selectNewClassFeat("talent", self.classLevel - 1)
            elif ability[1] == "trick": # classChoseFeats, lists with levels
                self.selectNewClassFeat("trick", self.classLevel - 1)
            elif ability[1] == "class":
                toMakeClass = ability[2]
                for makeClass in toMakeClass:
                    makeClass = newClassSkill
                    if newClassSkill == "any":
                        newClassSkill = self.getUserResponse(possibleSkill, "You get to select a Skill to be turned into a class skill. Options are {}".format(", ".join(possibleSkill)))
                    self.makeClassSkill(newClassSkill)
            elif ability[1] == "skills":
                for skill in ability[2]:
                    self.skillMisc[skill[0]] += skill[1]
                    self.skill[skill[0]] += skill[1]
            elif ability[1] == "revelation": # classChoseFeats, lists with levels
                self.selectNewClassFeat("revelation", self.classLevel - 1)
            elif ability[1] == "zenith": # classChoseFeats, single list
                self.selectNewClassFeat("zenith", self.classLevel - 1)
            elif ability[1] == "style": # classChoseFeats, dictionary
                possibleStyles = [x for x in classChoseFeats["soldier"]["styles"]]
                for style in self.styles:
                    possibleStyles.remove(style)
                printText = "please enter the style name you would like to add. Possible styles are: {}".format(", ".join(possibleStyles))
                entered = self.getUserResponse(possibleStyles, printText)
                self.styles.append(entered)
                self.classFeats.append(entered.title())
            elif ability[1] == "technique1":
                self.classFeats.append(classChoseFeats["soldier"]["styles"][self.styles[0]][self.classLevel - 1])
            elif ability[1] == "technique2":
                self.classFeats.append(classChoseFeats["soldier"]["styles"][self.styles[1]][(self.classLevel - 1) - 8])
            elif ability[1] == "combat":
                self.selectNewFeat(combat=True)
            elif ability[1] == "gear": # classChoseFeats, lists with levels
                self.selectNewClassFeat("gear", self.classLevel - 1)
            elif ability[1] == "hack": # classChoseFeats, lists with levels
                self.selectNewClassFeat("hack", self.classLevel - 1)
            elif ability[1] == "feat":
                self.chosenFeats.append(ability[2])

            elif ability[1] == "add expertise": # envoy # this is not shown on the excel sheet, might just ignore it then # TODO
                pass
            elif ability[1] == "influence": # solarian # add two skills, one each from two lists
                pass
            elif ability[1] == "weapon": # all
                pass

            elif ability[1] == "words": # nothing happens
                pass
            else:
                print(ability, "has not yet been implemented")


            result = [replacable for replacable in listReplaceables if replacable in ability[0]]
            if len(result) != 0:
                result = result[0]
                result = [oldAbility for oldAbility in listClassAbilities if result in oldAbility]
                if len(result) != 0:
                    result = result[0]
                    result = listClassAbilities.index(result)
                    listClassAbilities[result] = ability[0]
                else:
                    listClassAbilities.append(ability[0])
            else:
                listClassAbilities.append(ability[0])

        for i in range(len(listClassAbilities)):
            listWriteToFile.append([classBoxes[i], listClassAbilities[i]])

        for i in range(len(self.classFeats)):
            listWriteToFile.append([otherBoxes[i], self.classFeats[i]])

        for i in range(len(self.chosenFeats)):
            listWriteToFile.append([featBoxes[i], self.chosenFeats[i]])

        self.writeToFile("listPass", listWriteToFile)

    def makeClassSkill(self, newClassSkill):
        if self.skillClass[newClassSkill] == 0:
            self.skillClass[newClassSkill] = 3
        else:
            self.skillMisc[newClassSkill] += 1

    def abilityIncrease(self):
        if self.classLevel % 2 == 1:
            self.selectNewFeat()
        if self.classLevel % 5 == 0:
            possibleAbilities = ["(str)ength", "(dex)terity", "(con)stitution", "(int)elligence", "(wis)dom", "(cha)risma"]
            toIncreaseNumber = 4
            toIncrease = []
            while toIncreaseNumber > 0:
                printText = "You get to increase {} more attributes. Possible attributes: {}".format(toIncreaseNumber, possibleAbilities)
                entered = self.getUserResponse(possibleAttributes, printText)
                entered = attributeShorthand[entered]
                self.abilityIncreases[entered] += 1
                self.attributes[entered] += 1
                if self.attributes[entered] < 18:
                    self.attributes[entered] += 1
                index = [x for x in possibleAbilities if attributeShortener[entered].lower() in x][0]
                possibleAbilities.remove(index)
                toIncreaseNumber -= 1
            self.calcAtributMod()
            self.initiative = self.mods["dex"]

            listToWriteToFile = []
            listToWriteToFile.append([htmlTags["init_total"], self.initiative])
            listToWriteToFile.append([htmlTags["init_dex"], self.mods["dex"]])
            listToWriteToFile.append([htmlTags["abilityStr"], self.abilityIncreases["strength"]])
            listToWriteToFile.append([htmlTags["abilityDex"], self.abilityIncreases["dexterity"]])
            listToWriteToFile.append([htmlTags["abilityCon"], self.abilityIncreases["constitution"]])
            listToWriteToFile.append([htmlTags["abilityInt"], self.abilityIncreases["intelligence"]])
            listToWriteToFile.append([htmlTags["abilityWis"], self.abilityIncreases["wisdom"]])
            listToWriteToFile.append([htmlTags["abilityCha"], self.abilityIncreases["charisma"]])
            listToWriteToFile.append([htmlTags["attrStrMod"], self.mods["str"]])
            listToWriteToFile.append([htmlTags["attrDexMod"], self.mods["dex"]])
            listToWriteToFile.append([htmlTags["attrConMod"], self.mods["con"]])
            listToWriteToFile.append([htmlTags["attrIntMod"], self.mods["int"]])
            listToWriteToFile.append([htmlTags["attrWisMod"], self.mods["wis"]])
            listToWriteToFile.append([htmlTags["attrChaMod"], self.mods["cha"]])
            listToWriteToFile.append([htmlTags["attrStr"], self.attributes["strength"]])
            listToWriteToFile.append([htmlTags["attrDex"], self.attributes["dexterity"]])
            listToWriteToFile.append([htmlTags["attrCon"], self.attributes["constitution"]])
            listToWriteToFile.append([htmlTags["attrInt"], self.attributes["intelligence"]])
            listToWriteToFile.append([htmlTags["attrWis"], self.attributes["wisdom"]])
            listToWriteToFile.append([htmlTags["attrCha"], self.attributes["charisma"]])
            self.writeToFile("listPass", listToWriteToFile)

    def levelUp(self): # TODO Spells
        #levels = [1300, 3300, 6000, 10000, 15000, 23000, 34000, 50000, 71000, 105000,
        #          14500, 210000, 295000, 425000, 600000, 850000, 1200000, 1700000, 2400000]
        #currLevel = 1
        #for level in levels:
        #    if self.experience >= level:
        #        currLevel += 1
        #    else:
        #        break
        if self.classLevel < 20:
            self.classLevel = self.classLevel + 1
            self.abilityIncrease()
            self.addSkillPoints()
            listToWriteToFile = []
            for skill in self.skillRanks:
                self.skills[skill] += self.skillRanks[skill] + min(1, self.skillRanks[skill]) * self.skillClass[skill]
                listToWriteToFile.append([htmlTags[skill], self.skills[skill]])
                listToWriteToFile.append([htmlTags[skill + "Rank"], self.skillRanks[skill]])
            self.featsAndAbilities()
            self.calcHP()
            listToWriteToFile.append([htmlTags["sp"], self.SP])
            listToWriteToFile.append([htmlTags["hp"], self.HP])
            listToWriteToFile.append([htmlTags["rp"], self.RP])
            listToWriteToFile.append([htmlTags["className"], self.className + " (" + str(self.classLevel) + ")"])
            self.writeToFile("listPass", listToWriteToFile)

    def getUserResponse(self, options, text="", include=True):
        entered = ""
        if include:
            while entered not in options:
                entered = input(text).lower()
        else:
            while entered in options:
                entered = input(text).lower()
        return entered

    def updateHTML(self):
        listWriteToFile = []
        listWriteToFile.append([htmlTags["name"], self.name])
        listWriteToFile.append([htmlTags["race"], self.raceName])
        listWriteToFile.append([htmlTags["raceStr"], raceStatList[self.raceName.split()[0]]["strength"]])
        listWriteToFile.append([htmlTags["raceDex"], raceStatList[self.raceName.split()[0]]["dexterity"]])
        listWriteToFile.append([htmlTags["raceCon"], raceStatList[self.raceName.split()[0]]["constitution"]])
        listWriteToFile.append([htmlTags["raceInt"], raceStatList[self.raceName.split()[0]]["intelligence"]])
        listWriteToFile.append([htmlTags["raceWis"], raceStatList[self.raceName.split()[0]]["wisdom"]])
        listWriteToFile.append([htmlTags["raceCha"], raceStatList[self.raceName.split()[0]]["charisma"]])
        listWriteToFile.append([htmlTags["theme"], self.theme])
        listWriteToFile.append([htmlTags["themeStr"], self.themeAttributes["strength"]])
        listWriteToFile.append([htmlTags["themeDex"], self.themeAttributes["dexterity"]])
        listWriteToFile.append([htmlTags["themeCon"], self.themeAttributes["constitution"]])
        listWriteToFile.append([htmlTags["themeInt"], self.themeAttributes["intelligence"]])
        listWriteToFile.append([htmlTags["themeWis"], self.themeAttributes["wisdom"]])
        listWriteToFile.append([htmlTags["themeCha"], self.themeAttributes["charisma"]])

        listWriteToFile.append([htmlTags["attrStr"], self.attributes["strength"]])
        listWriteToFile.append([htmlTags["attrDex"], self.attributes["dexterity"]])
        listWriteToFile.append([htmlTags["attrCon"], self.attributes["constitution"]])
        listWriteToFile.append([htmlTags["attrInt"], self.attributes["intelligence"]])
        listWriteToFile.append([htmlTags["attrWis"], self.attributes["wisdom"]])
        listWriteToFile.append([htmlTags["attrCha"], self.attributes["charisma"]])

        listWriteToFile.append([htmlTags["attrStrPoint"], self.spentPoints["Str"]])
        listWriteToFile.append([htmlTags["attrDexPoint"], self.spentPoints["Dex"]])
        listWriteToFile.append([htmlTags["attrConPoint"], self.spentPoints["Con"]])
        listWriteToFile.append([htmlTags["attrIntPoint"], self.spentPoints["Int"]])
        listWriteToFile.append([htmlTags["attrWisPoint"], self.spentPoints["Wis"]])
        listWriteToFile.append([htmlTags["attrChaPoint"], self.spentPoints["Cha"]])

        listWriteToFile.append([htmlTags["className"], self.className + " (" + str(self.classLevel) + ")"])

        for skill in classesStatBonus[self.className]["classBonus"]:
            listWriteToFile.append([htmlTags[skill + "Class"], self.skillClass[skill]])
            listWriteToFile.append([htmlTags[skill], self.skills[skill]])
            listWriteToFile.append([htmlTags[skill + "Rank"], self.skillRanks[skill]])

        listWriteToFile.append([htmlTags["eac"], self.eac])
        listWriteToFile.append([htmlTags["eac_armor"], 0])
        listWriteToFile.append([htmlTags["eac_dex"], self.mods["dex"]])
        listWriteToFile.append([htmlTags["eac_misc"], 0])
        listWriteToFile.append([htmlTags["kac"], self.kac])
        listWriteToFile.append([htmlTags["kac_armor"], 0])
        listWriteToFile.append([htmlTags["kac_dex"], self.mods["dex"]])
        listWriteToFile.append([htmlTags["kac_misc"], 0])
        listWriteToFile.append([htmlTags["vsCombat"], self.vsCombat])


        listWriteToFile.append([htmlTags["attrStrMod"], self.mods["str"]])
        listWriteToFile.append([htmlTags["attrDexMod"], self.mods["dex"]])
        listWriteToFile.append([htmlTags["attrConMod"], self.mods["con"]])
        listWriteToFile.append([htmlTags["attrIntMod"], self.mods["int"]])
        listWriteToFile.append([htmlTags["attrWisMod"], self.mods["wis"]])
        listWriteToFile.append([htmlTags["attrChaMod"], self.mods["cha"]])

        listWriteToFile.append([htmlTags["init_total"], self.initiative])
        listWriteToFile.append([htmlTags["init_dex"], self.mods["dex"]])
        listWriteToFile.append([htmlTags["init_misc"], self.initiative_misc])

        listWriteToFile.append([htmlTags["fortSave"], self.fortSave])
        listWriteToFile.append([htmlTags["reflexSave"], self.reflexSave])
        listWriteToFile.append([htmlTags["willSave"], self.willSave])

        listWriteToFile.append([htmlTags["fortSaveBase"], classesStatBonus[self.className]["fort"][self.classLevel - 1]])
        listWriteToFile.append([htmlTags["reflexSaveBase"], classesStatBonus[self.className]["reflex"][self.classLevel - 1]])
        listWriteToFile.append([htmlTags["willSaveBase"], classesStatBonus[self.className]["will"][self.classLevel - 1]])

        listWriteToFile.append([htmlTags["fortSaveAbility"], self.mods["con"]])
        listWriteToFile.append([htmlTags["reflexSaveAbility"], self.mods["dex"]])
        listWriteToFile.append([htmlTags["willSaveAbility"], self.mods["wis"]])

        listWriteToFile.append([htmlTags["fortSaveMisc"], 0])
        listWriteToFile.append([htmlTags["reflexSaveMisc"], 0])
        listWriteToFile.append([htmlTags["willSaveMisc"], 0])

        listWriteToFile.append([htmlTags["melee"], self.melee])
        listWriteToFile.append([htmlTags["melee_bab"], classesStatBonus[self.className]["bab"][self.classLevel - 1]])
        listWriteToFile.append([htmlTags["melee_ability"], self.mods["str"]])
        listWriteToFile.append([htmlTags["melee_misc"], 0])

        listWriteToFile.append([htmlTags["range"], self.range])
        listWriteToFile.append([htmlTags["range_bab"], classesStatBonus[self.className]["bab"][self.classLevel - 1]])
        listWriteToFile.append([htmlTags["range_ability"], self.mods["dex"]])
        listWriteToFile.append([htmlTags["range_misc"], 0])

        listWriteToFile.append([htmlTags["throw"], self.throw])
        listWriteToFile.append([htmlTags["throw_bab"], classesStatBonus[self.className]["bab"][self.classLevel - 1]])
        listWriteToFile.append([htmlTags["throw_ability"], self.mods["str"]])
        listWriteToFile.append([htmlTags["throw_misc"], 0])

        listWriteToFile.append([htmlTags["sp"], self.SP])
        listWriteToFile.append([htmlTags["hp"], self.HP])
        listWriteToFile.append([htmlTags["rp"], self.RP])

        listWriteToFile.append([htmlTags["spendablePoints"], 0])
        listWriteToFile.append([htmlTags["perLevelPoints"], classesStatBonus[self.className]["skills"] + self.mods["int"]])

        listWriteToFile.append([htmlTags["acrobaticsMod"], self.mods["dex"]])
        listWriteToFile.append([htmlTags["athleticsMod"], self.mods["str"]])
        listWriteToFile.append([htmlTags["bluffMod"], self.mods["cha"]])
        listWriteToFile.append([htmlTags["computersMod"], self.mods["int"]])
        listWriteToFile.append([htmlTags["cultureMod"], self.mods["int"]])
        listWriteToFile.append([htmlTags["diplomacyMod"], self.mods["cha"]])
        listWriteToFile.append([htmlTags["disguiseMod"], self.mods["cha"]])
        listWriteToFile.append([htmlTags["engineeringMod"], self.mods["int"]])
        listWriteToFile.append([htmlTags["intimidateMod"], self.mods["cha"]])
        listWriteToFile.append([htmlTags["life scienceMod"], self.mods["int"]])
        listWriteToFile.append([htmlTags["medicineMod"], self.mods["int"]])
        listWriteToFile.append([htmlTags["mysticismMod"], self.mods["wis"]])
        listWriteToFile.append([htmlTags["perceptionMod"], self.mods["wis"]])
        listWriteToFile.append([htmlTags["physical scienceMod"], self.mods["int"]])
        listWriteToFile.append([htmlTags["pilotingMod"], self.mods["dex"]])
        listWriteToFile.append([htmlTags["professionMod"], -1])
        listWriteToFile.append([htmlTags["profession2Mod"], -1])
        listWriteToFile.append([htmlTags["sense motiveMod"], self.mods["wis"]])
        listWriteToFile.append([htmlTags["slight of handMod"], self.mods["dex"]])
        listWriteToFile.append([htmlTags["stealthMod"], self.mods["dex"]])
        listWriteToFile.append([htmlTags["survivalMod"], self.mods["wis"]])
        self.writeToFile("listPass", listWriteToFile)
        self.featsAndAbilities()

    def readFromHTML(self, fileName):
        try:
            fp = open("{}.html".format(fileName))
            soup = BeautifulSoup(fp, 'html.parser')

            self.SP                              = soup.find(attrs={"id": htmlTags["sp"]})["value"]
            self.HP                              = soup.find(attrs={"id": htmlTags["hp"]})["value"]
            self.RP                              = soup.find(attrs={"id": htmlTags["rp"]})["value"]

            self.kac                             = soup.find(attrs={"id": htmlTags["kac"]})["value"]
            self.eac                             = soup.find(attrs={"id": htmlTags["eac"]})["value"]

            self.name                            = soup.find(attrs={"id": htmlTags["name"]})["value"]
            self.throw                           = soup.find(attrs={"id": htmlTags["throw"]})["value"]
            self.range                           = soup.find(attrs={"id": htmlTags["range"]})["value"]
            self.melee                           = soup.find(attrs={"id": htmlTags["melee"]})["value"]

            self.theme                           = soup.find(attrs={"id": htmlTags["theme"]})["value"]

            self.vsCombat                        = soup.find(attrs={"id": htmlTags["vsCombat"]})["value"]
            self.raceName                        = soup.find(attrs={"id": htmlTags["race"]})["value"]

            classNameLevel                       = soup.find(attrs={"id": htmlTags["className"]})["value"]
            self.className, level                = classNameLevel.split()
            self.classLevel                      = int(level[1:-1])

            self.fortSave                        = soup.find(attrs={"id": htmlTags["fortSave"]})["value"]
            self.willSave                        = soup.find(attrs={"id": htmlTags["willSave"]})["value"]

            self.reflexSave                      = soup.find(attrs={"id": htmlTags["reflexSave"]})["value"]
            self.initiative                      = soup.find(attrs={"id": htmlTags["init_total"]})["value"]
            self.initiative_misc                 = soup.find(attrs={"id": htmlTags["init_misc"]})["value"]

            self.mods["str"]                     = int(soup.find(attrs={"id": htmlTags["attrStrMod"]})["value"])
            self.mods["dex"]                     = int(soup.find(attrs={"id": htmlTags["attrDexMod"]})["value"])
            self.mods["con"]                     = int(soup.find(attrs={"id": htmlTags["attrConMod"]})["value"])
            self.mods["int"]                     = int(soup.find(attrs={"id": htmlTags["attrIntMod"]})["value"])
            self.mods["wis"]                     = int(soup.find(attrs={"id": htmlTags["attrWisMod"]})["value"])
            self.mods["cha"]                     = int(soup.find(attrs={"id": htmlTags["attrChaMod"]})["value"])

            self.spentPoints["Str"]              = int(soup.find(attrs={"id": htmlTags["attrStrPoint"]})["value"])
            self.spentPoints["Dex"]              = int(soup.find(attrs={"id": htmlTags["attrDexPoint"]})["value"])
            self.spentPoints["Con"]              = int(soup.find(attrs={"id": htmlTags["attrConPoint"]})["value"])
            self.spentPoints["Int"]              = int(soup.find(attrs={"id": htmlTags["attrIntPoint"]})["value"])
            self.spentPoints["Wis"]              = int(soup.find(attrs={"id": htmlTags["attrWisPoint"]})["value"])
            self.spentPoints["Cha"]              = int(soup.find(attrs={"id": htmlTags["attrChaPoint"]})["value"])

            self.abilityIncreases["strength"]    = int(soup.find(attrs={"id": htmlTags["abilityStr"]})["value"])
            self.abilityIncreases["dexterity"]   = int(soup.find(attrs={"id": htmlTags["abilityDex"]})["value"])
            self.abilityIncreases["constitution"]= int(soup.find(attrs={"id": htmlTags["abilityCon"]})["value"])
            self.abilityIncreases["intelligence"]= int(soup.find(attrs={"id": htmlTags["abilityInt"]})["value"])
            self.abilityIncreases["wisdom"]      = int(soup.find(attrs={"id": htmlTags["abilityWis"]})["value"])
            self.abilityIncreases["charisma"]    = int(soup.find(attrs={"id": htmlTags["abilityCha"]})["value"])

            self.attributes["strength"]          = int(soup.find(attrs={"id": htmlTags["attrStr"]})["value"])
            self.attributes["dexterity"]         = int(soup.find(attrs={"id": htmlTags["attrDex"]})["value"])
            self.attributes["constitution"]      = int(soup.find(attrs={"id": htmlTags["attrCon"]})["value"])
            self.attributes["intelligence"]      = int(soup.find(attrs={"id": htmlTags["attrInt"]})["value"])
            self.attributes["wisdom"]            = int(soup.find(attrs={"id": htmlTags["attrWis"]})["value"])
            self.attributes["charisma"]          = int(soup.find(attrs={"id": htmlTags["attrCha"]})["value"])

            self.themeAttributes["strength"]     = int(soup.find(attrs={"id": htmlTags["themeStr"]})["value"])
            self.themeAttributes["dexterity"]    = int(soup.find(attrs={"id": htmlTags["themeDex"]})["value"])
            self.themeAttributes["constitution"] = int(soup.find(attrs={"id": htmlTags["themeCon"]})["value"])
            self.themeAttributes["intelligence"] = int(soup.find(attrs={"id": htmlTags["themeInt"]})["value"])
            self.themeAttributes["wisdom"]       = int(soup.find(attrs={"id": htmlTags["themeWis"]})["value"])
            self.themeAttributes["charisma"]     = int(soup.find(attrs={"id": htmlTags["themeCha"]})["value"])


            for skill in classesStatBonus["envoy"]["classBonus"]:
                self.skills[skill] = int(soup.find(attrs={"id": htmlTags[skill]})["value"])
                self.skillRanks[skill] = int(soup.find(attrs={"id": htmlTags[skill + "Rank"]})["value"])
                self.skillClass[skill] = int(soup.find(attrs={"id": htmlTags[skill + "Class"]})["value"])
                self.skillMisc[skill] = int(soup.find(attrs={"id": htmlTags[skill + "Misc"]})["value"])

        except FileNotFoundError:
            print("""The Character name you entered does not have a file.
                    Please create the character with the wizard or enter another name""")



    def writeToFile(self, attributeName, attributeNameValue):

        try:
            fp = open("{}.html".format(self.name))
        except FileNotFoundError:
            fp = open("CharacterSheet.html")

        soup = BeautifulSoup(fp, 'html.parser')
        if attributeName == "listPass":
            for a_name, a_name_value in attributeNameValue:
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
                soup.find(attrs={"id": attributeName})["value"] = attributeNameValue
            except TypeError:
                print("------------------")
                print(attributeName)
                print(attributeNameValue)
                print(soup.find(attrs={"id": attributeName}))
                print("------------------")

        with open("{}.html".format(self.name), "w") as out:
            out.write(str(soup))
        fp.close()
