from transport_classes.vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, brand: str, model: str, year: int, capacity: int):
        super().__init__(brand, model, year)
        self._capacity = capacity

    def get_capacity(self) -> int:
        return self._capacity

    def set_capacity(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Вместимость автобуса должна быть положительной.")
        self._capacity = capacity