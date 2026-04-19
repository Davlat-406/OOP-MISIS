

from validate import (
    validate_name,
    validate_ip,
    validate_connections,
    validate_status,
    validate_active
)
import time


class Server:
    """Базовый класс для представления сервера"""
    
    def __init__(self, name: str, ip: str, active: bool, connections: int = 0, status: str = "Offline", max_connections: int = 64):
        # Вызов сеттеров для проверки данных
        self.name = name
        self.ip = ip
        self.active = active
        self.connections = connections
        self.status = status
        self._max_connections = max_connections
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not validate_name(value):
            raise ValueError("Некорректное имя сервера")
        self._name = value
    
    @property
    def ip(self):
        return self._ip
    
    @ip.setter
    def ip(self, value):
        if not validate_ip(value):
            raise ValueError("Некорректный IP-адрес")
        self._ip = value
    
    @property
    def active(self):
        return self._active
    
    @active.setter
    def active(self, value):
        if not validate_active(value):
            raise ValueError("Некорректное значение активности")
        self._active = value
    
    @property
    def connections(self):
        return self._connections
    
    @connections.setter
    def connections(self, value):
        if not validate_connections(value):
            raise ValueError("Некорректное количество подключений")
        self._connections = value
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        if not validate_status(value):
            raise ValueError("Некорректный статус сервера")
        self._status = value
    
    @property
    def max_connections(self):
        return self._max_connections
    
    def __str__(self):
        active_status = "Активен" if self._active else "Неактивен"
        return f"Имя: {self.name}, IP: {self.ip}, Статус: {self.status}, Подключений: {self.connections}, {active_status}, Макс. подключений: {self._max_connections}"
    
    def __repr__(self):
        return f"Server(name='{self.name}', ip='{self.ip}', active={self.active}, connections={self.connections}, status='{self.status}', max_connections={self._max_connections})"
    
    def __eq__(self, other):
        if not isinstance(other, Server):
            return NotImplemented
        return (self.name == other.name and 
                self.ip == other.ip and 
                self.active == other.active and 
                self.connections == other.connections and 
                self.status == other.status)
    
    def ping(self):
        """Проверка доступности сервера"""
        if not self._active:
            return f"Сервер {self._name} НЕАКТИВЕН, пинг невозможен"
        return f"Сервер {self._name} отвечает. Статус: {self._status}"
    
    def connect(self):
        """Подключение к серверу"""
        if not self._active:
            raise Exception(f"Нельзя подключиться: сервер {self._name} неактивен")
        if self._status != "Online":
            raise Exception(f"Нельзя подключиться: сервер {self._status}")
        if self._connections >= self._max_connections:
            raise Exception(f"Достигнут лимит подключений ({self._max_connections})")
        
        self._connections += 1
        return f"Подключено к {self._name}. Текущие подключения: {self._connections}"
    
    def disconnect(self):
        """Отключение от сервера"""
        if self._connections <= 0:
            raise Exception("Нет активных подключений")
        self._connections -= 1
        return f"Отключено от {self._name}. Осталось подключений: {self._connections}"
    
    def restart(self):
        """Перезагрузка сервера"""
        if self._connections > 0:
            raise Exception(f"Нельзя перезагрузить: {self._connections} активных подключений")
        
        old_status = self._status
        self._status = "Maintenance"
        
        # Имитация перезагрузки
        time.sleep(1)
        
        self._status = old_status
        return f"Сервер {self._name} перезагружен"