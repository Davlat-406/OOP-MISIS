

from base import Server
from models import GameServer, DatabaseServer
from collection import ServerCollection
from strategies import (
    by_name, by_ip, by_connections, by_status, by_name_then_connections,
    is_online, is_active, is_game_server, is_database_server,
    make_status_filter, make_connections_filter,
    DiscountStrategy, UpgradeStrategy, ReportStrategy,
    to_string, extract_name, extract_ip
)


def print_separator(title):
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)


def print_collection(collection, title="Коллекция"):
    print(f"\n{title} ({len(collection)} объектов):")
    for server in collection:
        print(f"  - {server}")


def main():
    print("ЛАБОРАТОРНАЯ РАБОТА №5: ФУНКЦИИ КАК АРГУМЕНТЫ. СТРАТЕГИИ (ОЦЕНКА 5)")
    

    print_separator("1. СОЗДАНИЕ КОЛЛЕКЦИИ (5+ объектов)")
    
    collection = ServerCollection()
    
    # Добавляем обычные серверы
    collection.add(Server("WebServer", "192.168.1.1", True, 0, "Online", 100))
    collection.add(Server("BackupServer", "192.168.1.2", True, 0, "Offline", 50))
    collection.add(Server("MaintenanceServer", "192.168.1.3", True, 0, "Maintenance", 30))
    
    # Добавляем игровые серверы
    collection.add(GameServer("CS2", "10.0.0.1", True, 45, "Online", 64, "FPS", 32))
    collection.add(GameServer("Valorant", "10.0.0.2", True, 30, "Online", 50, "Tactical", 20))
    collection.add(GameServer("Minecraft", "10.0.0.3", True, 5, "Online", 100, "Sandbox", 50))
    
    # Добавляем серверы БД
    collection.add(DatabaseServer("Postgres", "10.0.0.4", True, 3, "Online", 50, "PostgreSQL", 500))
    collection.add(DatabaseServer("MySQL", "10.0.0.5", True, 8, "Online", 30, "MySQL", 200))
    collection.add(DatabaseServer("Redis", "10.0.0.6", False, 0, "Offline", 20, "Cache", 10))
    
    print_collection(collection, "Исходная коллекция")
    
    # ========== 2. СОРТИРОВКА ТРЕМЯ РАЗНЫМИ СТРАТЕГИЯМИ (для 3) ==========
    print_separator("2. СОРТИРОВКА ТРЁМЯ СТРАТЕГИЯМИ")
    
    # Стратегия 1: по имени
    sorted_by_name = ServerCollection()
    for s in sorted(collection, key=by_name):
        sorted_by_name.add(s)
    print_collection(sorted_by_name, "Сортировка по имени (by_name)")
    
    # Стратегия 2: по количеству подключений
    sorted_by_conn = ServerCollection()
    for s in sorted(collection, key=by_connections):
        sorted_by_conn.add(s)
    print_collection(sorted_by_conn, "Сортировка по подключениям (by_connections)")
    
    # Стратегия 3: по статусу
    sorted_by_status = ServerCollection()
    for s in sorted(collection, key=by_status):
        sorted_by_status.add(s)
    print_collection(sorted_by_status, "Сортировка по статусу (by_status)")
    
    # ========== 3. ФИЛЬТРАЦИЯ ДВУМЯ ФУНКЦИЯМИ (для 3) ==========
    print_separator("3. ФИЛЬТРАЦИЯ ДВУМЯ ФУНКЦИЯМИ")
    
    # Фильтр 1: только онлайн серверы
    online_servers = collection.filter_by(is_online)
    print_collection(online_servers, "Только онлайн серверы")
    
    # Фильтр 2: только активные серверы
    active_servers = collection.filter_by(is_active)
    print_collection(active_servers, "Только активные серверы")
    
    # ========== 4. ПРИМЕНЕНИЕ map (для 4) ==========
    print_separator("4. ПРИМЕНЕНИЕ map (преобразование коллекции)")
    
    # Преобразование в имена
    names = list(map(extract_name, collection))
    print(f"\nИмена всех серверов: {names}")
    
    # Преобразование в строки
    strings = list(map(to_string, collection))
    print(f"\nСтроковые представления (первые 3):")
    for s in strings[:3]:
        print(f"  - {s}")
    
    # ========== 5. ФАБРИКА ФУНКЦИЙ (для 4) ==========
    print_separator("5. ФАБРИКА ФУНКЦИЙ")
    
    # Создаём фильтр для статусов "Online" и "Maintenance"
    status_filter = make_status_filter(["Online", "Maintenance"])
    filtered_by_status = collection.filter_by(status_filter)
    print_collection(filtered_by_status, "Серверы со статусом Online или Maintenance")
    
    # Создаём фильтр для подключений (от 20 до 50)
    connections_filter = make_connections_filter(min_connections=20, max_connections=50)
    filtered_by_conn = collection.filter_by(connections_filter)
    print_collection(filtered_by_conn, "Серверы с подключениями от 20 до 50")
    
    # ========== 6. МЕТОДЫ COLLECTION: sort_by(), filter_by(), apply() (для 4) ==========
    print_separator("6. МЕТОДЫ sort_by(), filter_by(), apply()")
    
    # Сортировка через метод коллекции
    collection.sort_by(by_name)
    print_collection(collection, "После sort_by(by_name)")
    
    # Фильтрация через метод коллекции
    game_servers = collection.filter_by(is_game_server)
    print_collection(game_servers, "Только игровые серверы (filter_by)")
    
    # Применение функции (apply)
    names_list = collection.apply(extract_name)
    print(f"\nИмена через apply(): {names_list}")
    
    # ========== 7. CALLABLE-ОБЪЕКТ (паттерн Стратегия) (для 5) ==========
    print_separator("7. CALLABLE-ОБЪЕКТЫ (ПАТТЕРН СТРАТЕГИЯ)")
    
    # Создаём стратегию скидки
    discount = DiscountStrategy(0.15)
    print(f"Стратегия: {discount}")
    
    # Применяем стратегию к серверам
    apply_results = collection.apply(discount)
    print("Результаты применения скидки:")
    for res in apply_results[:5]:
        print(f"  - {res}")
    
    # Другая стратегия
    upgrade = UpgradeStrategy("max_connections")
    print(f"\nСтратегия: {upgrade}")
    upgrade_results = collection.apply(upgrade)
    print("Результаты улучшения серверов:")
    for res in upgrade_results[:5]:
        print(f"  - {res}")
    
    # ========== 8. ЦЕПОЧКА ОПЕРАЦИЙ (для 5) ==========
    print_separator("8. ЦЕПОЧКА ОПЕРАЦИЙ")
    
    # Создаём новую коллекцию
    chain_collection = ServerCollection()
    chain_collection.add(Server("ServerA", "1.1.1.1", True, 10, "Online", 100))
    chain_collection.add(Server("ServerB", "1.1.1.2", True, 50, "Online", 100))
    chain_collection.add(Server("ServerC", "1.1.1.3", False, 0, "Offline", 100))
    chain_collection.add(GameServer("GameX", "2.2.2.1", True, 80, "Online", 100, "FPS", 50))
    chain_collection.add(DatabaseServer("DBX", "2.2.2.2", True, 20, "Online", 50, "PostgreSQL", 1000))
    
    print_collection(chain_collection, "Исходная коллекция для цепочки")
    
    # Цепочка: фильтр -> сортировка -> применение
    print("\n--- ПРИМЕР ЦЕПОЧКИ: filter_by(is_online).sort_by(by_connections).apply(discount) ---")
    
    result = (chain_collection
        .filter_by(is_online)
        .sort_by(by_connections)
        .apply(DiscountStrategy(0.2)))
    
    print("Результаты цепочки:")
    for res in result:
        print(f"  - {res}")
    
    # Цепочка: фильтр по типу -> сортировка -> отчёт
    print("\n--- ДРУГАЯ ЦЕПОЧКА: filter_by(is_game_server).sort_by(by_name).apply(extract_name) ---")
    
    game_names = (chain_collection
        .filter_by(is_game_server)
        .sort_by(by_name)
        .apply(extract_name))
    
    print(f"Имена игровых серверов по алфавиту: {game_names}")
    
       # ========== 9. ЗАМЕНА СТРАТЕГИИ БЕЗ ИЗМЕНЕНИЯ КОДА КОЛЛЕКЦИИ ==========
    print_separator("9. ЗАМЕНА СТРАТЕГИИ БЕЗ ИЗМЕНЕНИЯ КОДА")
    
    # СОЗДАЁМ КОЛЛЕКЦИЮ (раньше её не было!)
    test_collection = ServerCollection()
    test_collection.add(Server("ZServer", "1.1.1.1", True, 0, "Online", 100))
    test_collection.add(Server("AServer", "1.1.1.2", True, 0, "Online", 100))
    test_collection.add(Server("MServer", "1.1.1.3", True, 0, "Online", 100))
    
    print("Исходный порядок: ZServer, AServer, MServer")
    
    test_collection.sort_by(by_name)
    print(f"После sort_by(by_name): {list(map(extract_name, test_collection))}")
    
    test_collection.sort_by(by_ip)
    print(f"После sort_by(by_ip): {list(map(extract_name, test_collection))}")
    
    # ========== 10. СРАВНЕНИЕ lambda И ИМЕНОВАННОЙ ФУНКЦИИ (для 4) ==========
    print_separator("10. lambda vs ИМЕНОВАННАЯ ФУНКЦИЯ")
    
    lambda_collection = ServerCollection()
    lambda_collection.add(Server("BServer", "1.1.1.1", True, 0, "Online", 100))
    lambda_collection.add(Server("AServer", "1.1.1.2", True, 0, "Online", 100))
    lambda_collection.add(Server("CServer", "1.1.1.3", True, 0, "Online", 100))
    
    # Сортировка через lambda
    lambda_collection.sort_by(lambda x: x.name)
    print(f"Сортировка через lambda: {list(map(extract_name, lambda_collection))}")
    
    # Сортировка через именованную функцию (by_name)
    lambda_collection.sort_by(by_name)
    print(f"Сортировка через by_name: {list(map(extract_name, lambda_collection))}")
    
    # Фильтрация через lambda
    filtered_lambda = lambda_collection.filter_by(lambda x: x.name > "AServer")
    print(f"Фильтр через lambda (name > 'AServer'): {list(map(extract_name, filtered_lambda))}")
    
    # ========== ИТОГ ==========
    print_separator("ВЫВОД")
    print("Лабораторная работа №5 выполнена на оценку 5")
    print("Реализовано:")
    print("  - 5+ стратегий сортировки (by_name, by_ip, by_connections, by_status, by_name_then_connections)")
    print("  - 4+ функции-фильтра (is_online, is_active, is_game_server, is_database_server)")
    print("  - Применение map, filter, sorted")
    print("  - Фабрика функций (make_status_filter, make_connections_filter)")
    print("  - Callable-объекты (DiscountStrategy, UpgradeStrategy, ReportStrategy)")
    print("  - Методы sort_by(), filter_by(), apply() в коллекции")
    print("  - Цепочка операций filter_by().sort_by().apply()")
    print("  - Замена стратегии без изменения кода коллекции")
    print("\nРабота завершена успешно!")


if __name__ == "__main__":
    main()
    