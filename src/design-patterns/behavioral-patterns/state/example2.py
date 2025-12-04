from abc import ABC, abstractmethod


class TripState(ABC):
    @abstractmethod
    def assign_driver(self, trip):
        pass

    @abstractmethod
    def start_trip(self, trip):
        pass

    @abstractmethod
    def complete_trip(self, trip):
        pass

    @abstractmethod
    def cancel_trip(self, trip):
        pass


class RequestedState(TripState):
    def complete_trip(self, trip):
        raise Exception("Trip not started yet")

    def cancel_trip(self, trip):
        trip.state = CancelledState()
        print("Trip cancelled")

    def start_trip(self, trip):
        raise Exception("Driver not assigned")

    def assign_driver(self, trip):
        trip.state = DriverAssignedState()
        print("Driver Assigned")


class DriverAssignedState(TripState):
    def complete_trip(self, trip):
        raise Exception("Trip not started yet")

    def cancel_trip(self, trip):
        trip.state = CancelledState()
        print("Trip cancelled after driver assignment")

    def start_trip(self, trip):
        trip.state = OngoingState()
        print("Trip started")

    def assign_driver(self, trip):
        raise Exception("Driver already assigned")


class OngoingState(TripState):
    def complete_trip(self, trip):
        trip.state = CompletedState()
        print("Trip started")

    def cancel_trip(self, trip):
        raise Exception("Trip already started")

    def start_trip(self, trip):
        raise Exception("Trip cannot be cancelled after starting assignment")

    def assign_driver(self, trip):
        raise Exception("Driver already assigned")


class CompletedState(TripState):
    def assign_driver(self, trip):
        raise Exception("Trip already completed.")

    def start_trip(self, trip):
        raise Exception("Trip already completed.")

    def complete_trip(self, trip):
        raise Exception("Trip already completed.")

    def cancel_trip(self, trip):
        raise Exception("Completed trip cannot be cancelled.")


class CancelledState(TripState):
    def assign_driver(self, trip):
        raise Exception("Trip is cancelled.")

    def start_trip(self, trip):
        raise Exception("Trip is cancelled.")

    def complete_trip(self, trip):
        raise Exception("Trip is cancelled.")

    def cancel_trip(self, trip):
        raise Exception("Trip already cancelled.")


class Trip:
    def __init__(self):
        self.state = RequestedState()

    def assign_driver(self):
        self.state.assign_driver(self)

    def start_trip(self):
        self.state.start_trip(self)

    def complete_trip(self):
        self.state.complete_trip(self)

    def cancel_trip(self):
        self.state.cancel_trip(self)


if __name__ == "__main__":
    trip = Trip()

    trip.assign_driver()  # REQUESTED → DRIVER_ASSIGNED
    trip.start_trip()  # DRIVER_ASSIGNED → ONGOING
    trip.complete_trip()  # ONGOING → COMPLETED

    # trip.cancel_trip()   # Will raise: cannot cancel after starting
