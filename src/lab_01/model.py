from validate import (
    validate_name,
    validate_ip,
    validate_connections,
    validate_status,
    validate_active
)
import time

class Server():
    
    def __init__(self, name: str, ip: str, active: bool, connections: int = 0, status: str = "Offline", max_connections: int = 64):
        
        self._name = name
        self._ip = ip
        self._active = active
        self._connections = connections
        self._status = status
        self._max_connections = max_connections
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        
        if not validate_name(value):
            raise ValueError
        
        self._name = value
    
    @property
    def ip(self):
        return self._ip
    
    @ip.setter
    def ip(self, value):
        
        if not validate_ip(value):
            raise ValueError
        
        self._name = value
    
    @property
    def active(self):
        return self._active
    
    @active.setter
    def active(self, value):
        
        if not validate_active(value):
            raise ValueError
        
        self._name = value
    
    @property
    def connections(self):
        return self._connections
    
    @connections.setter
    def connections(self, value):
        
        if not validate_connections(value):
            raise ValueError
        
        self._name = value
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        
        if not validate_status(value):
            raise ValueError

        self._status = value
        
    def __str__(self):
        
        return f"Имя: {self.name}, Айпи: {self.ip}, Статус: {self.status}, Кол-во соединений: {self.connections}, Доступен/Недоступен: {self.active}"
    
    def __repr__(self):
        
        return f"name={self.name}, ip={self.ip}, status={self.status}, connections={self.connections}"
    
    def __eq__(self, value):
        
        if not isinstance(value, Server):
            return NotImplemented

        return (self.name == value.name
                and self.ip == value.ip
                and self.active == value.active
                and self.connections == value.connections
                and self.status == value.status) 
    
    def ping(self):
        """Проверка доступности"""
        if not self._active:
            return f"Сервер {self._name} НЕАКТИВЕН, пинг невозможен"
        return f"Сервер {self._name} отвечает."
    
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
    
        #Имитация перезагрузки 
        time.sleep(3)  
    
        self._status = old_status
        return f"Сервер {self._name} перезагружен"
    
    
    
object = Server('asda','123.213.123.123',True, 0,"Offline",54)
object_2 = Server('sdfghj',"222.222.222.222",True, 0,"Offline",54)
print(object)
object.ip = "111.111.111.111"
object.status = "Online"
object.connect()
object_2.connect()
print(object)
print(object_2)