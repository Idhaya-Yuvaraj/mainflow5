import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import datetime
import requests
from PIL import ImageTk, Image
from tkinter import messagebox

root = tk.Tk()
root.geometry("600x270")
root.title("Currency Converter")
root.iconbitmap("C:\\Idhaya Yuvaraj\\icon.ico")
root.minsize(600, 270)
root.maxsize(600, 270)

image = Image.open("C:\\Idhaya Yuvaraj\\currency.png")
zoom = 0.5

pixels_x, pixels_y = tuple([int(zoom * x) for x in image.size])
img = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y)))
panel = Label(root, image=img)
panel.place(x=190, y=35)


def show_data():
    amount = E1.get()
    from_currency = c1.get()
    to_currency = c2.get()
    url = "http://api.currencylayer.com/live?access_key=051cac750cc2eb41048af8f8c39b5d3a&format=1"

    if amount.strip() == "":
        messagebox.showerror("Currency Converter", "Please Fill the Amount")
    elif to_currency.strip() == "":
        messagebox.showerror("Currency Converter", "Please Choose the Currency")
    else:
        data = requests.get(url).json()
        currency = "USD" + to_currency.strip()
        amount = int(amount)
        cc = data["quotes"].get(currency)
        if cc:
            cur_conv = cc * amount
            E2.insert(0, cur_conv)
            text.insert("end", f"{amount} United States Dollar Equals {cur_conv} {to_currency}\n\n Last Time Update --- \t {datetime.now()}")
        else:
            messagebox.showerror("Currency Converter", f"Conversion rate for {to_currency} not found.")


def clear():
    E1.delete(0, END)
    E2.delete(0, END)
    text.delete(1.0, END)


l1 = Label(root, text="USD Currency Converter Using Python", font=("verdana", "10", "bold"))
l1.place(x=150, y=15)

amt = Label(root, text="Amount", font=("roboto", "10", "bold"))
amt.place(x=20, y=15)
E1 = Entry(root, width=20, borderwidth=1, font=("roboto", "10", "bold"))
E1.place(x=20, y=40)

c1 = tk.StringVar(value="USD")
c2 = tk.StringVar()

currencychoose1 = ttk.Combobox(root, width=20, textvariable=c1, state="readonly", font=("roboto", 10, "bold"))
currencychoose1["values"] = ("USD",)
currencychoose1.place(x=300, y=40)
currencychoose1.current(0)

E2 = Entry(root, width=20, borderwidth=1, font=("roboto", "10", "bold"))
E2.place(x=20, y=80)

currencychoose2 = ttk.Combobox(root, width=20, textvariable=c2, state="readonly", font=("roboto", 10, "bold"))
currencychoose2["values"] = ("ALL", "AFN", "ARS", "AWG", "AUD", "AZN", "BSD", "BBD", "BYN", "BZD", "BMD", "BOB", "BAM", "BWP", "BGN", "BND",
                             "KHR", "CAD", "KYD", "CLP", "CNY", "COP", "CRC", "HRK", "CUP", "CZK", "DKK", "DDP", "XCD", "EGP", "SVC", "EUR",
                             "FKP", "FJD", "GHS", "GIP", "GTQ", "GGP", "GYD", "HNL", "HKD", "HUF", "ISK", "INR", "IDR", "IRR", "IMP", "ILS",
                             "JMD", "JPY", "KZL", "KPW", "KRW", "KOS", "KGS", "LAK", "LBP", "LRD", "MKD", "MYR", "MUR", "MXN", "MNT", "MZN",
                             "NAD", "NPR", "ANG", "NZD", "NIO", "NGN", "NOK", "OMR", "PKR", "PAB", "PYG", "PEN", "PHP", "PLN", "QAR", "RON",
                             "RUB", "SHP", "SAR", "RSD", "SCR", "SGD", "SBD", "SOS", "ZAR", "LKR", "SEK", "CHF", "SRD", "SYP", "TWD", "THB",
                             "TTD", "TRY", "TVD", "UAH", "GBP", "UYU", "UZS", "VEF", "VND", "YER", "ZWD")
currencychoose2.place(x=300, y=80)

text = Text(root, height=7, width=52, font=("verdana", "10", "bold"))
text.place(x=100, y=120)

B = Button(root, text="Search", command=show_data, font=("verdana", "10", "bold"), borderwidth=2, bg="red", fg="white")
B.place(x=20, y=120)

clear_button = Button(root, text="Clear", command=clear, font=("verdana", "10", "bold"), borderwidth=2, bg="red", fg="white")
clear_button.place(x=20, y=170)

root.mainloop()
