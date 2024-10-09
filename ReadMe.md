# Pinned Counter App 

This is a simple desktop counter application built using Python's Tkinter library. The app features a transparent background, a "+" button to increment the counter, and a "-" button to decrement it. It also includes a "Close" button to exit the app.

## Features
- Desktop widget-like experience (window without borders).
- Pinned app.
- Increment and decrement buttons.
- Close button to exit the application.

## uses
you can use the app for following </br>
- 1. Use the counter to keep track of tasks completed or actions performed throughout the day.
- 2. Count daily habits (e.g., number of glasses of water consumed, hours spent reading).
- 3. Use the app to count the days until a specific event (like a birthday or holiday).
- 4. Maintain score for games played with friends or family.

## Prerequisites
Make sure you have Python and pip installed on your system.

- Python 3.x
- Tkinter (comes pre-installed with most Python distributions)

## How to Run the App
1. Clone or download this repository to your local machine.
2. Navigate to the project folder using a terminal:

    ```bash
    cd counter_app
    ```

3. Run the app with the following command:

    ```bash
    python main.py
    ```

## Running as a Standalone Executable
If you want to run the app independently (without Python or VS Code), you can package it into an executable file.

### Steps to Create an Executable:
1. Install PyInstaller:

    ```bash
    pip install pyinstaller
    ```

2. Package the App: Use the following command to convert the Python script into a standalone executable:

    ```bash
    pyinstaller --onefile --noconsole main.py
    ```

3. Run the Executable: After packaging, you will find the executable in the `dist/` folder:

    - On Windows: `main.exe`
    - On macOS/Linux: `main`
    
   Double-click the executable to run the app.

## Folder Structure
```plaintext
counter_app/
│
├── build/          # PyInstaller build folder (auto-generated)
├── dist/           # Contains the generated executable
│   └── main.exe    # The standalone executable (on Windows)
├── main.py         # Main Python file
└── README.md       # This documentation

```
## License
This project is open-source and free to use.
```


 
 
