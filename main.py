#Version 1.0.0.1///Tkinter GUI Engine Built by Ibukun///

import tkinter
import ast

#Early code to experiement different designs.
#frame = tkinter.LabelFrame(text="Calculator", width=300, height=300, bd=5)
#frame.grid(row=0, column=0, columnspan=3, padx=8)


window = tkinter.Tk()
#calc = tkinter.Entry()
#calc.grid(row=1)


#entry1 = tkinter.Text(window,
#                      height=4,
#                      width=20,
#                      )

large_font = ("Verdana", 30)


entry1 = tkinter.Entry(window,
                       font=large_font
)

entry1.grid(row=5, column=0)


seven_button = tkinter.Button(
    text="7",
    width=6,
    height=3,
    bg="grey",
    fg="white",
    command=lambda:entry1.insert(tkinter.END, 7)
)
seven_button.grid(row=6, column=1)


eight_button = tkinter.Button(
    text="8",
    width=6,
    height=3,
    bg="grey",
    fg="white",
    command=lambda:entry1.insert(tkinter.END, 8)
)
eight_button.grid(row=6, column=2)

nine_button = tkinter.Button(
    text="9",
    width=6,
    height=3,
    bg="grey",
    fg="white",
    command=lambda:entry1.insert(tkinter.END, "9")
)
nine_button.grid(row=6, column=3)

plus_button = tkinter.Button(
    text="+",
    width=6,
    height=3,
    bg="blue",
    fg="white",
    command=lambda:entry1.insert(tkinter.END, "+")
)
plus_button.grid(row=6, column=4)

four_button = tkinter.Button(
    text="4",
    width=6,
    height=3,
    bg="grey",
    fg="white",
    command=lambda:entry1.insert(tkinter.END, "4")
)
four_button.grid(row=7, column=1)

five_button = tkinter.Button(
    text="5",
    width=6,
    height=3,
    bg="grey",
    fg="white",
    command=lambda:entry1.insert(tkinter.END, "5")
)
five_button.grid(row=7, column=2)

six_button = tkinter.Button(
    text="6",
    width=6,
    height=3,
    bg="grey",
    fg="white",
    command=lambda:entry1.insert(tkinter.END, "6")
)
six_button.grid(row=7, column=3)


star_button = tkinter.Button(
    text="*",
    width=6,
    height=3,
    bg="blue",
    fg="white",
    command=lambda:entry1.insert(tkinter.END, "*")
)
star_button.grid(row=7, column=4)

one_button = tkinter.Button(
    text="1",
    width=6,
    height=3,
    bg="grey",
    fg="white",
    command=lambda:entry1.insert(tkinter.END, "1")
)
one_button.grid(row=8, column=1)

two_button = tkinter.Button(
    text="2",
    width=6,
    height=3,
    bg="grey",
    fg="white",
    command=lambda:entry1.insert(tkinter.END, "2")
)
two_button.grid(row=8, column=2)

three_button = tkinter.Button(
    text="3",
    width=6,
    height=3,
    bg="grey",
    fg="white",
    command=lambda:entry1.insert(tkinter.END, "3")
)
three_button.grid(row=8, column=3)

divide_button = tkinter.Button(
    text="/",
    width=6,
    height=3,
    bg="blue",
    fg="white",
    command=lambda:entry1.insert(tkinter.END, "/")

)
divide_button.grid(row=8, column=4)

zero_button = tkinter.Button(
    text="0",
    width=6,
    height=3,
    bg="grey",
    fg="white",
    command=lambda:entry1.insert(tkinter.END, "0")
)
zero_button.grid(row=10, column=1)

decimal_button = tkinter.Button(
    text="∙",
    width=6,
    height=3,
    bg="grey",
    fg="white",
    command=lambda:entry1.insert(tkinter.END, ".")
)
decimal_button.grid(row=10, column=2)

minus_button = tkinter.Button(
    text="-",
    width=6,
    height=3,
    bg="blue",
    fg="white",
    command=lambda:entry1.insert(tkinter.END, "-")
)
minus_button.grid(row=10, column=3)


c_button = tkinter.Button(
    text="C",
    width=6,
    height=3,
    bg="orange",
    fg="white",
    command=lambda:entry1.delete(0, tkinter.END)
)
c_button.grid(row=5, column=4)

def delete_button():
    v = entry1.get()[:-1]
    entry1.delete(0, tkinter.END)
    entry1.insert(0, v)

del_button = tkinter.Button(
    text="CE",
    width=6,
    height=3,
    bg="orange",
    fg="white",
    command=lambda:delete_button()
)

del_button.grid(row=5, column=3)




def get_ans():
    global calc
    calc = entry1.get()
    if len(calc) > 0:
        print(calc)
        print(len(calc))
        global ans
        ans = eval(calc)
        global stored_ans
        stored_ans = ans
        print(ans)
        entry1.delete(0, tkinter.END)
        #var1 = lambda:entry1.insert(0, ans)

def returner():
    get_ans()
    return entry1.insert(0, round(ans, 3))


equals_button = tkinter.Button(
    text="=",
    width=6,
    height=3,
    bg="blue",
    fg="white",
    command=lambda:returner()
    #command=lambda:entry1.insert(0, ast.literal_eval(calc))
    #command=clear_line() and answer()

)
equals_button.grid(row=10, column=4)

ans_button = tkinter.Button(
    text="Ans",
    width=6,
    height=3,
    bg="orange",
    fg="white",
    command=lambda:entry1.insert(tkinter.END, stored_ans)
)
ans_button.grid(row=5, column=2)

def copy():
    from tkinter import Tk
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(entry1.get())


copy_to_clip = tkinter.Button(
    text="Copy",
    width=6,
    height=3,
    bg="orange",
    fg="white",
    command=lambda:copy()
)

copy_to_clip.grid(row=5, column=1)

    

window.mainloop()
