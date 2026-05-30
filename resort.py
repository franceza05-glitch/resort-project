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

class Booking:

    def __init__(self, name, room_number, people, price, days, check_in):

        self.name = name
        self.room_number = room_number
        self.people = people
        self.price = price
        self.days = days
        
        self.check_in = check_in
        self.check_out = self.check_in + timedelta(days=days)



# list เก็บลูกค้าทั้งหมด
#คนเข้าพัก
guests = []

#จองล่วงหน้า
bookings = []


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

def add_booking():
    name = booking_name_entry.get()
    room = booking_room_entry.get()
    people = int(booking_people_entry.get())
    price = float(booking_price_entry.get())
    days = int(booking_days_entry.get())
    check_in_str = booking_date_entry.get()

    try:
        check_in = datetime.strptime(check_in_str, "%d/%m/%Y %H:%M")
    except ValueError:
        messagebox.showerror("Error", "Invalid date format! Use dd/mm/yyyy hh:mm")
        return

    booking = Booking(
        name,
        room,
        people,
        price,
        days,
        check_in
    )

    bookings.append(booking)
    
    update_booking_list()

    messagebox.showinfo("Success", "Booking Added!")

    booking_window.destroy()

   

def update_booking_list():
    booking_list.delete(0, tk.END)

    for i, b in enumerate(bookings):

        text = (
            f"{i+1}. "
            f"{b.name} | "
            f"Room {b.room_number} | "
            f"{b.people} people | "
            f"${b.price} | "
            f"{b.days} days | "
            f"Check-in: {b.check_in.strftime('%d/%m/%Y %H:%M')} | "
            f"Check-out: {b.check_out.strftime('%d/%m/%Y')}"
        )

        booking_list.insert(tk.END, text)


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


# หน้าต่างเข้าพัก
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

# หน้าต่างการจอง
def open_booking_window():

    global booking_name_entry
    global booking_room_entry
    global booking_people_entry
    global booking_price_entry
    global booking_days_entry
    global booking_date_entry
    global booking_list
    global booking_window


    booking_window = tk.Toplevel()

    booking_window.title(
            "Booking"
    )

    booking_window.geometry(
            "400x300"
    )
    # Name
    tk.Label(
        booking_window,
        text="Customer Name"
    ).pack()

    booking_name_entry = tk.Entry(
        booking_window
    )

    booking_name_entry.pack()

    # Room
    tk.Label(
        booking_window,
        text="Room Number"
    ).pack()

    booking_room_entry = tk.Entry(
        booking_window
    )

    booking_room_entry.pack()

    # People
    tk.Label(
        booking_window,
        text="People"
    ).pack()

    booking_people_entry = tk.Entry(
        booking_window
    )

    booking_people_entry.pack()

    # Price
    tk.Label(
        booking_window,
        text="Price"
    ).pack()

    booking_price_entry = tk.Entry(
        booking_window
    )

    booking_price_entry.pack()

    # Days
    tk.Label(
        booking_window,
        text="Stay Days"
    ).pack()

    booking_days_entry = tk.Entry(
        booking_window
    )

    booking_days_entry.pack()

    tk.Label(
        booking_window,
        text="Check-in (dd/mm/yyyy hh:mm)"
    ).pack()

    booking_date_entry = tk.Entry(
    booking_window
    )

    booking_date_entry.pack()

    

    # Button
    add_button = tk.Button(
        booking_window,
        text="Add Booking",
        command=add_booking
    )

    add_button.pack(
        pady=10
    )

    # Listbox
    booking_list = tk.Listbox(
        booking_window,
        width=100,
        height=15
    )

    booking_list.pack(
        pady=10
    )

    update_booking_list()

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

booking_button = tk.Button(
    window,
    text="Booking",
    width=20,
    height=2,
    command=open_booking_window
)
booking_button.pack(
    pady=10
)


# เริ่มโปรแกรม
window.mainloop()