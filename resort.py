import tkinter as tk
from tkinter import messagebox


class Room:

    def __init__(self, room_number, people, price):
        self.room_number = room_number
        self.people = people
        self.price = price


def save_room():

    room_number = room_entry.get()
    people = people_entry.get()
    price = price_entry.get()

    room = Room(room_number, people, price)

    messagebox.showinfo(
        "Success",
        f"ห้อง {room.room_number}\n"
        f"จำนวนคน: {room.people} คน\n"
        f"ราคา: {room.price} บาท"
    )


# สร้างหน้าต่าง
window = tk.Tk()
window.title("Nongsamor Resort System")
window.geometry("300x250")

# เลขห้อง
tk.Label(window, text="Room Number").pack()
room_entry = tk.Entry(window)
room_entry.pack()

# จำนวนคน
tk.Label(window, text="Number of People").pack()
people_entry = tk.Entry(window)
people_entry.pack()

# ราคา
tk.Label(window, text="Price").pack()
price_entry = tk.Entry(window)
price_entry.pack()

# ปุ่มบันทึก
save_button = tk.Button(window, text="Save Room", command=save_room)
save_button.pack(pady=10)

# เริ่มโปรแกรม
window.mainloop()