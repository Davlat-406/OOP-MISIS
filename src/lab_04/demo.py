# demo.py
# Демонстрация работы интерфейсов и абстрактных классов (ЛР-4, оценка 5)

from base import Server
from models import GameServer, DatabaseServer
from collection import ServerCollection
from interfaces import Printable, Comparable, Connectable


def print_separator(title):
    """Печать разделителя с заголовком"""
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)


def print_all(printable_items):
    """
    Универсальная функция, работающая через интерфейс Printable
    Принимает список объектов, реализующих Printable
    """
    print("\n--- Вывод через интерфейс Printable ---")
    for item in printable_items:
        print(f"  {item.to_string()}")


def compare_all(comparable_items):
    """
    Универсальная функция, работающая через интерфейс Comparable
    """
    print("\n--- Сравнение через интерфейс Comparable ---")
    for i in range(len(comparable_items) - 1):
        result = comparable_items[i].compare_to(comparable_items[i + 1])
        if result < 0:
            print(f"  {comparable_items[i].name} < {comparable_items[i + 1].name}")
        elif result > 0:
            print(f"  {comparable_items[i].name} > {comparable_items[i + 1].name}")
        else:
            print(f"  {comparable_items[i].name} == {comparable_items[i + 1].name}")


def main():
    print("ЛАБОРАТОРНАЯ РАБОТА №4: ИНТЕРФЕЙСЫ И АБСТРАКТНЫЕ КЛАССЫ (ОЦЕНКА 5)")
    
    # ========== 1. СОЗДАНИЕ ОБЪЕКТОВ ==========
    print_separator("1. СОЗДАНИЕ ОБЪЕКТОВ РАЗНЫХ ТИПОВ")
    
    # Обычный сервер
    server = Server("WebServer", "192.168.1.1", True, 0, "Online", 100)
    
    # Игровой сервер
    game = GameServer("CS2", "10.0.0.1", True, 10, "Online", 64, "FPS", 32)
    
    # Сервер БД
    db = DatabaseServer("Postgres", "10.0.0.2", True, 5, "Online", 50, "PostgreSQL", 500)
    
    print("Созданы объекты:")
    print(f"  {server}")
    print(f"  {game}")
    print(f"  {db}")
    
    # ========== 2. ПРОВЕРКА РЕАЛИЗАЦИИ ИНТЕРФЕЙСОВ ==========
    print_separator("2. ПРОВЕРКА РЕАЛИЗАЦИИ ИНТЕРФЕЙСОВ (isinstance)")
    
    for obj in [server, game, db]:
        print(f"\n  {obj.name}:")
        print(f"    Printable: {isinstance(obj, Printable)}")
        print(f"    Comparable: {isinstance(obj, Comparable)}")
        print(f"    Connectable: {isinstance(obj, Connectable)}")
    
    # ========== 3. УНИВЕРСАЛЬНАЯ ФУНКЦИЯ print_all() ==========
    print_separator("3. УНИВЕРСАЛЬНАЯ ФУНКЦИЯ print_all()")
    
    printable_list = [server, game, db]
    print_all(printable_list)
    
    # ========== 4. РАБОТА ЧЕРЕЗ ИНТЕРФЕЙС Connectable ==========
    print_separator("4. РАБОТА ЧЕРЕЗ ИНТЕРФЕЙС Connectable")
    
    for obj in [server, game, db]:
        if isinstance(obj, Connectable):
            print(f"\n  {obj.name}:")
            print(f"    Есть подключения: {obj.is_connected()}")
            try:
                print(f"    Подключаемся: {obj.connect()}")
                print(f"    Отключаемся: {obj.disconnect()}")
            except Exception as e:
                print(f"    Ошибка: {e}")
    
    # ========== 5. РАБОТА ЧЕРЕЗ ИНТЕРФЕЙС Comparable ==========
    print_separator("5. РАБОТА ЧЕРЕЗ ИНТЕРФЕЙС Comparable")
    
    compare_all([game, db])
    
    # ========== 6. КОЛЛЕКЦИЯ И ФИЛЬТРАЦИЯ ПО ИНТЕРФЕЙСУ ==========
    print_separator("6. КОЛЛЕКЦИЯ И ФИЛЬТРАЦИЯ ПО ИНТЕРФЕЙСУ")
    
    collection = ServerCollection()
    collection.add(server)
    collection.add(game)
    collection.add(db)
    
    print("Все объекты в коллекции:")
    for s in collection:
        print(f"  - {s.name}")
    
    print("\nТолько объекты, реализующие Printable:")
    for s in collection.get_printable():
        print(f"  - {s.name}: {s.to_string()}")
    
    print("\nТолько объекты, реализующие Comparable:")
    for s in collection.get_comparable():
        print(f"  - {s.name}")
    
    # ========== 7. ПОЛИМОРФИЗМ ЧЕРЕЗ ИНТЕРФЕЙС ==========
    print_separator("7. ПОЛИМОРФИЗМ (без if type ==)")
    
    print("Вызов to_string() для разных объектов:")
    for obj in [server, game, db]:
        print(f"  {obj.__class__.__name__}: {obj.to_string()}")
    
    # ========== 8. ДОБАВЛЕНИЕ НОВЫХ ОБЪЕКТОВ И ПРОВЕРКА ФИЛЬТРАЦИИ ==========
    print_separator("8. ДОБАВЛЕНИЕ НОВЫХ ОБЪЕКТОВ И ПРОВЕРКА ФИЛЬТРАЦИИ")
    
    game2 = GameServer("Valorant", "10.0.0.3", True, 20, "Online", 50, "Tactical FPS", 20)
    db2 = DatabaseServer("MySQL", "10.0.0.4", True, 3, "Online", 30, "MySQL", 200)
    offline_server = Server("Backup", "10.0.0.5", False, 0, "Offline", 100)
    
    collection.add(game2)
    collection.add(db2)
    collection.add(offline_server)
    
    print(f"Всего объектов в коллекции: {len(collection)}")
    
    print("\nИгровые серверы (get_game_servers):")
    for s in collection.get_game_servers():
        print(f"  - {s.name}: {s.game_type}, макс игроков: {s.max_players}")
    
    print("\nСерверы БД (get_database_servers):")
    for s in collection.get_database_servers():
        print(f"  - {s.name}: {s.db_type}, хранилище: {s.storage_gb} GB")
    
    # ========== 9. СОРТИРОВКА ==========
    print_separator("9. СОРТИРОВКА КОЛЛЕКЦИИ")
    
    print("Сортировка по имени:")
    collection.sort_by_name()
    for s in collection:
        print(f"  - {s.name}")
    
    # ========== 10. СЦЕНАРИЙ: МОНИТОРИНГ СЕРВЕРОВ ==========
    print_separator("10. СЦЕНАРИЙ: МОНИТОРИНГ СЕРВЕРОВ")
    
    monitoring = ServerCollection()
    monitoring.add(GameServer("Minecraft", "10.1.1.1", True, 5, "Online", 100, "Sandbox", 50))
    monitoring.add(GameServer("Rust", "10.1.1.2", True, 45, "Online", 100, "Survival", 100))
    monitoring.add(DatabaseServer("MongoDB", "10.1.1.3", True, 3, "Online", 50, "NoSQL", 500))
    monitoring.add(DatabaseServer("Redis", "10.1.1.4", False, 0, "Offline", 20, "Cache", 10))
    
    print("Мониторинг серверов (вывод через интерфейс Printable):")
    for s in monitoring.get_printable():
        print(f"  {s.to_string()}")
    
    print("\nАктивные серверы:")
    for s in monitoring.get_active_servers():
        print(f"  - {s.name}: {s.status}")
    
    print("\nСерверы с высокими подключениями (>40):")
    high_load = monitoring.get_servers_with_connections(min_connections=40)
    for s in high_load:
        print(f"  - {s.name}: {s.connections} подключений")
    
    # ========== 11. ЗАПРЕТ ДУБЛИКАТОВ ==========
    print_separator("11. ЗАПРЕТ ДУБЛИКАТОВ")
    
    try:
        duplicate = GameServer("CS2", "10.0.0.1", True, 0, "Online", 64, "FPS", 32)
        collection.add(duplicate)
    except ValueError as e:
        print(f"Ошибка (корректно): {e}")
    
    # ========== 12. ДОСТУП ПО ИНДЕКСУ ==========
    print_separator("12. ДОСТУП ПО ИНДЕКСУ (__getitem__)")
    
    print(f"Первый сервер: {collection[0].name}")
    print(f"Последний сервер: {collection[-1].name}")
    print("Срез [1:4]:")
    for s in collection[1:4]:
        print(f"  - {s.name}")

if __name__ == "__main__":
    main()