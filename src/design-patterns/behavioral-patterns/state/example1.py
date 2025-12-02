from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass


class StateA(State):
    def handle(self, context):
        print("switching from A to B")
        context.state = StateB()


class StateB(State):
    def handle(self, context):
        print("switching from B to A")
        context.state = StateA()


class Context:
    def __init__(self):
        self.state = StateA()

    def request(self):
        self.state.handle(self)


if __name__ == "__main__":
    ctx = Context()
    ctx.request()
    ctx.request()
    ctx.request()
