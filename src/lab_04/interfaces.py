
from abc import ABC, abstractmethod


class Printable(ABC):
    """Интерфейс для объектов, которые можно вывести в строку"""
    
    @abstractmethod
    def to_string(self) -> str:
        """Вернуть строковое представление объекта"""
        pass


class Comparable(ABC):
    """Интерфейс для объектов, которые можно сравнивать"""
    
    @abstractmethod
    def compare_to(self, other) -> int:
        """
        Сравнить текущий объект с other
        """
        pass


class Connectable(ABC):
    """Интерфейс для объектов, к которым можно подключиться"""
    
    @abstractmethod
    def connect(self) -> str:
        """Подключиться к объекту"""
        pass
    
    @abstractmethod
    def disconnect(self) -> str:
        """Отключиться от объекта"""
        pass
    
    @abstractmethod
    def is_connected(self) -> bool:
        """Проверить, есть ли подключение"""
        pass
