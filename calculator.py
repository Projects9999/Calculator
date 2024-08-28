from tkinter import *

def btnclick(number):
    global val
    val=val + str(number)
    data.set(val)
def btn_clr():
    global val
    val=""
    data.set("")
def btn_eql():
    global val

    try:
        result=str(eval(val))

    except Exception as error:
        print("error")
        data.set("Error")
    result = str(eval(val))
    data.set(result)






root=Tk()

root.title("Dhruv's calculator")
root.geometry('361x381+500+200')
data=StringVar()
val=""
display=Entry(root,bd=29,textvariable=data,bg="grey",justify="right", font=("ariel",20))
display.grid(row=0,columnspan=4)
btn7=Button(root,text="7",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(7))
btn7.grid(row=1,column=0)
btn8=Button(root,text="8",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(8))
btn8.grid(row=1,column=1)
btn9=Button(root,text="9",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(9))
btn9.grid(row=1,column=2)
btn_add=Button(root,text="+",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick('+'))
btn_add.grid(row=1,column=3)

#next row
btn4=Button(root,text="4",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(4))
btn4.grid(row=2,column=0)
btn5=Button(root,text="5",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(5))
btn5.grid(row=2,column=1)
btn6=Button(root,text="6",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(6))
btn6.grid(row=2,column=2)
btn_sub=Button(root,text="-",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick('-'))
btn_sub.grid(row=2,column=3)

#new row
btn1=Button(root,text="1",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(1))
btn1.grid(row=3,column=0)
btn2=Button(root,text="2",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(2))
btn2.grid(row=3,column=1)
btn3=Button(root,text="3",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(3))
btn3.grid(row=3,column=2)
btn_mul=Button(root,text="X",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick('*'))
btn_mul.grid(row=3,column=3)

#next raw
btn_c=Button(root,text="c",font=("Ariel",12,"bold"),bg="grey",bd=12,height=2,width=6,command=btn_clr)
btn_c.grid(row=4,column=0)
btn0=Button(root,text="0",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(0))
btn0.grid(row=4,column=1)
btn_div=Button(root,text="÷",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick('/'))
btn_div.grid(row=4,column=2)
btn_eql=Button(root,text="=",font=("Ariel",12,"bold"),bg="grey",bd=12,height=2,width=6,command=btn_eql)
btn_eql.grid(row=4,column=3)




mainloop()
