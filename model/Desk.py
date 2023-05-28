from abc import ABC, abstractmethod

'''
abstract class
his children:ChildrenTable, CoffeeTable, DiningTable, WritingDesk
'''


class Desk(ABC):

    def __init__(self, height, width, length, has_keyboard_tray):
        self.height = height
        self.width = width
        self.length = length
        self.has_keyboard_tray = has_keyboard_tray
        self.material = None

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def dir_list(self, value=None):
        if value is not None:
            mydict = {k: v for k, v in self.__dict__.items() if isinstance(value, value)}
            print(mydict)

    def __iter__(self):
        yield from self.__dict__.items()


@abstractmethod
def increase_the_heigh_to_the_tableto_the_maximum():
    """
    abstract method that tells whether it is possible to increase
    the height of the table, provided that
     the height is != the maximum height
    """
    pass


@abstractmethod
def move_down():
    """
    abstract method that tells whether it is possible to reduce
     the height of the table provided that it is != 0
    """
    pass
