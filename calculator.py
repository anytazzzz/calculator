import tkinter as tk

def get_values():
    num1 = int(number1_entry.get())   #переводит в число, что ввел человек
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    answer_entry.delete(0, "end")
    answer_entry.insert(0, value)


def add():
    num1= int(number1_entry.get())
    num2 = int(number2_entry.get())
    res = num1 + num2
    answer_entry.delete(0, "end")
    answer_entry.insert(0, res)

def sub():
    num1= int(number1_entry.get())
    num2 = int(number2_entry.get())
    res = num1 - num2
    answer_entry.delete(0, "end")
    answer_entry.insert(0, res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)




window = tk.Tk()
window.title ("Калькулятор")
window.geometry("350x350")
button_add = tk.Button(window, text = "+", width=2, height=2, command=add)
button_add.place(x = 100, y = 200)
button_add = tk.Button(window, text = "-", width=2, height=2, command=sub)
button_add.place(x = 150, y = 200)
button_add = tk.Button(window, text = "*", width=2, height=2, command=mul)
button_add.place(x = 200, y = 200)
button_add = tk.Button(window, text = ":", width=2, height=2, command=div)
button_add.place(x = 250, y = 200)
number1_entry = tk.Entry(window, width = 28)
number1_entry.place(x = 100, y = 75)
number2_entry = tk.Entry(window, width = 28)
number2_entry.place(x = 100, y = 150)
answer_entry = tk.Entry(window, width = 28)
answer_entry.place(x = 100, y = 300)
number1 = tk.Label(window, text = "Ввидете первое число:")  #надпись
number1.place(x = 100, y = 50)
number2 = tk.Label(window, text = "Ввидете второе число:")  #надпись
number2.place(x = 100, y = 125)
answer = tk.Label(window, text = "Ответ:")  #надпись
answer.place(x = 100, y = 275)
window.mainloop()