class DeskManager:
    def __init__(self):
        self.desks = []

    def add_desk(self, new_desk):
        self.desks.append(new_desk)

    def add_desks(self, desks):
        self.desks.extend(desks)

    def find_all_with_height_greater_than(self, height):
        return [desk for desk in self.desks if desk.get_height() > height]

    def find_with_keyboard_tray(self):
        return [desk for desk in self.desks if desk.has_keyboard_tray]
