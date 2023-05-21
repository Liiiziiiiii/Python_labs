from manager.DeskManager import DeskManager
from model.Desk import Desk
from model.CoffeeTable import CoffeeTable
from model.DiningTable import DiningTable
from model.ChildrenTable import ChildrenTable

print("\t\tFIRST PART\n")

desks = [CoffeeTable(10, 10, 10, False, 10, 10, 10, 10),
         DiningTable(35, 350, 9600, False),
         ChildrenTable(60, 130, 3, False, 5000, 10)]

for desk in desks:
    print(desk)

desk_manager = DeskManager()
for desk in desks:
    desk_manager.add_desk(desk)
desk_manager.add_desk(DiningTable(20, 10, 10, True, 10, 10))

print("\n\t\tSECOND PART\n")
print("Desks with height greater than 10:\n")

desks_with_greater_height = desk_manager.find_all_with_height_greater_than(10)

for desk in desks_with_greater_height:
    print(desk)

print("\nDesks with keyboard tray:\n")

desks_with_keyboard_tray = desk_manager.find_with_keyboard_tray()

for desk in desks_with_keyboard_tray:
    print(desk)
