import pytest
from py_check.vending_machine import *
from py_check.vending_item import *

class TestVendingMachine:
  @pytest.fixture(autouse=True)
  def setup_class(self):
      inventory = []
      self.vending_machine = VendingMachine(inventory)

      item = VendingItem()
      item.slot = "A1"
      item.type = "Squirtle"
      item.quantity = 10
      item.price = 2.50

      item2 = VendingItem()
      item2.slot = "A2"
      item2.type = "Charmander"
      item2.quantity = 10
      item2.price = 5.50

      self.vending_machine.add_to_inventory(item)
      self.vending_machine.add_to_inventory(item2)

  def test_show_welcome_should_print_welcome_message(self):
      # Arrange
      inventory = []
      vending_machine = VendingMachine(inventory)

      #Act 
      test_message = vending_machine.show_welcome()

      #Assert
      assert test_message == "Hello. Please make a selection."


  def test_get_inventory_should_return_current_vending_inventory(self):
      # Arrange
      expected_inventory = []
      vending_machine = VendingMachine(expected_inventory)

      # Act
      result_inventory = vending_machine.get_inventory()

      # Assert
      assert len(result_inventory) == 0

  def test_add_to_inventory_should_add_item_to_current_inventory(self):
      # Arrange
      item = VendingItem()
      item.slot = "A1"
      item.type = "Squirtle"
      item.quantity = 10
      item.price = 2.50

      inventory = []
      vending_machine = VendingMachine(inventory)

      # Act
      vending_machine.add_to_inventory(item)
      
      # Assert
      assert len(vending_machine.inventory) == 1    
      
  def test_purchase_product_should_hand_out_item_when_money_exact(self):
      # Arrange
      item = VendingItem()
      item.slot = "A1"
      item.type = "Squirtle"
      item.quantity = 10
      item.price = 2.50

      inventory = []
      vending_machine = VendingMachine(inventory)

      vending_machine.add_to_inventory(item)

      # Act
      message = vending_machine.purchase_product("A1", 2.50)
      
      # Assert
      assert message == "Thanks for purchasing!"  

  # test_purchase_product_should_hand_out_item_when_money_more_than_enough

  def test_purchase_product_should_hand_out_item_when_money_more_than_enough(self):
      # Arrange
      item = VendingItem()
      item.slot = "A1"
      item.type = "Squirtle"
      item.quantity = 10
      item.price = 2.50

      inventory = []
      vending_machine = VendingMachine(inventory)

      vending_machine.add_to_inventory(item)

      # Act
      message = vending_machine.purchase_product("A1", 3)
      
      # Assert
      assert message == "Thanks for purchasing! Your change: 0.5"  

  def test_purchase_product_should_return_msg_when_money_not_enough(self):
      # Arrange
      item = VendingItem()
      item.slot = "A1"
      item.type = "Squirtle"
      item.quantity = 10
      item.price = 2.50

      inventory = []
      vending_machine = VendingMachine(inventory)

      vending_machine.add_to_inventory(item)

      # Act
      message = vending_machine.purchase_product("A1", 1)
      
      # Assert
      assert message == "Please add more money"  

  def test_purchase_product_should_return_item_when_enough_money_and_second_item(self):
      # Arrange
      item = VendingItem()
      item.slot = "A1"
      item.type = "Squirtle"
      item.quantity = 10
      item.price = 2.50

      item2 = VendingItem()
      item2.slot = "A2"
      item2.type = "Charmander"
      item2.quantity = 10
      item2.price = 5.50
      inventory = []
      vending_machine = VendingMachine(inventory)

      vending_machine.add_to_inventory(item)
      vending_machine.add_to_inventory(item2)

      # Act
      message = vending_machine.purchase_product("A2", 6)
      
      # Assert
      assert message == "Thanks for purchasing! Your change: 0.5"  
      
  def test_purchase_product_should_error_when_out_of_inventory(self):
    # Arrange
    item = VendingItem()
    item.slot = "A1"
    item.type = "Squirtle"
    item.quantity = 1
    item.price = 2.50

    inventory = []
    vending_machine = VendingMachine(inventory)

    vending_machine.add_to_inventory(item)

    # Act
    message = vending_machine.purchase_product("A1", 2.50)
    message2 = vending_machine.purchase_product("A1", 2.50)
    
    # Assert
    assert message == "Thanks for purchasing!" 
    assert message2 == "Out of Inventory!"  

  def test_purchase_product_should_error_slot_doesnt_exist(self):
    # Arrange
    item = VendingItem()
    item.slot = "A1"
    item.type = "Squirtle"
    item.quantity = 1
    item.price = 2.50

    inventory = []
    vending_machine = VendingMachine(inventory)

    vending_machine.add_to_inventory(item)

    # Act
    message = vending_machine.purchase_product("Z1", 2.50)
    
    # Assert
    assert message == "Invalid item selected." 