import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta


class ResortGuest:

    def __init__(self, name, room_number, people, price, days):

        self.name = name
        self.room_number = room_number
        self.people = people
        self.price = price
        self.days = days

        self.check_in = datetime.now()
        self.check_out = self.check_in + timedelta(days=days)


# list เก็บลูกค้าทั้งหมด
guests = []


def add_guest():

    name = name_entry.get()
    room = room_entry.get()
    people = int(people_entry.get())
    price = float(price_entry.get())
    days = int(days_entry.get())

    guest = ResortGuest(
        name,
        room,
        people,
        price,
        days
    )

    guests.append(guest)

    messagebox.showinfo("Success", "Guest Added!")

    update_guest_list()


def update_guest_list():

    guest_list.delete(0, tk.END)

    for i, g in enumerate(guests):

        text = (
            f"{i+1}. "
            f"{g.name} | "
            f"Room {g.room_number} | "
            f"{g.days} days | "
            f"Check-in: {g.check_in.strftime('%d/%m/%Y %H:%M')} | "
            f"Check-out: {g.check_out.strftime('%d/%m/%Y')}"
        )

        guest_list.insert(tk.END, text)


# สร้างหน้าต่าง
window = tk.Tk()

window.title("Resort System")
window.geometry("500x500")


# Name
tk.Label(window, text="Customer Name").pack()
name_entry = tk.Entry(window)
name_entry.pack()

# Room
tk.Label(window, text="Room Number").pack()
room_entry = tk.Entry(window)
room_entry.pack()

# People
tk.Label(window, text="People").pack()
people_entry = tk.Entry(window)
people_entry.pack()

# Price
tk.Label(window, text="Price").pack()
price_entry = tk.Entry(window)
price_entry.pack()

# Days
tk.Label(window, text="Stay Days").pack()
days_entry = tk.Entry(window)
days_entry.pack()


# ปุ่มเพิ่มลูกค้า
add_button = tk.Button(
    window,
    text="Add Guest",
    command=add_guest
)

add_button.pack(pady=10)


# list แสดงข้อมูลลูกค้า
guest_list = tk.Listbox(window, width=70, height=15)
guest_list.pack(pady=10)


# เริ่มโปรแกรม
window.mainloop()