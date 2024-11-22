from transport_classes.vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, brand: str, model: str, year: int, type_of_bike: str):
        super().__init__(brand, model, year)
        self._type_of_bike = type_of_bike

    def get_type_of_bike(self) -> str:
        return self._type_of_bike

    def set_type_of_bike(self, type_of_bike: str) -> None:
        self._type_of_bike = type_of_bike