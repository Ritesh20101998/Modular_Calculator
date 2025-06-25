from calculator.basic import add, subtract, multiply, divide
from calculator.scientific import power, sqrt, sine, cosine, tangent
from calculator.new_finance import simple_interest, compound_interest
from calculator.graphical import plot_y_equals_x_squared

def scientific_calculator():
    print("\nScientific Calculator")
    print("Select operation:")
    print("1. Power (x^y)")
    print("2. Square Root (√x)")
    print("3. Sine (sin x)")
    print("4. Cosine (cos x)")
    print("5. Tangent (tan x)")
    print("6. Go Back")
    while True:
        choice = input("Enter choice (1/2/3/4/5/6): ")
        if choice == '6':
            break
        try:
            if choice == '1':
                x = float(input("Enter base: "))
                y = float(input("Enter exponent: "))
                result = power(x, y)
            elif choice == '2':
                x = float(input("Enter number: "))
                result = sqrt(x)
            elif choice == '3':
                x = float(input("Enter angle in degrees: "))
                result = sine(x)
            elif choice == '4':
                x = float(input("Enter angle in degrees: "))
                result = cosine(x)
            elif choice == '5':
                x = float(input("Enter angle in degrees: "))
                result = tangent(x)
            else:
                print("Invalid choice.")
                continue
            formatted = f"{result:.3f}".rstrip('0').rstrip('.')
            print(f"Result: {formatted}")
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue
        next_calc = input("Do you want to perform another scientific calculation? (yes/no): ")
        if next_calc.lower() != 'yes':
            break

def financial_calculator():
    print("\nFinancial Calculator")
    print("Select operation:")
    print("1. Simple Interest")
    print("2. Compound Interest")
    print("3. Go Back")
    while True:
        choice = input("Enter choice (1/2/3): ")
        if choice == '3':
            break
        try:
            if choice == '1':
                p = float(input("Enter principal: "))
                r = float(input("Enter rate (%): "))
                t = float(input("Enter time (years): "))
                result = simple_interest(p, r, t)
            elif choice == '2':
                p = float(input("Enter principal: "))
                r = float(input("Enter rate (%): "))
                t = float(input("Enter time (years): "))
                n = float(input("Enter compounding frequency per year: "))
                result = compound_interest(p, r, t, n)
            else:
                print("Invalid choice.")
                continue
            formatted = f"{result:.3f}".rstrip('0').rstrip('.')
            print(f"Result: {formatted}")
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue
        next_calc = input("Do you want to perform another financial calculation? (yes/no): ")
        if next_calc.lower() != 'yes':
            break

def graphical_calculator():
    print("\nGraphical Calculator")
    print("1. Plot y = x^2")
    print("2. Go Back")
    while True:
        choice = input("Enter choice (1/2): ")
        if choice == '2':
            break
        if choice == '1':
            plot_y_equals_x_squared()
        else:
            print("Invalid choice.")

def main():
    while True:
        print("\nSelect Calculator Type:")
        print("1. Basic Calculator")
        print("2. Scientific Calculator")
        print("3. Financial Calculator")
        print("4. Graphical Calculator")
        print("5. Exit")
        calc_type = input("Enter choice (1/2/3/4/5): ")
        if calc_type == '1':
            basic_calculator()
        elif calc_type == '2':
            scientific_calculator()
        elif calc_type == '3':
            financial_calculator()
        elif calc_type == '4':
            graphical_calculator()
        elif calc_type == '5':
            print("Thank you for using it!! Goodbye! 😊")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")

def basic_calculator():
    print("\nBasic Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Go Back")
    while True:
        choice = input("Enter choice (1/2/3/4/5): ")
        if choice == '5':
            break
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue
            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            if isinstance(result, float):
                formatted = f"{result:.3f}".rstrip('0').rstrip('.')
                print(f"Result: {formatted}")
            else:
                print(f"Result: {result}")
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
            continue
        next_calc = input("Do you want to perform another calculation? (yes/no): ")
        if next_calc.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
