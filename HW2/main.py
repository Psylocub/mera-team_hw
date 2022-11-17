from models.models import Toyota

while True:
    print("1. Add new car\n" +
          "2. Get all cars\n" +
          "3. Exit\n")

    flag = int(input("Choose menu item: "))
    if flag == 1:
        engine = input("Car engine: ")
        color = input("Car color: ")
        car = Toyota(engine, color)
        car.save()
    elif flag == 2:
        Toyota.get_all_cars()
    elif flag == 3:
        break
    print()
