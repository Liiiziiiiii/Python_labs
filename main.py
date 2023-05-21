
class WritingDesk:
    __instance = None
    def __init__(self, number_of_drawers=2, has_keyboard_tray=True, max_weight = 10,  current_height=10, max_height=20):
        self.number_of_drawers = number_of_drawers
        self.has_keyboard_tray = has_keyboard_tray
        self.max_weight = max_weight
        self.current_height = current_height
        self.max_height = max_height



    def __str__(self):
        return (f"WritingDesk: numberOfDrawers {self.number_of_drawers}, hasKeyboardTray {self.has_keyboard_tray}, " 
               f"maxWeightCapacity {self.max_weight}, currentHeight {self.current_height}, "
               f"maxHeight {self.max_height}")

    def adjust_height(self, centimeters):
        '''
        increase table if height !=  max height
        '''

        if (self.current_height + centimeters) < self.max_height:
            print("You can increase it by", abs((self.current_height + centimeters) - self.max_height))
        else:
            print("You cannot increase it")

    def move_down(self, centimeters):
        '''
        reduce table if current height != 0

        '''
        if self.current_height + centimeters > 0:
            print("You can reduce it by", (self.current_height + centimeters))
        else:
            print("You cannot reduce it")

    @staticmethod
    def get_instance():
        if not WritingDesk.__instance:
            WritingDesk.__instance = WritingDesk()
        return WritingDesk.__instance



writing_desks = [
    WritingDesk(),
    WritingDesk(40, True, 100, 20, 100),
    WritingDesk.get_instance(),
    WritingDesk.get_instance()
]



for writing_desk in writing_desks:
    print(writing_desk)
