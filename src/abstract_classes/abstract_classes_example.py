# Abstract Base Classes — define a contract that subclasses must implement

from abc import ABC, abstractmethod


# 1. Basic ABC
class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        ...

    @abstractmethod
    def perimeter(self) -> float:
        ...

    def describe(self) -> str:
        return f"area={self.area()}, perimeter={self.perimeter()}"


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


c = Circle(5)
r = Rectangle(4, 6)

print(c.describe())  # area=78.53975, perimeter=31.4159
print(r.describe())  # area=24, perimeter=20

# Shape()  # TypeError: Can't instantiate abstract class


# 2. Abstract property
class Animal(ABC):

    @property
    @abstractmethod
    def sound(self) -> str:
        ...

    def speak(self):
        print(self.sound)


class Dog(Animal):
    @property
    def sound(self) -> str:
        return "woof"


class Cat(Animal):
    @property
    def sound(self) -> str:
        return "meow"


Dog().speak()  # woof
Cat().speak()  # meow


# 3. Concrete methods in ABC — shared logic subclasses inherit
class Logger(ABC):

    @abstractmethod
    def log(self, message: str) -> None:
        ...

    def info(self, message: str) -> None:
        self.log(f"[INFO] {message}")

    def error(self, message: str) -> None:
        self.log(f"[ERROR] {message}")


class ConsoleLogger(Logger):
    def log(self, message: str) -> None:
        print(message)


logger = ConsoleLogger()
logger.info("server started")   # [INFO] server started
logger.error("connection lost") # [ERROR] connection lost
