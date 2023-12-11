import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temperature = float(entry_temperature.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid temperature")
        return

    original_unit = combo_original_unit.get()

    if original_unit == "Celsius":
        fahrenheit = (temperature * 9/5) + 32
        kelvin = temperature + 273.15
        celsius = temperature
    elif original_unit == "Fahrenheit":
        celsius = (temperature - 32) * 5/9
        kelvin = (temperature + 459.67) * 5/9
        fahrenheit = temperature
    elif original_unit == "Kelvin":
        celsius = temperature - 273.15
        fahrenheit = (temperature * 9/5) - 459.67
        kelvin = temperature
    else:
        messagebox.showerror("Error", "Invalid unit")
        return

    result_label.config(text=f"{temperature:.2f} {original_unit} is:\n"
                             f"{celsius:.2f} Celsius\n"
                             f"{fahrenheit:.2f} Fahrenheit\n"
                             f"{kelvin:.2f} Kelvin")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")

# Style
style = ttk.Style()
style.configure("TButton", padding=10, font=("Helvetica", 12))
style.configure("TLabel", padding=10, font=("Helvetica", 12))
style.configure("TCombobox", padding=8, font=("Helvetica", 12))

# Temperature entry
label_temperature = ttk.Label(root, text="Enter Temperature:")
label_temperature.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_temperature = ttk.Entry(root)
entry_temperature.grid(row=0, column=1, padx=10, pady=10)

# Original unit dropdown
label_original_unit = ttk.Label(root, text="Original Unit:")
label_original_unit.grid(row=1, column=0, padx=10, pady=10, sticky="e")
original_units = ["Celsius", "Fahrenheit", "Kelvin"]
combo_original_unit = ttk.Combobox(root, values=original_units, state="readonly")
combo_original_unit.grid(row=1, column=1, padx=10, pady=10)
combo_original_unit.current(0)

# Convert button
convert_button = ttk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=2, column=0, columnspan=2, pady=20)

# Result label
result_label = ttk.Label(root, text="", font=("Helvetica", 10))
result_label.grid(row=3, column=0, columnspan=2, pady=5)

# Run the GUI
root.mainloop()
