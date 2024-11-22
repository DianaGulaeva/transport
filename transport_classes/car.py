from transport_classes.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int, fuel_type: str, doors: int):
        super().__init__(brand, model, year)
        self._fuel_type = fuel_type
        self.set_doors(doors)

    def get_fuel_type(self) -> str:
        return self._fuel_type

    def set_fuel_type(self, fuel_type: str) -> None:
        self._fuel_type = fuel_type

    def get_doors(self) -> int:
        return self._doors

    def set_doors(self, doors: int) -> None:
        if doors <= 0:
            raise ValueError("Количество дверей должно быть положительным.")
        self._doors = doors