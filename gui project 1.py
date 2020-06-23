from tkinter import *
from PIL import Image,ImageTk






win=Tk()
win.title("Iage Viewer")
win.geometry("600x400")

#Labell infor



ll=Label(text="enter x_exis pixel", font=" Arial 20 bold")
ll.place(x=100,y=100)
# Label for y axis
ll1=Label(text="enter y exis pixel",  font=" Arial 20 bold")
Label(text="your image path", font=" Arial 20 bold").place(x=100,y=50)
ll1.place(x=100,y=160)


#Entry info




ent=Entry(textvariable=IntVar(),width=30)
ent.place(x=350,y=110)
ent2=Entry(textvariable=IntVar(),width=30)
ent2.place(x=350,y=170)
ent3=Entry(textvariable=StringVar(),width=30)
ent3.place(x=350,y=60)


def click():
    global img5
    top=Toplevel()
    img=Image.open("2.jpg")
    img5=img.resize((int(ent.get()),int(ent2.get())))
    img5=ImageTk.PhotoImage(img5)
   

    lab=Label(top,image=img5,bd=2)
    lab.pack()
   
    

    

but=Button(text="Image Viwe ",bg="gray",font =" Arial 10 bold",command=click,width=50,height=2)
but.place(x=150,y=220)

win.mainloop()
 
