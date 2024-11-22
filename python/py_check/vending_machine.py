from dataclasses import dataclass

class VendingMachine:
  def __init__(self, inventory):
    self.inventory = inventory
    return

  def show_welcome(self) -> str:
    return "Hello. Please make a selection."

  def get_inventory(self):

    return self.inventory

  def add_to_inventory(self, item):
    #need to check what is already in inventory
    # check the slot
    inv = {}
    if inv[item.slot] == null
      inv[item.slot] = item
      
    # self.inventory.append(item)

  def purchase_product(self, slot, cash):
    for item in self.inventory:
        if slot == item.slot and item.quantity > 0: 
            if cash == item.price:
                item.quantity -= 1
                return "Thanks for purchasing!"
            elif slot == item.slot and cash > item.price:
                item.quantity -= 1
                change = cash - item.price
                return "Thanks for purchasing! Your change: " + str(change)
            else:
                return "Please add more money" 
        elif slot == item.slot and item.quantity == 0:
            return "Out of Inventory!"

    return "Invalid item selected."
