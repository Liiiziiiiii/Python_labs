class DeskManager:


    def init(self):
        self.desks = []

    def add_drone(self, new_drone):
        self.drone_list.append(new_drone)

    def add_drones(self, drones):
        self.drone_list.extend(drones)

    def get_desks(self):
        return self.desks

    def find_all_with_height_greater_than(self, height):
        return [desk for desk in self.desks_list if desk.get_height() > height]

    def find_with_keyboard_tray(self):
        return [desk for desk in self.desks_list if desk.has_keyboard_tray]


