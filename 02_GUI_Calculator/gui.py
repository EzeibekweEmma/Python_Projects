from tkinter import *


def btn_click(value):
    screen.insert(END, value)


def btn_click_del():
    screen.delete(len(screen.get()) - 1, END)


def btn_click_equa():
    ans = screen.get()
    if "^" in ans:
        ans = ans.replace("^", "**")
    if "÷" in ans:
        ans = ans.replace("÷", "/")
    if "×" in ans:
        ans = ans.replace("×", "*")

    screen.delete(0, END)
    screen.insert(0, eval(ans))


def btn_click_clear():
    screen.delete(0, END)


window = Tk()
window.title("Calculator")
icon = PhotoImage(file="calculator icon.png")
window.iconphoto(True, icon)

body = Frame(window,
             bg="lightblue",
             pady=5,
             padx=5)
body.pack(pady=5, padx=5)

screen = Entry(body,
               width=18,
               font=("sans", 20),
               borderwidth=5, )
screen.grid(row=0, column=0, columnspan=4, pady=(5, 10))

btn_1 = Button(body, text="1", font=("sans", 20), padx=15, pady=5, command=lambda: btn_click(1))
btn_2 = Button(body, text="2", font=("sans", 20), padx=15, pady=5, command=lambda: btn_click(2))
btn_3 = Button(body, text="3", font=("sans", 20), padx=15, pady=5, command=lambda: btn_click(3))
btn_4 = Button(body, text="4", font=("sans", 20), padx=15, pady=5, command=lambda: btn_click(4))
btn_5 = Button(body, text="5", font=("sans", 20), padx=15, pady=5, command=lambda: btn_click(5))
btn_6 = Button(body, text="6", font=("sans", 20), padx=15, pady=5, command=lambda: btn_click(6))
btn_7 = Button(body, text="7", font=("sans", 20), padx=15, pady=5, command=lambda: btn_click(7))
btn_8 = Button(body, text="8", font=("sans", 20), padx=15, pady=5, command=lambda: btn_click(8))
btn_9 = Button(body, text="9", font=("sans", 20), padx=15, pady=5, command=lambda: btn_click(9))
btn_0 = Button(body, text="0", font=("sans", 20), padx=15, pady=5, command=lambda: btn_click(0))

btn_clear = Button(body, text="C", font=("sans", 20), fg="#f00", activeforeground="#f00", padx=13, pady=5,
                   command=btn_click_clear)
btn_del = Button(body, text="Del", font=("sans", 20), fg="#0f5", activeforeground="#0f5", padx=2, pady=5,
                 command=btn_click_del)
btn_squ = Button(body, text="√", font=("sans", 20), padx=15, pady=5, command=lambda: btn_click('√'))
btn_pow = Button(body, text="^", font=("sans", 20), padx=15, pady=5, command=lambda: btn_click("^"))
btn_equa = Button(body, text="=", font=("sans", 20), padx=49, pady=5, command=btn_click_equa)
btn_add = Button(body, text="+", font=("sans", 20), padx=13, pady=40, command=lambda: btn_click("+"))
btn_mins = Button(body, text="-", font=("sans", 20), padx=17, pady=5, command=lambda: btn_click('-'))
btn_times = Button(body, text="×", font=("sans", 20), padx=14, pady=5, command=lambda: btn_click("×"))
btn_div = Button(body, text="÷", font=("sans", 20), padx=13, pady=5, command=lambda: btn_click("÷"))

# display buttons
btn_clear.grid(row=1, column=0, pady=(0, 2))
btn_del.grid(row=1, column=1, pady=(0, 2))
btn_pow.grid(row=1, column=2, pady=(0, 2))
btn_div.grid(row=1, column=3, pady=(0, 2))

btn_1.grid(row=2, column=0, pady=(0, 2))
btn_2.grid(row=2, column=1, pady=(0, 2))
btn_3.grid(row=2, column=2, pady=(0, 2))
btn_times.grid(row=2, column=3, pady=2)

btn_4.grid(row=3, column=0, pady=2)
btn_5.grid(row=3, column=1, pady=2)
btn_6.grid(row=3, column=2, pady=2)
btn_mins.grid(row=3, column=3, pady=2)

btn_7.grid(row=4, column=0, pady=2)
btn_8.grid(row=4, column=1, pady=2)
btn_9.grid(row=4, column=2, pady=2)
btn_add.grid(row=4, rowspan=2, column=3, pady=2)

btn_0.grid(row=5, column=0, pady=2)
btn_equa.grid(row=5, column=1, columnspan=2, pady=2)


window.mainloop()
