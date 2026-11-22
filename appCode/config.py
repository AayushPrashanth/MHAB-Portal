# Importing the required libraries
from logging import config
import configparser
import ttkbootstrap as ttk
from dataclasses import dataclass

# Load configuration
config = configparser.ConfigParser()
config.read('appCode/config.ini')

@dataclass(frozen=True)
class AppConfig:
    # Color
    primary_red_color: str = config.get('colors', 'PRIMARY_RED_COLOR')
    secondary_red_color: str = config.get('colors', 'SECONDARY_RED_COLOR')

    primary_yellow_color: str = config.get('colors', 'PRIMARY_YELLOW_COLOR')
    secondary_yellow_color: str = config.get('colors', 'SECONDARY_YELLOW_COLOR')

    primary_black_color: str = config.get('colors', 'PRIMARY_BLACK_COLOR')

    primary_grey_color: str = config.get('colors', 'PRIMARY_GREY_COLOR')
    secondary_grey_color: str = config.get('colors', 'SECONDARY_GREY_COLOR')

    primary_white_color: str = config.get('colors', 'PRIMARY_WHITE_COLOR')

    # Font
    default_font: str = config.get('fonts', 'DEFAULT_FONT')
    small_font_size: int = config.getint('fonts', 'SMALL_FONT_SIZE')
    medium_font_size: int = config.getint('fonts', 'MEDIUM_FONT_SIZE')
    large_font_size: int = config.getint('fonts', 'LARGE_FONT_SIZE')

    # App
    title: str = config.get('app', 'TITLE')
    initial_window_scale: float = config.getfloat('app', 'INITIAL_WINDOW_SCALE')

    # Logos
    primary_logo_white_path: str = config.get('logos', 'PRIMARY_LOGO_WHITE_PATH')
    primary_logo_red_australia_path: str = config.get('logos', 'PRIMARY_LOGO_RED_AUSTRALIA_PATH')