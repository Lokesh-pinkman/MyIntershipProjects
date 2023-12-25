def temperature_converter():
    print("Temperature Converter")
    choice = input("Choose conversion direction (C to F or F to C): ").upper()

    if choice == 'C TO F':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.")
    elif choice == 'F TO C':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius.")
    else:
        print("Invalid choice. Please enter either 'C to F' or 'F to C'.")

def length_converter():
    print("Length Converter")
    choice = input("Choose conversion direction (M to FT or FT to M): ").upper()

    if choice == 'M TO FT':
        meters = float(input("Enter length in meters: "))
        feet = meters * 3.28084
        print(f"{meters} meters is equal to {feet} feet.")
    elif choice == 'FT TO M':
        feet = float(input("Enter length in feet: "))
        meters = feet / 3.28084
        print(f"{feet} feet is equal to {meters} meters.")
    else:
        print("Invalid choice. Please enter either 'M to FT' or 'FT to M'.")

def weight_converter():
    print("Weight Converter")
    choice = input("Choose conversion direction (KG to LB or LB to KG): ").upper()

    if choice == 'KG TO LB':
        kilograms = float(input("Enter weight in kilograms: "))
        pounds = kilograms * 2.20462
        print(f"{kilograms} kilograms is equal to {pounds} pounds.")
    elif choice == 'LB TO KG':
        pounds = float(input("Enter weight in pounds: "))
        kilograms = pounds / 2.20462
        print(f"{pounds} pounds is equal to {kilograms} kilograms.")
    else:
        print("Invalid choice. Please enter either 'KG to LB' or 'LB to KG'.")

def main():
    print("Unit Converter")
    print("1. Temperature Converter")
    print("2. Length Converter")
    print("3. Weight Converter")

    choice = int(input("Enter your choice (1, 2, or 3): "))

    if choice == 1:
        temperature_converter()
    elif choice == 2:
        length_converter()
    elif choice == 3:
        weight_converter()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
