# demo.py
# Демонстрация работы класса ServerCollection (ЛР-2, оценка 5)

from model import Server
from collection import ServerCollection
import time


def print_separator(title):
    """Печать разделителя с заголовком"""
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)


def main():
    print("ЛАБОРАТОРНАЯ РАБОТА №2: КОЛЛЕКЦИЯ ОБЪЕКТОВ")
    print("Класс ServerCollection - контейнер для хранения серверов")

    # ========== 1. СОЗДАНИЕ СЕРВЕРОВ ==========
    print_separator("1. СОЗДАНИЕ СЕРВЕРОВ")
    
    try:
        server1 = Server("WebServer", "192.168.1.10", True, 0, "Online", 100)
        server2 = Server("DbServer", "192.168.1.20", True, 5, "Online", 50)
        server3 = Server("TestServer", "10.0.0.1", False, 0, "Offline", 10)
        server4 = Server("BackupServer", "192.168.1.30", True, 2, "Online", 200)
        server5 = Server("MaintenanceServer", "10.0.0.5", True, 0, "Maintenance", 20)
        
        print("Созданы серверы:")
        print(f"  - {server1}")
        print(f"  - {server2}")
        print(f"  - {server3}")
        print(f"  - {server4}")
        print(f"  - {server5}")
    except Exception as e:
        print(f"Ошибка создания серверов: {e}")
        return

    # ========== 2. ДОБАВЛЕНИЕ В КОЛЛЕКЦИЮ ==========
    print_separator("2. ДОБАВЛЕНИЕ СЕРВЕРОВ В КОЛЛЕКЦИЮ")
    
    collection = ServerCollection()
    
    print("Добавляем серверы в коллекцию...")
    collection.add(server1)
    collection.add(server2)
    collection.add(server3)
    collection.add(server4)
    collection.add(server5)
    
    print(f"Коллекция содержит {len(collection)} серверов")
    print(collection)

    # ========== 3. ПРОВЕРКА ЗАПРЕТА ДУБЛИКАТОВ ==========
    print_separator("3. ПРОВЕРКА ЗАПРЕТА ДУБЛИКАТОВ")
    
    try:
        print("Пытаемся добавить сервер с существующим IP (192.168.1.10)...")
        duplicate_server = Server("WebServer2", "192.168.1.10", True, 0, "Online", 100)
        collection.add(duplicate_server)
    except ValueError as e:
        print(f"Ошибка (корректно): {e}")

    # ========== 4. ПРОВЕРКА ТИПА ПРИ ДОБАВЛЕНИИ ==========
    print_separator("4. ПРОВЕРКА ТИПА ДОБАВЛЯЕМЫХ ОБЪЕКТОВ")
    
    try:
        print("Пытаемся добавить строку вместо сервера...")
        collection.add("это не сервер")
    except TypeError as e:
        print(f"Ошибка (корректно): {e}")

    # ========== 5. ПОИСК ОБЪЕКТОВ (find_by_*) ==========
    print_separator("5. ПОИСК ОБЪЕКТОВ (find_by_*)")
    
    print("Поиск по имени 'DbServer':")
    found = collection.find_by_name("DbServer")
    print(f"  Результат: {found}")
    
    print("\nПоиск по IP '10.0.0.1':")
    found = collection.find_by_ip("10.0.0.1")
    print(f"  Результат: {found}")
    
    print("\nПоиск по несуществующему имени 'NoName':")
    found = collection.find_by_name("NoName")
    print(f"  Результат: {found}")

    # ========== 6. ИТЕРАЦИЯ (__iter__) И ДЛИНА (__len__) ==========
    print_separator("6. ИТЕРАЦИЯ ПО КОЛЛЕКЦИИ (for server in collection)")
    
    print("Перебираем все серверы в коллекции:")
    for i, server in enumerate(collection):
        print(f"  {i+1}. {server.name} - {server.status} - {server.connections} подключений")
    
    print(f"\nВсего серверов в коллекции: {len(collection)}")

    # ========== 7. ДОСТУП ПО ИНДЕКСУ (__getitem__) ==========
    print_separator("7. ДОСТУП ПО ИНДЕКСУ (collection[n])")
    
    print(f"Первый сервер: {collection[0]}")
    print(f"Второй сервер: {collection[1]}")
    print(f"Последний сервер: {collection[-1]}")
    
    print("\nСрез [1:3]:")
    sliced = collection[1:3]
    for server in sliced:
        print(f"  - {server.name}")

    # ========== 8. СОРТИРОВКА ==========
    print_separator("8. СОРТИРОВКА КОЛЛЕКЦИИ")
    
    # Создаём копию для демонстрации сортировки
    sorted_collection = ServerCollection()
    sorted_collection.add(server1)
    sorted_collection.add(server2)
    sorted_collection.add(server3)
    sorted_collection.add(server4)
    sorted_collection.add(server5)
    
    print("Исходный порядок:")
    for server in sorted_collection:
        print(f"  - {server.name}")
    
    print("\nСортировка по имени (sort_by_name):")
    sorted_collection.sort_by_name()
    for server in sorted_collection:
        print(f"  - {server.name}")
    
    print("\nСортировка по количеству подключений (sort_by_connections):")
    sorted_collection.sort_by_connections()
    for server in sorted_collection:
        print(f"  - {server.name}: {server.connections} подключений")

    # ========== 9. ФИЛЬТРАЦИЯ (логические операции) ==========
    print_separator("9. ФИЛЬТРАЦИЯ КОЛЛЕКЦИИ")
    
    print("Активные серверы (get_active_servers):")
    active_servers = collection.get_active_servers()
    for server in active_servers:
        print(f"  - {server.name}")
    
    print(f"\nКоличество активных серверов: {len(active_servers)}")
    
    print("\nОнлайн серверы (get_online_servers):")
    online_servers = collection.get_online_servers()
    for server in online_servers:
        print(f"  - {server.name}")
    
    print("\nСерверы с подключениями более 0:")
    connected_servers = collection.get_servers_with_connections(min_connections=1)
    for server in connected_servers:
        print(f"  - {server.name}: {server.connections} подключений")

    # ========== 10. УДАЛЕНИЕ ==========
    print_separator("10. УДАЛЕНИЕ СЕРВЕРОВ")
    
    print(f"Коллекция до удаления: {len(collection)} серверов")
    print(collection)
    
    print("Удаляем TestServer (по объекту):")
    collection.remove(server3)
    print(f"После удаления: {len(collection)} серверов")
    
    print("\nУдаляем по индексу 2 (remove_at):")
    removed = collection.remove_at(2)
    print(f"Удалён сервер: {removed.name}")
    print(f"После удаления: {len(collection)} серверов")
    
    print("\nКоллекция после удалений:")
    print(collection)

    # ========== 11. ЖИЗНЕННЫЙ ЦИКЛ (сценарий использования) ==========
    print_separator("11. СЦЕНАРИЙ ИСПОЛЬЗОВАНИЯ: МОНИТОРИНГ СЕРВЕРОВ")
    
    # Создаём новую коллекцию для сценария
    monitoring = ServerCollection()
    
    print("Создаём тестовые серверы для мониторинга...")
    mon1 = Server("Frontend", "10.0.1.1", True, 45, "Online", 100)
    mon2 = Server("Backend", "10.0.1.2", True, 30, "Online", 100)
    mon3 = Server("Cache", "10.0.1.3", True, 0, "Maintenance", 50)
    mon4 = Server("Database", "10.0.1.4", False, 0, "Offline", 100)
    
    monitoring.add(mon1)
    monitoring.add(mon2)
    monitoring.add(mon3)
    monitoring.add(mon4)
    
    print(f"\nСостояние системы: {len(monitoring)} серверов")
    print(monitoring)
    
    print("\nПроверка активных серверов:")
    for server in monitoring.get_active_servers():
        print(f"  - {server.name}: {server.status}")
    
    print("\nПроверка нагрузки (серверы с > 40 подключений):")
    high_load = monitoring.get_servers_with_connections(min_connections=40)
    for server in high_load:
        print(f"  - {server.name}: {server.connections} подключений")
    
    print("\nСигнал тревоги: высоконагруженные серверы требуют внимания!")

    # ========== 12. ДЕМОНСТРАЦИЯ РАБОТЫ С ПУСТОЙ КОЛЛЕКЦИЕЙ ==========
    print_separator("12. ДЕМОНСТРАЦИЯ РАБОТЫ С ПУСТОЙ КОЛЛЕКЦИЕЙ")
    
    empty_collection = ServerCollection()
    print(f"Пустая коллекция: {empty_collection}")
    print(f"Длина пустой коллекции: {len(empty_collection)}")
    print(f"Поиск в пустой коллекции: {empty_collection.find_by_name('anything')}")
    
    try:
        print("Попытка получить элемент по индексу 0:")
        empty_collection[0]
    except IndexError as e:
        print(f"Ошибка (корректно): {e}")

    # ========== ИТОГОВЫЙ ВЫВОД ==========
    print_separator("ИТОГОВЫЙ ВЫВОД")
    print("Лабораторная работа №2 выполнена на оценку 5")
    print("Реализованы все требования:")
    print("  - add(), remove(), remove_at()")
    print("  - find_by_name(), find_by_ip()")
    print("  - __len__(), __iter__(), __getitem__()")
    print("  - Сортировка (sort_by_name, sort_by_connections)")
    print("  - Фильтрация (get_active_servers, get_online_servers)")
    print("  - Проверка типа и дубликатов")
    print("\nРабота завершена успешно!")


if __name__ == "__main__":
    main()