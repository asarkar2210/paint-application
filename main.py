from tkinter import * ;

root = Tk() 
root.title("Paint")
root.geometry("1100x600")

strokeSize = IntVar()
options = [1,2,3,4,5,6,7,8,9,10]
strokeColor = StringVar()
strokeColor.set("black")
prevPoint = [0,0]
currPoint = [0,0]

def usePencil ():
    strokeColor.set("black")
    canvas["cursor"] = "arrow"
    

def useEraser () :
    strokeColor.set("white")
    canvas["cursor"] = DOTBOX

def paint(event): 
    global prevPoint, currPoint
    x = event.x
    y = event.y
    currPoint = [x,y]
    
    #canvas.create_oval(x, y, x+20, y+20, fill="black")
    if prevPoint != [0,0]:
        canvas.create_polygon(prevPoint[0], prevPoint[1], currPoint[0], currPoint[1], fill=strokeColor.get(),outline=strokeColor.get(), width=strokeSize.get())

    prevPoint = currPoint
    
    if event.type == "5":
        prevPoint=[0,0]

frame1 = Frame(root, height=100, width=11)
frame1.grid(row=0, column=0, sticky=NW)

toolsFrame = Frame (frame1, height=100, width=100)
toolsFrame.grid(row=0, column=0)

pencilButton = Button(toolsFrame, text="Pencil", width=10, command=usePencil)
pencilButton.grid(row=0, column=0)

eraserButton = Button(toolsFrame, text="Eraser", width=10, command=useEraser)
eraserButton.grid(row=1, column=0)

toolsLabel = Label(toolsFrame, text="Tools", width=10)
toolsLabel.grid(row=2, column=0)

sizeFrame = Frame (frame1, height=100, width=100)
sizeFrame.grid(row=0, column=1)

defaultButton = Button(sizeFrame, text="Default", width=10, command=usePencil)
defaultButton.grid(row=0, column=0)


sizeList = OptionMenu(sizeFrame, strokeSize, *options)
sizeList.grid(row=1, column=0)

sizeLabel = Label(sizeFrame,text="Size", width=10)
sizeLabel.grid(row=2, column=0)


frame2 = Frame(root, height=500, width=1100)
frame2.grid(row=1, column=0)

canvas = Canvas(frame2, height=500, width=1100, bg="white")
canvas.grid(row=0, column=0)
    
canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", paint)

root.resizable(False , False)
root.mainloop()