from dataclasses import dataclass
from typing import Literal, Optional

ArmorWeight = Literal["Heavy", "Light"]
DamageType = Literal["Acid", "Cold", "Electricity", "Fire", "Sonic", "Bludgeoning", "Piercing",
                     "Slashing"]
DamageAmount = Literal['1d3', '1d4', '2d4', '3d4', '4d4', '5d4', '6d4', '7d4', '8d4', '12d4',
                       '1d6', '2d6', '3d6', '4d6', '5d6', '6d6', '8d6', '9d6', '11d6', '12d6',
                       '16d6', '1d8', '2d8', '3d8', '5d8', '8d8', '4d8', '6d8', '7d8', '9d8',
                       '12d8', '1d10', '2d10', '3d10', '4d10', '5d10', '6d10', '7d10', '8d10',
                       '10d10', '12d10', '1d12', '2d12', '3d12', '4d12', '5d12', '6d12', '7d12',
                       '8d12', '9d12']

@dataclass
class Item:
    name: str
    value: int
    level: int

@dataclass
class Weapon(Item):
    damage_type: DamageType
    damage_amount: DamageAmount
    critical: Optional[str]

@dataclass
class RangedWeapon(Weapon):
    weapon_range: int
    capacity: int
    usage: int

@dataclass
class Armor(Item):
    armor_weight: ArmorWeight
    eac: int
    kac: int
    dex: str
    ac_penalty: Optional[str]
    speed: Optional[str]
    upgrade_slots: int
