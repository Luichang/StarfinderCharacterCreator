import math
from bs4 import BeautifulSoup
from starfinderDicts import *
from feats import feats
from spells import spells

class character:
    def __init__(self, fileName=""):

        self.spellLevel = -1

        self.listClassAbilities = []
        self.chosenFeats = []
        self.classFeats = []
        self.styles = [] # this is soldier, mystic, and operative exclusive
        self.spells = [[], [], [], [], [], [], []]
        self.additionalSpells = [[], [], [], [], [], [], []] # for spells provided outside of class level up
        self.expertise = []

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
            "sleight of hand" : 0,
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
            "sleight of hand" : 0,
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
            "sleight of hand" : 0,
            "stealth"         : 0,
            "survival"        : 0
        }

        self.skillDabbler = {
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
            "sleight of hand" : 0,
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

        self.writeToFile(htmlTags["name"], self.name.title())

        self.raceName = self.getUserResponse(["android", "human", "kasatha", "lashunta(korasha)",
                                              "lashunta(damaya)", "shirren", "vesk", "ysoki"],
                                              """Please chose a race, options are: android, human, kasatha, lashunta(korasha), lashunta(damaya), shirren, vesk, ysoki"""
                                            )

        listToWriteToFile = []
        listToWriteToFile.append([htmlTags["race"], self.raceName.title()])
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
            listToWriteToFile.append([htmlTags["race"], self.raceName.title()])
            listToWriteToFile.append([htmlTags[htmlEnteredTag], 2])
            self.writeToFile("listPass", listToWriteToFile)

        self.theme = self.getUserResponse(["ace pilot", "bounty hunter", "icon", "mercenary", "outlaw", "priest",
                                        "scholar", "spacefarer", "xenoseeker", "themeless"],
                                          """Chose a theme. Possible themes are: "ace pilot, bounty hunter, icon, mercenary, outlaw, priest, scholar, spacefarer, xenoseeker, themeless""")

        self.writeToFile(htmlTags["theme"], self.theme.title())

        self.themeAttributes = themes[self.theme]
        if self.theme == "themeless":
            entered = self.getUserResponse(possibleAttributes,
                                           """Themeless get to increase one stat by 1. Possible attributes: (str)ength, (dex)terity, (con)stitution, (int)elligence, (wis)dom, (cha)risma""")

            self.themeAttributes[attributeShorthand[entered]] = 1
            self.theme += " (" + entered + ")"
            self.writeToFile(htmlTags["theme"], self.theme.title())

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

        className = self.className.title() + " (" + str(self.classLevel) + ")"
        if self.className == "soldier":
            self.key = self.getUserResponse(["str", "dex"], """Soldier has to chose the key ability. Possible are str and dex""")
            className += " [" + str(self.key) + "]"
        else:
            self.key = classesStatBonus[self.className]["key"]


        listToWriteToFile.append([htmlTags["className"], className])

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

        self.initiative_misc = 0
        self.initiative = self.mods["dex"] + self.initiative_misc

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

        self.fortSave_misc = 0
        self.reflexSave_misc = 0
        self.willSave_misc = 0

        listToWriteToFile += self.calcSave()

        self.melee_misc = 0
        self.range_misc = 0
        self.throw_misc = 0

        listToWriteToFile += self.calcAttack()

        listToWriteToFile.append([htmlTags["spendablePoints"], 0])
        listToWriteToFile.append([htmlTags["perLevelPoints"], classesStatBonus[self.className]["skills"] + self.mods["int"]])

        self.writeToFile("listPass", listToWriteToFile)

        self.addSkillPoints()

        listToWriteToFile = self.calcSkills()
        self.writeToFile("listPass", listToWriteToFile)
        self.featsAndAbilities()

        self.addSpells()

    def calcSave(self):
        listToWriteToFile = []
        self.fortSave = classesStatBonus[self.className]["fort"][self.classLevel - 1] + self.mods["con"] + self.fortSave_misc
        self.reflexSave = classesStatBonus[self.className]["reflex"][self.classLevel - 1] + self.mods["dex"] + self.reflexSave_misc
        self.willSave = classesStatBonus[self.className]["will"][self.classLevel - 1] + self.mods["wis"] + self.willSave_misc

        listToWriteToFile.append([htmlTags["fortSave"], self.fortSave])
        listToWriteToFile.append([htmlTags["reflexSave"], self.reflexSave])
        listToWriteToFile.append([htmlTags["willSave"], self.willSave])

        listToWriteToFile.append([htmlTags["fortSaveBase"], classesStatBonus[self.className]["fort"][self.classLevel - 1]])
        listToWriteToFile.append([htmlTags["reflexSaveBase"], classesStatBonus[self.className]["reflex"][self.classLevel - 1]])
        listToWriteToFile.append([htmlTags["willSaveBase"], classesStatBonus[self.className]["will"][self.classLevel - 1]])

        listToWriteToFile.append([htmlTags["fortSaveAbility"], self.mods["con"]])
        listToWriteToFile.append([htmlTags["reflexSaveAbility"], self.mods["dex"]])
        listToWriteToFile.append([htmlTags["willSaveAbility"], self.mods["wis"]])

        listToWriteToFile.append([htmlTags["fortSaveMisc"], self.fortSave_misc])
        listToWriteToFile.append([htmlTags["reflexSaveMisc"], self.reflexSave_misc])
        listToWriteToFile.append([htmlTags["willSaveMisc"], self.willSave_misc])
        return listToWriteToFile

    def calcAttack(self):
        listToWriteToFile = []
        self.melee = classesStatBonus[self.className]["bab"][self.classLevel - 1] + self.mods["str"] + self.melee_misc
        self.range = classesStatBonus[self.className]["bab"][self.classLevel - 1] + self.mods["dex"] + self.range_misc
        self.throw = classesStatBonus[self.className]["bab"][self.classLevel - 1] + self.mods["str"] + self.throw_misc

        listToWriteToFile.append([htmlTags["melee"], self.melee])
        listToWriteToFile.append([htmlTags["melee_bab"], classesStatBonus[self.className]["bab"][self.classLevel - 1]])
        listToWriteToFile.append([htmlTags["melee_ability"], self.mods["str"]])
        listToWriteToFile.append([htmlTags["melee_misc"], self.melee_misc])

        listToWriteToFile.append([htmlTags["range"], self.range])
        listToWriteToFile.append([htmlTags["range_bab"], classesStatBonus[self.className]["bab"][self.classLevel - 1]])
        listToWriteToFile.append([htmlTags["range_ability"], self.mods["dex"]])
        listToWriteToFile.append([htmlTags["range_misc"], self.range_misc])

        listToWriteToFile.append([htmlTags["throw"], self.throw])
        listToWriteToFile.append([htmlTags["throw_bab"], classesStatBonus[self.className]["bab"][self.classLevel - 1]])
        listToWriteToFile.append([htmlTags["throw_ability"], self.mods["str"]])
        listToWriteToFile.append([htmlTags["throw_misc"], self.throw_misc])
        return listToWriteToFile

    def printSpells(self):
        listToWriteToFile = []
        spellBoxes = [
            ["spell001", "spell002", "spell003", "spell004", "spell005", "spell006", "spell007", "spell008"],
            ["spell101", "spell102", "spell103", "spell104", "spell105", "spell106", "spell107", "spell108"],
            ["spell201", "spell202", "spell203", "spell204", "spell205", "spell206", "spell207"],
            ["spell301", "spell302", "spell303", "spell304", "spell305", "spell306", "spell307"],
            ["spell401", "spell402", "spell403", "spell404", "spell405", "spell406", "spell407"],
            ["spell501", "spell502", "spell503", "spell504", "spell505", "spell506"],
            ["spell601", "spell602", "spell603", "spell604", "spell605", "spell606"]
        ]
        for i in range(7):
            fullSpellList = self.spells[i] + self.additionalSpells[i]
            for j in range(len(fullSpellList)):
                listToWriteToFile.append([htmlTags[spellBoxes[i][j]], fullSpellList[j]])
        return listToWriteToFile

    def printSpellNumbers(self):
        spellWordBoxes = [["spell0known"], ["spell1known", "spell1day"],
                          ["spell2known", "spell2day"], ["spell3known", "spell3day"],
                          ["spell4known", "spell4day"], ["spell5known", "spell5day"],
                          ["spell6known", "spell6day"]]

        listToWriteToFile = []
        if self.className == "technomancer" or self.className == "mystic":
            self.spellLevel = self.classLevel

            bonusList = []
            for bonus in spellsBonus:
                if bonus[0] > self.attributes[attributeShorthand[self.key]]:
                    break
                bonusList = bonus[1:]

            for i in range(7):
                listToWriteToFile.append([htmlTags[spellWordBoxes[i][0]], spellsKnown[self.classLevel - 1][i]])
                if len(spellWordBoxes[i]) > 1:
                    perDay = spellsDay[self.classLevel - 1][i - 1] + bonusList[i]
                    listToWriteToFile.append([htmlTags[spellWordBoxes[i][1]], perDay])
        else:
            for i in range(7):
                listToWriteToFile.append([htmlTags[spellWordBoxes[i][0]], 0])
                if len(spellWordBoxes[i]) > 1:
                    perDay = 0
                    listToWriteToFile.append([htmlTags[spellWordBoxes[i][1]], perDay])
        return listToWriteToFile


    def addSpells(self):
        listToWriteToFile = []
        if self.className == "technomancer" or self.className == "mystic":
            listOfPickableSpells = [[], [], [], [], [], [], []]
            for i in range(7):
                if spellsKnown[self.classLevel - 1][i] > 0:
                    listOfPickableSpells[i] += spells[self.className][i]

            if self.classLevel > 1:
                for i in range(7):
                    if spellsKnown[self.classLevel - 1][i] - spellsKnown[self.classLevel - 2][i] == 0:
                        listOfPickableSpells[i] = []

            for i in range(7):
                for spell in self.spells[i]:
                    if spell in listOfPickableSpells[i]:
                        listOfPickableSpells[i].remove(spell)

            for i in range(7):
                if listOfPickableSpells[i] != []:
                    numToAdd = spellsKnown[self.classLevel - 1][i]
                    if self.classLevel > 1:
                        numToAdd -= spellsKnown[self.classLevel - 2][i]
                    for j in range(numToAdd):
                        printText = "please enter spell name to add a point to. Possible spells are: {}".format(
                        ", ".join(listOfPickableSpells[i]))
                        entered = self.getUserResponse([x.lower() for x in listOfPickableSpells[i]], printText)
                        entered = entered.title()
                        listOfPickableSpells[i].remove(entered)
                        self.spells[i].append(entered)

            listToWriteToFile += self.printSpells()
        listToWriteToFile += self.printSpellNumbers()
        self.writeToFile("listPass", listToWriteToFile)


    def calcSkills(self):
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
        for skill in self.skills:
            self.skills[skill] += self.skillRanks[skill] + self.skillClass[skill] + self.skillMisc[skill]
            listToWriteToFile.append([htmlTags[skill], self.skills[skill]])
            listToWriteToFile.append([htmlTags[skill + "Rank"], self.skillRanks[skill]])
            listToWriteToFile.append([htmlTags[skill + "Class"], self.skillClass[skill]])
            listToWriteToFile.append([htmlTags[skill + "Misc"], self.skillMisc[skill] + self.skillDabbler[skill]])
        return listToWriteToFile

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

        for longFeat in self.chosenFeats:
            feat = longFeat
            if longFeat == "weapon focus" or longFeat == "weapon specialization" or longFeat == "skill focus":
                feat = longFeat.split("[")[0].rstrip()
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

    def checkForStyle(self, checkStyle):
        for style in self.styles:
            if style == checkStyle:
                return True
        return False

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
                        elif check[0] == "style":
                            if not self.checkForStyle(check[1]):
                                toAdd = False
                        elif check[0] == "from":
                            if not self.checkFrom(check[1]):
                                toAdd = False
                if toAdd:
                    selected.append(feat)
        return selected

    def selectNewFeat(self, combat=False):
        addFeat = False
        additionalInfo = ""
        possibleFeats = self.filterFeats(combat)
        for feat in self.chosenFeats:
            if feat in possibleFeats:
                possibleFeats.remove(feat)
        while not addFeat:
            printText = "please enter feat name you would like to add. Possible feats are: {}".format(", ".join(possibleFeats))
            lowerChosenFeats = [x.lower() for x in possibleFeats]
            entered = self.getUserResponse(lowerChosenFeats, printText)
            addFeat = True
            if entered == "weapon focus" or entered == "weapon specialization":
                weaponFeats = ["advanced melee", "advanced melee weapon", "basic melee",
                               "basic melee weapon", "grenade", "heavy", "heavy weapon",
                               "longarm", "small arm", "sniper", "sniper weapon", "special", "special weapon"]
                weaponFeatsSmall = ["advanced melee weapon", "basic melee weapon", "grenade", "heavy weapon",
                               "longarm", "small arm", "sniper weapon", "special weapon"]
                if entered == "weapon specialization":
                    weaponFeats.remove("grenade")
                    weaponFeatsSmall.remove("grenade")

                weaponTypeText = "With which weapon type do you wish to use this feat? \n Possible weapon types are: {}".format(", ".join(weaponFeatsSmall))
                weaponEntered = self.getUserResponse(weaponFeats, weaponTypeText)
                weaponFeatsDict = {
                    "advanced melee"        : "Advanced Melee Weapon Proficiency",
                    "advanced melee weapon" : "Advanced Melee Weapon Proficiency",
                    "basic melee"           : "Basic Melee Weapon Proficiency",
                    "basic melee weapon"    : "Basic Melee Weapon Proficiency",
                    "grenade"               : "Grenade Proficiency",
                    "heavy"                 : "Heavy Weapon Proficiency",
                    "heavy weapon"          : "Heavy Weapon Proficiency",
                    "longarm"               : "Longarm Proficiency",
                    "small arm"             : "Small Arm Proficiency",
                    "sniper"                : "Sniper Weapon Proficiency",
                    "sniper weapon"         : "Sniper Weapon Proficiency",
                    "special"               : "Special Weapon Proficiency",
                    "special weapon"        : "Special Weapon Proficiency"
                }
                additionalInfo = " [{}]".format(weaponFeatsDict[weaponEntered])
                if weaponFeatsDict[weaponEntered] not in self.chosenFeats:
                    addFeat = False
                    print("You do not have the {}, please selsct a different feat".format(weaponFeatsDict[weaponEntered]))
                    additionalInfo = ""
            elif entered == "skill focus":
                printText = "please enter the skill you would like to focus. Possible skills are: {}".format(", ".join([x for x in self.skills]))
                skillEntered = self.getUserResponse([x for x in self.skills], printText)
                additionalInfo = " [{}]".format(skillEntered.title())
                self.skillMisc[skillEntered] += 3

        enteredFeatIndex = lowerChosenFeats.index(entered)
        self.chosenFeats.append(possibleFeats[enteredFeatIndex] + additionalInfo)

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
        printText = "please enter class feat name you would like to add. Possible feats are: {}".format(", ".join(possibleClassFeats))
        lowerClassFeats = [x.lower() for x in possibleClassFeats]
        entered = self.getUserResponse(lowerClassFeats, printText)
        enteredFeatIndex = lowerClassFeats.index(entered)
        self.classFeats.append(possibleClassFeats[enteredFeatIndex])

    def featsAndAbilities(self):

        possibleSkill = ["acrobatics", "athletics", "bluff", "computers", "culture", "diplomacy", "disguise", "engineering",
                         "intimidate", "life science", "medicine", "mysticism", "perception", "physical science", "piloting",
                         "sense motive", "sleight of hand", "stealth", "survival"]

        listToWriteToFile = []
        for i in range(len(raceAbilities[self.raceName.split()[0]])):
            raceAbilityBlock = raceAbilities[self.raceName.split()[0]][i]
            if raceAbilityBlock[1] == "stats":
                for block in raceAbilityBlock[2]:
                    if block[0] == "any":
                        printText = "please enter skill name to add {} point(s) to. Possible skills are: {}".format(block[1], ", ".join(possibleSkill))
                        block[0] = self.getUserResponse(possibleSkill, printText)
                    self.skillMisc[block[0]] += block[1]
                    self.skills[block[0]] += block[1]
                    listToWriteToFile.append([htmlTags[block[0]], self.skills[block[0]]])
                    listToWriteToFile.append([htmlTags[block[0] + "Misc"], self.skillMisc[block[0]]])
            elif raceAbilityBlock[1] == "spell": # TODO
                for i in range(2):
                    for spell in raceAbilityBlock[2][i]:
                        if spell not in self.additionalSpells:
                            self.additionalSpells[i].append(spell)
            elif raceAbilityBlock[1] == "feat":
                self.selectNewFeat()
            elif raceAbilityBlock[1] == "words":
                pass
            else:
                print("The race Ability", raceAbilityBlock[1], "has not yet been implemented")

        themeName = self.theme.split("(")[0].rstrip()
        if self.classLevel == 1:
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
        if self.classLevel >= 6:
            if themeAbilities[themeName][1][1] != "words":
                # +2 bonus to skill checks for skills with 0 ranks in skill
                for skill in self.skills:
                    if self.skillRanks[skill] == 0:
                        self.skillDabbler[skill] = 2
        if self.classLevel == 12:
            if themeAbilities[themeName][2][1] != "words": # the alternative is spell and needs to add a spell, only priest will have this
                # ^ Choose one 1st-level mystic spell with some connection to your deity's portfolio
                # (subject to the GM's approval). If you have levels in the mystic class, you gain 1
                # additional 1stlevel spell per day and add the chosen spell to your list of mystic
                # spells known. Otherwise, you can use the chosen spell once per day as a spell-like ability.
                possibleSpells = spells["mystic"][1]
                printText = "as a priest you may choose one 1st-level mystic spell. Possible spells are {}".format(", ".join(possibleSpells))
                entered = self.getUserResponse(possibleSpells, printText)
                self.additionalSpells[1].append(entered)


        listReplaceables = ["Expertise", "Bypass", "Miracle", "Coordinated", "Channel", "Operative's", # Operative's might not be just words
                            "Trick", "Quick", "Sidereal", "Techlore", "Cache", "Skill"] # Sidereal is not just words, Techlore is not just words
        #for level in range(1, self.classLevel + 1):
        for ability in classAbilities[self.className][self.classLevel - 1]:
            if ability[1] == "improvisation": # classChoseFeats, lists with levels
                self.selectNewClassFeat("improvisation", self.classLevel)
            elif ability[1] == "talent": # classChoseFeats, lists with levels
                self.selectNewClassFeat("talent", self.classLevel)
            elif ability[1] == "trick": # classChoseFeats, lists with levels
                self.selectNewClassFeat("trick", self.classLevel)
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
            elif ability[1] == "revelation": # classChoseFeats, lists with levels
                self.selectNewClassFeat("revelation", self.classLevel)
            elif ability[1] == "zenith": # classChoseFeats, single list
                self.selectNewClassFeat("zenith", self.classLevel)
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
                self.selectNewClassFeat("gear", self.classLevel)
            elif ability[1] == "hack": # classChoseFeats, lists with levels
                self.selectNewClassFeat("hack", self.classLevel)
            elif ability[1] == "feat":
                self.chosenFeats.append(ability[2])
            elif ability[1] == "edge":
                self.initiative_misc += 1
                self.initiative = self.mods["dex"] + self.initiative_misc
                listToWriteToFile.append([htmlTags["init_total"], self.initiative])
                listToWriteToFile.append([htmlTags["init_dex"], self.mods["dex"]])
                listToWriteToFile.append([htmlTags["init_misc"], self.initiative_misc])
                for skill in self.skillMisc:
                    self.skillMisc[skill] += 1
            elif ability[1] == "specialization":
                if ability[2][0] == "feat":
                    self.chosenFeats.append(ability[2][1])
                    possibleSpecialization = [x for x in classChoseFeats["operative"]["specialization"]]
                    printText = "please enter the specialization name you would like to add. Possible specialization are: {}".format(", ".join(possibleSpecialization))
                    entered = self.getUserResponse([x.lower() for x in possibleSpecialization], printText)
                    entered = entered.title()
                    self.styles.append(entered)
                    self.classFeats.append(entered)
                    skill1, skill2 = classChoseFeats["operative"]["specialization"][self.styles[0]][0]
                    self.chosenFeats.append("Skill Focus [{}]".format(skill1.title()))
                    self.chosenFeats.append("Skill Focus [{}]".format(skill2.title()))
                    self.skillMisc[skill1] += 3
                    self.skillMisc[skill2] += 3
                elif ability[2][0] == "exploit":
                    self.classFeats.append(classChoseFeats["operative"]["specialization"][self.styles[0]][1])
                elif ability[2][0] == "power":
                    self.classFeats.append(classChoseFeats["operative"]["specialization"][self.styles[0]][2])
            elif ability[1] == "exploit":
                self.selectNewClassFeat("exploit", self.classLevel)
            elif ability[1] == "connection":
                possibleConnection = [x for x in classChoseFeats["mystic"]["connection"]]
                printText = "please enter the connnection name you would like to add. Possible connections are: {}".format(", ".join(possibleConnection))
                entered = self.getUserResponse([x.lower() for x in possibleConnection], printText)
                entered = entered.title()
                self.styles.append(entered)
                self.classFeats.append(entered)
            elif ability[1] == "cpower":
                self.classFeats.append(classChoseFeats["mystic"]["connection"][self.styles[0]]["feat"][ability[2]])
            elif ability[1] == "spell":
                self.additionalSpells[ability[2] + 1].append(classChoseFeats["mystic"]["connection"][self.styles[0]]["spell"][ability[2]])
            elif ability[1] == "channel":
                skill1, skill2 = classChoseFeats["mystic"]["connection"][self.styles[0]]["skill"]
                self.skillMisc[skill1] += 1
                self.skillMisc[skill2] += 1
            elif ability[1] == "expertise":
                self.expertise.append("sense motive")
            elif ability[1] == "add expertise": # envoy # this is not shown on the excel sheet, might just ignore it then # TODO
                possibleExpertise = ["bluff", "computers", "culture", "diplomacy", "disguise", "engineering", "intimidate", "medicine"]
                for expertise in self.expertise:
                    if expertise in possibleExpertise:
                        possibleExpertise.remove(expertise)
                printText = "please enter the skill you would like to add as additional expertise. Possible expertise are: {}".format(", ".join(possibleExpertise))
                entered = self.getUserResponse(possibleExpertise, printText)
                self.expertise.append(entered)
            elif ability[1] == "influence": # solarian # add two skills, one each from two lists
                possibleGraviton = classChoseFeats["solarian"]["graviton"]
                possiblePhoton = classChoseFeats["solarian"]["photon"]
                for influence in self.expertise:
                    if influence in possibleGraviton:
                        possibleGraviton.remove(influence)
                    if influence in possiblePhoton:
                        possiblePhoton.remove(influence)
                printText = "please enter the influence you would like to add as the Graviton influence. Possible influences are: {}".format(", ".join(possibleGraviton))
                entered = self.getUserResponse(possibleGraviton, printText)
                self.expertise.append(entered)
                printText = "please enter the influence you would like to add as the Photon influence. Possible influences are: {}".format(", ".join(possiblePhoton))
                entered = self.getUserResponse(possiblePhoton, printText)
                self.expertise.append(entered)

            elif ability[1] == "weapon": # all # TODO
                pass
            elif ability[1] == "words": # nothing happens
                pass
            else:
                print(ability, "has not yet been implemented")


            result = [replacable for replacable in listReplaceables if replacable in ability[0]]
            if len(result) != 0:
                result = result[0]
                result = [oldAbility for oldAbility in self.listClassAbilities if result in oldAbility]
                if len(result) != 0:
                    result = result[0]
                    result = self.listClassAbilities.index(result)
                    self.listClassAbilities[result] = ability[0]
                else:
                    self.listClassAbilities.append(ability[0])
            else:
                self.listClassAbilities.append(ability[0])

        listToWriteToFile += self.calcSkills()

        listToWriteToFile += self.printAbilities()

        listToWriteToFile += self.printSpells()

        self.writeToFile("listPass", listToWriteToFile)

    def printAbilities(self):
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

        listToWriteToFile = []

        for i in range(len(raceAbilities[self.raceName.split()[0]])):
            raceAbilityBlock = raceAbilities[self.raceName.split()[0]][i]
            listToWriteToFile.append([raceBoxes[i], raceAbilityBlock[0]])

        themeName = self.theme.split("(")[0].rstrip()
        if self.classLevel >= 1:
            listToWriteToFile.append([themeBoxes[0], themeAbilities[themeName][0][0]])
        if self.classLevel >= 6:
            listToWriteToFile.append([themeBoxes[1], themeAbilities[themeName][1][0]])
        if self.classLevel >= 12:
            listToWriteToFile.append([themeBoxes[2], themeAbilities[themeName][2][0]])
        if self.classLevel >= 18:
            listToWriteToFile.append([themeBoxes[3], themeAbilities[themeName][3][0]])

        j = 0
        for i in range(len(self.listClassAbilities)):
            if "Expertise" in self.listClassAbilities[i]: # expertise and influence
                for expertise in self.expertise:
                    listToWriteToFile.append([classBoxes[i + j], self.listClassAbilities[i] + " [{}]".format(expertise)])
                    j += 1
                j -= 1
            else:
                listToWriteToFile.append([classBoxes[i + j], self.listClassAbilities[i]])

        for i in range(len(self.classFeats)):
            listToWriteToFile.append([otherBoxes[i], self.classFeats[i]])

        for i in range(len(self.chosenFeats)):
            listToWriteToFile.append([featBoxes[i], self.chosenFeats[i]])
        return listToWriteToFile


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
            self.initiative = self.mods["dex"] + self.initiative_misc

            listToWriteToFile = []
            listToWriteToFile.append([htmlTags["init_total"], self.initiative])
            listToWriteToFile.append([htmlTags["init_dex"], self.mods["dex"]])
            listToWriteToFile.append([htmlTags["init_misc"], self.initiative_misc])
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
            listToWriteToFile+= self.calcSkills()
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
            listToWriteToFile += self.calcSkills()
            self.featsAndAbilities()
            self.calcHP()
            listToWriteToFile.append([htmlTags["sp"], self.SP])
            listToWriteToFile.append([htmlTags["hp"], self.HP])
            listToWriteToFile.append([htmlTags["rp"], self.RP])
            className = self.className.title() + " (" + str(self.classLevel) + ")"
            if self.className == "soldier":
                className += " [" + str(self.key) + "]"
            listToWriteToFile.append([htmlTags["className"], className])
            self.addSpells()
            listToWriteToFile += self.calcAttack()
            listToWriteToFile += self.calcSave()
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
        listToWriteToFile = []
        listToWriteToFile.append([htmlTags["name"], self.name.title()])
        listToWriteToFile.append([htmlTags["race"], self.raceName.title()])
        listToWriteToFile.append([htmlTags["raceStr"], raceStatList[self.raceName.split()[0]]["strength"]])
        listToWriteToFile.append([htmlTags["raceDex"], raceStatList[self.raceName.split()[0]]["dexterity"]])
        listToWriteToFile.append([htmlTags["raceCon"], raceStatList[self.raceName.split()[0]]["constitution"]])
        listToWriteToFile.append([htmlTags["raceInt"], raceStatList[self.raceName.split()[0]]["intelligence"]])
        listToWriteToFile.append([htmlTags["raceWis"], raceStatList[self.raceName.split()[0]]["wisdom"]])
        listToWriteToFile.append([htmlTags["raceCha"], raceStatList[self.raceName.split()[0]]["charisma"]])
        listToWriteToFile.append([htmlTags["theme"], self.theme.title()])
        listToWriteToFile.append([htmlTags["themeStr"], self.themeAttributes["strength"]])
        listToWriteToFile.append([htmlTags["themeDex"], self.themeAttributes["dexterity"]])
        listToWriteToFile.append([htmlTags["themeCon"], self.themeAttributes["constitution"]])
        listToWriteToFile.append([htmlTags["themeInt"], self.themeAttributes["intelligence"]])
        listToWriteToFile.append([htmlTags["themeWis"], self.themeAttributes["wisdom"]])
        listToWriteToFile.append([htmlTags["themeCha"], self.themeAttributes["charisma"]])

        listToWriteToFile.append([htmlTags["attrStr"], self.attributes["strength"]])
        listToWriteToFile.append([htmlTags["attrDex"], self.attributes["dexterity"]])
        listToWriteToFile.append([htmlTags["attrCon"], self.attributes["constitution"]])
        listToWriteToFile.append([htmlTags["attrInt"], self.attributes["intelligence"]])
        listToWriteToFile.append([htmlTags["attrWis"], self.attributes["wisdom"]])
        listToWriteToFile.append([htmlTags["attrCha"], self.attributes["charisma"]])

        listToWriteToFile.append([htmlTags["attrStrPoint"], self.spentPoints["Str"]])
        listToWriteToFile.append([htmlTags["attrDexPoint"], self.spentPoints["Dex"]])
        listToWriteToFile.append([htmlTags["attrConPoint"], self.spentPoints["Con"]])
        listToWriteToFile.append([htmlTags["attrIntPoint"], self.spentPoints["Int"]])
        listToWriteToFile.append([htmlTags["attrWisPoint"], self.spentPoints["Wis"]])
        listToWriteToFile.append([htmlTags["attrChaPoint"], self.spentPoints["Cha"]])

        listToWriteToFile.append([htmlTags["abilityStr"], self.abilityIncreases["strength"]])
        listToWriteToFile.append([htmlTags["abilityDex"], self.abilityIncreases["dexterity"]])
        listToWriteToFile.append([htmlTags["abilityCon"], self.abilityIncreases["constitution"]])
        listToWriteToFile.append([htmlTags["abilityInt"], self.abilityIncreases["intelligence"]])
        listToWriteToFile.append([htmlTags["abilityWis"], self.abilityIncreases["wisdom"]])
        listToWriteToFile.append([htmlTags["abilityCha"], self.abilityIncreases["charisma"]])

        className = self.className.title() + " (" + str(self.classLevel) + ")"
        if self.className == "soldier":
            className += " [" + str(self.key) + "]"
        listToWriteToFile.append([htmlTags["className"], className])

        listToWriteToFile.append([htmlTags["eac"], self.eac])
        listToWriteToFile.append([htmlTags["eac_armor"], 0])
        listToWriteToFile.append([htmlTags["eac_dex"], self.mods["dex"]])
        listToWriteToFile.append([htmlTags["eac_misc"], 0])
        listToWriteToFile.append([htmlTags["kac"], self.kac])
        listToWriteToFile.append([htmlTags["kac_armor"], 0])
        listToWriteToFile.append([htmlTags["kac_dex"], self.mods["dex"]])
        listToWriteToFile.append([htmlTags["kac_misc"], 0])
        listToWriteToFile.append([htmlTags["vsCombat"], self.vsCombat])

        listToWriteToFile.append([htmlTags["attrStrMod"], self.mods["str"]])
        listToWriteToFile.append([htmlTags["attrDexMod"], self.mods["dex"]])
        listToWriteToFile.append([htmlTags["attrConMod"], self.mods["con"]])
        listToWriteToFile.append([htmlTags["attrIntMod"], self.mods["int"]])
        listToWriteToFile.append([htmlTags["attrWisMod"], self.mods["wis"]])
        listToWriteToFile.append([htmlTags["attrChaMod"], self.mods["cha"]])

        listToWriteToFile.append([htmlTags["init_total"], self.initiative])
        listToWriteToFile.append([htmlTags["init_dex"], self.mods["dex"]])
        listToWriteToFile.append([htmlTags["init_misc"], self.initiative_misc])

        listToWriteToFile += self.calcSave()

        listToWriteToFile += self.calcAttack()

        listToWriteToFile.append([htmlTags["sp"], self.SP])
        listToWriteToFile.append([htmlTags["hp"], self.HP])
        listToWriteToFile.append([htmlTags["rp"], self.RP])

        listToWriteToFile.append([htmlTags["spendablePoints"], 0])
        listToWriteToFile.append([htmlTags["perLevelPoints"], classesStatBonus[self.className]["skills"] + self.mods["int"]])

        listToWriteToFile += self.calcSkills()
        listToWriteToFile += self.printAbilities()

        listToWriteToFile += self.printSpellNumbers()

        listToWriteToFile += self.printSpells()

        self.writeToFile("listPass", listToWriteToFile)

    def readFromHTML(self, fileName):
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

        spellBoxes = [
            ["spell001", "spell002", "spell003", "spell004", "spell005", "spell006", "spell007", "spell008"],
            ["spell101", "spell102", "spell103", "spell104", "spell105", "spell106", "spell107", "spell108"],
            ["spell201", "spell202", "spell203", "spell204", "spell205", "spell206", "spell207"],
            ["spell301", "spell302", "spell303", "spell304", "spell305", "spell306", "spell307"],
            ["spell401", "spell402", "spell403", "spell404", "spell405", "spell406", "spell407"],
            ["spell501", "spell502", "spell503", "spell504", "spell505", "spell506"],
            ["spell601", "spell602", "spell603", "spell604", "spell605", "spell606"]]
        try:
            fp = open("{}.html".format(fileName))
            soup = BeautifulSoup(fp, 'html.parser')

            self.SP                              = soup.find(attrs={"id": htmlTags["sp"]})["value"]
            self.HP                              = soup.find(attrs={"id": htmlTags["hp"]})["value"]
            self.RP                              = soup.find(attrs={"id": htmlTags["rp"]})["value"]

            self.kac                             = soup.find(attrs={"id": htmlTags["kac"]})["value"]
            self.eac                             = soup.find(attrs={"id": htmlTags["eac"]})["value"]

            self.name                            = soup.find(attrs={"id": htmlTags["name"]})["value"]

            self.theme                           = soup.find(attrs={"id": htmlTags["theme"]})["value"].lower()

            self.vsCombat                        = soup.find(attrs={"id": htmlTags["vsCombat"]})["value"]
            self.raceName                        = soup.find(attrs={"id": htmlTags["race"]})["value"].lower()

            classNameLevel                       = soup.find(attrs={"id": htmlTags["className"]})["value"]
            classNameLevel                       = classNameLevel.split()
            self.className                       = classNameLevel[0].lower()
            self.classLevel                      = int(classNameLevel[1][1:-1])

            self.melee_misc                      = int(soup.find(attrs={"id": htmlTags["melee_misc"]})["value"])
            self.range_misc                      = int(soup.find(attrs={"id": htmlTags["range_misc"]})["value"])
            self.throw_misc                      = int(soup.find(attrs={"id": htmlTags["throw_misc"]})["value"])

            self.melee                           = classesStatBonus[self.className]["bab"][self.classLevel - 1] + self.mods["str"] + self.melee_misc
            self.range                           = classesStatBonus[self.className]["bab"][self.classLevel - 1] + self.mods["dex"] + self.range_misc
            self.throw                           = classesStatBonus[self.className]["bab"][self.classLevel - 1] + self.mods["str"] + self.throw_misc

            self.key                             = classesStatBonus[self.className]["key"]
            if self.className == "soldier":
                self.key                         = classNameLevel[2][1:-1]

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

            self.fortSave_misc                   = int(soup.find(attrs={"id": htmlTags["fortSaveMisc"]})["value"])
            self.reflexSave_misc                 = int(soup.find(attrs={"id": htmlTags["reflexSaveMisc"]})["value"])
            self.willSave_misc                   = int(soup.find(attrs={"id": htmlTags["willSaveMisc"]})["value"])

            self.fortSave                        = classesStatBonus[self.className]["fort"][self.classLevel - 1] + self.mods["con"] + self.fortSave_misc
            self.reflexSave                      = classesStatBonus[self.className]["reflex"][self.classLevel - 1] + self.mods["dex"] + self.reflexSave_misc
            self.willSave                        = classesStatBonus[self.className]["will"][self.classLevel - 1] + self.mods["wis"] + self.willSave_misc

            for skill in classesStatBonus["envoy"]["classBonus"]:
                self.skills[skill] = int(soup.find(attrs={"id": htmlTags[skill]})["value"])
                self.skillRanks[skill] = int(soup.find(attrs={"id": htmlTags[skill + "Rank"]})["value"])
                self.skillClass[skill] = int(soup.find(attrs={"id": htmlTags[skill + "Class"]})["value"])
                self.skillMisc[skill] = int(soup.find(attrs={"id": htmlTags[skill + "Misc"]})["value"])
                if self.theme == "spacefarer" and self.skillRanks[skill] == 0:
                    self.skillDabbler[skill] = 2
                    self.skillMisc[skill] -= 2

            for classBox in classBoxes:
                try:
                    classFeat = soup.find(attrs={"id": classBox})["value"]
                    if "Expertise" in classFeat:
                        self.expertise.append(classFeat.split()[1][1:-1])
                        if "Expertise" not in listClassAbilities:
                            self.listClassAbilities.append(classFeat.split()[0])
                    else:
                        self.listClassAbilities.append(classFeat)

                except KeyError:
                    break

            for otherBox in otherBoxes:
                try:
                    otherFeat = soup.find(attrs={"id": otherBox})["value"]
                    self.classFeats.append(otherFeat)
                    if self.className == "soldier":
                        if otherFeat in classChoseFeats["soldier"]["styles"]:
                            self.styles.append(otherFeat)
                    elif self.className == "operative":
                        if otherFeat in classChoseFeats["operative"]["specialization"]:
                            self.styles.append(otherFeat)
                    elif self.className == "mystic":
                        if otherFeat in classChoseFeats["mystic"]["connection"]:
                            self.styles.append(otherFeat)
                except KeyError:
                    break

            for featBox in featBoxes:
                try:
                    chosenFeat = soup.find(attrs={"id": featBox})["value"]
                    self.chosenFeats.append(chosenFeat)
                except KeyError:
                    break


            for i in range(7):
                fullSpellList = []
                for spellBox in spellBoxes[i]:
                    try:

                        addingSpell = soup.find(attrs={"id": htmlTags[spellBox]})["value"]
                        fullSpellList.append(addingSpell)
                    except KeyError:
                        break
                #self.spells[i] + self.additionalSpells[i]
                for j in range(len(fullSpellList)):
                    if j < spellsKnown[self.classLevel - 1][i]:
                        self.spells[i].append(fullSpellList[j])
                    else:
                        self.additionalSpells[i].append(fullSpellList[j])

            # self.expertise
            # self.chosenFeats "weapon focus" or "weapon specialization" or "skill focus"

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

        with open("{}.html".format(self.name.lower()), "w") as out:
            out.write(str(soup))
        fp.close()
