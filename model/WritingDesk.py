from model.Desk import Desk


class WritingDesk(Desk):

    def __init__(self, height, width, length, has_keyboard_tray, age_of_the_child, max_height):
        super().__init__(height, width, length, has_keyboard_tray)
        self.age_of_the_child = age_of_the_child
        self.max_height = max_height

    def increase_the_height_of_the_table_to_the_maximum(self, centimeters):
        if (self.height + centimeters) < self.max_height:
            print(f"You can increase it by {abs((self.height + centimeters) - self.max_height)} WritingDesk")
        else:
            print("You cannot increase WritingDesk")
        return centimeters

    def move_down(self, centimeters):
        if (self.height + centimeters) > 0:
            print(f"You can reduce it by {self.height + centimeters} WritingDesk")
        else:
            print("You cannot reduce WritingDesk")
        return 0

    def __str__(self):
        return f"WritingDesk(height={self.height}, width={self.width}, length={self.length}, has_keyboard_tray={self.has_keyboard_tray}, age_of_the_child={self.age_of_the_child}, max_height={self.max_height})"