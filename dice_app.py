from tkinter import ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle
from settings import Settings
from buttons import Buttons

class DiceApp:
    '''Simple app for d&d dice'''
    def __init__(self, master):
        self.master = master
        self.settings = Settings(self.master)
        self.buttons = Buttons(self.master, self.settings)
