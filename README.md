# My Codex Project

This repository contains a simple Python program that downloads a random image
from [idiod.qabyldau.com](https://idiod.qabyldau.com) every 15 seconds and
shows it in a window. The application was designed for macOS but should work on
any platform that supports Python and Tkinter.

## Requirements

- Python 3
- Pillow, Requests and BeautifulSoup (`pip install -r requirements.txt`)

## Usage

1. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the program:

   ```bash
   python3 random_image_viewer.py
   ```

A window will open and update with a random picture from the website every 15 seconds.
