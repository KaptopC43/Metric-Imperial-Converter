def length():
    while True:
        print("\nLength Converter")
        print("1. m -> ft")
        print("2. ft -> m")
        print("3. Back to main menu")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "3":
            break

        if choice not in ["1", "2"]:
            print("Invalid input")
            continue

        while True:
            val_input = input("Enter value to convert: ").strip()
            try:
                val = float(val_input)
                if val <= 0:
                    print("Invalid input: Value must be greater than 0")
                    continue
                break
            except ValueError:
                print("Invalid input")

        if choice == "1":
            res = val * 3.28084
            print(f"{res:.2f} ft")
        elif choice == "2":
            res = val / 3.28084
            print(f"{res:.2f} m")


def mass():
    while True:
        print("\nMass Converter")
        print("1. kg -> lbs")
        print("2. lbs -> kg")
        print("3. Back to main menu")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "3":
            break

        if choice not in ["1", "2"]:
            print("Invalid input")
            continue

        while True:
            val_input = input("Enter value to convert: ").strip()
            try:
                val = float(val_input)
                if val <= 0:
                    print("Invalid input: Value must be greater than 0")
                    continue
                break
            except ValueError:
                print("Invalid input")

        if choice == "1":
            res = val * 2.20462
            print(f"{res:.2f} lbs")
        elif choice == "2":
            res = val / 2.20462
            print(f"{res:.2f} kg")


def temperature():
    while True:
        print("\nTemperature Converter")
        val_input = input("Enter temperature (or 'B' to go back): ").strip().upper()

        if val_input == "B":
            break

        try:
            temp = float(val_input)
        except ValueError:
            print("Invalid input")
            continue

        while True:
            unit = str(input("Enter unit (C or F, or 'B' to go back): ")).strip().upper()

            if unit == "B":
                break
            elif unit == "C":
                res = (temp * 9 / 5) + 32
                output_unit = "F"
                print(f"{res:.1f}°{output_unit}")
                break
            elif unit == "F":
                res = (temp - 32) * 5 / 9
                output_unit = "C"
                print(f"{res:.1f}°{output_unit}")
                break
            else:
                print("Invalid unit")


def liquid_volume():
    while True:
        print("\nLiquid Volume Converter")
        print("1. L -> gal")
        print("2. gal -> L")
        print("3. Back to main menu")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "3":
            break

        if choice not in ["1", "2"]:
            print("Invalid input")
            continue

        while True:
            val_input = input("Enter value to convert: ").strip()
            try:
                val = float(val_input)
                if val <= 0:
                    print("Invalid input: Value must be greater than 0")
                    continue
                break
            except ValueError:
                print("Invalid input")

        if choice == "1":
            res = val * 0.264172
            print(f"{res:.2f} gal")
        elif choice == "2":
            res = val / 0.264172
            print(f"{res:.2f} L")


while True:
    print("\nMetric <-> Imperial Converter")
    print("1. Length")
    print("2. Mass")
    print("3. Temperature")
    print("4. Liquid Volume")

    choice = input("Enter your choice (1-4 or Q to quit): ").strip().upper()

    if choice == "Q":
        print("Closing program")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid input")
        continue

    if choice == "1":
        length()
    elif choice == "2":
        mass()
    elif choice == "3":
        temperature()
    elif choice == "4":
        liquid_volume()