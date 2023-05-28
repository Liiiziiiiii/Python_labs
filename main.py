from manager.desk_manager import DeskManager
from model.coffee_table import CoffeeTable
from model.dining_table import DiningTable
from model.children_table import ChildrenTable
from model.writing_desk import WritingDesk

desks = [CoffeeTable(50, 10, 10, False, 10, 10, 10, 9),
         DiningTable(50, 350, 9600, False, 10, 10),
         ChildrenTable(60, 130, 3, False, 5000, 10),
         WritingDesk(10, 60, 60, True, 30, 40)]

desk_manager = DeskManager()

desk_manager.add_desks(desks)
desk_manager.add_desk(DiningTable(20, 10, 10, False, 10, 10))

desks_with_greater_height = desk_manager.increase_the_high_to_the_table_to_the_maximum(10)

for desk in desks_with_greater_height:
    print(desk)

print("\nDesks with keyboard tray:\n")

desks_with_keyboard_tray = desk_manager.move_down()

for desk in desks_with_keyboard_tray:
    print(desk)

print("List of heights:")
print(desk_manager.list_of_height())

print("\nIndexed list:")
desk_manager.indexed_list()

print("\nNumeric list:")
desk_manager.numeric_list()

print("\nAll and Any conditions:")
print(desk_manager.check_condition_all_any(5))
