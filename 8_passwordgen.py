from tkinter import *
from tkinter import ttk
import string
import random

def generator():
    global var
    var.set("")
    e.delete(0,END)
    sm_alpha=string.ascii_lowercase
    cap_alpha=string.ascii_uppercase
    num=string.digits
    sp_char=string.punctuation

    all=sm_alpha+cap_alpha+num+sp_char
    pass_length=int(len_box.get())


    password=" "
    if com.get() == 'Low Strength':
        for i in range(0, pass_length):
            password = password + random.choice(sm_alpha+cap_alpha)
            var.set(password)

    elif com.get() == 'Medium Strength':
        for i in range(0, pass_length):
            password = password + random.choice(sm_alpha+cap_alpha+num)
            var.set(password)
    elif com.get() == 'High Strength':
        for i in range(0,pass_length):
            password = password + random.choice(all)
            var.set(password)

    e.insert(0,password)
    print(password)

root=Tk()
root.geometry('680x410')
root.config(bg="pink")
ch=IntVar()
var=StringVar()
a=('Helvetica',16,'bold')
myLabel=Label(root,text='Password Generator',font=('Times new Roman',30,'bold'),bg='pink',justify='center')
myLabel.grid(pady=25,padx=50)
com= ttk.Combobox(root,font=('Aerial',13),width=15,state='readonly')
com['values']=('Low Strength','Medium Strength','High Strength')
com.current(1)
com.place(x=250,y=97)
my_len=Label(root,text='Enter Password Length',font=a,bg='pink')
my_len.grid(padx=50,pady=30)
len_box=Spinbox(root,from_=5,to_=30,width=10,font=a,state='readonly')
len_box.grid(ipady=5,padx=50,pady=5)
gen_button=Button(root,text="Generate",font=('Helvetica',13,'bold'),command=generator)
gen_button.grid(pady=20,padx=50)
e=Entry(root,width=50,borderwidth=10,font=15)
e.grid(padx=50,pady=15)
root.mainloop()