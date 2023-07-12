from pathlib import Path
import json
from tkinter import *
from tkinter import messagebox

window = Tk()

window.title('حساب کتاب')
window.geometry("1240x360")
window.configure(bg="gray")


L_row = Label(text='ردیف', fg="yellow",
              bg="black", font=("B Yekan", 12), width=20)
L_row.grid(row=0, column=5, padx=10, pady=10)
E_row = Entry(font=("B Yekan", 12))
E_row.grid(row=1, column=5, padx=10)

L_date = Label(text="تاریخ", bg="black", fg="yellow",
               font=("B Yekan", 12), width=20)
L_date.grid(row=0, column=4)
E_date = Entry(font=("B Yekan", 12))
E_date.grid(row=1, column=4, padx=10)

L_price = Label(text="قیمت", bg="black", fg="yellow",
                font=("B Yekan", 12), width=20)
L_price.grid(row=0, column=3)
E_price = Entry(font=("B Yekan", 12))
E_price.grid(row=1, column=3, padx=10)

L_type = Label(text="نوع", bg="black", fg="yellow",
               font=("B Yekan", 12), width=20)
L_type.grid(row=0, column=2)
E_type = Entry(font=("B Yekan", 12))
E_type.grid(row=1, column=2, padx=10)

L_description = Label(text="توضیحات", bg="black",
                      fg="yellow", font=("B Yekan", 12), width=20)
L_description.grid(row=0, column=1)
E_description = Entry(font=("B Yekan", 12))
E_description.grid(row=1, column=1, padx=10)

L_rows = Label(text="ردیف ها", bg="black",
               fg="yellow", font=("B Yekan", 12), width=20)
L_rows.grid(row=2, column=2)
E_rows = Entry(font=("B Yekan", 12))
E_rows.grid(row=2, column=1)

L_sum = Label(text="جمع قیمت ردیف ها", bg="black",
              fg="yellow", font=("B Yekan", 12), width=20)
L_sum.grid(row=3, column=2)
E_sum = Entry(font=("B Yekan", 12))
E_sum.grid(row=3, column=1)

L_price_finder = Label(text="<< قیمت بالاتر از", bg="black",
                       fg="yellow", font=("B Yekan", 12), width=20)
L_price_finder.grid(row=2, column=5)
E_price_finder = Entry(font=("B Yekan", 12))
E_price_finder.grid(row=2, column=4)

L_type_finder = Label(text="<< نوع مورد نظر", bg="black",
                      fg="yellow", font=("B Yekan", 12), width=20)
L_type_finder.grid(row=3, column=5)
E_type_finder = Entry(font=("B Yekan", 12))
E_type_finder.grid(row=3, column=4)

L_date_finder = Label(text="تاریخ نگار", bg="black",
                      fg="yellow", font=("B Yekan", 12), width=20)
L_date_finder.grid(row=4, column=5)

L_date_finder_from = Label(text=" از", bg="black",
                           fg="yellow", font=("B Yekan", 12), width=20)
L_date_finder_from.grid(row=4, column=4)
E_date_finder_from = Entry(font=("B Yekan", 12))
E_date_finder_from.grid(row=5, column=4)

L_date_finder_to = Label(text=" تا", bg="black",
                         fg="yellow", font=("B Yekan", 12), width=20)
L_date_finder_to.grid(row=4, column=3)
E_date_finder_to = Entry(font=("B Yekan", 12))
E_date_finder_to.grid(row=5, column=3)


esm = Label(text='Arshia Afshar / Alireza Tanha',
            bg='black', fg='white', width=30)
esm.grid(row=5, column=1, columnspan=2)

iut = Label(text='<< IUT >>', bg='black', fg='white', width=17)
iut.grid(row=0, column=0)
####################################################

path_date = Path("date.json")
if path_date.exists():
    with open("date.json", "r") as file:
        dict_date = json.load(file)
else:
    dict_date = {}

path_perice = Path("price.json")
if path_perice.exists():
    with open("price.json", "r") as file:
        dict_price = json.load(file)
else:
    dict_price = {}

path_type = Path("type.json")
if path_type.exists():
    with open("type.json", "r") as file:
        dict_type = json.load(file)
else:
    dict_type = {}

path_description = Path("description.json")
if path_description.exists():
    with open("description.json", "r") as file:
        dict_description = json.load(file)
else:
    dict_description = {}

####################################################


def register(event):

    row = E_row.get()
    E_row.delete(0, END)

    date = E_date.get()
    E_date.delete(0, END)

    price = E_price.get()
    E_price.delete(0, END)

    type = E_type.get()
    E_type.delete(0, END)

    description = E_description.get()
    E_description.delete(0, END)

    dict_date[row] = date

    import json
    with open("date.json", "w") as file:
        json.dump(dict_date, file, indent=4)

    dict_price[row] = price

    with open("price.json", "w") as file:
        json.dump(dict_price, file, indent=4)

    dict_type[row] = type

    with open("type.json", "w") as file:
        json.dump(dict_type, file, indent=4)

    dict_description[row] = description

    with open("description.json", "w") as file:
        json.dump(dict_description, file, indent=4)


def search(event):
    row = E_row.get()
    if row in dict_price:

        E_date.delete(0, END)
        E_date.insert(0, dict_date[row])

        E_price.delete(0, END)
        E_price.insert(0, dict_price[row])

        E_type.delete(0, END)
        E_type.insert(0, dict_type[row])

        E_description.delete(0, END)
        E_description.insert(0, dict_description[row])
    else:
        E_date.delete(0, END)
        E_date.insert(0, "پیدا نشد")
        E_price.delete(0, END)
        E_price.insert(0, "پیدا نشد")
        E_type.delete(0, END)
        E_type.insert(0, "پیدا نشد")
        E_description.delete(0, END)
        E_description.insert(0, "پیدا نشد")
        messagebox.showwarning(message="Not found")


def price_finder(event):
    price = int(E_price_finder.get())
    sum = 0
    E_rows.delete(0, END)
    E_sum.delete(0, END)
    for i in dict_price:
        if int(dict_price[i]) >= price:
            E_rows.insert(0, "("+i+")")
            sum = sum + int(dict_price[i])
    E_sum.insert(0, sum)


def type_finder(event):
    type = E_type_finder.get()
    sum = 0
    E_rows.delete(0, END)
    E_sum.delete(0, END)
    for i in dict_type:
        if dict_type[i] == type:
            E_rows.insert(0, "("+i+")")
            sum = sum + int(dict_price[i])
    E_sum.insert(0, sum)


def date_finder(event):
    date_from = int(E_date_finder_from.get())
    date_to = int(E_date_finder_to.get())
    sum = 0
    E_rows.delete(0, END)
    E_sum.delete(0, END)
    for i in dict_date:
        if date_from <= int(dict_date[i]) <= date_to:
            E_rows.insert(0, "("+i+")")
            sum = sum + int(dict_price[i])
    E_sum.insert(0, sum)


def all_finder(event):
    price = int(E_price_finder.get())
    type = E_type_finder.get()
    date_from = int(E_date_finder_from.get())
    date_to = int(E_date_finder_to.get())
    sum = 0
    E_rows.delete(0, END)
    E_sum.delete(0, END)
    for i in dict_price:
        if int(dict_price[i]) >= price:
            if dict_type[i] == type:
                if date_from <= int(dict_date[i]) <= date_to:
                    E_rows.insert(0, "("+i+")")
                    sum = sum + int(dict_price[i])
    E_sum.insert(0, sum)


def delete(event):
    E_row.delete(0, END)
    E_date.delete(0, END)
    E_price.delete(0, END)
    E_type.delete(0, END)
    E_description.delete(0, END)
    E_rows.delete(0, END)
    E_sum.delete(0, END)
    E_price_finder.delete(0, END)
    E_type_finder.delete(0, END)
    E_date_finder_from.delete(0, END)
    E_date_finder_to.delete(0, END)


B_register = Button(text="ثبت", font=("B Yekan", 12),
                    bg="yellow", fg="black", padx=50, pady=1)
B_register.grid(row=1, column=0, padx=10)
B_register.bind("<Button-1>", register)

B_search = Button(text="جستو(ردیف)", bg="yellow",
                  font=("B Yekan", 12), padx=27, pady=1)
B_search.grid(row=2, column=0, padx=10)
B_search.bind("<Button-1>", search)

B_price_finder = Button(text="جستو(قیمت)",
                        bg="yellow", font=("B Yekan", 12), padx=30)
B_price_finder.grid(row=2, column=3, pady=20)
B_price_finder.bind("<Button-1>", price_finder)

B_type_finder = Button(text="جستو(نوع)",
                       bg="yellow", font=("B Yekan", 12), padx=32)
B_type_finder.grid(row=3, column=3)
B_type_finder.bind("<Button-1>", type_finder)

B_date_finder = Button(text="جستو(تاریخ)",
                       bg="yellow", font=("B Yekan", 12), padx=50)
B_date_finder.grid(row=5, column=5)
B_date_finder.bind("<Button-1>", date_finder)

B_all_finder = Button(text="جستو(همه ویژگی ها)",
                      bg="yellow", font=("B Yekan", 12))
B_all_finder.grid(row=4, column=0, padx=10, pady=20)
B_all_finder.bind("<Button-1>", all_finder)

B_delete = Button(text="پاک کردن", fg="black", bg="red",
                  font=("B Yekan", 12), padx=30)
B_delete.grid(row=5, column=0, padx=10,)
B_delete.bind("<Button-1>", delete)


window.mainloop()
