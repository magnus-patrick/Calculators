from sympy import sympify, Eq, solve, diff, integrate, symbols, limit, Sum
from scipy.integrate import odeint
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

x = symbols("x")

def choice():
    choice = input("\nWhat do you want to do?\n1. Algebra\n2. Derivative\n3. Integral\n4. Graph\n5. Limit\n6. Sum\n7. ODE\n8. Histogram\n9. Subplot\n10. FFT\nResponse: ")
    
    if choice == "1" or choice.lower() == "algebra":
        def algebra():
            left = sympify(input("Left side of equation (eg x**2, 2*x): "))
            right = sympify(input("Right side of equation (eg 2, x**0.5): "))
            equation = Eq(left, right)
            solution = solve(equation)
            print(f"The solutions/s to the equation is/are {solution}")
        algebra()

    elif choice == "2" or choice.lower() == "derivative":
        def derivative():
            function = sympify(input("Function to take the derivative of: "))
            deriv = diff(function, x)
            print(f"The derivative of {function} is {deriv}")
        derivative()

    elif choice == "3" or choice.lower() == "integral":
        def integral():
            choice = input("Do you want to take the indefinite integral or definite integral? (1 or 2): ")
            if choice == "1":
                function = sympify(input("Function to take the integral of: "))
                indef_integral = integrate(function, x)
                print(f"The integral of {function} is", indef_integral, "+ c")
            elif choice == "2":
                function = sympify(input("Function to take the integral of: "))
                a = float(input("Lower bound: "))
                b = float(input("Upper bound: "))
                def_integral = integrate(function, (x, a, b))
                print(f"The definite integral of {function} from [{a},{b}] is {def_integral}")
        integral()

    elif choice == "4" or choice.lower() == "graph":
        def graph(): #Note to self. Remember SciencePlots! It's becoming a problem at the moment.
            x = np.linspace(-4*np.pi, 4*np.pi, 20) #
            y1 = 5 * np.sin(5 * x + 5)
            y2 = 5 * np.sin(5 * x + 4.9)
            plt.figure(figsize = (9, 5))
            plt.title('State of a Pendulum') #Probably does not accurately represent pendulums. This is just an example.
            plt.plot(x, y1, '-', color = 'red', ms = 4, label = 'Prediction') #o means only the dots gets plotted. Number depends
            plt.plot(x, y2, 'o', color = 'green', ms = 5 , label = 'Results') #ms determines the size of the dots.
            plt.xlabel('Angle (rad)')
            plt.ylabel('Momentum (kg * m/s)')
            plt.grid()
            plt.legend(loc = 'upper left', ncol = 2) #Adds a legend at the upper left with 2 columns.
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
            a_x = sympify(input("Function a_x: "))
            start = sympify(input("Number to start at (typically 0 or 1): "))
            end = sympify(input("Number to stop at (can be oo as well!): "))
            the_sum = Sum(a_x, (x, start, end)).n() #.n() approximates while .doit() gives exact answer
            print(f"{a_x}, starting at {start}, ending at {end}, gives {the_sum}")
        summation()
    
    elif choice == "7" or choice.lower() == "ode":
        def ordinary():
            
            def lorenz(t, state, sigma, beta, rho):
                x, y, z = state
                dx = sigma * (y - x) #Differential equations
                dy = x * (rho - z) - y
                dz = x * y - beta * z
                return [dx, dy, dz]
            
            x = sympify(input("x: "))
            y = sympify(input("y: "))
            z = sympify(input("z: "))
            y0 = [x, y, z] #Initial conditions

            #Ed Lorenz used these values for the parameters.
            sigma = 10
            beta = 8 / 3
            rho = 28
            p = (sigma, beta, rho) #parameters

            t = np.arange(0.0, 30.0, 0.01)

            ode_sol = odeint(lorenz, y0, t, p, tfirst = True)

            fig = plt.figure()
            ax = fig.add_subplot(1, 2, 1, projection = "3d")
            ax.plot(ode_sol[:, 0],
                    ode_sol[:, 1],
                    ode_sol[:, 2], color = 'white')
            ax.set_title(f"dx/dt = σ(y - x)\ndy/dt = x(ρ - z) - y\ndz/dt = xy - βz\nx =  {x}\ny =  {y}\nz =  {z}")

            line_color = input("Color of line: ").lower()
            line, = ax.plot([], [], [], lw = 0.7, color = f'{line_color}')

            def initial():
                line.set_data([], [])
                line.set_3d_properties([])
                return line,

            def update(frame):
                line.set_data(ode_sol[:frame, 0], ode_sol[:frame, 1])
                line.set_3d_properties(ode_sol[:frame, 2])
                return line,

            animation = FuncAnimation(fig, update, frames = len(t), init_func = initial, interval = 1, blit = True)
            plt.show()

        ordinary()
    
    elif choice == "8" or choice.lower() == "histogram":
        def hist():
            hist1 = np.random.randn(1000)*2 - 0.4 #np.random.randn generates 1000 random numbers between 0 and 1.
            hist2 = np.random.randn(1000)*2 - 0.4
            plt.figure(figsize = (7, 4))
            plt.hist(hist1, bins = 40, density = True) #histtype = 'step' only traces the borders of the bins. 
            plt.hist(hist2, bins = 40, density = True, color = 'red') #density = True makes it a probability density plot
            plt.xlabel('x')
            plt.ylabel('Probability')
            plt.show()
        hist()
    
    elif choice == '9' or choice.lower() == 'subplot':
        def sub(): #Creates 2 figures on the same window.
            x = np.linspace(-20, 20, 20)
            y1 = 3*x**2 + 5*x
            y2 = np.gradient(y1, x)
            fig, axes = plt.subplots(1, 2, figsize = (10, 3.5))
            fig.text(0.5, 0.03, 'x', ha = 'center', fontsize = 15) #ha means horizontal alignment.
            axes[0].plot(x, y1, color = 'red', ms = 4)
            axes[0].set_ylabel('y') #It seems that set_ylabel() is used when making subplots.
            axes[0].set_title(f'f(x)') #Same with set_title() instead of plt.title()
            axes[0].tick_params(axis = 'both', labelsize = 7) #Reduces the size of the numbers on both axes.
            axes[0].grid()

            axes[1].plot(x, y2, color = 'green', ms = 4)
            axes[1].set_title("f'(x)")
            axes[1].tick_params(axis = 'both', labelsize = 7)
            axes[1].grid()     
            plt.show()          
        sub()
    
    elif choice == '10' or choice.lower() == 'fft':
        def fourier(): #Fourier transform tells you the frequencies that make up a signal or a time series.
            N = 600
            dx = 1.0 / 800.0
            t = np.linspace(0.0, N*dx, N, endpoint = False)
            x = np.sin(50.0 * 2.0*np.pi*t) + np.cos(200 * 2*np.pi*t)
            xf = fft(x)
            tf = fftfreq(N, dx)[:N//2]
            plt.plot(tf, np.abs(xf[:N//2]))
            plt.grid()
            plt.show()
        fourier()

def restart():
    restart = input("Want to do another operation? (y or n): ")
    return restart.lower() == "y" or restart.lower() == "yes"

choice()

while restart():
    choice()
