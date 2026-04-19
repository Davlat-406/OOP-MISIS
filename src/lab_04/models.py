

from base import Server
from interfaces import Printable, Comparable


class GameServer(Server, Printable, Comparable):
    """Игровой сервер - дочерний класс от Server"""
    
    def __init__(self, name, ip, active, connections, status, max_connections, game_type, max_players):
        super().__init__(name, ip, active, connections, status, max_connections)
        self._game_type = game_type
        self._max_players = max_players
    
    @property
    def game_type(self):
        return self._game_type
    
    @property
    def max_players(self):
        return self._max_players
    
    def start_match(self):
        return f"Матч на сервере {self.name} (игра: {self._game_type}) начат!"
    
    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str} | Тип игры: {self._game_type} | Макс игроков: {self._max_players}"
    
    # ===== РЕАЛИЗАЦИЯ ИНТЕРФЕЙСА Printable 
    def to_string(self) -> str:
        return f"[GAME] {self.name} | {self._game_type} | {self.connections}/{self._max_players} игроков"
    
    # ===== РЕАЛИЗАЦИЯ ИНТЕРФЕЙСА Comparable 
    def compare_to(self, other) -> int:
        if not isinstance(other, GameServer):
            return 1
        if self._max_players < other._max_players:
            return -1
        elif self._max_players > other._max_players:
            return 1
        else:
            return 0


class DatabaseServer(Server, Printable, Comparable):
    """Сервер базы данных - дочерний класс от Server"""
    
    def __init__(self, name, ip, active, connections, status, max_connections, db_type, storage_gb):
        super().__init__(name, ip, active, connections, status, max_connections)
        self._db_type = db_type
        self._storage_gb = storage_gb
    
    @property
    def db_type(self):
        return self._db_type
    
    @property
    def storage_gb(self):
        return self._storage_gb
    
    def execute_query(self, query):
        return f"Выполнение запроса к {self._db_type}: {query}"
    
    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str} | Тип БД: {self._db_type} | Хранилище: {self._storage_gb} GB"
    
    # реалиация интерфейса Printable 
    def to_string(self) -> str:
        return f"[DB] {self.name} | {self._db_type} | {self._storage_gb}GB | {self.status}"
    
    # реалиация интерфейса Comparable сортировки
    def compare_to(self, other) -> int:
        if not isinstance(other, DatabaseServer):
            return 1
        if self._storage_gb < other._storage_gb:
            return -1
        elif self._storage_gb > other._storage_gb:
            return 1
        else:
            return 0