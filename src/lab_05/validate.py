

def validate_name(value):
    """Проверка имени сервера"""
    if not isinstance(value, str):
        return False
    if not value.strip():
        return False
    if len(value) < 3 or len(value) > 50:
        return False
    return True

def validate_ip(value):
    """Проверка IP-адреса"""
    if not isinstance(value, str):
        return False
    
    parts = value.split('.')
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit():
            return False
        if not (0 <= int(part) <= 255):
            return False
    return True

def validate_connections(value):
    """Проверка количества подключений"""
    if not isinstance(value, (int, float)):
        return False
    if value < 0:
        return False
    if value > 1000:  # максимальный лимит
        return False
    return True

def validate_status(value):
    """Проверка статуса сервера"""
    if not isinstance(value, str):
        return False
    
    allowed = ["Online", "Offline", "Maintenance"]
    if value not in allowed:
        return False
    return True

def validate_active(value):
    """Проверка активности"""
    return isinstance(value, bool)