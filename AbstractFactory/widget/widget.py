from abc import abstractmethod


from abc import ABC

class AutosFactory(ABC):

    @abstractmethod
    def get_turismo(self):
        pass

    @abstractmethod
    def get_sports(self):
        pass

    @abstractmethod
    def get_utilitarian(self):
        pass


class WindowsUI():
    pass

class MacUI():
    pass

class Linux():
    pass