from tkinter import Tk, BOTH, Canvas
import tkinter.ttk as ttk
from PIL import Image, ImageTk

def main():


    gui = GUI()


class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Artist Guessing Game")
        self.root.geometry("1800x1200")
        self.root.resizable(False, False)
        self.create_startup_screen()
        self.root.mainloop()

    def create_startup_screen(self):
        image_path = "Images/TS_Eras_Tour.jpg"
        img = Image.open(image_path)
        img = ImageTk.PhotoImage(img)

        # Create a label to display the image
        label = ttk.Label(self.root, image=img)
        label.pack()


if __name__ == "__main__":
    main()


#HOW DO I PUT A IMAGE IN WHAT THE HELL

    