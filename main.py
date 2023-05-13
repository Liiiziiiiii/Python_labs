class WritingDesk:
    def __init__(self, number_of_drawers=0, has_keyboard_tray=False, max_weight_capacity=0, current_height=0, max_height=0):
        self.__number_of_drawers = number_of_drawers
        self.__has_keyboard_tray = has_keyboard_tray
        self.__max_weight_capacity = max_weight_capacity
        self.__current_height = current_height
        self.__max_height = max_height

    @property
    def has_keyboard_tray(self):
        return self.__has_keyboard_tray

    @has_keyboard_tray.setter
    def has_keyboard_tray(self, value):
        pass


    @property
    def number_of_drawers(self):
        return self.__number_of_drawers

    @number_of_drawers.setter
    def number_of_drawers(self, value):
        pass

    def __str__(self):
        return f"WritingDesk: numberOfDrawers {self.__number_of_drawers}, hasKeyboardTray {self.__has_keyboard_tray}, " \
               f"maxWeightCapacity {self.__max_weight_capacity}, currentHeight {self.__current_height}, " \
               f"maxHeight {self.__max_height}"

    def adjust_height(self, centimeters):
        if (self.__current_height + centimeters) < self.__max_height:
            print("You can increase it by", abs((self.__current_height + centimeters) - self.__max_height))
        else:
            print("You cannot increase it")

    def move_down(self, centimeters):
        if self.__current_height + centimeters > 0:
            print("You can reduce it by", (self.__current_height + centimeters))
        else:
            print("You cannot reduce it")

    @staticmethod
    def get_instance():
        if not WritingDesk.instance:
            WritingDesk.instance = WritingDesk()
        return WritingDesk.instance



writing_desks = [
    WritingDesk(),
    WritingDesk(4, True, 9, 2, 100),
    WritingDesk.get_instance(),
    WritingDesk.get_instance()
]

for writing_desk in writing_desks:
    print(writing_desk)
