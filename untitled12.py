from tkinter import *
import tkinter

root = Tk()
root.title("bonk")
root.geometry("600x400")
car1 = Label(root)
mexico1 = Label(root)
plane1 = Label(root)
duck1 = Label(root)
bird1 = Label(root)
car1.place(relx=0.5,rely=0.35,anchor=CENTER)
mexico1.place(relx=0.5,rely=0.4,anchor=CENTER)
plane1.place(relx=0.5,rely=0.45,anchor=CENTER)
duck1.place(relx=0.5,rely=0.5,anchor=CENTER)
bird1.place(relx=0.5,rely=0.55,anchor=CENTER)
dictionary={
'car':'a vehicle that flies',
'mexico':'a state',    
'plane':'a type of bird',
'duck':'a type of bird',
'bird':'a type of duck'
}
print(dictionary)
def car():
    car1["text"]=dictionary["car"]    
def mexico():
    mexico1["text"]=dictionary["mexico"]    
def plane():
    plane1["text"]=dictionary["plane"]
def duck():
    duck1["text"]=dictionary["duck"]
def bird():
    bird1["text"]=dictionary["bird"]
car=Button(root,text="define car",command=car)
mexico=Button(root,text="define mexico",command=mexico)
plane=Button(root,text="define plane",command=plane)
duck=Button(root,text="define duck",command=duck)
bird=Button(root,text="define bird",command=bird)
car.place(relx=0.5,rely=0.1,anchor=CENTER)
mexico.place(relx=0.5,rely=0.15,anchor=CENTER)
plane.place(relx=0.5,rely=0.2,anchor=CENTER)
duck.place(relx=0.5,rely=0.25,anchor=CENTER)
bird.place(relx=0.5,rely=0.3,anchor=CENTER)
root.mainloop()
        
    