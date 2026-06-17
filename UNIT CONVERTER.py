import tkinter as tk
from tkinter import ttk, messagebox

# Function to perform conversion
def convert():
    try:
        value = float(entry_value.get())
        choice = combo.get()

        if choice == "Kilometers to Miles":
            result = value * 0.621371

        elif choice == "Miles to Kilometers":
            result = value * 1.60934

        elif choice == "Kilograms to Pounds":
            result = value * 2.20462

        elif choice == "Pounds to Kilograms":
            result = value * 0.453592

        elif choice == "Celsius to Fahrenheit":
            result = (value * 9/5) + 32

        elif choice == "Fahrenheit to Celsius":
            result = (value - 32) * 5/9

        elif choice == "Centimeters to Inches":
            result = value / 2.54

        elif choice == "Inches to Centimeters":
            result = value * 2.54

        elif choice == "Meters to Feet":
            result = value * 3.28084

        elif choice == "Feet to Meters":
            result = value / 3.28084

        else:
            result = "Select a conversion"

        result_label.config(text=f"Result: {round(result, 4)}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")


# Create window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x250")

# Heading
title_label = tk.Label(root, text="Unit Converter Tool",
                        font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Input box
tk.Label(root, text="Enter Value:").pack()
entry_value = tk.Entry(root, width=20)
entry_value.pack(pady=5)

# Dropdown menu
tk.Label(root, text="Select Conversion:").pack()

options = [
    "Kilometers to Miles",
    "Miles to Kilometers",
    "Kilograms to Pounds",
    "Pounds to Kilograms",
    "Celsius to Fahrenheit",
    "Fahrenheit to Celsius",
    "Centimeters to Inches",
    "Inches to Centimeters",
    "Meters to Feet",
    "Feet to Meters"
]

combo = ttk.Combobox(root, values=options, width=25)
combo.pack(pady=5)
combo.current(0)

# Convert button
convert_button = tk.Button(root,
                           text="Convert",
                           command=convert,
                           bg="lightblue",
                           font=("Arial", 12))
convert_button.pack(pady=10)

# Result label
result_label = tk.Label(root,
                        text="Result:",
                        font=("Arial", 14))
result_label.pack(pady=10)

# Run application
root.mainloop()