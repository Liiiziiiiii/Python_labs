from typing import List

from decorators.argument_count_decorator import argument_count_decorator
from decorators.no_more_than_3_outputs_decorator import no_more_than_3_outputs_decorator
from model.desk import Desk
from model.writing_desk import WritingDesk


class DeskManager:
    # def __init__(self):
    #     self.desks = []

    def __init__(self):
        self.desks: List[Desk] = []

    def __len__(self):
        return len(self.desks)

    def __getitem__(self, item):
        return self.desks.append(item)

    def __iter__(self):
        return iter(self.desks)

    def list_of_height(self):
        print("list_of_heights")
        height_list = [desk.width for desk in self.desks]
        return height_list

    def indexed_list(self):
        print("Indexed_list:")
        for index, desk in enumerate(self.desks):
            print(index + 1, desk)

    def numeric_list(self):
        print("Numeric_list:")
        for object, function in zip(self.desks, self.list_of_height()):
            print(object, function)

    def check_condition_all_any(self, value):
        print("All and Any:")
        all_satisfy = all(plate.width > value for plate in self.desks)
        any_satisfy = any(plate.width > value for plate in self.desks)
        return {"all": all_satisfy, "any": any_satisfy}

    def add_desk(self, desk):
        self.desks.append(desk)

    def add_desks(self, desks):
        self.desks.extend(desks)

    @no_more_than_3_outputs_decorator
    def increase_the_high_to_the_table_to_the_maximum(self, weight):
        return list(filter(lambda desk: desk.get_height() > weight, self.desks))

    @argument_count_decorator
    def move_down(self):
        return list(filter(lambda desk: isinstance(desk, WritingDesk) and desk.has_keyboard_tray == True, self.desks))
