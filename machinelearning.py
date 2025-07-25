from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import tk

from calculator import clear_entry

# Load the digits dataset
digits = load_digits()

# Display the first 5 images and their labels
fig, axes = plt.subplots(1, 5, figsize=(10, 5))
for ax, image, label in zip(axes, digits.images, digits.target):
    ax.imshow(image, cmap='gray')
    ax.set_title(f"Label: {label}")
    ax.axis('off')
plt.show()# This code loads the digits dataset from sklearn and displays the first 5 images with their labels.
# Configure the grid layout for buttons
for i in range(1, 5):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)
# Clear button
clear_button = tk.Button(
    window,
    text='C',
    font=('Arial', 18),
    command=lambda: entry.delete(0, tk.END)
)
clear_button.grid(row=5, column=1)
# Function to handle button clicks
def on_button_click(value):
    """
    Handles button clicks and updates the entry widget.
    """
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + value)
    font=('Arial', 18),
    command=clear_entry