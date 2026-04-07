from model import Server


class ServerCollection:
    #Коллекция серверов - контейнер для хранения объектов Server
    
    def __init__(self):
        #Инициализация пустой коллекции
        self._items = []
    
    def add(self, server):
        
        #Добавить сервер в коллекцию
        #Проверка: тип должен быть Server, не должно быть дубликата по IP
        
        # Проверка типа
        if not isinstance(server, Server):
            raise TypeError(f"Можно добавлять только объекты Server")
        
        # Проверка на дубликат по IP
        for existing in self._items:
            if existing.ip == server.ip:
                raise ValueError(f"Сервер с IP {server.ip} уже существует в коллекции")
        
        self._items.append(server)
    
    def remove(self, server):
        #Удалить сервер из коллекции
        if server not in self._items:
            raise ValueError(f"Сервер {server.name} не найден в коллекции")
        self._items.remove(server)
    
    def remove_at(self, index):
        #Удалить сервер по индексу (для оценки 5)
        length = len(self._items)
        if index < 0:
            index = length + index
        if index < 0 or index >= length:
            raise IndexError(f"Индекс {index} вне диапазона. Длина коллекции: {length}")
        return self._items.pop(index)
    
    def get_all(self):
        #Вернуть список всех серверов
        return self._items.copy()
    
    def find_by_name(self, name):
        #Найти сервер по имени (для оценки 4)
        for server in self._items:
            if server.name == name:
                return server
        return None
    
    def find_by_ip(self, ip):
        #Найти сервер по IP-адресу (для оценки 4)
        for server in self._items:
            if server.ip == ip:
                return server
        return None
    
    def find_by_status(self, status):
        #Найти все серверы с определённым статусом
        result = ServerCollection()
        for server in self._items:
            if server.status == status:
                result.add(server)
        return result
    
    def __len__(self):
        #Вернуть количество серверов в коллекции
        return len(self._items)
    
    def __iter__(self):
        #Сделать коллекцию итерируемой
        return iter(self._items)
    
    def __getitem__(self, index):
        #Доступ по индексу collection[0] и collection[-1]
        length = len(self._items)
        
        if isinstance(index, slice):
            # Поддержка срезов
            result = ServerCollection()
            for server in self._items[index]:
                result.add(server)
            return result
        else:
            # Поддержка одиночного индекса (включая отрицательные)
            if index < 0:
                index = length + index
            if index < 0 or index >= length:
                raise IndexError(f"Индекс {index} вне диапазона. Длина коллекции: {length}")
            return self._items[index]
    
    def __str__(self): #Просто красивый вывод
        if len(self._items) == 0:
            return "Коллекция пуста"
        
        result = f"Коллекция серверов (всего: {len(self._items)}):\n"
        result += "-" * 50 + "\n"
        for i, server in enumerate(self._items):
            result += f"{i+1}. {server}\n"
        return result
    
    def __repr__(self):
        #Для прогеров
        return f"ServerCollection({len(self._items)} servers)"
    
    def sort_by_name(self):
        #Сортировка по имени
        self._items.sort(key=lambda s: s.name)
    
    def sort_by_ip(self):
        #Сортировка по IP-адресу 
        self._items.sort(key=lambda s: s.ip)
    
    def sort_by_connections(self):
        #Сортировка по количеству подключений
        self._items.sort(key=lambda s: s.connections)
    
    def sort_by_status(self):
        #Сортировка по статусу
        status_order = {"Online": 0, "Offline": 1, "Maintenance": 2}
        self._items.sort(key=lambda s: status_order.get(s.status, 3))
    
    def get_active_servers(self):
        #Вернуть новую коллекцию только с активными серверами
        result = ServerCollection()
        for server in self._items:
            if server.active:
                result.add(server)
        return result
    
    def get_inactive_servers(self):
        #Вернуть новую коллекцию только с неактивными серверами
        result = ServerCollection()
        for server in self._items:
            if not server.active:
                result.add(server)
        return result
    
    def get_online_servers(self):
        #Вернуть новую коллекцию только с онлайн серверами
        result = ServerCollection()
        for server in self._items:
            if server.status == "Online":
                result.add(server)
        return result
    
    def get_servers_with_connections(self, min_connections=0, max_connections=None):
        #Вернуть коллекцию серверов с подключениями в заданном диапазоне
        result = ServerCollection()
        for server in self._items:
            if server.connections >= min_connections:
                if max_connections is None or server.connections <= max_connections:
                    result.add(server)
        return result
    