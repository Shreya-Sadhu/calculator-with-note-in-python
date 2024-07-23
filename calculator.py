import tkinter as tk
from tkinter import ttk

# Function to evaluate the calculator expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the calculator input
def clear():
    entry.delete(0, tk.END)

# Function to append text to the notes section
def append_note():
    note = notes_entry.get()
    if note:
        notes_text.insert(tk.END, note + '\n')
        notes_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator with Notes")

# Create the calculator frame
calc_frame = ttk.Frame(root, padding="10")
calc_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create the entry widget for the calculator
entry = ttk.Entry(calc_frame, width=20, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, pady=5)

# Create calculator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    button = ttk.Button(calc_frame, text=text, command=lambda t=text: entry.insert(tk.END, t) if t != '=' else evaluate_expression())
    button.grid(row=row, column=col, sticky=(tk.W, tk.E), padx=5, pady=5)

# Create the clear button
clear_button = ttk.Button(calc_frame, text="C", command=clear)
clear_button.grid(row=4, column=3, sticky=(tk.W, tk.E), padx=5, pady=5)

# Create the notes frame
notes_frame = ttk.Frame(root, padding="10")
notes_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create the notes entry widget
notes_entry = ttk.Entry(notes_frame, width=50, font=("Arial", 12))
notes_entry.grid(row=0, column=0, pady=5)

# Create the add note button
add_note_button = ttk.Button(notes_frame, text="Add Note", command=append_note)
add_note_button.grid(row=0, column=1, padx=5, pady=5)

# Create the text widget for displaying notes
notes_text = tk.Text(notes_frame, width=60, height=10, font=("Arial", 12))
notes_text.grid(row=1, column=0, columnspan=2, pady=5)

# Start the main event loop
root.mainloop()