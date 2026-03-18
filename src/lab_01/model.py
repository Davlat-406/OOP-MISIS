
from validate import (
    validate_connections,
    validate_ip,
    validate_name,
    validate_status
)

class Server:
    #Атрибут
    total_servers = 0
    #Доп атрибут
    max_connections = 1000
    
    def __init__(self, name, ip, status="offline", connections=0):
        #Создание по типу пустых папок
        self._name = None
        self._ip = None
        self._status = None
        self._connections = None
        self._active = True  # НОВОЕ СОСТОЯНИЕ
        
        #Вызов валидаций и сеттеров
        self.validate_name(name)
        self.validate_ip(ip)
        self.validate_status(status)
        self.validate_connections(connections)
        
        self.name = name
        self.ip = ip
        self.status = status
        self.connections = connections
        
        Server.total_servers += 1
    
    #Свойства
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self.validate_name(value)#Метод отдельный
        self._name = value.strip()
    
    @property
    def ip(self):
        return self._ip
    
    @ip.setter
    def ip(self, value):
        self.validate_ip(value)#Вызов отдел метода
        self._ip = value
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        self.validate_status(value)#Вызов 
        self._status = value
    
    @property
    def connections(self):
        return self._connections
    
    @connections.setter
    def connections(self, value):
        self.validate_connections(value)#Вызов
        self._connections = int(value)
    
    #Новые методы для состояния
    
    def activate(self):
        """Активировать сервер"""
        if not self._active:
            self._active = True
            return f"Сервер {self._name} активирован"
        return f"Сервер {self._name} уже активен"
    
    def deactivate(self):
        """Деактивировать сервер"""
        if self._active:
            if self._connections > 0:
                raise Exception(f"Нельзя деактивировать: есть активные подключения ({self._connections})")
            self._active = False
            return f"Сервер {self._name} деактивирован"
        return f"Сервер {self._name} уже неактивен"
    
    def is_active(self):
        """Проверка активности"""
        return self._active
    
    
    
    def __str__(self):
        if self._active:
            active_status = "АКТИВЕН"
        else:
            active_status = "НЕАКТИВЕН" 
        return (f"{self._name} ({self._ip}) - {self._status} | "
                f"Подключений: {self._connections} | {active_status}")
    
    def __repr__(self):
        return (f"Server(name='{self._name}', ip='{self._ip}', "
                f"status='{self._status}', connections={self._connections})")
    
    def __eq__(self, other):
        if not isinstance(other, Server):
            return False
        return (self._ip == other._ip) and (self._name == other._name)
    
    #Бизнес метод
    
    
    def ping(self):
        """Проверка доступности"""
        if not self._active:
            return f"Сервер {self._name} НЕАКТИВЕН, пинг невозможен"
        return f"Сервер {self._name} отвечает. Статус: {self._status}"
    
    def connect(self):
        """Подключение к серверу"""
        if not self._active:
            raise Exception(f"Нельзя подключиться: сервер {self._name} неактивен")
        if self._status != "online":
            raise Exception(f"Нельзя подключиться: сервер {self._status}")
        if self._connections >= Server.max_connections:
            raise Exception(f"Достигнут лимит подключений ({Server.max_connections})")
        
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
        self._status = "maintenance"
    
        #Имитация перезагрузки 
        import time
        time.sleep(3)  
    
        self._status = old_status
        return f"Сервер {self._name} перезагружен"
    
