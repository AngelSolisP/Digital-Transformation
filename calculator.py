import tkinter as tk

def on_button_click(value):
    """
    This function is called when a number or operator button is clicked.
    It appends the clicked value to the entry field.
    """
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + value)

def clear_entry():
    """
    Clears the entry field.
    """
    entry.delete(0, tk.END)

def calculate_result():
    """
    Calculates the result of the expression in the entry field.
    Handles errors and displays the result.
    """
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error: Div by 0")
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# --- GUI Setup ---
window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")
window.resizable(False, False) # Make window not resizable

# Entry widget to display the expression and result
entry = tk.Entry(window, font=('Arial', 24), borderwidth=2, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10, sticky="nsew")

# --- Button Layout ---
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2)
]

for (text, row, col) in buttons:
    button = tk.Button(
        window,
        text=text,
        font=('Arial', 18),
        command=lambda t=text: on_button_click(t)
    )
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    window.grid_columnconfigure(col, weight=1)
    window.grid_rowconfigure(row, weight=1)

# Clear button
clear_button = tk.Button(
    window,
    text='C',
    font=('Arial', 18),
    command=clear_entry
)
clear_button.grid(row=4, column=3, sticky="nsew", padx=5, pady=5)

# Equals button
equals_button = tk.Button(
    window,
    text='=',
    font=('Arial', 18),
    command=calculate_result
)
equals_button.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
window.grid_rowconfigure(5, weight=1)


if __name__ == "__main__":
    window.mainloop()