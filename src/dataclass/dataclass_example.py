from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    id: int
    name: str
    email: Optional[str] = None
    is_active: bool = True

    def activate(self) -> None:
        self.is_active = True
    
    def deactivate(self) -> None:
        self.is_active = False


def main():
    user1 = User(1, "Alice", "alice@example.com")
    user2 = User(2, "Bob")  
    user3 = User(3, "Charlie", is_active=False)

    print("User 1:", user1)
    print("User 2:", user2)
    print("User 3:", user3)

    print("\nComparison:")
    print(f"user1 == user2: {user1 == user2}")
    print(f"user1 != user3: {user1 != user3}")

    print("\nActivating/Deactivating users:")
    print(f"Before - User 1 active: {user1.is_active}")
    user1.deactivate()
    print(f"After deactivate - User 1 active: {user1.is_active}")
    user1.activate()
    print(f"After activate - User 1 active: {user1.is_active}")


if __name__ == "__main__":
    main()
