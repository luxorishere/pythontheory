from tkinter import *

# Create the main window
root = Tk()
root.title("Simple Calculator")

# Create entry field for user input
entry_field = Entry(root, width=35, borderwidth=5, bg="lightblue", fg="black", font=("Arial", 20))
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to update the entry field
def update_entry_field(number):
    current = entry_field.get()
    entry_field.delete(0, END)
    entry_field.insert(0, str(current) + str(number))

# Function to clear the entry field
def clear_entry_field():
    entry_field.delete(0, END)

# Function to calculate the result
def calculate_result():
    try:
        result = eval(entry_field.get())
        entry_field.delete(0, END)
        entry_field.insert(0, str(result))
    except:
        entry_field.delete(0, END)
        entry_field.insert(0, "Error")

# Create buttons for numbers 0-9
button_1 = Button(root, text="1", padx=20, pady=10, bg="lightgreen", fg="black", font=("Arial", 16), command=lambda: update_entry_field(1))
button_2 = Button(root, text="2", padx=20, pady=10, bg="lightgreen", fg="black", font=("Arial", 16), command=lambda: update_entry_field(2))
button_3 = Button(root, text="3", padx=20, pady=10, bg="lightgreen", fg="black", font=("Arial", 16), command=lambda: update_entry_field(3))
button_4 = Button(root, text="4", padx=20, pady=10, bg="lightgreen", fg="black", font=("Arial", 16), command=lambda: update_entry_field(4))
button_5 = Button(root, text="5", padx=20, pady=10, bg="lightgreen", fg="black", font=("Arial", 16), command=lambda: update_entry_field(5))
button_6 = Button(root, text="6", padx=20, pady=10, bg="lightgreen", fg="black", font=("Arial", 16), command=lambda: update_entry_field(6))
button_7 = Button(root, text="7", padx=20, pady=10, bg="lightgreen", fg="black", font=("Arial", 16), command=lambda: update_entry_field(7))
button_8 = Button(root, text="8", padx=20, pady=10, bg="lightgreen", fg="black", font=("Arial", 16), command=lambda: update_entry_field(8))
button_9 = Button(root, text="9", padx=20, pady=10, bg="lightgreen", fg="black", font=("Arial", 16), command=lambda: update_entry_field(9))
button_0 = Button(root, text="0", padx=20, pady=10, bg="lightgreen", fg="black", font=("Arial", 16), command=lambda: update_entry_field(0))

# Create buttons for basic operations
button_add = Button(root, text="+", padx=20, pady=10, bg="lightblue", fg="black", font=("Arial", 16), command=lambda: update_entry_field("+"))
button_subtract = Button(root, text="-", padx=20, pady=10, bg="lightblue", fg="black", font=("Arial", 16), command=lambda: update_entry_field("-"))
button_multiply = Button(root, text="*", padx=20, pady=10, bg="lightblue", fg="black", font=("Arial", 16), command=lambda: update_entry_field("*"))
button_divide = Button(root, text="/", padx=20, pady=10, bg="lightblue", fg="black", font=("Arial", 16), command=lambda: update_entry_field("/"))

# Create button for equals
button_equals = Button(root, text="=", padx=20, pady=10, bg="lightgreen", fg="black", font=("Arial", 16), command=calculate_result)

# Create button for clear
button_clear = Button(root, text="Clear", padx=20, pady=10, bg="lightblue", fg="black", font=("Arial", 16), command=clear_entry_field)

# Place buttons on the GUI
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

button_equals.grid(row=4, column=2)
button_clear.grid(row=4, column=1)

# Start the GUI event loop
root.mainloop()k