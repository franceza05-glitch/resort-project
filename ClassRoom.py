class Room:
    def __init__(self,room_number,people,price):
        self.room_number = room_number
        self.people = people
        self.price = price

#รับค่า
room_number = input("Enter room number: ") 
people = int(input("Enter number of people: "))
price = float(input("Enter price: "))

#สร้าง object
room1 = Room(room_number, people, price)

#แสดงผล
print(f"ห้อง: {room1.room_number}")
print(f"จำนวนคน: {room1.people} คน")  
print(f"ราคา: {room1.price} บาท")