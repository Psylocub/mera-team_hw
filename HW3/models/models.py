from framework.models import Model


class Plant(Model):
    file = "plants.json"

    def __init__(self, name, location):
        self.name = name
        self.location = location


class Salon(Model):
    file = "salons.json"

    def __init__(self, name, address, size):
        self.name = name
        self.address = address
        self.size = size


class Employee(Model):
    file = "employees.json"

    def __init__(self, name, object_id, type_of_work):
        self.name = name
        self.object_id = object_id
        self.type_of_work = type_of_work

    @classmethod
    def get_employees_by_work_type(cls, place_of_work):
        list_of_employees = []
        data = cls.get_data()
        if len(data) > 0:
            keys = data[0].keys()
            for el in data:
                for key in keys:
                    if key == "type_of_work":
                        if el[key] == place_of_work:
                            list_of_employees.append(el["name"])
        return list_of_employees

    def get_work(self):
        if self.type_of_work == "plant":
            return Plant.get_by_id(self.object_id)
        elif self.type_of_work == "salon":
            return Salon.get_by_id(self.object_id)
        else:
            return {}

    @classmethod
    def get_by_id(cls, id):
        employee_dict = super().get_by_id(id)
        employee = Employee(
            employee_dict["name"],
            int(employee_dict["object_id"]),
            employee_dict["type_of_work"])
        work_of_employee = employee.get_work()
        cls.print_object([employee_dict])
        print("Employee work: ")
        cls.print_object([work_of_employee])
