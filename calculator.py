import streamlit as st

# 🎨 Set the title
st.title("🧮 Simple Calculator App")

# ✍️ User inputs
num1 = st.number_input("Enter the first number", step=1.0, format="%.2f")
num2 = st.number_input("Enter the second number", step=1.0, format="%.2f")
operation = st.selectbox("Select Operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# 🧠 Perform calculation
def calculate(a, b, op):
    if op == "Addition":
        return a + b
    elif op == "Subtraction":
        return a - b
    elif op == "Multiplication":
        return a * b
    elif op == "Division":
        if b != 0:
            return a / b
        else:
            return "❌ Cannot divide by zero!"

# 📢 Display result
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.success(f"Result: {result}")
