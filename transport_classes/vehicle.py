from typing import List

class Vehicle:
    vehicles_db: List['Vehicle'] = []

    def __init__(self, brand: str, model: str, year: int):
        self.set_brand(brand)
        self.set_model(model)
        self.set_year(year)
        Vehicle.vehicles_db.append(self)

    def get_brand(self) -> str:
        return self._brand

    def set_brand(self, brand: str) -> None:
        self._brand = brand

    def get_model(self) -> str:
        return self._model

    def set_model(self, model: str) -> None:
        self._model = model

    def get_year(self) -> int:
        return self._year

    def set_year(self, year: int) -> None:
        if year < 1886:
            raise ValueError("Год должен быть не ранее 1886.")
        self._year = year

    @staticmethod
    def delete_vehicle(vehicle: 'Vehicle') -> None:
        if vehicle in Vehicle.vehicles_db:
            Vehicle.vehicles_db.remove(vehicle)
        else:
            raise ValueError("Транспортное средство не найдено.")