from model.desk import Desk


class CoffeeTable(Desk):
    def __init__(self, height, width, length, has_keyboard_tray, number_of_guests, number_of_shelves, mini_height, max_height):
        super().__init__(height, width, length, has_keyboard_tray)
        self.number_of_guests = number_of_guests
        self.number_of_shelves = number_of_shelves
        self.mini_height = mini_height
        self.max_height = max_height
        self.material = {"glass", "wood"}

    def increaseTheHeightOfTheTableToTheMaximum(self, centimeters):
        if (self.height + centimeters) < self.max_height:
            print(f"You can increase it by {abs((self.height + centimeters) - self.max_height)} CoffeeTable")
        else:
            print("You cannot increase CoffeeTable")
        return 0

    def moveDown(self, centimeters):
        if (self.height + centimeters) > 0:
            print(f"You can reduce it by {self.height + centimeters} CoffeeTable")
        else:
            print("You cannot reduce CoffeeTable")
        return 0




    def __str__(self):
        return f"CoffeeTable(height={self.height}, width={self.width}, length={self.length}, has_keyboard_tray={self.has_keyboard_tray}, number_of_guests={self.number_of_guests}, number_of_shelves={self.number_of_shelves}, mini_height={self.mini_height}, max_height={self.max_height})"
