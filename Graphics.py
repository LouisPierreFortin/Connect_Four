import tkinter as tk

def on_click(event):
    """Draw a small red circle where the user clicks."""
    r = 5
    canvas.create_oval(event.x - r, event.y - r, event.x + r, event.y + r, fill="red", outline="")

# Create the main application window
root = tk.Tk()
root.title("Connect Four")
root.geometry("980x700")

# Create a Canvas widget
canvas = tk.Canvas(root, width=196, height=140, bg="white")
canvas.pack(pady=10)

# Draw basic shapes
canvas.create_line(10, 10, 200, 50, fill="blue", width=2)  # Line
canvas.create_rectangle(50, 80, 150, 150, outline="green", width=2)  # Rectangle
canvas.create_oval(200, 80, 300, 150, fill="yellow", outline="black")  # Oval
canvas.create_polygon(350, 80, 400, 150, 300, 150, fill="orange")  # Polygon
canvas.create_text(250, 200, text="Hello Canvas!", font=("Arial", 16, "bold"), fill="purple")  # Text

# Bind mouse click event
canvas.bind("<Button-1>", on_click)

# Run the Tkinter event loop
root.mainloop()



