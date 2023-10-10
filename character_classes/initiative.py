class Initiative:
    def __init__(self) -> None:
        self.initiative = 0
        self.initiative_misc = 0

    def update_initiative(self, dex_mod):
        self.initiative = dex_mod + self.initiative_misc
