import io
import random
import tkinter as tk
from PIL import Image, ImageTk
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


SOURCE_URL = 'https://idiod.qabyldau.com'


def fetch_image_urls():
    """Retrieve image URLs from the SOURCE_URL page."""
    resp = requests.get(SOURCE_URL)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')
    supported = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
    urls = []
    for img in soup.find_all('img'):
        src = img.get('src')
        if not src:
            continue
        if src.lower().endswith(supported):
            urls.append(urljoin(SOURCE_URL, src))
    return urls


class RandomImageApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Random Image Viewer')
        self.label = tk.Label(self)
        self.label.pack(expand=True)
        self.images = fetch_image_urls()
        if not self.images:
            raise ValueError(f'No images found at {SOURCE_URL}')
        self.show_image()

    def show_image(self):
        url = random.choice(self.images)
        resp = requests.get(url)
        resp.raise_for_status()
        img = Image.open(io.BytesIO(resp.content))
        # Resize to fit window while maintaining aspect ratio
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        img.thumbnail((w, h))
        photo = ImageTk.PhotoImage(img)
        self.label.configure(image=photo)
        self.label.image = photo
        self.after(15000, self.show_image)


def main():
    """Start the random image viewer."""
    app = RandomImageApp()
    app.mainloop()


if __name__ == '__main__':
    main()
