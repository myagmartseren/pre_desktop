from tkinter import * 

def onObjectClick1(event):
    print("1")
    canv.itemconfig(obj1, image=my_pic2)
    canv.tag_bind(obj1, '<Leave>', onObjectClick2)     

def onObjectClick2(event):
    print("2")
    canv.itemconfig(obj1, image=my_pic1)
    canv.tag_bind(obj1, '<Enter>', onObjectClick1)        
    
root = Tk()    
canv = Canvas(root, width=300, height=300)
my_pic1 = PhotoImage(file="./assets/frames/frame3/button_1.png")
my_pic2 = PhotoImage(file="./assets/frames/frame3/button_2.png")

obj1 = canv.create_image(50,50,image=my_pic1, anchor=NW)
canv.tag_bind(obj1, '<Enter>', onObjectClick1)        
canv.tag_bind(obj1, '<Leave>', onObjectClick2)        
canv.pack()

root.mainloop()