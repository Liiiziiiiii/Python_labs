from manager.set_manager import SetManager
from model.children_table import ChildrenTable
from model.coffee_table import CoffeeTable
from model.dining_table import DiningTable
from model.writing_desk import WritingDesk


class RegularManager:
    def __init__(self):
        self.desks = []


# Creating an instance of the RegularManager class
regular_manager = RegularManager()

# Adding drones to the drone_list attribute of the regular_manager
regular_manager.desks.append(CoffeeTable(50, 10, 10, False, 10, 10, 10, 9))
regular_manager.desks.append(DiningTable(50, 350, 9600, False, 10, 10))
regular_manager.desks.append(ChildrenTable(60, 130, 3, False, 5000, 10))
regular_manager.desks.append(WritingDesk(10, 60, 60, True, 30, 40))

# Creating an instance of the SetManager class with the regular_manager object
set_manager = SetManager(regular_manager)

# Now you can perform operations on the set_manager object
# such as iterating over favorite sets, getting the length, accessing items by index, etc.
