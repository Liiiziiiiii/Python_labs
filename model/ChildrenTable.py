from model.Desk import Desk
'''
Inherited from Desk
'''

class ChildrenTable(Desk):
    def __init__(self, height, width, length, has_keyboard_tray, age_of_the_child, max_height):
        super().__init__(height, width, length, has_keyboard_tray)
        self.age_of_the_child = age_of_the_child
        self.max_height = max_height

    def increaseTheHeightOfTheTableToTheMaximum(self, centimeters):
        if (self.height + centimeters) < self.max_height:
            print(f"You can increase it by {abs((self.height + centimeters) - self.max_height)} ChildrenTable")
        else:
            print("You cannot increase ChildrenTable")
        return centimeters

    def moveDown(self, centimeters):
        if (self.height + centimeters) > 0:
            print(f"You can reduce it by {self.height + centimeters} ChildrenTable")
        else:
            print("You cannot reduce ChildrenTable")
        return 0

    def __str__(self):
        return f"ChildrenTable(height={self.height}, width={self.width}, length={self.length}, has_keyboard_tray={self.has_keyboard_tray}, age_of_the_child={self.age_of_the_child}, max_height={self.max_height})"
