class InstantiateCSVError(Exception):
    def print_error(self):
        return "InstantiateCSVError: Файл item.csv поврежден"
