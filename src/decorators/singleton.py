import threading
from functools import wraps


def Singleton(cls):
    _instance = None
    _lock = threading.Lock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        nonlocal _instance
        if _instance is None:
            with _lock:
                if _instance is None:
                    _instance = cls(*args, **kwargs)
        return _instance

    return wrapper


@Singleton
class DBClient:
    def __init__(self):
        print("Initializing DBClient")
        
        
if __name__ == "__main__":
    a = DBClient()
    b = DBClient()
    print(a is b) 