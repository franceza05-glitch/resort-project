import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta


class ResortGuest:

    def __init__(self, name, room_number, people, price, days ):

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

        
def open_guest_window():

    global name_entry
    global room_entry
    global people_entry
    global price_entry
    global days_entry
    global guest_list

    guest_window = tk.Toplevel()

    guest_window.title(
        "Guest Check-in"
    )

    guest_window.geometry(
        "700x500"
    )

    # Name
    tk.Label(
        guest_window,
        text="Customer Name"
    ).pack()

    name_entry = tk.Entry(
        guest_window
    )

    name_entry.pack()

    # Room
    tk.Label(
        guest_window,
        text="Room Number"
    ).pack()

    room_entry = tk.Entry(
        guest_window
    )

    room_entry.pack()

    # People
    tk.Label(
        guest_window,
        text="People"
    ).pack()

    people_entry = tk.Entry(
        guest_window
    )

    people_entry.pack()

    # Price
    tk.Label(
        guest_window,
        text="Price"
    ).pack()

    price_entry = tk.Entry(
        guest_window
    )

    price_entry.pack()

    # Days
    tk.Label(
        guest_window,
        text="Stay Days"
    ).pack()

    days_entry = tk.Entry(
        guest_window
    )

    days_entry.pack()

    # Button
    add_button = tk.Button(
        guest_window,
        text="Add Guest",
        command=add_guest
    )

    add_button.pack(
        pady=10
    )

    # Listbox
    guest_list = tk.Listbox(
        guest_window,
        width=100,
        height=15
    )

    guest_list.pack(
        pady=10
    )

    update_guest_list()

# สร้างหน้าต่าง
window = tk.Tk()

window.title(
    "Resort System"
)

window.geometry(
    "400x300"
)


title_label = tk.Label(
    window,
    text="RESORT SYSTEM",
    font=("Arial", 20)
)

title_label.pack(
    pady=30
)

# ปุ่มเข้าพัก
guest_button = tk.Button(
    window,
    text="Guest Check-in",
    width=20,
    height=2,
    command=open_guest_window
)

guest_button.pack(
    pady=10
)



# เริ่มโปรแกรม
window.mainloop()