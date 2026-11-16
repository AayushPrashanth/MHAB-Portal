# Importing Libraries
from logging import config
import tkinter as tk
import configparser

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Initilise application window
root = tk.Tk()

# Set the window title & initial positioning
root.title(config.get('app', 'TITLE'))
root.eval("tk::PlaceWindow . center")

# Set the primary color
root.configure(bg=config.get('colors', 'PRIMARY_BLACK_COLOR'))

# Run the application
root.mainloop()