from models.models import Plant, Employee, Salon

while True:
    print("1. Add new plant\n" +
          "2. Get all plants\n" +
          "3. Get plant by id\n" +
          "4. Add new employee\n" +
          "5. Get all employees\n" +
          "6. Get employee bu plant id\n" +
          "7. Add new salon\n" +
          "8. Get all salons\n" +
          "9. Get salon by id\n" +
          "10. Get all emoloyees by place of work\n"
          )
    flag = int(input("Choose menu item: "))
    if flag == 1:
        name = input("Plant name: ")
        location = input("Plant location: ")
        plant = Plant(name, location)
        plant.save()
    elif flag == 2:
        Plant.get_all()
    elif flag == 3:
        id = int(input("Type id to search: "))
        plant = Plant.get_by_id(id)
        Plant.print_object(plant)
    elif flag == 4:
        name = input("Employee name: ")
        object_id = input("Employee work id: ")
        type_of_work = input("Where work employee: ")
        employee = Employee(name, object_id, type_of_work)
        employee.save()
    elif flag == 5:
        Employee.get_all()
    elif flag == 6:
        id = int(input("Type id to search: "))
        Employee.get_by_id(id)
    elif flag == 7:
        name = input("Salon name: ")
        address = input("Address: ")
        size = input("Size: ")
        employee = Salon(name, address, size)
        employee.save()
    elif flag == 8:
        Salon.get_all()
    elif flag == 9:
        id = int(input("Type id to search: "))
        salon = Salon.get_by_id(id)
        Salon.print_object(salon)
    elif flag == 10:
        place_of_work = input("Place of work: ")
        print(f"The follow employees work in {place_of_work}:")
        list_of_employees = Employee.get_employees_by_work_type(place_of_work)
        print(*list_of_employees, sep="\n")
    print()
