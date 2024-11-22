class DataManagerError(Exception):
    """Исключение, связанное с ошибками в DataManager."""
    pass


class VehicleNotFoundError(Exception):
    """Исключение, возникающее при отсутствии транспортного средства в базе."""
    pass