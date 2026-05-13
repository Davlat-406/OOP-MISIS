from base import Server
from models import GameServer, DatabaseServer


def by_name(item):
    """Стратегия сортировки по имени (алфавит)"""
    return item.name


def by_ip(item):
    """Стратегия сортировки по IP-адресу"""
    return item.ip


def by_connections(item):
    """Стратегия сортировки по количеству подключений"""
    return item.connections


def by_status(item):
    """Стратегия сортировки по статусу (Online -> Offline -> Maintenance)"""
    status_order = {"Online": 0, "Offline": 1, "Maintenance": 2}
    return status_order.get(item.status, 3)


def by_name_then_connections(item):
    """Стратегия сортировки по имени, затем по подключениям"""
    return (item.name, item.connections)


def is_online(item):
    """Фильтр: оставить только онлайн серверы"""
    return item.status == "Online"


def is_active(item):
    """Фильтр: оставить только активные серверы"""
    return item.active


def has_high_load(item, threshold=40):
    """Фильтр: серверы с нагрузкой выше порога"""
    return item.connections >= threshold


def is_game_server(item):
    """Фильтр: оставить только игровые серверы"""
    return isinstance(item, GameServer)


def is_database_server(item):
    """Фильтр: оставить только серверы БД"""
    return isinstance(item, DatabaseServer)



def to_string(item):
    """Преобразовать объект в строку"""
    return str(item)


def extract_name(item):
    """Извлечь имя сервера"""
    return item.name


def extract_ip(item):
    """Извлечь IP-адрес"""
    return item.ip


def apply_discount(item, discount=0.1):
    """Применить скидку (шутка для демонстрации)"""
    # Здесь можно добавить реальную логику, например, уменьшить max_connections
    return item


def make_status_filter(allowed_statuses):
    """
    Фабрика: создаёт фильтр для статусов.
    Возвращает функцию, которая проверяет, находится ли статус в allowed_statuses.
    """
    def status_filter(item):
        return item.status in allowed_statuses
    return status_filter


def make_connections_filter(min_connections=0, max_connections=None):
    """
    Фабрика: создаёт фильтр для количества подключений.
    """
    def connections_filter(item):
        if item.connections < min_connections:
            return False
        if max_connections is not None and item.connections > max_connections:
            return False
        return True
    return connections_filter



class DiscountStrategy:
    """
    Callable-объект для применения скидки.
    Используется как стратегия в apply()
    """
    def __init__(self, percent):
        self.percent = percent
    
    def __call__(self, item):
        # Здесь можно применить скидку к серверу
        # Для демонстрации просто возвращаем строку
        return f"{item.name}: применена скидка {self.percent*100}%"
    
    def __str__(self):
        return f"DiscountStrategy({self.percent*100}%)"


class UpgradeStrategy:
    """
    Callable-объект для улучшения сервера.
    """
    def __init__(self, upgrade_type):
        self.upgrade_type = upgrade_type
    
    def __call__(self, item):
        if self.upgrade_type == "max_connections":
            # Увеличиваем максимальное количество подключений
            item._max_connections = int(item._max_connections * 1.5)
            return f"{item.name}: максимальные подключения увеличены до {item._max_connections}"
        elif self.upgrade_type == "speed":
            return f"{item.name}: скорость сервера увеличена"
        return f"{item.name}: улучшен по типу {self.upgrade_type}"
    
    def __str__(self):
        return f"UpgradeStrategy({self.upgrade_type})"


class ReportStrategy:
    """
    Callable-объект для генерации отчёта.
    """
    def __call__(self, item):
        return {
            "name": item.name,
            "ip": item.ip,
            "status": item.status,
            "connections": item.connections,
            "active": item.active
        }
    
    def __str__(self):
        return "ReportStrategy (генерирует словарь с данными)"