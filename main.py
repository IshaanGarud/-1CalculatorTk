""" A simple Calculator made by Inu
Just a simple project by a Kid who broke his eye a day ago
It has in-built A.I. too!
Try it out for yourself by doing 2+2.

I dunno about Copyright....
still , Inu©

"""


from tkinter import *
import tkinter.font as font

root = Tk()
root.title("First GUI Calculator project by Inu :)")
root.geometry("690x1485")

headfont = font.Font(family="Comic Sans", size=8, weight="bold")
headline = Label(root,
             text = "A simple Calculator [12|1|22]. \n",
             fg = "green",
             font=headfont)
headline.grid(row=0, column=1)

# ----------------------------------------------------------------                       

label1 = Label(root, text="First Number:- ")                                                   
inp1 = Entry(root)
label2 = Label(root, text="Second Number:- ")                                                   
inp2 = Entry(root)

answer = Label()

def intelligence(a, b):
    if a<10 or b<10:
        answer["text"], answer["fg"], answer["font"] = "Woah Man yo Serious?,\n You can't do that simple shit?", "red", headfont
    else:
        answer["fg"] = "black"
        answer["font"] ="TkDefaultFont"
    
def Add():
    a = int(inp1.get())
    b = int(inp2.get())
    answer["text"] = a+b
    intelligence(a, b)    
def Sub():
    a = int(inp1.get())
    b = int(inp2.get())
    answer["text"] = a-b
    intelligence(a, b)   
def Mul():
    a = int(inp1.get())
    b = int(inp2.get())
    answer["text"] = a*b
    intelligence (a, b)    
def Div():
    a = int(inp1.get())
    b = int(inp2.get())
    answer["text"] = a/b
    intelligence (a, b)
def Root():
    a = int(inp1.get())
    b = int(inp2.get())
    answer["text"] = a**(1/b)
    answer["fg"], answer["font"] = "black", "TkDefaultFont"
def Pow():
    a = int(inp1.get())
    b = int(inp2.get())
    answer["text"] = a**b
    answer["fg"], answer["font"] = "black", "TkDefaultFont"

      
        

b_add = Button(root, text="+", command=Add, bg="grey")
b_sub = Button(root, text="-", command=Sub, bg="grey")
b_mul = Button(root, text="×", command=Mul, bg="grey")
b_div = Button(root, text="÷", command=Div, bg="grey")
b_root = Button(root, text="√", command=Root, bg="grey")
b_power = Button(root, text="^", command=Pow, bg="grey")

label1.grid(row=1, column=0)
inp1.grid(row=1, column=1)
label2.grid(row=2, column=0)
inp2.grid(row=2, column=1)

b_add.grid(row=3, column=0)
b_sub.grid(row=3, column=1)
b_mul.grid(row=4, column=0)
b_div.grid(row=4, column=1)
b_root.grid(row=5, column=0)
b_power.grid(row=5, column=1)

answer.grid(row=6, column=0)
 
# ----------------------------------------------------------------                       


root.mainloop()
