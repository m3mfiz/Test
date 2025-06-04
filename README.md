# My Codex Project

This repository contains a simple Python program that displays a random image
from a specified folder every 15 seconds. The application was designed for
macOS but should work on any platform that supports Python and Tkinter.

## Requirements

- Python 3
- Pillow (`pip install -r requirements.txt`)
- Flask

## Usage

1. Place some images in a directory on your computer.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the program, passing the directory that contains your images:

   ```bash
   python3 random_image_viewer.py /path/to/your/images
   ```

A window will open and update with a random picture every 15 seconds.

## Login Page

This repository also includes a simple web server that serves `login.html` and
checks a hard-coded username and password. To run the server:

```bash
python3 server.py
```

Visit `http://localhost:5000` in your browser to see the login form. The
default credentials are `admin` / `secret`.
