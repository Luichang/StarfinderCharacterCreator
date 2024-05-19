class Spells:
    def __init__(self) -> None:
        self.race_spells = []
        self.is_priest = False
        self.spellcaster = False

    def update_race_spells(self, race_spell_list):
        self.race_spells = race_spell_list

    def update_theme_spells(self, is_priest: bool):
        self.is_priest = is_priest
