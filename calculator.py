# Modular Calculator CLI Entry Point

# --- Imports ---
from calculator.basic import add, subtract, multiply, divide
from calculator.scientific import power, sqrt, sine, cosine, tangent
from calculator.finance import simple_interest, compound_interest, emi_calculator, emi_amortization_schedule
from calculator.planning import sip_calculator, lumpsum_calculator, fv, pv, pmt, nper, rate
from calculator.graphical import plot_y_equals_x_squared, plot_multiple_functions
import numpy as np

# --- Main Menu ---
def main():
    while True:
        print("\nSelect Calculator Type:")
        print("1. Basic Calculator")
        print("2. Scientific Calculator")
        print("3. Financial Calculator")
        print("4. Graphical Calculator")
        print("5. Planning Calculator")
        print("6. Exit")
        calc_type = input("Enter choice (1/2/3/4/5/6): ")
        if calc_type == '1':
            basic_calculator()
        elif calc_type == '2':
            scientific_calculator()
        elif calc_type == '3':
            financial_calculator()
        elif calc_type == '4':
            graphical_calculator()
        elif calc_type == '5':
            planning_calculator()
        elif calc_type == '6':
            print("Thank you for using it!! Goodbye! 😊")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, 5, or 6.")

# --- Calculator Menus ---
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
    print("3. EMI Calculator")
    print("4. EMI Amortization Schedule")
    print("5. Go Back")
    while True:
        choice = input("Enter choice (1/2/3/4/5): ")
        if choice == '5':
            break
        try:
            if choice == '1':
                p = float(input("Enter principal: "))
                r = float(input("Enter rate (%): "))
                t = float(input("Enter time (years): "))
                result = simple_interest(p, r, t)
                formatted = f"{result:.3f}".rstrip('0').rstrip('.')
                print(f"Result: {formatted}")
            elif choice == '2':
                p = float(input("Enter principal: "))
                r = float(input("Enter rate (%): "))
                t = float(input("Enter time (years): "))
                n = float(input("Enter compounding frequency per year: "))
                result = compound_interest(p, r, t, n)
                formatted = f"{result:.3f}".rstrip('0').rstrip('.')
                print(f"Result: {formatted}")
            elif choice == '3':
                principal = float(input("Enter loan amount: "))
                rate = float(input("Enter annual interest rate (%): "))
                tenure = int(input("Enter tenure (months): "))
                result = emi_calculator(principal, rate, tenure)
                print(f"EMI: {result['EMI']}")
                print(f"Total Payment: {result['Total Payment']}")
                print(f"Total Interest: {result['Total Interest']}")
            elif choice == '4':
                principal = float(input("Enter loan amount: "))
                rate = float(input("Enter annual interest rate (%): "))
                tenure = int(input("Enter tenure (months): "))
                schedule = emi_amortization_schedule(principal, rate, tenure)
                print("\nMonth | EMI | Principal Paid | Interest Paid | Remaining Principal")
                for row in schedule:
                    print(f"{row['Month']:>5} | {row['EMI']:>10.2f} | {row['Principal Paid']:>14.2f} | {row['Interest Paid']:>13.2f} | {row['Remaining Principal']:>19.2f}")
                save_excel = input("\nDo you want to save this schedule as an Excel file? (yes/no): ")
                if save_excel.lower() == 'yes':
                    filepath = input("Enter filename (e.g., emi_schedule.xlsx): ")
                    from calculator.finance import emi_amortization_to_excel
                    emi_amortization_to_excel(principal, rate, tenure, filepath)
                    print(f"Schedule saved to {filepath}")
            else:
                print("Invalid choice.")
                continue
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue
        except Exception as e:
            print(f"Error: {e}")
        next_calc = input("Do you want to perform another financial calculation? (yes/no): ")
        if next_calc.lower() != 'yes':
            break

def graphical_calculator():
    print("\nGraphical Calculator")
    print("1. Plot y = x^2")
    print("2. Plot Multiple Functions")
    print("3. Go Back")
    while True:
        choice = input("Enter choice (1/2/3): ")
        if choice == '3':
            break
        elif choice == '1':
            plot_y_equals_x_squared()
        elif choice == '2':
            try:
                num_funcs = int(input("Enter number of functions to plot: "))
                functions = []
                labels = []
                for i in range(num_funcs):
                    func_str = input(f"Enter function {i+1} (e.g., 'lambda x: x**2'): ")
                    func = eval(func_str)
                    functions.append(func)
                    label = input(f"Enter label for function {i+1}: ")
                    labels.append(label)
                plot_multiple_functions(functions, labels)
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Invalid choice.")

def planning_calculator():
    print("\nGeneral Financial Planning")
    print("Select operation:")
    print("1. SIP Calculator")
    print("2. Lumpsum Calculator")
    print("3. Time Value of Money (FV, PV, PMT, N, Rate)")
    print("4. Go Back")
    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice == '4':
            break
        try:
            if choice == '1':
                mi = float(input("Enter monthly investment: "))
                r = float(input("Enter annual interest rate (%): "))
                n = int(input("Enter tenure (months): "))
                result = sip_calculator(mi, r, n)
                print(result)
            elif choice == '2':
                p = float(input("Enter principal (lumpsum): "))
                r = float(input("Enter annual interest rate (%): "))
                n = float(input("Enter tenure (years): "))
                result = lumpsum_calculator(p, r, n)
                print(result)
            elif choice == '3':
                print("\nTime Value of Money")
                print("1. Future Value (FV)")
                print("2. Present Value (PV)")
                print("3. Payment per period (PMT)")
                print("4. Number of Periods (N)")
                print("5. Interest Rate (I/Y)")
                print("6. Go Back")
                sub = input("Enter choice (1/2/3/4/5/6): ")
                if sub == '1':
                    pv_ = float(input("Enter Present Value (PV): "))
                    r = float(input("Enter rate per period (as decimal, e.g., 0.01): "))
                    n = int(input("Enter number of periods: "))
                    print(f"Future Value: {fv(pv_, r, n):.2f}")
                elif sub == '2':
                    fv_ = float(input("Enter Future Value (FV): "))
                    r = float(input("Enter rate per period (as decimal, e.g., 0.01): "))
                    n = int(input("Enter number of periods: "))
                    print(f"Present Value: {pv(fv_, r, n):.2f}")
                elif sub == '3':
                    pv_ = float(input("Enter Present Value (PV): "))
                    r = float(input("Enter rate per period (as decimal, e.g., 0.01): "))
                    n = int(input("Enter number of periods: "))
                    print(f"PMT: {pmt(pv_, r, n):.2f}")
                elif sub == '4':
                    pv_ = float(input("Enter Present Value (PV): "))
                    pmt_ = float(input("Enter Payment per period (PMT): "))
                    r = float(input("Enter rate per period (as decimal, e.g., 0.01): "))
                    print(f"Number of Periods: {nper(pv_, pmt_, r):.2f}")
                elif sub == '5':
                    pv_ = float(input("Enter Present Value (PV): "))
                    pmt_ = float(input("Enter Payment per period (PMT): "))
                    n = int(input("Enter number of periods: "))
                    print(f"Interest Rate: {rate(pv_, pmt_, n):.4f}")
                elif sub == '6':
                    continue
                else:
                    print("Invalid choice.")
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")
        next_calc = input("Do you want to perform another planning calculation? (yes/no): ")
        if next_calc.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
