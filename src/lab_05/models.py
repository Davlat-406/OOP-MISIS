
from base import Server


class GameServer(Server):
    """Игровой сервер - дочерний класс от Server"""
    
    def __init__(self, name, ip, active, connections, status, max_connections, game_type, max_players):
        # Вызов конструктора родителя
        super().__init__(name, ip, active, connections, status, max_connections)
        
        # Новые атрибуты
        self._game_type = game_type#вид игры
        self._max_players = max_players#максимальное кол-во игроков
    
    @property
    def game_type(self):
        return self._game_type
    
    @property
    def max_players(self):
        return self._max_players
    
    # Новый метод
    def start_match(self):
        return f"Матч на сервере {self.name} (игра: {self._game_type}) начат!"
    
    # Переопределение метода __str__
    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str} | Тип игры: {self._game_type} | Макс игроков: {self._max_players}"


class DatabaseServer(Server):
    """Сервер базы данных - дочерний класс от Server"""
    
    def __init__(self, name, ip, active, connections, status, max_connections, db_type, storage_gb):
        # Вызов конструктора родителя
        super().__init__(name, ip, active, connections, status, max_connections)
        
        # Новые атрибуты
        self._db_type = db_type #тип хранилища
        self._storage_gb = storage_gb #объем хранилища
    
    @property
    def db_type(self):
        return self._db_type
    
    @property
    def storage_gb(self):
        return self._storage_gb
    
    # Новый метод
    def execute_query(self, query):
        return f"Выполнение запроса к {self._db_type}: {query}"
    
    # Переопределение метода __str__
    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str} | Тип БД: {self._db_type} | Хранилище: {self._storage_gb} GB"