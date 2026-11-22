# Importing Libraries
import tkinter as tk
from appCode.classes import AppConfig 
from PIL import ImageTk

# Initilise application window
root = tk.Tk()

# Set the window title & initial positioning
root.title(AppConfig().get_title())
root.eval("tk::PlaceWindow . center")

# Create frame 1
frame1 = tk.Frame(root, height=400, width=600, bg=AppConfig().get_primary_black_color())
frame1.pack(fill=tk.BOTH, expand=True)
frame1.grid(row=0, column=0)

# Frame 1 content
img = AppConfig().get_primary_logo_red_australia()
img_widget = tk.Label(frame1, image=img, bg=AppConfig().get_primary_black_color())
img_widget.image = img  # Keep a reference to the image to prevent garbage collection

img_widget.pack(pady=20)

# Run the application
root.mainloop()