def calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose operation: ")

    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice == "4":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")


def length_converter():
    meter = float(input("Enter meters: "))
    print("Kilometers:", meter / 1000)
    print("Centimeters:", meter * 100)


def weight_converter():
    kg = float(input("Enter kilograms: "))
    print("Grams:", kg * 1000)
    print("Pounds:", kg * 2.20462)


def temperature_converter():
    c = float(input("Enter Celsius: "))
    print("Fahrenheit:", (c * 9/5) + 32)
    print("Kelvin:", c + 273.15)


while True:
    print("\nINTERACTIVE CALCULATOR")
    print("1. Calculator")
    print("2. Length Converter")
    print("3. Weight Converter")
    print("4. Temperature Converter")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        calculator()
    elif choice == "2":
        length_converter()
    elif choice == "3":
        weight_converter()
    elif choice == "4":
        temperature_converter()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice")