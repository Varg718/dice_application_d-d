from tkinter import ttk
from ttkthemes import ThemedStyle

class Buttons:
    def __init__(self, master, settings):
        # Animation buttons
        self.animate_d4_button = ttk.Button(master, text="Roll d4", command=lambda: settings.animate_roll(4, 10, 100), style='Toolbutton.TButton')
        self.animate_d6_button = ttk.Button(master, text="Roll d6", command=lambda: settings.animate_roll(6, 10, 100), style='Toolbutton.TButton')
        self.animate_d8_button = ttk.Button(master, text="Roll d8", command=lambda: settings.animate_roll(8, 10, 100), style='Toolbutton.TButton')
        self.animate_d10_button = ttk.Button(master, text="Roll d10", command=lambda: settings.animate_roll(10, 10, 100), style='Toolbutton.TButton')
        self.animate_d12_button = ttk.Button(master, text="Roll d12", command=lambda: settings.animate_roll(12, 10, 100), style='Toolbutton.TButton')
        self.animate_d20_button = ttk.Button(master, text="Roll d20", command=lambda: settings.animate_roll(20, 10, 100), style='Toolbutton.TButton')
        # Putting the buttons on the screen
