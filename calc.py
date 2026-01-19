from tkinter import *

window=Tk()
window.title("calculator")
window.geometry("395x440+100+100")
window.resizable(False,False)
window.configure(bg="#8095D8")
exp=StringVar()
res=StringVar()
ex=""
def add(n):
    if n=="=":
        res.set(eval(ex))
        globals()['ex']=""
    else:
        globals()['ex']+=n
    exp.set(ex)
Label(window,textvariable=exp,width=53,height=2).place(x=12,y=12)
Label(window,textvariable=res,width=53,height=3,
      bg="#FFFFFF").place(x=12,y=52)

Button(window,text="9",font=("Arial",16,"bold"),fg="#FFFFFF",
       width=6,height=2,bg="#C4C7AB",command=lambda:add("9")).place(x=12,y=108)
Button(window,text="8",font=("Arial",16,"bold"),fg="#FFFFFF",
       width=6,height=2,bg="#C4C7AB",command=lambda:add("8")).place(x=106,y=108)
Button(window,text="7",font=("Arial",16,"bold"),fg="#FFFFFF",
       width=6,height=2,bg="#C4C7AB",command=lambda:add("7")).place(x=200,y=108)
Button(window,text="/",font=("Arial",16,"bold"),fg="#FFFFFF",
       width=6,height=2,bg="#D398C1",command=lambda:add("/")).place(x=295,y=108)

Button(window,text="6",font=("Arial",16,"bold"),fg="#FFFFFF",
       width=6,height=2,bg="#C4C7AB",command=lambda:add("6")).place(x=12,y=180)
Button(window,text="5",font=("Arial",16,"bold"),fg="#FFFFFF",
       width=6,height=2,bg="#C4C7AB",command=lambda:add("5")).place(x=106,y=180)
Button(window,text="4",font=("Arial",16,"bold"),fg="#FFFFFF",
       width=6,height=2,bg="#C4C7AB",command=lambda:add("4")).place(x=200,y=180)
Button(window,text="*",font=("Arial",16,"bold"),fg="#FFFFFF",
       width=6,height=2,bg="#D398C1",command=lambda:add("*")).place(x=295,y=180)

Button(window,text="3",font=("Arial",16,"bold"),fg="#FFFFFF",
       width=6,height=2,bg="#C4C7AB",command=lambda:add("3")).place(x=12,y=252)
Button(window,text="2",font=("Arial",16,"bold"),fg="#FFFFFF",
       width=6,height=2,bg="#C4C7AB",command=lambda:add("2")).place(x=106,y=252)
Button(window,text="1",font=("Arial",16,"bold"),fg="#FFFFFF",
       width=6,height=2,bg="#C4C7AB",command=lambda:add("1")).place(x=200,y=252)
Button(window,text="-",font=("Arial",16,"bold"),fg="#FFFFFF",
       width=6,height=2,bg="#D398C1",command=lambda:add("-")).place(x=295,y=252)

Button(window,text="c",font=("Arial",16,"bold"),fg="#FFFFFF",
       width=6,height=2,bg="#D398C1",command=lambda:add("c")).place(x=12,y=324)
Button(window,text="0",font=("Arial",16,"bold"),fg="#FFFFFF",
       width=6,height=2,bg="#C4C7AB",command=lambda:add("0")).place(x=106,y=324)
Button(window,text="=",font=("Arial",16,"bold"),fg="#FFFFFF",
       width=6,height=2,bg="#D398C1",command=lambda:add("=")).place(x=200,y=324)
Button(window,text="+",font=("Arial",16,"bold"),fg="#FFFFFF",
       width=6,height=2,bg="#D398C1",command=lambda:add("+")).place(x=295,y=324)
window.mainloop()
