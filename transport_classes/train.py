from transport_classes.vehicle import Vehicle

class Train(Vehicle):
    def __init__(self, brand: str, model: str, year: int, number_of_cars: int):
        super().__init__(brand, model, year)
        self.set_number_of_cars(number_of_cars)

    def get_number_of_cars(self) -> int:
        return self._number_of_cars

    def set_number_of_cars(self, number_of_cars: int) -> None:
        if number_of_cars <= 0:
            raise ValueError("Количество вагонов должно быть положительным.")
        self._number_of_cars = number_of_cars