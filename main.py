import tkinter as tk
from math import pi, sqrt, sin, cos, tan, asin, acos, atan, log, exp, e

calculation= ""     #variabila globala - initialaizata cu un sir vid


def add_to_calculation(symbol):
    global calculation
    calculation +=str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))

        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "ERROR")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def update_display():
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def backspace():
    global calculation
    calculation = calculation[:-1]
    update_display()

#culori
#https://htmlcolorcodes.com
##17202A

#aspectul ferestrei: obiect, dimensiune, titlu si culoarea fundalulu(din spatele butoanelor)
root = tk.Tk()#create the object
root.geometry("328x412") #lenght x height
root.title("Scientific Calculator") #title of the window
root.configure(bg="#000000")

text_result = tk.Text(root, height = 2, width = 18, font = ("Arial",24), bg= "#000000", fg= "#FFFFFF")
text_result.grid(columnspan = 10)

#buttons for numbers
#9
btn_9 = tk.Button(root, text = "9", command = lambda: add_to_calculation(9), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")#lambda: folosim aceasta functie ca sa apeleze functia
btn_9.grid(row = 5, column = 3)
#8
btn_8 = tk.Button(root, text = "8", command = lambda: add_to_calculation(8), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_8.grid(row = 5, column = 2)
#7
btn_7 = tk.Button(root, text = "7", command = lambda: add_to_calculation(7), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_7.grid(row = 5, column = 1)
#6
btn_6 = tk.Button(root, text = "6", command = lambda: add_to_calculation(6), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_6.grid(row = 6, column = 3)
#5
btn_5 = tk.Button(root, text = "5", command = lambda: add_to_calculation(5), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_5.grid(row = 6, column = 2)
#4
btn_4 = tk.Button(root, text = "4", command = lambda: add_to_calculation(4), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_4.grid(row = 6, column = 1)
#3
btn_3 = tk.Button(root, text = "3", command = lambda: add_to_calculation(3), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_3.grid(row = 7, column = 3)
#2
btn_2 = tk.Button(root, text = "2", command = lambda: add_to_calculation(2), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_2.grid(row = 7, column = 2)
#1
btn_1 = tk.Button(root, text = "1", command = lambda: add_to_calculation(1), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_1.grid(row = 7, column = 1)
#0
btn_0 = tk.Button(root, text = "0", command = lambda: add_to_calculation(0), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_0.grid(row = 8, column = 1)

#Brackets buttons
btn_open = tk.Button(root, text = "(", command = lambda: add_to_calculation("("), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_open.grid(row = 8, column = 2)
btn_close = tk.Button(root, text = ")", command = lambda: add_to_calculation(")"), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_close.grid(row = 8, column = 3)

#Simple operation buttons

#add
btn_add = tk.Button(root, text = "+", command = lambda: add_to_calculation("+"), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_add.grid(row = 8, column = 4)

#substraction
btn_sub = tk.Button(root, text = "-", command = lambda: add_to_calculation("-"), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_sub.grid(row = 7, column = 4)

#multiplication
btn_mul = tk.Button(root, text = "*", command = lambda: add_to_calculation("*"), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_mul.grid(row = 6, column = 4)

#division
btn_div1 = tk.Button(root, text = "/", command = lambda: add_to_calculation("/"), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_div1.grid(row =5, column = 4)

#dot
btn_div1 = tk.Button(root, text = ".", command = lambda: add_to_calculation("."), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_div1.grid(row =9, column = 3)

#butoane esentiale - nu functioneaza cu lambda!
# =
btn_equal = tk.Button(root, text = "=", command = evaluate_calculation, width = 6, font = ("Arial", 16), bg = "#33D825", fg = "#FFFFFF")
btn_equal.grid(row = 9, column = 4)
#backspace
btn_backspace = tk.Button(root, text="⌫", command=backspace, width=6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_backspace.grid(row=9, column=2)
# C
btn_TOTALDEL = tk.Button(root, text = "C", command = clear_field, width = 6, font = ("Arial", 16), bg= "#000000", fg= "#D51616")
btn_TOTALDEL.grid(row = 9, column = 1)

#special functions
#sin
btn_sin = tk.Button(root, text = "sin", command = lambda: add_to_calculation("sin("), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_sin.grid(row = 2, column = 1)

#cos
btn_cos = tk.Button(root, text = "cos", command = lambda: add_to_calculation("cos("), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_cos.grid(row = 2, column = 2)

#tan
btn_tg = tk.Button(root, text = "tan", command = lambda: add_to_calculation("tan("), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_tg.grid(row = 2, column = 3)

#power
btn_pow = tk.Button(root, text = "^", command = lambda: add_to_calculation("**"), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_pow.grid(row = 4, column = 3)

#pi
btn_pi = tk.Button(root, text = "π", command = lambda: add_to_calculation("pi"), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_pi.grid(row = 4, column = 1)

#e
btn_e = tk.Button(root, text = "e", command = lambda: add_to_calculation("e"), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_e.grid(row = 4, column = 2)

#ln
btn_ln = tk.Button(root, text = "ln", command = lambda: add_to_calculation("log("), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_ln.grid(row = 3, column = 4)

#√
btn_pow = tk.Button(root, text = "√", command = lambda: add_to_calculation("sqrt("), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_pow.grid(row = 4, column = 4)

#asin
btn_asin = tk.Button(root, text = "asin", command = lambda: add_to_calculation("asin("), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_asin.grid(row = 3, column = 1)

#acos
btn_acos = tk.Button(root, text = "acos", command = lambda: add_to_calculation("acos("), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_acos.grid(row = 3, column = 2)

#atan
btn_atan = tk.Button(root, text = "atan", command = lambda: add_to_calculation("atan("), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_atan.grid(row = 3, column = 3)

#exp
btn_exp = tk.Button(root, text = "exp", command = lambda: add_to_calculation("exp("), width = 6, font = ("Arial", 16), bg= "#000000", fg= "#FFFFFF")
btn_exp.grid(row = 2, column = 4)

root.mainloop() #run the main loop- keep the window open
