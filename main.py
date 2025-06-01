from tkinter import * ;

root = Tk() 
root.title("Paint")
root.geometry("1100x600")

frame1 = Frame(root, height=100, width=1100, bg="red")
frame1.grid(row=0, column=0)

frame2 = Frame(root, height=500, width=1100, bg="yellow")
frame2.grid(row=1, column=0)

canvas = Canvas(frame2, height=500, width=1100, bg="white")
canvas.grid(row=0, column=0)

prevPoint = [0,0]
currPoint = [0,0]

def paint(event): 
    global prevPoint, currPoint
    x = event.x
    y = event.y
    currPoint = [x,y]
    
    #canvas.create_oval(x, y, x+20, y+20, fill="black")
    if prevPoint != [0,0]:
        canvas.create_line(prevPoint[0], prevPoint[1], currPoint[0], currPoint[1])

    prevPoint = currPoint
    
    if event.type == "5":
        prevPoint=[0,0]
    
canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", paint)

root.resizable(False , False)
root.mainloop()