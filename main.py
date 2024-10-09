# File: main.py

import tkinter as tk
from tkinter import ttk

# Function to increment the counter
def increment_counter():
    global counter_value
    counter_value += 1
    counter_label.config(text=str(counter_value))

# Function to decrement the counter
def decrement_counter():
    global counter_value
    counter_value -= 1
    counter_label.config(text=str(counter_value))

# Function to move the app window by dragging it
def start_move(event):
    global x_offset, y_offset
    x_offset = event.x
    y_offset = event.y

def on_move(event):
    x = event.x_root - x_offset
    y = event.y_root - y_offset
    root.geometry(f"+{x}+{y}")

# Initialize the main window
def create_counter_app():
    global root, counter_label, x_offset, y_offset
    root = tk.Tk()
    root.title("Counter App")

    # Set light grey background
    background_color = "#d3d3d3"  # Light grey color
    root.config(bg=background_color)
    root.geometry("100x170")  # Set initial window size

    # Enable resizing
    root.wm_attributes("-alpha", 0.7)
    root.resizable(True, True)

    # Ensure the window stays on top of other windows (pinned)
    root.wm_attributes("-topmost", True)

    # Bind mouse events to allow dragging the window
    root.bind("<Button-1>", start_move)  # Click to start move
    root.bind("<B1-Motion>", on_move)    # Move the window by dragging

    # Initialize counter value
    global counter_value
    counter_value = 0

    # Create a label to display the counter
    counter_label = ttk.Label(root, text=str(counter_value), font=("Helvetica", 24), background=background_color)
    counter_label.pack(pady=20)

    # Create "+" button to increment the counter
    increment_button = ttk.Button(root, text="+", command=increment_counter)
    increment_button.pack(pady=10)

    # Create "-" button to decrement the counter
    decrement_button = ttk.Button(root, text="-", command=decrement_counter)
    decrement_button.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()

# Entry point of the script
if __name__ == "__main__":
    create_counter_app()
