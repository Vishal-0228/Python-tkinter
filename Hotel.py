from tkinter import Tk, Label, Frame
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from Customer import Cust_Win
from Room import Roombooking
from details import DetailsRoom

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1500x700+0+0")

        # First image
        img1 = Image.open(r"D:\Hotel Management\hh.jpg")
        img1 = img1.resize((1550, 140), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        # LOGO image
        img2 = Image.open(r"D:\Hotel Management\logohotel.png")
        img2 = img2.resize((230, 140), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)  # Changed variable name to self.photoimg2

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

        lbl_title = Label(self.root, text="GRAND HOTEL", font=("times new roman", 40, "bold"), bg="black", fg="gold")
        lbl_title.place(x=0, y=140, width=1550, height=50)

        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold")
        lbl_menu.place(x=0, y=0, width=230)

        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=150)

        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.cust_details, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="ROOM", command=self.Roombooking, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS", command=self.DetailsRoom, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", command=self.logout, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=1)

        # Center  image
        img3 = Image.open(r"D:\Hotel Management\slide3.jpg")
        img3 = img3.resize((1100, 500), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1100, height=500)

        # Corner  image
        img4 = Image.open(r"D:\Hotel Management\myh.jpg")
        img4 = img4.resize((230, 410), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=225, width=230, height=410)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def Roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)

    def DetailsRoom(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_window)

    def logout(self):
        self.root.destroy()

if __name__ == '__main__':
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
