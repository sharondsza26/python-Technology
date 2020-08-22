from tkinter import *

# Main Window
root = Tk()
root.geometry("415x415")
root.title("Chat Client")

#Subbordinate
taData = StringVar()
taData.set("")

#Label added to the Main Window
ta = Label(root, textvariable=taData)
ta.pack()

#Creating Panel and adding it to the MainWindow
p1 = Frame(root)

#Creating TextBox,Button and Adding it to the Panel
tf = Entry(p1)
send = Button(p1,text="Send")
tf.pack(side="left")
send.pack(side="left")

#Event handler
def printMessage(event):
    global tf
    message = tf.get()
    taData.set("{} \n {}".format(taData.get(),message))
    tf.delete(0,END)

#Adding Event Handler to the Button
send.bind("<Button>", printMessage)
p1.pack()
root.mainloop()