# demo.py
# Демонстрация работы наследования и полиморфизма (ЛР-3, оценка 5)

from base import Server
from models import GameServer, DatabaseServer
from collection import ServerCollection


def print_separator(title):
    """Печать разделителя с заголовком"""
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)


def main():
    print("ЛАБОРАТОРНАЯ РАБОТА №3: НАСЛЕДОВАНИЕ И ПОЛИМОРФИЗМ (ОЦЕНКА 5)")
    
    # ========== 1. СОЗДАНИЕ ОБЪЕКТОВ ==========
    print_separator("1. СОЗДАНИЕ ОБЪЕКТОВ")
    
    try:
        # Обычный сервер
        server = Server("WebServer", "192.168.1.1", True, 0, "Online", 100)
        
        # Игровой сервер
        game = GameServer("CS2", "10.0.0.1", True, 10, "Online", 64, "FPS", 32)
        
        # Сервер БД
        db = DatabaseServer("Postgres", "10.0.0.2", True, 5, "Online", 50, "PostgreSQL", 500)
        
        print("Созданы объекты:")
        print(f"  - {server}")
        print(f"  - {game}")
        print(f"  - {db}")
    except Exception as e:
        print(f"Ошибка создания объектов: {e}")
        return

    # ========== 2. НОВЫЕ МЕТОДЫ ДОЧЕРНИХ КЛАССОВ ==========
    print_separator("2. НОВЫЕ МЕТОДЫ ДОЧЕРНИХ КЛАССОВ")
    
    print(f"GameServer.start_match(): {game.start_match()}")
    print(f"DatabaseServer.execute_query(): {db.execute_query('SELECT * FROM users')}")
    
    # ========== 3. ПРОВЕРКА НАСЛЕДОВАНИЯ ==========
    print_separator("3. ПРОВЕРКА НАСЛЕДОВАНИЯ")
    
    print("Вызов методов родителя у дочерних объектов:")
    print(f"  game.ping(): {game.ping()}")
    print(f"  db.ping(): {db.ping()}")
    print(f"  game.connect(): {game.connect()}")
    print(f"  game.disconnect(): {game.disconnect()}")
    
    # ========== 4. ПЕРЕОПРЕДЕЛЕНИЕ __str__ ==========
    print_separator("4. ПЕРЕОПРЕДЕЛЕНИЕ __str__ (разное поведение)")
    
    print("Вывод через print для разных типов:")
    print(f"  Server: {server}")
    print(f"  GameServer: {game}")
    print(f"  DatabaseServer: {db}")
    
    # ========== 5. КОЛЛЕКЦИЯ С РАЗНЫМИ ТИПАМИ ==========
    print_separator("5. КОЛЛЕКЦИЯ С РАЗНЫМИ ТИПАМИ СЕРВЕРОВ")
    
    collection = ServerCollection()
    collection.add(server)
    collection.add(game)
    collection.add(db)
    
    print(f"Всего серверов в коллекции: {len(collection)}")
    print("\nСодержимое коллекции:")
    for s in collection:
        print(f"  - {s}")
    
    # ========== 6. ПРОВЕРКА ТИПОВ (isinstance) ==========
    print_separator("6. ПРОВЕРКА ТИПОВ (isinstance)")
    
    for s in collection:
        if isinstance(s, GameServer):
            print(f"  {s.name} - это игровой сервер (игра: {s.game_type})")
        elif isinstance(s, DatabaseServer):
            print(f"  {s.name} - это сервер БД (тип: {s.db_type})")
        elif isinstance(s, Server):
            print(f"  {s.name} - это обычный сервер")
    
    # ========== 7. ФИЛЬТРАЦИЯ ПО ТИПУ ==========
    print_separator("7. ФИЛЬТРАЦИЯ ПО ТИПУ")
    
    # Добавим ещё серверов для наглядности
    game2 = GameServer("Valorant", "10.0.0.3", True, 0, "Online", 50, "Tactical FPS", 20)
    db2 = DatabaseServer("MySQL", "10.0.0.4", True, 3, "Online", 30, "MySQL", 200)
    
    collection.add(game2)
    collection.add(db2)
    
    print("Игровые серверы (get_game_servers):")
    game_servers = collection.get_game_servers()
    for s in game_servers:
        print(f"  - {s.name}: {s.game_type}, макс игроков: {s.max_players}")
    
    print("\nСерверы БД (get_database_servers):")
    db_servers = collection.get_database_servers()
    for s in db_servers:
        print(f"  - {s.name}: {s.db_type}, хранилище: {s.storage_gb} GB")
    
    # ========== 8. ПОЛИМОРФИЗМ ==========
    print_separator("8. ПОЛИМОРФИЗМ (один метод - разное поведение)")
    
    print("Вызов __str__ для всех объектов в коллекции:")
    for s in collection:
        print(f"  {s.__class__.__name__}: {s}")
    
    # ========== 9. ЗАПРЕТ ДУБЛИКАТОВ ==========
    print_separator("9. ЗАПРЕТ ДУБЛИКАТОВ")
    
    try:
        duplicate = GameServer("CS2", "10.0.0.1", True, 0, "Online", 64, "FPS", 32)
        collection.add(duplicate)
    except ValueError as e:
        print(f"Ошибка (корректно): {e}")
    
    # ========== 10. УДАЛЕНИЕ ==========
    print_separator("10. УДАЛЕНИЕ СЕРВЕРОВ")
    
    print(f"Коллекция до удаления: {len(collection)} серверов")
    collection.remove(server)
    print(f"После удаления обычного сервера: {len(collection)} серверов")
    
    # ========== 11. ПОЛНЫЙ СЦЕНАРИЙ ==========
    print_separator("11. СЦЕНАРИЙ: ИГРОВОЙ КЛАСТЕР")
    
    # Создаём кластер игровых серверов
    game_cluster = ServerCollection()
    
    g1 = GameServer("DE_Dust2", "10.1.1.1", True, 24, "Online", 32, "CS2", 32)
    g2 = GameServer("DE_Inferno", "10.1.1.2", True, 18, "Online", 32, "CS2", 32)
    g3 = GameServer("SummonersRift", "10.1.1.3", True, 12, "Online", 10, "LoL", 10)
    
    game_cluster.add(g1)
    game_cluster.add(g2)
    game_cluster.add(g3)
    
    print("Игровой кластер:")
    for s in game_cluster:
        print(f"  - {s.name} | Игра: {s.game_type} | Игроки: {s.connections}/{s.max_players}")
    
    print(f"\nВсего игровых серверов: {len(game_cluster)}")
    print("Все серверы в кластере активны и онлайн!")
    
    # ========== ИТОГ ==========
    print_separator("ВЫВОД")
    print("Лабораторная работа №3 выполнена на оценку 5")
    print("Реализовано:")
    print("  - Базовый класс Server")
    print("  - Дочерние классы: GameServer, DatabaseServer")
    print("  - Новые атрибуты (game_type, max_players, db_type, storage_gb)")
    print("  - Новые методы (start_match, execute_query)")
    print("  - Переопределение __str__")
    print("  - Полиморфизм (разное поведение __str__)")
    print("  - Фильтрация коллекции по типу (get_game_servers, get_database_servers)")
    print("  - Проверка типов через isinstance()")
    print("\nРабота завершена успешно!")


if __name__ == "__main__":
    main()