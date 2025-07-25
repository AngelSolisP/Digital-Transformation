import tkinter as tk

window = tk.Tk()
window.title("My GUI")
window.geometry("400x300")

label = tk.Label(window, text="Hello, Tkinter!")
label.pack()

button = tk.Button(window, text="Click Me", command=window.quit)
button.pack()

entry = tk.Entry(window)
entry.pack()

window.mainloop()      
# This code creates a simple GUI application using Tkinter.
# It includes a label, a button, and an entry field.
# The application will close when the button is clicked.