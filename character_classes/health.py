class Health:
    stamina_points: int
    hit_points: int
    resolve_points: int
    def __init__(self) -> None:
        self.stamina_points = 0
        self.hit_points = 0
        self.resolve_points = 0

    def update_hit_points(self, *,
                        class_hp: int,
                        race_hp: int,
                        class_stamina: int,
                        class_mod: int,
                        con_mod: int,
                        character_level: int) -> None:
        """calculates the current HP, SP, and RP
        """
        self.stamina_points = max(1, (max(0, class_stamina + con_mod)) * character_level)
        self.hit_points = max(1, (class_hp * character_level) + race_hp)
        self.resolve_points = max(1, max(1, character_level // 2) + class_mod)
