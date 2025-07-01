import tkinter as tk
import time

stackSource = []
stackAuxiliary = []
stackDestination = []

#Moves disk from source to destination
def moveDisk(source, destination):
    disk = source.pop() #remove disk from source
    destination.append(disk) #place disk on destination
    root.update() #update the UI 
    updateDisplay() #draw the disks
    time.sleep(.750)#wait 750 milliseconds

#Algorithm to move the disks
def towerOfHanoi(n, source, auxiliary, destination):
    if n == 1:  #base case bottom most element
        moveDisk(source, destination)
    else:
        towerOfHanoi(n-1, source, destination, auxiliary) #Move the top n−1 disks from the source rod to the auxiliary rod.
        moveDisk(source, destination)                     #Move the largest disk from the source rod to the destination rod.
        towerOfHanoi(n-1, auxiliary, source, destination) #Move the n−1 disks from the auxiliary rod to the destination rod.

#startup function that initializes stuff when the start button gets pressed
def start():
    global numberOfDisks #total number of disks
    numberOfDisks = userInput.get() #makes the number of stacks equal to the number in the text box
    if numberOfDisks.isdigit(): 
        numberOfDisks = int(numberOfDisks) #convert to integer
        if numberOfDisks < 1:
            print("Please input a positive n")
            return #exit function
        else:
            print("The inputted Number of disks n =", numberOfDisks)
    else:
        print("Please print a number")
        return #exit function
    newStack(numberOfDisks) #declare a new stack
    towerOfHanoi(numberOfDisks, stackSource,  stackAuxiliary, stackDestination)

def newStack(n):
    #clear all stacks
    stackSource.clear()
    stackAuxiliary.clear()
    stackDestination.clear()

    #add elements to source stack
    for i in range(n, 0, -1): #start at the max size (n) and loop to 1
        stackSource.append(i) #place largest n at bottom of stack
    updateDisplay()

def drawDisks(canvas, stack):
    #clears the canvas
    canvas.delete("all")
    #finds canvasWidth and height
    canvasWidth = canvas.winfo_width()
    canvasHeight = canvas.winfo_height()

    #gets the middle of the canvas for the rod
    canvasMiddle = int(canvasWidth/2)
    
    #creates a line for the rod
    canvas.create_line(canvasMiddle, 0, canvasMiddle, canvasHeight) 
    
    #Expressions for dynamically scaling the disk height with a max and min height
    if (canvasHeight / numberOfDisks > 20):
        diskHeight = 20 #maximum disk height
    elif(canvasHeight / numberOfDisks < 4):
        diskHeight = 4 #minimum disk height
    else:
        diskHeight = int(canvasHeight/numberOfDisks) #dynamic scaling disk height

    for index, size in enumerate(stack): #starts from the largest disk and builds upwards

        diskWidth = size*20

        x1 = canvasMiddle - diskWidth / 2
        x2 = canvasMiddle + diskWidth / 2

        y2= canvasHeight-diskHeight*index
        y1 = y2 - diskHeight
       # print(index)
        canvas.create_rectangle(x1, y1, x2, y2, fill="purple")
    return

def updateDisplay():
    try:
        #draws the disks in the UI for each stack
        drawDisks(canvasSource, stackSource)
        drawDisks(canvasAuxiliary, stackAuxiliary)
        drawDisks(canvasDestination, stackDestination)
    except tk.TclError: 
        pass #this error will occur if you close the window while the program is running so its just to ignore those errors

#setup the main widget window
root = tk.Tk() #creates the window to display the stacks
root.title("Tower of Hanoi") #sets the title of the window
root.geometry("900x400") #sets the size of the window for the stacks

root.columnconfigure([0,1,2], weight=1, uniform="Columns")
root.rowconfigure(1, weight=1, uniform="Rows")

#setups user input box
userInput = tk.Entry(root, borderwidth=3, relief="solid") #gets the input of whatever is placed in the input text box
userInput.grid(row=0, column=0, sticky="ew")

#setups start button
startBtn = tk.Button(root, text="Start", command=start)
startBtn.grid(row=0, column=1, columnspan=2, sticky="ew")

#setups canvases to be a widget of root
canvasSource = tk.Canvas(root, bg="blue", highlightthickness=0)
canvasAuxiliary = tk.Canvas(root, bg="red", highlightthickness=0)
canvasDestination = tk.Canvas(root, bg="green", highlightthickness=0)

#setups canvases in their designated grid
canvasSource.grid(row=1, column=0, sticky="nesw")
canvasAuxiliary.grid(row=1, column=1, sticky="nesw")
canvasDestination.grid(row=1, column=2, sticky="nesw")

root.mainloop()