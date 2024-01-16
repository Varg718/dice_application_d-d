import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import random
from ttkthemes import ThemedStyle

class DiceApp:
    '''Simple app for d&d dice'''

    def __init__(self, master):
        self.master = master
        self.master.title("Dice Roller App")
        self.master.geometry("500x300")
        self.master.resizable(width=False, height=False)

        # Setting up the path for the bg
        image_path = r"/home/robertw/Desktop/git_hub_projects/dice/new_one.jpg"

        # Converting the img
        self.image = Image.open(image_path).convert('RGBA')
        self.image = self.resize_image((500, 300))
        self.image_tk = ImageTk.PhotoImage(self.image)

        # Setting transparency on bg
        self.image.putalpha(128)

        # Creating canvas for img
        self.canvas = tk.Canvas(master, width=500, height=300)
        self.canvas.pack()

        # Displaying the img on canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_tk)

        # Initializing buttons and label
        style = ThemedStyle(self.master)
        style.set_theme("black")

        # Configuring the buttons settings
        style.configure("TButton",
                        foreground="white",
                        background="#4B0082",  # Blue color
                        font=("Helvetica", 10),
                        borderwidth=0,
                        focuscolor="#4B0082",  # Blue color
                        focusthickness=3,
                        relief="flat",
                        padding=(1, 2),  
                        bordercolor="#4B0082",  
                        lightcolor="#4B0082",  
                        darkcolor="#4B0082",  
                        border_radius =20 
                        )
        
        # Setting buttons style
        style.configure("Toolbutton.TButton",
                        relief="flat",
                        borderwidth=0,
                        )

        # Label result
        self.result_label = ttk.Label(master, text="", font=("Helvetica", 35), background="black", foreground="white")
        self.canvas.create_window(250, 150, window=self.result_label)

        # Info label
        self.info_label = ttk.Label(master, text="Choose the dice and click 'Roll'", font=("Helvetica", 12), style='TButton')
        self.canvas.create_window(250, 270, window=self.info_label)

        # Animation buttons
        self.animate_d4_button = ttk.Button(master, text="Roll d4", command=lambda: self.animate_roll(4, 10, 100), style='Toolbutton.TButton')
        self.animate_d6_button = ttk.Button(master, text="Roll d6", command=lambda: self.animate_roll(6, 10, 100), style='Toolbutton.TButton')
        self.animate_d8_button = ttk.Button(master, text="Roll d8", command=lambda: self.animate_roll(8, 10, 100), style='Toolbutton.TButton')
        self.animate_d10_button = ttk.Button(master, text="Roll d10", command=lambda: self.animate_roll(10, 10, 100), style='Toolbutton.TButton')
        self.animate_d12_button = ttk.Button(master, text="Roll d12", command=lambda: self.animate_roll(12, 10, 100), style='Toolbutton.TButton')
        self.animate_d20_button = ttk.Button(master, text="Roll d20", command=lambda: self.animate_roll(20, 10, 100), style='Toolbutton.TButton')

        # Putting the buttons on the screen
        self.canvas.create_window(50, 50, anchor=tk.NW, window=self.animate_d4_button)
        self.canvas.create_window(120, 50, anchor=tk.NW, window=self.animate_d6_button)
        self.canvas.create_window(190, 50, anchor=tk.NW, window=self.animate_d8_button)
        self.canvas.create_window(260, 50, anchor=tk.NW, window=self.animate_d10_button)
        self.canvas.create_window(330, 50, anchor=tk.NW, window=self.animate_d12_button)
        self.canvas.create_window(400, 50, anchor=tk.NW, window=self.animate_d20_button)

    def resize_image(self, new_size):
        return self.image.resize(new_size)

    def roll_dice(self, sides):
        result = random.randint(1, sides)
        self.show_result(f"{result}")

    def animate_roll(self, sides, iterations, delay):
        self.info_label.config(text=f"Throwing dice d{sides}...")
        self.animate_helper(sides, iterations, delay)

    def animate_helper(self, sides, iterations, delay):
        if iterations > 0:
            color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            self.canvas.configure(bg=color)
            self.master.update()
            self.master.after(delay, self.animate_helper, sides, iterations - 1, delay)
        else:
            self.roll_dice(sides)
            self.info_label.config(text="Choose a dice and click 'Roll'")

    def show_result(self, message):
        self.result_label.config(text=message)

# Creating the main window of the app
root = tk.Tk()
app = DiceApp(root)

# Starting the app
root.mainloop()

