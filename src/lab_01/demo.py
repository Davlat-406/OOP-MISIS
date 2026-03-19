from model import Server
import time

def print_separator(title):
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)

def main():
    print("Демонстрация класса Server (оценка 5)")
    print_separator("1. Создание серверов")

    try:
        # Создаём серверы с корректными данными
        server1 = Server(
            name="WebServer",
            ip="192.168.1.10",
            active=True,
            connections=0,
            status="Online",
            max_connections=100
        )
        server2 = Server(
            name="DbServer",
            ip="192.168.1.20",
            active=True,
            connections=5,
            status="Online",
            max_connections=50
        )
        server3 = Server(
            name="TestServer",
            ip="10.0.0.1",
            active=False,
            status="Offline"
        )
        print("Серверы успешно созданы")
    except Exception as e:
        print(f"Ошибка создания: {e}")
        return

    print_separator("2. Вывод информации (__str__ и __repr__)")
    print("__str__:")
    print(server1)
    print(server2)
    print(server3)
    print("\n__repr__:")
    print(repr(server1))
    print(repr(server2))

    print_separator("3. Атрибуты класса и экземпляра")
    print(f"server1.max_connections = {server1._max_connections}")
    print(f"server2.max_connections = {server2._max_connections}")

    print_separator("4. Изменение свойств через setter (с валидацией)")
    try:
        print(f"Текущее имя server1: {server1.name}")
        server1.name = "WebServerUpdated"
        print(f"Новое имя: {server1.name}")
    except ValueError:
        print("Ошибка: недопустимое имя")

    try:
        print(f"Текущий статус server2: {server2.status}")
        server2.status = "Maintenance"
        print(f"Новый статус: {server2.status}")
    except ValueError:
        print("Ошибка: недопустимый статус")

    try:
        print("Пытаемся установить неверный IP...")
        server1.ip = "999.999.999.999"  # должно вызвать исключение
    except ValueError:
        print("Ожидаемая ошибка валидации IP")

    print_separator("5. Бизнес-методы: ping, connect, disconnect")

    print("Ping сервера:")
    print(server1.ping())
    print(server3.ping())  # неактивный

    print("\nПодключения к server1:")
    try:
        print(server1.connect())
        print(server1.connect())
        print(f"Текущие подключения: {server1.connections}")
    except Exception as e:
        print(f"Ошибка: {e}")

    print("\nПопытка подключиться к server3 (неактивен):")
    try:
        print(server3.connect())
    except Exception as e:
        print(f"Ожидаемая ошибка: {e}")

    print("\nОтключение от server1:")
    try:
        print(server1.disconnect())
        print(f"Осталось подключений: {server1.connections}")
    except Exception as e:
        print(f"Ошибка: {e}")

    print_separator("6. Перезагрузка сервера")
    try:
        print("Перезагружаем server2...")
        print(server2.restart())
        print("Сервер перезагружен")
    except Exception as e:
        print(f"Ошибка: {e}")

    print_separator("7. Сравнение объектов (__eq__)")
    server1_copy = Server(
        name="WebServer",
        ip="192.168.1.10",
        active=True,
        connections=0,
        status="Online",
        max_connections=100
    )
    print(f"server1 == server1_copy? {server1 == server1_copy}")
    print(f"server1 == server2? {server1 == server2}")

    print_separator("8. Демонстрация логических состояний")
    print("Переводим server1 в неактивное состояние (прямое изменение _active для демо)")
    server1._active = False
    print(server1.ping())
    try:
        server1.connect()
    except Exception as e:
        print(f"Ожидаемая ошибка подключения: {e}")

    print_separator("9. Обработка некорректного создания (try/except)")
    print("Пытаемся создать сервер с пустым именем:")
    try:
        bad_server = Server(name="", ip="1.1.1.1", active=True)
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("Пытаемся создать сервер с отрицательным числом подключений:")
    try:
        bad_server = Server(name="Bad", ip="1.1.1.1", active=True, connections=-5)
    except ValueError as e:
        print(f"Ошибка: {e}")

    print_separator("10. Полный жизненный цикл сервера")
    new_server = Server(
        name="NewServer",
        ip="10.10.10.10",
        active=True,
        status="Online",
        max_connections=10
    )
    print(new_server)
    print(new_server.ping())
    print(new_server.connect())
    print(new_server.connect())
    print(new_server.disconnect())
    print(new_server.restart())
    new_server._active = False
    print(new_server.ping())
    print("Демонстрация завершена")

if __name__ == "__main__":
    main()
