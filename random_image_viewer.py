import os
import random
import tkinter as tk
from PIL import Image, ImageTk
import argparse


def get_images(directory):
    supported = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
    return [os.path.join(directory, f) for f in os.listdir(directory)
            if f.lower().endswith(supported)]


class RandomImageApp(tk.Tk):
    def __init__(self, directory):
        super().__init__()
        self.title('Random Image Viewer')
        self.directory = directory
        self.label = tk.Label(self)
        self.label.pack(expand=True)
        self.images = get_images(directory)
        if not self.images:
            raise ValueError(f'No images found in {directory}')
        self.show_image()

    def show_image(self):
        path = random.choice(self.images)
        img = Image.open(path)
        # Resize to fit window while maintaining aspect ratio
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        img.thumbnail((w, h))
        photo = ImageTk.PhotoImage(img)
        self.label.configure(image=photo)
        self.label.image = photo
        self.after(15000, self.show_image)


def main():
    parser = argparse.ArgumentParser(description='Display random images from a folder every 15 seconds.')
    parser.add_argument('directory', help='Folder containing images')
    args = parser.parse_args()
    app = RandomImageApp(args.directory)
    app.mainloop()


if __name__ == '__main__':
    main()
