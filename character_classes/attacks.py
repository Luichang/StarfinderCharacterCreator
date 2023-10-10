class Attacks:
    def __init__(self) -> None:
        self.melee = 0
        self.range = 0
        self.throw = 0
        self.melee_misc = 0
        self.range_misc = 0
        self.throw_misc = 0

    def update_attack(self, bab, str_mod, dex_mod):
        """update attack tab related boxes. Needs class_name to be set
        """
        self.melee = bab + str_mod + self.melee_misc
        self.range = bab + dex_mod + self.range_misc
        self.throw = bab + str_mod + self.throw_misc
