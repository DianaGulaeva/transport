import json
import os
import xml.etree.ElementTree as ET
from transport_classes.car import Car
from transport_classes.bike import Bike
from transport_classes.truck import Truck
from transport_classes.bus import Bus
from exceptions import DataManagerError, VehicleNotFoundError


class DataManager:

    @staticmethod
    def save_to_json(filename: str, data: list):
        """Сохранение данных в файл в формате JSON."""
        try:
            with open(filename, 'w') as file:
                json.dump([{
                               key.lstrip('_'): value for key, value in obj.__dict__.items()
                           } | {'type': obj.__class__.__name__} for obj in data], file, indent=4)
            print(f"Данные успешно сохранены в {filename}")
        except Exception as e:
            raise DataManagerError(f"Ошибка при сохранении в JSON: {e}")

    @staticmethod
    def save_to_xml(filename: str, data: list) -> None:
        try:
            root = ET.Element("items")
            for obj in data:
                obj_elem = ET.SubElement(root, "item")
                for key, value in obj.__dict__.items():
                    child = ET.SubElement(obj_elem, key)
                    child.text = str(value)
            tree = ET.ElementTree(root)
            tree.write(filename)
            print(f"Данные успешно сохранены в {filename}")
        except Exception as e:
            raise DataManagerError(f"Ошибка при сохранении в XML: {e}")

    @staticmethod
    def load_from_xml(filename: str, class_type) -> list:
        if not os.path.exists(filename):
            raise DataManagerError(f"Файл '{filename}' не найден.")
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            return [class_type(**{child.tag: child.text for child in item}) for item in root.findall("item")]
        except Exception as e:
            raise DataManagerError(f"Ошибка при загрузке из XML: {e}")

    @staticmethod
    def load_from_json(filename: str, class_type: object) -> object:
        """Загрузка данных из файла JSON."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                print("----------------------")
                print("Загруженные данные:\n" + "\n".join(str(item) for item in data))
                print("----------------------")

                # Убираем подчеркивания из имен ключей
                processed_data = [
                    {key.lstrip('_'): value for key, value in item.items() if key != 'type'}
                    for item in data
                ]

                # Определяем класс для каждого объекта на основе его типа
                loaded_objects = []
                for item in processed_data:
                    vehicle_type = item.get('type')
                    if not vehicle_type:
                        raise ValueError(f"Отсутствует или неверное значение для типа транспорта в: {item}")

                    if not vehicle_type:
                        raise VehicleNotFoundError(f"Отсутствует или неверное значение для типа транспорта в: {item}")

                    if vehicle_type == 'Car':
                        loaded_objects.append(Car(**item))
                    elif vehicle_type == 'Truck':
                        loaded_objects.append(Truck(**item))
                    elif vehicle_type == 'Bike':
                        loaded_objects.append(Bike(**item))
                    elif vehicle_type == 'Bus':
                        loaded_objects.append(Bus(**item))
                    else:
                        raise VehicleNotFoundError(f"Неизвестный тип транспорта: {vehicle_type}")

                return loaded_objects
        except Exception as e:
            raise DataManagerError(f"Ошибка при загрузке из JSON: {e}")