import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def false_position_method(f, a, b, tol, max_iterations):
    if f(a) * f(b) >= 0:
        raise ValueError("The function does not satisfy the intermediate value theorem in the given interval.")
    
    results = []  # List to store results for each iteration
    
    for iteration in range(1, max_iterations + 1):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        fc = f(c)

        # Calculate the error in this iteration
        e = abs(fc)
        
        result = {
            "Iteration": iteration,
            "a": a,
            "c": c,
            "b": b,
            "f(c)": fc,
            "E": e
        }
        
        results.append(result)
         
        if e < tol:
            result["Approximate Solution"] = c
            result["Convergence Iterations"] = iteration
            break  # Exit the loop when convergence is reached
        
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    
    if 'Approximate Solution' not in result:
        result["Convergence Iterations"] = max_iterations
        result["Approximate Solution"] = None
    
    return results

# Define your function f(x)
def f(x):
    return x**2 - 4

# Create an array of x values for plotting
x_values = np.linspace(-2, 4, 400)  # Adjust the range as needed

# Calculate corresponding y values
y_values = f(x_values)  

# Perform the False Position Method
result = false_position_method(f, 1, 3, 1e-6, 100)
approx_solution = [iteration_result.get("Approximate Solution") for iteration_result in result]

# Plot the function f(x)
plt.plot(x_values, y_values, color='blue')

# Mark the points of the False Position Method iterations
# for iteration_result in result:
#     plt.scatter(iteration_result["a"], 0, color='red', marker='o', label='a', zorder=5)
#     plt.scatter(iteration_result["b"], 0, color='green', marker='o', label='b', zorder=5)
#     plt.scatter(iteration_result["c"], 0, color='purple', marker='o', label='c', zorder=5)

# Mark the approximate solution point
plt.scatter(approx_solution, [0] * len(approx_solution), color='black', marker='x', zorder=5)

# Set the limits for the x and y axes
plt.xlim(-2, 4)  # Adjust the limits as needed
plt.ylim(-10, 10)  # Adjust the limits as needed

# Add labels and legend
plt.xlabel('x', fontweight='bold')
plt.ylabel('f(x)', fontweight='bold')
plt.legend()

plt.grid()
plt.show()


