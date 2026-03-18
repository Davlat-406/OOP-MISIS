from model import Server

def validate_name(self, value):
    if not isinstance(value, str):
        raise TypeError("Имя должно быть строкой")
    if not value.strip():
        raise ValueError("Имя не может быть пустым")
    return True
    
def validate_ip(self, value):
    if not isinstance(value, str):
        raise TypeError("IP должен быть строкой")
    parts = value.split('.')
    if len(parts) != 4:
        raise ValueError("Неверный формат IP")
    for part in parts:
        if not part.isdigit() or not (0 <= int(part) <= 255):
            raise ValueError("IP должен быть в формате xxx.xxx.xxx.xxx")
    return True
    
def validate_status(self, value):
    if not isinstance(value, str):
        raise TypeError("Статус должен быть строкой")
    allowed = ["online", "offline", "maintenance"]
    if value not in allowed:
        raise ValueError(f"Статус должен быть одним из: {allowed}")
    return True
    
def validate_connections(self, value):
    if not isinstance(value, (int, float)):
        raise TypeError("Количество подключений должно быть числом")
    if value < 0:
        raise ValueError("Количество подключений не может быть отрицательным")
    if value > Server.max_connections:
        raise ValueError(f"Превышен лимит подключений ({Server.max_connections})")
    return True