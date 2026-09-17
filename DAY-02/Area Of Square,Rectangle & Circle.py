import math

while True:
    print("\n1. Square")
    print("2. Circle")
    print("3. Rectangle")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        side = float(input("Enter the side: "))
        area = side * side
        print("Area of square =", area)
        break

    elif choice == 2:
        radius = float(input("Enter the radius: "))
        area = math.pi * radius * radius
        print("Area of circle =", area)
        break

    elif choice == 3:
        length = float(input("Enter the length: "))
        breadth = float(input("Enter the breadth: "))
        area = length * breadth
        print("Area of rectangle =", area)
        break

    else:
        print("Invalid choice! Please choose 1, 2, or 3.")
