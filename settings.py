from tkinter import ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle

class Settings:
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
                        background="#4B0082", # Blue color
                        font=("Helvetica", 10),
                        borderwidth=0,
                        focuscolor="#4B0082", # Blue color
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