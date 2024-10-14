import streamlit as st

# Function definitions for basic calculator operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Streamlit app interface
st.title("Simple Calculator")

# User input for numbers and operation
num1 = st.number_input("Enter the first number", value=0.0, format="%.2f")
num2 = st.number_input("Enter the second number", value=0.0, format="%.2f")

operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform the operation
if operation == "Add":
    result = add(num1, num2)
elif operation == "Subtract":
    result = subtract(num1, num2)
elif operation == "Multiply":
    result = multiply(num1, num2)
elif operation == "Divide":
    result = divide(num1, num2)

# Display the result
st.write(f"The result is: {result}")
