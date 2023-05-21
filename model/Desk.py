from abc import ABC, abstractmethod
'''
abstract class
his children:ChildrenTable, CoffeeTable, DiningTable, WritingDesk
'''


class Desk(ABC):
    # def init(self, height, width, length, has_keyboard_tray):
    #     self.height = height
    #     self.width = width
    #     self.length = length
    #     self.has_keyboard_tray = has_keyboard_tray

    def __init__(self, height, width, length, has_keyboard_tray):
        self.height = height
        self.width = width
        self.length = length
        self.has_keyboard_tray = has_keyboard_tray

    def get_height(self):
        return self.height


@abstractmethod
def increasetheheightofthetabletothemaximum(self, centimeters):
    '''
    abstract method that tells whether it is possible to increase
    the height of the table, provided that
     the height is != the maximum height
    '''
    pass


@abstractmethod
def movedown(self, centimeters):
    '''
    abstract method that tells whether it is possible to reduce
     the height of the table provided that it is != 0
    '''
    pass
