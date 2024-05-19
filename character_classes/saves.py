class Saves:
    def __init__(self) -> None:
        self.fort_save = 0
        self.reflex_save = 0
        self.will_save = 0

        self.fort_save_misc = 0
        self.reflex_save_misc = 0
        self.will_save_misc = 0

    def update_saves(self, fort, reflex, will, con_mod, dex_mod, wis_mod):
        self.fort_save = fort + con_mod + self.fort_save_misc
        self.reflex_save = reflex + dex_mod + self.reflex_save_misc
        self.will_save = will + wis_mod + self.will_save_misc
