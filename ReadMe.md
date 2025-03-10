# Pinned Counter App 

This is a simple desktop counting application built using Python's Tkinter library. The app features a gray background, a "+" button to increment the counter, and a "-" button to decrement it. It is pinned on screen and you and do other work while this is on and it will be pinned on screen.

![preview](https://i.ibb.co/HNSGpbT/image.png)

## Features
- Desktop widget-like experience (window without borders).
- Pinned app.
- Increment and decrement buttons.

## uses
you can use the app for following </br>
- Use the counter to keep track of tasks completed or actions performed throughout the day.
- Count daily habits (e.g., number of glasses of water consumed, hours spent reading).
- Use the app to count the days until a specific event (like a birthday or holiday).
- Maintain score for games played with friends or family.

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

## future plans 
Here are some wildly ambitious and totally realistic plans for enhancing the Counter App (because why not dream big?)

- Allow users to change the background color and font style of the counter display for a personalized experience.
- Implement functionality to manage multiple counters within the same app, allowing users to track different activities simultaneously. (Let’s implement multiple counters so you can track everything from how many cups of coffee you’ve had to how many times you’ve procrastinated today.)
- Implement keyboard shortcuts for incrementing and decrementing the counter for quicker access without needing to click buttons.
- Introduce a dark mode option to reduce eye strain, particularly useful for users who work in low-light environments.
- Implement a feedback mechanism for users to suggest new features or report issues, ensuring continuous improvement based on user needs.
 

## License
This project is open-source and free to use.


 
 
