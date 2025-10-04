from contextlib import contextmanager


@contextmanager
def managed_resource(name: str) -> None:
    print(f"Resource {name} acquired")
    yield f"resource-{name}"
    print(f"Resource {name} released")


with managed_resource("A") as resource:
    print(f"Using {resource}")
