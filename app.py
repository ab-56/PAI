import streamlit as st

# Function for basic arithmetic operations
def calculate(op, num1, num2):
    if op == "Add":
        return num1 + num2
    elif op == "Subtract":
        return num1 - num2
    elif op == "Multiply":
        return num1 * num2
    elif op == "Divide":
        if num2 == 0:
            return "Error! Division by zero."
        return num1 / num2
    else:
        return "Invalid Operation"

# Streamlit app layout
st.title("Simple Calculator")

# User inputs
num1 = st.number_input("Enter the first number", value=0)
num2 = st.number_input("Enter the second number", value=0)

# Operator selection
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

# Button to trigger calculation
if st.button("Calculate"):
    result = calculate(operation, num1, num2)
    st.write(f"Result: {result}")
