Counter App with Transparent Background
This is a simple desktop counter application built using Python's Tkinter library. The app features a transparent background, a "+" button to increment the counter, and a "-" button to decrement it. It also includes a "Close" button to exit the app.

Features
Transparent background.
Increment and decrement buttons.
Close button to exit the application.
Desktop widget-like experience (window without borders).
Prerequisites
Make sure you have Python and pip installed on your system.

Python 3.x
Tkinter (comes pre-installed with most Python distributions)
How to Run the App
Clone or download this repository to your local machine.
Navigate to the project folder using a terminal:
bash
Copy code
cd counter_app
Run the app with the following command:
bash
Copy code
python main.py
Running as a Standalone Executable
If you want to run the app independently (without Python or VS Code), you can package it into an executable file.

Steps to Create an Executable:
Install PyInstaller:

bash
Copy code
pip install pyinstaller
Package the App: Use the following command to convert the Python script into a standalone executable:

bash
Copy code
pyinstaller --onefile --noconsole main.py
Run the Executable: After packaging, you will find the executable in the dist/ folder:

On Windows: main.exe
On macOS/Linux: main
Double-click the executable to run the app.

Folder Structure
graphql
Copy code
counter_app/
│
├── build/          # PyInstaller build folder (auto-generated)
├── dist/           # Contains the generated executable
│   └── main.exe    # The standalone executable (on Windows)
├── main.py         # Main Python file
└── README.md       # This documentation
License
This project is open-source and free to use.
