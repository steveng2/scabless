# The GUI app for windows.
# loads in data from files
# please read readme.md
# design by steven garner
#


# fileing style for GUI eg file open, save as

from tkinter import *
def mainFunction():
   filewin = Toplevel(root)
   button = Button(filewin, text="Buton")
   button.pack()
def helpFunction():
    filewin = Toplevel(root)
    button = Button(filewin, text="Help")
    button = Button(filewin, text="Readme")
    print("This is where you read the reedme file")
    button.pack()


root = Tk()
menubar = Menu(root)
#main file navi
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=mainFunction)
filemenu.add_command(label="Open", command=mainFunction)
filemenu.add_command(label="Save", command=mainFunction)
filemenu.add_command(label="Save as...", command=mainFunction)
filemenu.add_command(label="Close", command=mainFunction)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=mainFunction)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=mainFunction)
editmenu.add_command(label="Copy", command=mainFunction)
editmenu.add_command(label="Paste", command=mainFunction)
editmenu.add_command(label="Delete", command=mainFunction)
editmenu.add_command(label="Select All", command=mainFunction)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=helpFunction)
helpmenu.add_command(label="About...", command=helpFunction)
menubar.add_cascade(label="Help", menu=helpmenu)

#dashboard where the entries words will go
root.config(menu=menubar)

#form entry for entrywords
entrywords= ['re','ed','ing','ies']
r = 0

for c in entrywords:
        Label(text=c, relief=RIDGE,width=15).grid(row=r,column=0)
        Entry(relief=SUNKEN,width=10).grid(row=r,column=1)
        r = r + 1

master = Tk()

def callback():
    print ("click!")

b = Button(master, text="OK", command=callback)
b.pack()

root.mainloop()
