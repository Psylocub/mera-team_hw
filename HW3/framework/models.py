import json
from abc import ABC


class Model(ABC):
    @classmethod
    def get_data(cls):
        file = open("database/" + cls.file, "r")
        data_in_json = file.read()
        data = json.loads(data_in_json)
        file.close()
        return data

    def generate_dict(self):
        return self.__dict__

    @classmethod
    def get_all(cls):
        data = cls.get_data()
        if len(data) > 0:
            keys = data[0].keys()
            for el in data:
                for key in keys:
                    if key == "id":
                        continue
                    print(el[key])

    @classmethod
    def print_object(cls, objects: list):
        if len(objects) > 0:
            keys = objects[0].keys()
            for object in objects:
                for key in keys:
                    if key == "id":
                        continue
                    print(object[key])

    @classmethod
    def get_by_id(cls, id):
        data = cls.get_data()
        counter = 0
        if len(data) > 0:
            for el in data:
                if id == el["id"]:
                    return el
                counter += 1
                if counter == len(data):
                    print("Not found element with this id")

    @staticmethod
    def save_to_file(path_to_file, data):
        file = open(path_to_file, "w")
        data_in_json = json.dumps(data)
        file.write(data_in_json)

    def save(self):
        data = self.get_data()
        new_el = self.generate_dict()
        if len(data) > 0:
            new_el["id"] = data[-1]["id"] + 1
        else:
            new_el["id"] = 1
        data.append(new_el)
        self.save_to_file("database/" + self.file, data)
