from tkinter import *
root=Tk()
root.title("login app")
root.geometry("400x400")
frame=Frame(root,bg="lightblue", height=200, width=360)
lbl1=Label(frame,text="full name",bg="blue",fg="white",width=12)
lbl2=Label(frame,text="email",bg="blue",fg="white",width=12)
lbl3=Label(frame,text="password",bg="blue",fg="white",width=12)
name_entry=Entry(frame)
email_entry=Entry(frame)
password_entry=Entry(frame,show="*")
def display():
    name=name_entry.get()
    greet= "Hello "+name
    message="\ncongratulations! for your new account"
    textbox.insert(END,greet)
    textbox.insert(END,message)
textbox=Text(bg="#BEBEBE", fg="black")
btn = Button(text = "Create Account", command=display, bg="red")

# Arrange all widgets
frame.place(x=20,y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
password_entry.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)

# Start the GUI event loop
root.mainloop()