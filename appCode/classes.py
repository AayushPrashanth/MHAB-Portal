# Importing the required libraries
from logging import config
import configparser
import tkinter as tk
from PIL import ImageTk

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

root = tk.Tk()
root.withdraw()  # Hide the root window to get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

# Define the AppConfig class
class AppConfig:
    def __init__(self):
        # Color
        self.primary_red_color = config.get('colors', 'PRIMARY_RED_COLOR')
        self.secondary_red_color = config.get('colors', 'SECONDARY_RED_COLOR')

        self.primary_yellow_color = config.get('colors', 'PRIMARY_YELLOW_COLOR')
        self.secondary_yellow_color = config.get('colors', 'SECONDARY_YELLOW_COLOR')

        self.primary_black_color = config.get('colors', 'PRIMARY_BLACK_COLOR')

        self.primary_grey_color = config.get('colors', 'PRIMARY_GREY_COLOR')
        self.secondary_grey_color = config.get('colors', 'SECONDARY_GREY_COLOR')

        self.primary_white_color = config.get('colors', 'PRIMARY_WHITE_COLOR')

        # App
        self.title = config.get('app', 'TITLE')

        root = tk.Tk()
        root.withdraw()  # Hide the root window to get screen dimensions

        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        root.destroy()

        # Logos
        self.primary_logo_white_path = config.get('logos', 'PRIMARY_LOGO_WHITE_PATH')
        self.primary_logo_red_australia_path = config.get('logos', 'PRIMARY_LOGO_RED_AUSTRALIA_PATH')


    # Get Color Methods
    def get_primary_red_color(self):
        return self.primary_red_color

    def get_secondary_red_color(self):
        return self.secondary_red_color

    def get_primary_yellow_color(self):
        return self.primary_yellow_color

    def get_secondary_yellow_color(self):
        return self.secondary_yellow_color

    def get_primary_black_color(self):
            return self.primary_black_color
    
    def get_primary_grey_color(self):
        return self.primary_grey_color

    def get_secondary_grey_color(self):
        return self.secondary_grey_color

    def get_primary_white_color(self):
        return self.primary_white_color
    
    # Get App Methods    
    def get_title(self):
        return self.title

    def get_screen_width(self):
        return self.screen_width

    def get_screen_height(self):
        return self.screen_height

    # Get Logo Methods
    def get_primary_logo_white_path(self):
        return f"{self.primary_logo_white_path}"

    def get_primary_logo_white(self):
        return ImageTk.PhotoImage(file=f"{self.primary_logo_white_path}")

    def get_primary_logo_red_australia_path(self):
        return f"{self.primary_logo_red_australia_path}"

    def get_primary_logo_red_australia(self):
        return ImageTk.PhotoImage(file=f"{self.primary_logo_red_australia_path}")
