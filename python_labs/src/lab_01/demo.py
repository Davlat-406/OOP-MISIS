from model import Server
def main():
    print("=" * 60)
    print("ТЕСТ КЛАССА SERVER")
    print("=" * 60)
    
    #Создание серверов
    s1 = Server("MainServer", "192.168.1.1", "online", 0)
    s2 = Server("BackupServer", "192.168.1.2", "offline", 0)
    print("Созданы серверы:")
    print(f"  s1: {s1}")
    print(f"  s2: {s2}")
    
    #Маг методы
    print("\n__str__:", s1)
    print("__repr__:", repr(s1))
    
    #Срав
    s3 = Server("MainServer", "192.168.1.1", "maintenance", 5)
    print(f"\ns1 == s3: {s1 == s3}")
    
    #Атрибуты
    print(f"\nВсего серверов: {Server.total_servers}")
    
    #Подключения
    print("\nПодключаемся:")
    for i in range(3):
        print(f"  {s1.connect()}")
    
    print(f"\nОтключаемся:")
    for i in range(2):
        print(f"  {s1.disconnect()}")
    
    #Состояние
    print(f"\nАктивен: {s1.is_active()}")
    print(f"Пинг: {s1.ping()}")
    
    try:
        s1.deactivate()
    except Exception as e:
        print(f"Ошибка деактивации: {e}")
    
    while s1._connections > 0:
        s1.disconnect()
    print(f"Деактивирован: {s1.deactivate()}")
    print(f"После деактивации: {s1}")
    print(f"Активирован: {s1.activate()}")
    
    #Перезагрузка
    
    print(f"\nПерезагрузка: {s1.restart()}")
    print(f"После перезагрузки: {s1}")
    
    #Валидация
    print("\nПроверка ошибок:")
    try:
        s_bad = Server("", "ip")
    except Exception as e:
        print(f"  Пустое имя: {e}")
    
    try:
        s_bad = Server("Test", "300.500.1.1")
    except Exception as e:
        print(f"  Неверный IP: {e}")
    
    try:
        s_bad = Server("Test", "192.168.1.1", "unknown")
    except Exception as e:
        print(f"  Неверный статус: {e}")
    
    try:
        s_bad = Server("Test", "192.168.1.1", "online", -5)
    except Exception as e:
        print(f"  Отрицательные подключения: {e}")

if __name__ == "__main__":
    main()