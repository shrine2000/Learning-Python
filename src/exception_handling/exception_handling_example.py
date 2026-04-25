# Exception Handling


# 1. Basic try / except / finally
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"error: {e}")
finally:
    print("always runs")


# 2. Multiple except blocks — catch specific exceptions
def parse_number(value):
    try:
        return int(value)
    except ValueError:
        print(f"cannot convert '{value}' to int")
    except TypeError:
        print("value must be a string or number")


parse_number("abc")   # ValueError
parse_number(None)    # TypeError


# 3. else — runs only when no exception was raised
try:
    x = int("42")
except ValueError:
    print("bad input")
else:
    print(f"parsed: {x}")  # runs because no exception


# 4. Custom exceptions
class AppError(Exception):
    pass

class ValidationError(AppError):
    def __init__(self, field, message):
        self.field = field
        super().__init__(f"{field}: {message}")


try:
    raise ValidationError("age", "must be positive")
except ValidationError as e:
    print(e)         # age: must be positive
    print(e.field)   # age


# 5. re-raise — catch, log, then let it propagate
def process(data):
    try:
        return int(data)
    except ValueError as e:
        print(f"logging: {e}")
        raise  # re-raises the same exception


# 6. raise from — chain exceptions
def fetch(user_id):
    try:
        raise KeyError("not found in DB")
    except KeyError as e:
        raise ValidationError("user_id", "does not exist") from e
        # traceback shows: "The above exception was the direct cause of..."


# 7. Never catch bare Exception silently
def bad():
    try:
        return int("abc")
    except Exception:
        pass  # hides the bug — never do this


def good(data):
    try:
        return int(data)
    except (ValueError, TypeError) as e:
        raise ValidationError("data", str(e)) from e
