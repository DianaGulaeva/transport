from transport_classes.vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, brand: str, model: str, year: int, max_load: float):
        super().__init__(brand, model, year)
        self._max_load = max_load

    def get_max_load(self) -> float:
        return self._max_load

    def set_max_load(self, max_load: float) -> None:
        if max_load <= 0:
            raise ValueError("Максимальная нагрузка должна быть положительной.")
        self._max_load = max_load