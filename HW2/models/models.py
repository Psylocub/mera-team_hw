import json


class Toyota:
    file = "cars.json"

    def __init__(self, engine, color):
        self.engine = engine
        self.color = color
        self.gear = 0

    def drive(self):
        print("drive")

    def change_gear(self, gear):
        self.gear = gear

    def change_color(self, color):
        self.color = color

    @classmethod
    def get_data(cls):
        with open("database/" + cls.file, "r") as file:
            data_in_json = file.read()
            data = json.loads(data_in_json)
        return data

    @classmethod
    def get_all_cars(cls):
        cars = cls.get_data()
        for car in cars:
            print(car["engine"], car["color"])

    def save(self):
        cars = self.get_data()
        new_car = {"engine": self.engine, "color": self.color}
        cars.append(new_car)
        with open("database/" + self.file, "w") as file:
            data_in_json = json.dumps(cars)
            file.write(data_in_json)