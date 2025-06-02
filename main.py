from tkinter import *
from tkinter import colorchooser
import PIL.ImageGrab as ImageGrab
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title("Paint App")
root.geometry("1100x600")

# All variables
options = [1, 2, 3, 4, 5, 10]
stroke_size = IntVar()
stroke_size.set(1)

stroke_color = StringVar()
stroke_color.set("black")
eraser_color = "white"

previousColor = StringVar()
previousColor.set("white")
previousColor2 = StringVar()
previousColor2.set("white")

prevPoint = [0, 0]
currentPoint = [0, 0]

textValue = StringVar()

# All Functions
def update_recent_colors(new_color):
    previousColor2.set(previousColor.get())
    previousColor.set(new_color)
    stroke_color.set(new_color)
    previousColorButton.config(bg=previousColor.get())
    previousColor2Button.config(bg=previousColor2.get())

def usePencil():
    stroke_color.set("black")
    canvas["cursor"] = "arrow"

def useEraser():
    stroke_color.set(eraser_color)
    canvas["cursor"] = "dotbox"

def selectColor():
    sel = colorchooser.askcolor(initialcolor=stroke_color.get(),
                                title="Select Color")
    color_hex = sel[1] or "black"
    update_recent_colors(color_hex)

def paint(event):
    global prevPoint, currentPoint
    x, y = event.x, event.y
    currentPoint = [x, y]
    if prevPoint != [0, 0]:
        canvas.create_polygon(
            prevPoint[0], prevPoint[1],
            currentPoint[0], currentPoint[1],
            fill=stroke_color.get(),
            outline=stroke_color.get(),
            width=penSize.get()
        )
    prevPoint = currentPoint
    if event.type == "5":  # mouse button release
        prevPoint = [0, 0]

def paintRight(event):
    x, y = event.x, event.y
    canvas.create_arc(
        x, y,
        x + stroke_size.get(), y + stroke_size.get(),
        fill=stroke_color.get(),
        outline=stroke_color.get(),
        width=stroke_size.get()
    )

# Known bug
def saveImage():
    try:
        fileLocation = filedialog.asksaveasfilename(defaultextension=".jpg")
        x = root.winfo_rootx()
        y = root.winfo_rooty()+100
        #print(x,y)
        img = ImageGrab.grab(bbox=(x,y,x+1100,y+500))
        img.save(fileLocation)
        showImage = messagebox.askyesno("Paint App", "Do you want to open image?")
        if showImage:
            img.show() 
            pass
    except Exception as e:
        messagebox.showinfo("Paint App", "Error occurred")
        print(e)

def clear():
    if messagebox.askokcancel("Paint App", "Do you want to clear everything?"):
        canvas.delete("all")

def createNew():
    if messagebox.askyesno("Paint App", "Save before clearing?"):
        saveImage()
    clear()

def help():
    helpText = (
        "1. Draw by holding left button to draw.\n"
        "2. Right button for dotted lines.\n"
        "3. Scroll-click to add text.\n"
        "4. 'More Colors' to pick a color.\n"
        "5. 'Clear' to clear canvas."
    )
    messagebox.showinfo("Help", helpText)

def about():
    messagebox.showinfo(
        "About",
        "This Paint App was created by Ayushman Sarkar for CIP 2025."
    )

def writeText(event):
    canvas.create_text(event.x, event.y, text=textValue.get())

def canvas_color():
    col = colorchooser.askcolor()[1]
    if col:
        canvas.config(background=col)
        global eraser_color
        eraser_color = col

# UI Elements

# Frame 1 (Tools Bar)
frame1 = Frame(root, height=100, width=1100)
frame1.grid(row=0, column=0, sticky=NW)

# Tools Frame
toolsFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3)
toolsFrame.grid(row=0, column=0)

Button(toolsFrame, text="Pencil", width=10, command=usePencil).grid(row=0, column=0)
Button(toolsFrame, text="Eraser", width=10, command=useEraser).grid(row=1, column=0)
Label(toolsFrame, text="Tools", width=10).grid(row=3, column=0)

# Size Scale
pen_size_scale_frame = LabelFrame(frame1, text="Size", bd=5, bg="white", relief=SUNKEN)
pen_size_scale_frame.grid(row=0, column=4)
penSize = Scale(pen_size_scale_frame, orient=HORIZONTAL,
                from_=1, to=35, length=170)
penSize.grid(row=0, column=1, padx=15)
penSize.set(5)

# Quick-pick Colors
colorsFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3)
colorsFrame.grid(row=0, column=2)
colors = [
    "#ff0000", "#ff4dd2", "#ffff33", "#000000", "#0066ff", "#ffffff",
    "#4dff4d", "#b300b3", "#00ffff", "#808080", "#99ffcc",
    "#336600", "#ff9966", "#ff99ff",
]
i = j = 0
for c in colors:
    Button(
        colorsFrame,
        bg=c, bd=2, relief=RIDGE,
        height=2, width=5,
        command=lambda col=c: update_recent_colors(col)
    ).grid(row=i, column=j)
    j += 1
    if j == 6:
        i, j = 1, 0

# More Colors & Previous
colorBoxFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3)
colorBoxFrame.grid(row=0, column=3)

Button(colorBoxFrame, text="More Colors", width=10, command=selectColor)\
    .grid(row=0, column=0)

previousColorButton = Button(
    colorBoxFrame,
    text="Previous", width=10,
    bg=previousColor.get(),
    command=lambda: stroke_color.set(previousColor.get())
)
previousColorButton.grid(row=1, column=0)

previousColor2Button = Button(
    colorBoxFrame,
    text="Previous2", width=10,
    bg=previousColor2.get(),
    command=lambda: stroke_color.set(previousColor2.get())
)
previousColor2Button.grid(row=2, column=0)

# Save/New/Clear
saveImageFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3)
saveImageFrame.grid(row=0, column=5)
Button(saveImageFrame, text="Save", width=10, command=saveImage)\
    .grid(row=0, column=0)
Button(saveImageFrame, text="New", width=10, command=createNew)\
    .grid(row=1, column=0)
Button(saveImageFrame, text="Clear", width=10, command=clear)\
    .grid(row=2, column=0)

# Help/About/Canvas Color
helpSettingFrame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3)
helpSettingFrame.grid(row=0, column=6)
Button(helpSettingFrame, text="Help", width=10, command=help)\
    .grid(row=0, column=0)
Button(helpSettingFrame, text="Canvas Color", width=10, command=canvas_color)\
    .grid(row=1, column=0)
Button(helpSettingFrame, text="About", width=10, command=about)\
    .grid(row=2, column=0)

# Text Entry
textFrame = Frame(frame1, height=100, width=200, relief=SUNKEN, borderwidth=3)
textFrame.grid(row=0, column=7)
Label(textFrame, text="Write your Text here:", width=20)\
    .grid(row=0, column=0)
Entry(textFrame, textvariable=textValue, width=20)\
    .grid(row=1, column=0)
Button(textFrame, text="Clear", width=20,
       command=lambda: textValue.set("")).grid(row=2, column=0)

# Frame 2 (Canvas)
frame2 = Frame(root, height=500, width=1100)
frame2.grid(row=1, column=0)
canvas = Canvas(frame2, height=500, width=1100, bg="white")
canvas.grid(row=0, column=0)

canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", paint)
canvas.bind("<B3-Motion>", paintRight)
canvas.bind("<Button-2>", writeText)

root.resizable(False, False)
root.mainloop()