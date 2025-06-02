
![Screenshot 2025-06-02 150719](https://github.com/user-attachments/assets/4fd4e513-2708-45d5-981d-af2d9c29ce6c)

# Paint App

A simple desktop drawing application built with Python’s Tkinter library. Draw freehand with customizable brush sizes and colors, erase, add text, and save your creations as images.
> This was submitted as my final project for Stanford Code in Place 2025

## Features

- Freehand drawing with left-click and drag  
- Dotted lines with right-click and drag  
- Custom brush size slider (1–35 px)  
- Quick-pick color palette and “More Colors” picker  
- “Previous” and “Previous2” buttons to recall last two colors  
- Eraser tool that matches the current canvas background  
- Add text via middle-click (scroll wheel click)  
- New, Clear, Save (saves screenshot of the drawing area)  
- About and Help dialogs  

## Table of Contents

- Installation  
- Usage  
- File Structure  
- Known Issues  
- Contributing  
- License  

## Installation

1. Make sure you have Python 3.6+ installed on Windows.  
2. Clone this repository:

   ```bash
   git clone https://github.com/your-username/paint-application.git
   cd paint-application
   ```

3. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

4. Install dependencies:

   ```bash
   pip install pillow
   ```

## Usage

Run the main script:

```bash
python main.py
```

The UI will open with two main sections:

- **Top toolbar** (tools, size slider, color palette, text input, etc.)  
- **Canvas** (draw area below)

Controls:

- Left-click & drag: freehand drawing  
- Right-click & drag: dotted strokes  
- Middle-click: place text (enter text in the input field first)  
- “More Colors”: pick a custom color dialog  
- “Previous” / “Previous2”: recall last two used colors  
- “Save”: saves the canvas as a `.jpg` (requires Pillow’s ImageGrab)  
- “New”: prompts to save, then clears canvas  
- “Clear”: clears without saving  

## File Structure

```
paint-application/
├── main.py            # Application entry point
├── README.md          # This file
└── (future assets…)   # e.g. icons, presets, etc.
```

## Known Issues

- The **Save** feature uses `ImageGrab.grab` on the application window; results may vary if the window is obscured.  
- On multi-monitor setups, coordinates may need adjustment.  
- The default save format is JPEG; transparency is not supported.  

## License

This project is provided under the MIT License. See LICENSE for details.
