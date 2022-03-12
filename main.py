""" A simple Calculator made by Inu
Just a simple project by a Kid who broke his eye a day ago
It has in-built A.I. too!
Try it out for yourself by doing 2+2.

I dunno about Copyright....
still , Inu©

"""


from tkinter import *
import tkinter.font as font
import math
import time
from time import strftime
 

root = Tk()
root.title("First GUI Calculator project by Inu :)")
root.geometry("690x1485")


headfont = font.Font(family="Comic Sans", size=8, weight="bold")
headline = Label(root,
             text = "A simple Calculator [12|1|22]. \n",
             fg = "green",
             font=headfont)
headline.grid(row=0, column=0)

# ----------------------------------------------------------------                       

label1 = Label(root, text="First Number:- ")                                                   
inp1 = Entry(root)
label2 = Label(root, text="Second Number:- ")                                                   
inp2 = Entry(root)

answer = Label()
wisdom = Label()


#---------------Clock/Watch-----------------------------
clock = Label(fg="green", font=headfont, bg="#BFFF00")   
def time():
    string = strftime('%H:%M:%S %p')
    clock.config(text = string)                             
    clock.after(1000, time)
 
clock.grid(row=0, column=1)
time()


#--------*Extra Functions*------------------------------------
def NullSafe(n1, n2):
    try:
        num1 = int(inp1.get())
    except:
        num1 = n1       
    try:
        num2 = int(inp2.get())
    except:       
        num2 = n2
    return num1, num2

def intelligence(a, b, res):
    if a<10 or b<10:
        answer["text"], answer["fg"], answer["font"] = "Woah Man yo Serious?,\n You can't do that simple shit?", "red", headfont
    else:
        answer["fg"] = "black"
        answer["font"] ="TkDefaultFont"

def Noice(res):
    if res==69 or res==420 or res==80085:
        answer["text"] = res, "Nice ಠ◡ಠ"   


#-----------Main_Logic---------------------------------                
def Add():
    a, b = NullSafe(0, 0)
    answer["text"] = result = a+b
    Noice(result)
    #intelligence(a, b, result)   
def Sub():
    a, b = NullSafe(0, 0)
    answer["text"] = result = a-b
    Noice(result)
    #intelligence(a, b, result)   
def Mul():
    a, b = NullSafe(1, 1)
    answer["text"] = result = a*b
    Noice(result)
    #intelligence (20, 20, result)    
def Div():
    a, b = NullSafe(0, 1)
    answer["text"] = result = a/b
    Noice(result)
    #intelligence (20, 20, result)
def Root():
    a, b = NullSafe(0, 2)
    answer["text"] = result = a**(1/b)
    answer["fg"], answer["font"] = "black", "TkDefaultFont"
    Noice(result)
def Pow():
    a, b = NullSafe(0, 1)
    answer["text"] = result = a**b
    answer["fg"], answer["font"] = "black", "TkDefaultFont"
    Noice(result)
    #intelligence (20, 20, result)
def Abs():
    a, b = NullSafe(0, 0)
    #b = int(inp2.get())
    answer["text"] = result = abs(a)
    Noice(result)
    #intelligence (20, 20, result)
def GeoMean():
    a, b = NullSafe(1, 1)
    mean = (a*b)
    answer["text"] = result = mean**0.5
    Noice(result)
    #intelligence (20, 20, result)
def SumUp():
    a, b = NullSafe(0, 0) 
    answer["text"] = result = ((a*(a+1))//2) - ((b*(b+1))//2)
    Noice(result)
    #intelligence (20, 20, result)
def Factorial():
    a, b = NullSafe(0, 0)
    answer["text"] = result = (math.factorial(a))
    Noice(result)

              
#-------------*Buttons*---------------------------------
b_add = Button(root, text="+", command=Add, bg="grey")
b_sub = Button(root, text="-", command=Sub, bg="grey")
b_mul = Button(root, text="×", command=Mul, bg="grey")
b_div = Button(root, text="÷", command=Div, bg="grey")
b_root = Button(root, text="√", command=Root, bg="grey")
b_power = Button(root, text="^", command=Pow, bg="grey")
b_abs = Button(root, text="absolute(No.1)", command=Abs, bg="orange")
b_geomean = Button(root, text="geo_mean", command=GeoMean, bg="orange")
b_sumUp = Button(root, text="Σ", command=SumUp, bg="lime")
b_factorial = Button(root, text="(Number1)!", command=Factorial, bg="lime")



#---------*Setting_Buttons & Text*-----------------------------------------
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
b_abs.grid(row=6, column=0)
b_geomean.grid(row=6, column=1)
b_sumUp.grid(row=7, column=0)
b_factorial.grid(row=7, column=1)

answer.grid(row=10, column=0)
 
 
# ----------------------------------------------------------------                       

root.mainloop()


"""def Sine():
    a = int(inp1.get())
    temp = math.sin(a)
    answer["text"] = math.degrees(temp)
def Cosine():
    a = int(inp1.get())
    answer["text"] = math.cos(a)
def Tangent():
    a = int(inp1.get())
    answer["text"] = math.tan(a)"""


#b_sine = Button(root, text="sin(a)", command=Sine, bg="#CBC3E3")
#b_cosine = Button(root, text="cosine(a)", command=Cosine, bg="#CBC3E3")
#b_tangent = Button(root, text="tangent(a)", command=Tangent, bg="#CBC3E3")


#b_sine.grid(row=8, column=0)
#b_cosine.grid(row=8, column=1)
#b_tangent.grid(row=9, column=0)


#++++++++++++++++
""" Code for Null Safety:
    try:
        a = int(inp1.get())
    except: 
        a = 0  
    try:
        b = int(inp2.get())   
    except:
        b = 0 
"""
