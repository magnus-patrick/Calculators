from sympy import sympify, Eq, solve, diff, integrate, symbols, limit, Sum, oo
from scipy.integrate import quad
import matplotlib.pyplot as plt
import numpy as np

x = symbols("x")

def choice():
    choice = input("\nWhat do you want to do?\n1. Algebra\n2. Derivative\n3. Integral\n4. Graph\n5. Limit\n6. Sum\nResponse: ")
    
    if choice == "1" or choice.lower() == "algebra":
        def algebra():
            left = sympify(input("Left side of equation (eg x**2, 2*x): "))
            right = sympify(input("Right side of equation (eg 2, x**0.5): "))
            equation = Eq(left, right)
            solution = solve(equation)
            print("The solutions/s to the equation is/are ", solution)
        algebra()

    elif choice == "2" or choice.lower() == "derivative":
        def derivative():
            function = sympify(input("Function to take the derivative of: "))
            deriv = diff(function, x)
            print(f"The derivative of {function} is", deriv)
        derivative()

    elif choice == "3" or choice.lower() == "integral":
        def integral():
            choice = input("Do you want to take the indefinite integral or definite integral? (1 or 2): ")
            if choice == "1":
                function = sympify(input("Function to take the integral of: "))
                indef_integral = integrate(function, x)
                print(f"The integral of {function} is", indef_integral)
            elif choice == "2":
                function = sympify(input("Function to take the integral of: "))
                a = float(input("Lower bound: "))
                b = float(input("Upper bound: "))
                new_function = lambda val: float(function.subs(x, val))
                def_integral = quad(new_function, a, b) #quad() only accepts lambda functions
                print(f"The definite integral of {function} from [{a},{b}] is {def_integral}")
        integral()

    elif choice == "4" or choice.lower() == "graph":
        def graph():
            x = np.linspace(-20, 20, 1000)
            y = 5 * np.cos(x) + 9
            plt.plot(x, y)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Wave Function')
            plt.grid(True)
            plt.show()
        graph()

    elif choice == "5" or choice.lower() == "limit":
        def the_limit():
            limit_function = sympify(input("Function to take limit of: "))
            a = sympify(input("Value that f approaches: "))
            lim = limit(limit_function, x, a)
            print(f"The limit of {limit_function} as it approaches {a} is {lim}")
        the_limit()
    
    elif choice == "6" or choice.lower() == "sum":
        def summation():
            a_n = sympify(input("Function a_n: "))
            start = sympify(input("Starting point (typically 0 or 1): "))
            the_sum = Sum(a_n, (x, start, oo)).doit() #.n() approximates while .doit() gives exact answer
            print(f"{a_n}, starting at {start}, ending at oo, gives {the_sum}")
        summation()

def restart():
    restart = input("Want to do another operation? (y or n): ")
    if restart.lower() == "y" or restart.lower() == "yes":
        return True
    else:
        return False

choice()

while restart():
    choice()
