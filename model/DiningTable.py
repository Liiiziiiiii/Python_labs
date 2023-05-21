from model.Desk import Desk


class DiningTable(Desk):


    def init(self, height, width, length, has_keyboard_tray, number_of_seats, max_height):
        super().init(height, width, length, has_keyboard_tray)
        self.number_of_seats = number_of_seats
        self.max_height = max_height

    def increase_the_height_of_the_table_to_the_maximum(self, centimeters):
        if (self.height + centimeters) < self.max_height:
            print(f"You can increase it by {abs((self.height + centimeters) - self.max_height)} DiningTable")
        else:
            print("You cannot increase DiningTable")
        return 0

    def move_down(self, centimeters):
        if (self.height + centimeters) > 0:
            print(f"You can reduce it by {self.height + centimeters} DiningTable")
        else:
            print("You cannot reduce DiningTable")
        return 0

    def __str__(self):
        return f"DiningTable(height={self.height}, width={self.width}, length={self.length}, has_keyboard_tray={self.has_keyboard_tray}, number_of_seats={self.number_of_seats}, max_height={self.max_height})"

