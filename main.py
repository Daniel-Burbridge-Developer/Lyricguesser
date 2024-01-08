from tkinter import Tk, BOTH, Canvas
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import time

def main():
    gui = GUI(1400, 500)


class GUI:
    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Lyrick Guesser")
        self.root.geometry(f"{self.width}x{self.height}")
        self.canvas = Canvas(self.root, width = self.width, height = self.height)
        self.canvas.pack(fill = BOTH, expand = True)
        self.create_startup_screen()
        self.root.mainloop()
        
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def create_startup_screen(self):
        img = self.imagify("Images/TS_Eras_Tour.jpg")
        self.canvas.create_image(0, 0, image = img, anchor = "nw")
        self.canvas.pack()

        ## Genuinely no idea why this is here instead of in the constructor, but the constructor somehow calls it BEFORE create_startup_screen() is finished even if pladed under create_startup_screen()????
        self.root.mainloop()
    
    def imagify(self, image_path):
        img = Image.open(image_path)
        return ImageTk.PhotoImage(img)


        


        
        


if __name__ == "__main__":
    main()




    