
# 1.Write a Python program using Matplotlib to plot a simple line graph showing the relationship between two lists of data. 
# The first list contains the numbers [1, 2, 3, 4, 5] and the second list contains the corresponding squares [1, 4, 9, 16, 25].

import matplotlib.pyplot as plt
import  numpy as np


def plot_list(x,y):
    X = np.array(x)
    Y = np.array(y)
    plt.plot(X,Y)
    plt.show()

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plot_list(x=x,y=y)



# 2.Create a Python program to plot a graph, add a title, and label the axes. Use the following data for the x and y axes:
# x-axis data: [1, 2, 3, 4, 5]
# y-axis data: [2, 4, 6, 8, 10]

def plot_list_label(x,y):
    X = np.array(x)
    Y = np.array(y)
    plt.plot(X,Y)
    plt.xlabel("X-axis") 
    plt.ylabel("Y-axis") 
    plt.title("Relation of 2 List")
    plt.show()

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plot_list_label(x=x,y=y)


# 3. Write a Python program using Matplotlib to create a scatter plot. Plot the following points:
# (1, 2), (2, 3), (3, 5), (4, 7), (5, 11)

def scatter_plot(x,y):
    plt.scatter(x,y)
    plt.show()

input = (1, 2), (2, 3), (3, 5), (4, 7), (5, 11)
x=[]
y=[]
for i in input:
    x.append(i[0])
    y.append(i[1])

scatter_plot(x=np.array(x),y=np.array(y))

# 4.Write a Python program to create a 1x2 grid of subplots. 
# The first subplot should show a simple line plot with data [1, 2, 3, 4] and [10, 20, 30, 40]. 
# The second subplot should display a bar plot with the same x-axis values and corresponding y-axis values [5, 10, 15, 20].

# Data for the plots
x = [1, 2, 3, 4]
y_line = [10, 20, 30, 40]
y_bar = [5, 10, 15, 20]

# Create a 1x2 grid of subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# First subplot: simple line plot
ax1.plot(x, y_line)
ax1.set_title('Line Plot')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis')

# Second subplot: bar plot
ax2.bar(x, y_bar)
ax2.set_title('Bar Plot')
ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')

# Display the plots
plt.tight_layout()
plt.show()




# 5.Write a Python program to find the maximum number in a list of numbers using a built-in function.
# Sample Input -> [10, 4, 45, 99, 12]
# Sample Output -> The maximum value is: 99

li = [10, 4, 45, 99, 12]
print(max(li))

# 6.Create a Python program that defines a custom function to calculate the factorial of a number. 
# The function should take one integer as an argument and return its factorial.
# Sample Input -> 5
# Sample Output -> The factorial of 5 is: 120


def factorial(n):
    if n < 0:
        return "Factorial is undefined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

number = 5
print(f"The factorial of {number} is {factorial(number)}")



# 7.Write a Python program that reads the contents of a file and prints them. Use the read() method to read the file.

filepath = "SampleText.txt"
f = open(filepath, "r")
print(f.read())


# 8.Write a Python program that checks if a file exists before performing operations like reading or writing.

import os

filepath = "SampleText.txt"
if os.path.isfile(filepath):
    f = open(filepath, "r")
    print(f.read())


# 9.Write a program to solve the below equations
# 2x+y=5
# x−y=1


import numpy as np

A = np.array([[2, 1], [1, -1]])
B = np.array([5, 1])
solution = np.linalg.solve(A, B)
x, y = solution

print(f"The solution to the equations is x = {x} and y = {y}.")



# 10.Write a program to integrate the function f(x)=x2 from 0 to 1.

import scipy.integrate as integrate
def f(x):
    return x**2
result, error = integrate.quad(f, 0, 1)

print(f"The integral of f(x) = x^2 from 0 to 1 is {result}.")


# 11.Write a program to find the inverse by inv() function and determinant det() function.

import numpy as np

matrix = np.array([[4, 7], [2, 6]])
inverse_matrix = np.linalg.inv(matrix)
determinant = np.linalg.det(matrix)

print("Matrix:")
print(matrix)
print("\nInverse of the matrix:")
print(inverse_matrix)
print("\nDeterminant of the matrix:")
print(determinant)

# 12. Write a program to apply a function to find square root for each element in the array.

import math

def find_square_roots(arr):
    return [math.sqrt(x) for x in arr]
array = [4, 16, 25, 36, 49]
square_roots = find_square_roots(array)
print(square_roots)

# 13.Write a program to Perform Arithmetic Operations on Multi-Dimensional Arrays.

import numpy as np

array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

addition = np.add(array1, array2)
subtraction = np.subtract(array1, array2)
multiplication = np.multiply(array1, array2)
division = np.divide(array1, array2)

print("Addition:\n", addition)
print("Subtraction:\n", subtraction)
print("Multiplication:\n", multiplication)
print("Division:\n", division)

# 14.Create a python program to check the missing values in a dataset.

import pandas as pd

# Sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, None, 22, 23, None],
    'City': ['New York', 'Los Angeles', None, 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
missing_values = df.isnull()
print("DataFrame with missing values indicated (True means missing):\n", missing_values)
missing_count = df.isnull().sum()
print("\nCount of missing values in each column:\n", missing_count)

# 15.Write a python program to group and aggregate the data.

import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah'],
    'Department': ['HR', 'Finance', 'HR', 'IT', 'Finance', 'IT', 'HR', 'Finance'],
    'Salary': [50000, 60000, 55000, 70000, 65000, 72000, 58000, 63000]
}
df = pd.DataFrame(data)
grouped = df.groupby('Department').agg({'Salary': 'mean'})
print("Grouped and Aggregated Data:\n", grouped)