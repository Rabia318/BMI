from tkinter import *
import math
window=Tk()


def counting_bmı():
    x=float(my_spinbox_1.get())
    a=(float(my_spinbox_2.get()))/100
    if x==0:
        print("Rest In Peace")
    if a>2.5:
        print("Are you Sultan KOSE?,Try again please :)")
    y=pow(a,2)
    bmı_value=( x /y)
    print(int(bmı_value))
    if x>0 and a<2.5:

        if bmı_value<18.5:
            print("Underweight")
        if bmı_value>18.5 and bmı_value<24.9:
            print("Normal")
        if bmı_value>25 and bmı_value<29.9:
            print("Overweigth")
        if bmı_value>30 and bmı_value<34.9:
            print("Obeze")
        if bmı_value>35 :
            print("Extremly obeze")

window.title("BMI COUNTER")
window.config(bg="cyan")
window.minsize(width=200,height=150)
window.config(padx=40,pady=40)
label_1=Label(text="Please enter your weight:")
label_1.grid(row=3,column=0)

my_spinbox_1=Spinbox(from_=0, to=250)
my_spinbox_1.grid(row=5,column=0)

label_2=Label(text="Please enter your height:")
my_spinbox_2=Spinbox(from_=0,to=250)

label_2.grid(row=3,column=2)
my_spinbox_2.grid(row=5,column=2)

counting_button=Button(text="Count",bg="MediumPurple1",fg="black",command=counting_bmı,width=20)
counting_button.grid(row=12,column=1)



window.mainloop()




