from items.item import Armor, Weapon
from items.item_constants import RangedWeaponConstants, MeleeWeapon, LightArmorConstants, HeavyArmorConstants

class Inventory:
    def __init__(self, starting_balance=0):
        self.items = []
        self.balance = starting_balance

    def add_item(self, item):
        self.items.append(item)

    def buy_item(self, item):
        if item.value <= self.balance:
            self.add_item(item)
            self.balance -= item.value
            print(f"Bought {item.name}. Remaining balance: {self.balance}")
        else:
            print(f"Insufficient funds to buy the item. Current funds are only: {self.balance}. Item costs: {item.value}")

    def spend_money(self, money):
        if money <= self.balance:
            self.balance -= money
            print(f"Bought something for {money}. Remaining balance: {self.balance}")
        else:
            print(f"Insufficient funds to buy the item. Current funds are only: {self.balance}. Item costs: {money}")

    def display_inventory(self):
        print("Inventory:")
        for idx, item in enumerate(self.items, start=1):
            print(f"{idx}. {item.name} - Value: {item.value}")

# Example usage
if __name__ == "__main__":
    inventory = Inventory(starting_balance=500)

    sword = MeleeWeapon.BATON_TACTICAL
    shield = LightArmorConstants.SECOND_SKIN

    inventory.buy_item(sword)
    inventory.buy_item(shield)

    inventory.display_inventory()
