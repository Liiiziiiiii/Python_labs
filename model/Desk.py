from abc import ABC, abstractmethod


class Desk(ABC):

    # def init(self, height, width, length, has_keyboard_tray):
    #     self.height = height
    #     self.width = width
    #     self.length = length
    #     self.has_keyboard_tray = has_keyboard_tray

    def __init__(self, height=10, width=10, length=10, hasKeyboardTray=True):
        self.height = height
        self.width = width
        self.length = length
        self.hasKeyboardTray = hasKeyboardTray

    @abstractmethod
    def increaseTheHeightOfTheTableToTheMaximum(self, centimeters):
        pass

    @abstractmethod
    def moveDown(self, centimeters):
        pass
