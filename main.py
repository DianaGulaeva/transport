from exceptions import DataManagerError
from transport_classes.data_manager import DataManager
from transport_classes.car import Car
from transport_classes.bike import Bike
from transport_classes.truck import Truck
from transport_classes.bus import Bus

def main():
    vehicles = [
        Car("Toyota", "Camry", 2020, "Gasoline", 5),
        Bike("Yamaha", "YZF-R3", 2019, "Sport"),
        Truck("Volvo", "FH16", 2018, 40000),
        Bus("Mercedes-Benz", "Citaro", 2021, 50),
    ]

    # Сохраняем данные
    try:
        DataManager.save_to_json("vehicles.json", vehicles)
    except DataManagerError as e:
        print(f"Ошибка при сохранении: {e}")

    # Загружаем данные
    try:
        loaded_vehicles = DataManager.load_from_json("vehicles.json", Car)  # Передаем класс Car
        print("Загруженные транспортные средства:")
        for vehicle in loaded_vehicles:
            print(vehicle)
    except DataManagerError as e:
        print(f"Ошибка при загрузке: {e}")

if __name__ == "__main__":
    main()