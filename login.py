from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector  # Add import to use MySQL
import re
import hashlib
from tkinter import simpledialog
from Hotel import HotelManagementSystem

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Load and set the background image
        self.bg = ImageTk.PhotoImage(file=r"D:\Hotel Management\Backgroung image  .jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Get the center of the window
        window_width = 340
        window_height = 450
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # Create a frame and place it at the center of the window
        frame = Frame(self.root, bg="black")
        frame.place(x=x, y=y, width=window_width, height=window_height)

        # Load the login icon image (resizing it to fit nicely)
        img1 = Image.open(r"D:/Hotel Management/LoginIconAppl.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Place the image inside the frame (relative to the frame)
        lblimg1 = Label(frame, image=self.photoimg1, bg="black", borderwidth=0)
        lblimg1.place(x=(window_width // 2) - 50, y=10, width=100, height=100)

        # Get Started text
        get_str = Label(frame, text="Admin Login", font=("times new roman", 20, "bold"), bg="black", fg="white")
        get_str.place(x=95, y=120)

        # Username Label and Entry field
        username_lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), bg="black", fg="white")
        username_lbl.place(x=50, y=170)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15))
        self.txtuser.place(x=50, y=200, width=250)

        # Password Label and Entry field
        password_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="black", fg="white")
        password_lbl.place(x=50, y=240)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15), show="*")
        self.txtpass.place(x=50, y=270, width=250)

        # Login Button
        login_btn = Button(frame, text="Login", command=self.login_function, font=("times new roman", 15, "bold"),
                           bd=3, relief=RIDGE, bg="white", fg="black", activeforeground="white", activebackground="black")
        login_btn.place(x=110, y=320, width=120, height=35)

        # Create New Account Label (clickable)
        create_account = Button(frame, text="Create New Account", command=self.create_account, font=("times new roman", 12),
                                bd=0, relief=FLAT, bg="black", fg="white", activeforeground="white", activebackground="black")
        create_account.place(x=10, y=370, width=150)

        # Forgot Password Label (clickable)
        forgot_pass = Button(frame, text="Forgot Password?", command=self.forgot_password, font=("times new roman", 12),
                             bd=0, relief=FLAT, bg="black", fg="white", activeforeground="white", activebackground="black")
        forgot_pass.place(x=10, y=400, width=150)

    def login_function(self):    
        username = self.txtuser.get().strip()
        password = self.txtpass.get().strip()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required!")
            return
        
        # Hash the entered password to compare with the hashed password in the database
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Connect to the database and check if the username and password match
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",        # Your MySQL username
                password="vishal0228",  # Your MySQL password
                database="registation"  # Your database name
            )
            cursor = connection.cursor()

            # Query to check if username and password exist in the database
            query = "SELECT * FROM users WHERE email = %s AND password = %s"
            cursor.execute(query, (username, hashed_password))
            result = cursor.fetchone()

            # If a match is found, allow login
            if result:
                messagebox.showinfo("Success", "Login successful!")

                # Close the current login window and open Hotel Management System
                self.root.destroy()  # Close the login window

                # Open the Hotel Management System
                hotel_root = Tk()  # Create a new Tkinter root window for HotelManagementSystem
                app = HotelManagementSystem(hotel_root)  # Create an instance of HotelManagementSystem
                hotel_root.mainloop()  # Start the Hotel Management System window
                # You can open a new window or proceed with the application
                # self.open_main_application()
            else:
                messagebox.showerror("Error", "Invalid Username or Password!")

            cursor.close()
            connection.close()
        
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {str(err)}")

    def create_account(self):
        self.new_window = Toplevel(self.root)
        self.app = Registration_Window(self.new_window)

    def forgot_password(self):
        # Creating a new window for forgot password
        self.forgot_password_window = Toplevel(self.root)
        self.forgot_password_window.title("Forgot Password")
        self.forgot_password_window.geometry("500x500+500+150")
        self.forgot_password_window.configure(bg="#f7f7f7")

        # Adding title
        title_label = Label(self.forgot_password_window, text="Forgot Password?", font=("Helvetica", 18, "bold"), bg="#f7f7f7", fg="black")
        title_label.pack(pady=20)

        # Email Label and Entry
        label_email = Label(self.forgot_password_window, text="Enter your registered email:", font=("Helvetica", 12,"bold"), bg="#f7f7f7", fg="black")
        label_email.pack(pady=10)

        self.entry_email = Entry(self.forgot_password_window, width=30, font=("Helvetica", 12), bd=2)
        self.entry_email.pack(pady=10)

        # Security Question Label and Combobox
        self.security_question_label = Label(self.forgot_password_window, text="Select Security Question:", font=("Helvetica", 12,"bold"), bg="#f7f7f7", fg="black")
        self.security_question_label.pack(pady=10)

        self.security_combo = ttk.Combobox(self.forgot_password_window, values=["Your pet's name?", "Your birth city?", "Your favorite book?"], font=("Helvetica", 12,"bold"))
        self.security_combo.pack(pady=10)
        self.security_combo.current(0)  # Set default selection

        # Security Answer Label and Entry
        label_sec_answer = Label(self.forgot_password_window, text="Answer:", font=("Helvetica", 12,"bold"), bg="#f7f7f7", fg="black")
        label_sec_answer.pack(pady=10)

        self.entry_sec_answer = Entry(self.forgot_password_window, width=30, font=("Helvetica", 12,"bold"), bd=2)
        self.entry_sec_answer.pack(pady=10)

        # Add Reset Password Button
        self.reset_password_button = Button(self.forgot_password_window, text="Reset Password", command=self.reset_password, font=("Helvetica", 12,"bold"), bg="blue", fg="white", activebackground="blue", activeforeground="white", bd=0)
        self.reset_password_button.pack(pady=30)

    def reset_password(self):
        email = self.entry_email.get().strip()
        security_question = self.security_combo.get().strip()
        security_answer = self.entry_sec_answer.get().strip()

        if email == "" or security_question == "" or security_answer == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.forgot_password_window)
            return

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="vishal0228",
                database="registation"
            )
            cursor = connection.cursor()

            # Query to find the user by email, security question, and answer
            query = "SELECT * FROM users WHERE email = %s AND security_question = %s AND security_answer = %s"
            cursor.execute(query, (email, security_question, security_answer))
            result = cursor.fetchone()

            if result:
                # If the user exists, allow them to reset their password
                new_password = simpledialog.askstring("Reset Password", "Enter your new password:", show='*', parent=self.forgot_password_window)
                if new_password:
                    hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()
                    update_query = "UPDATE users SET password = %s WHERE email = %s"
                    cursor.execute(update_query, (hashed_new_password, email))
                    connection.commit()

                    # Confirmation Window
                    messagebox.showinfo("Success", "Password reset successful!", parent=self.forgot_password_window)
                    self.forgot_password_window.destroy()  # Close the forgot password window
            else:
                messagebox.showerror("Error", "Invalid details. User not found!", parent=self.forgot_password_window)

            cursor.close()
            connection.close()
        
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {str(err)}", parent=self.forgot_password_window)



        #messagebox.showinfo("Forgot Password", "Forgot Password functionality to be implemented.")

class Registration_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1600x900")

        img3=Image.open(r"D:\Hotel Management\bed.jpg")
        img3=img3.resize((1500,900),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)


        lblimg=Label(self.root,image=self.photoimg3,bd=4)
        lblimg.place(x=0,y=0,width=1500,height=700)

        # Load the background image
       # background_image = Image.open(r"D:\Hotel Management\pp.jpg")
       # background_photo = ImageTk.PhotoImage(background_image)
        

        # Create a label for background
       # bg_label = Label(self.root, image=background_photo)
        #bg_label.place(relwidth=1, relheight=1)

        # Create a frame to hold the form fields
        frame = Frame(self.root, bg="white", bd=5)
        frame.place(relx=0.5, rely=0.5, relwidth=0.55, relheight=0.75, anchor="center")

        # Title
        label_title = Label(frame, text="REGISTER HERE", font=("Arial", 16), fg="red", bg="white")
        label_title.grid(row=0, column=1, columnspan=2, pady=10)

        # First Name
        label_firstname = Label(frame, text="First Name:", bg="white", font=("times new roman", 12, "bold"))
        label_firstname.grid(row=1, column=0, padx=10, pady=5)
        self.entry_firstname = Entry(frame)
        self.entry_firstname.grid(row=1, column=1, padx=10, pady=5)

        # Last Name
        label_lastname = Label(frame, text="Last Name:", bg="white", font=("times new roman", 12, "bold"))
        label_lastname.grid(row=1, column=2, padx=10, pady=5)
        self.entry_lastname = Entry(frame)
        self.entry_lastname.grid(row=1, column=3, padx=10, pady=5)

        # Contact No
        label_contact = Label(frame, text="Contact No:", bg="white", font=("times new roman", 12, "bold"))
        label_contact.grid(row=2, column=0, padx=10, pady=5)
        self.entry_contact = Entry(frame)
        self.entry_contact.grid(row=2, column=1, padx=10, pady=5)

        # Email
        label_email = Label(frame, text="Email:", bg="white", font=("times new roman", 12, "bold"))
        label_email.grid(row=2, column=2, padx=10, pady=5)
        self.entry_email = Entry(frame)
        self.entry_email.grid(row=2, column=3, padx=10, pady=5)

        # Security Question
        label_sec_question = Label(frame, text="Select Security Question:", bg="white", font=("times new roman", 12, "bold"))
        label_sec_question.grid(row=3, column=0, padx=10, pady=5)
        self.security_combo = ttk.Combobox(frame, values=["Your pet's name?", "Your birth city?", "Your favorite book?"])
        self.security_combo.grid(row=3, column=1, padx=10, pady=5)

        # Security Answer
        label_sec_answer = Label(frame, text="Security Answer:", bg="white", font=("times new roman", 12, "bold"))
        label_sec_answer.grid(row=4, column=0, padx=10, pady=5)
        self.entry_sec_answer = Entry(frame)
        self.entry_sec_answer.grid(row=4, column=1, padx=10, pady=5)

        # Password
        label_password = Label(frame, text="Password:", bg="white", font=("times new roman", 12, "bold"))
        label_password.grid(row=5, column=0, padx=10, pady=5)
        self.entry_password = Entry(frame, show='*')
        self.entry_password.grid(row=5, column=1, padx=10, pady=5)

        # Confirm Password
        label_confirm_password = Label(frame, text="Confirm Password:", bg="white", font=("times new roman", 12, "bold"))
        label_confirm_password.grid(row=5, column=2, padx=10, pady=5)
        self.entry_confirm_password = Entry(frame, show='*')
        self.entry_confirm_password.grid(row=5, column=3, padx=10, pady=5)

        # Register Button
        self.button_register = Button(frame, text="Register", command=self.register_user, bg="green", fg="white")
        self.button_register.grid(row=6, columnspan=2, pady=20)

        # Redirect to login page
        self.redirect_login = Button(frame, text="Already have an account? Login", command=self.redirect_to_login, bg="blue", fg="white")
        self.redirect_login.grid(row=7, columnspan=2)

    def validate_email(self, email):
        # Simple regex for email validation
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email)

    def register_user(self):
        first_name = self.entry_firstname.get().strip()
        last_name = self.entry_lastname.get().strip()
        contact_no = self.entry_contact.get().strip()
        email = self.entry_email.get().strip()
        security_question = self.security_combo.get().strip()
        security_answer = self.entry_sec_answer.get().strip()
        password = self.entry_password.get().strip()
        confirm_password = self.entry_confirm_password.get().strip()

        if (not first_name or not last_name or not contact_no or
            not email or not security_question or
            not security_answer or not password or not confirm_password):
            messagebox.showerror("Error", "All fields are required!")
            return

        if not self.validate_email(email):
            messagebox.showerror("Error", "Invalid email format!")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        # Hash the password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Connect to the database and insert the new user
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",        # Your MySQL username
                password="vishal0228",  # Your MySQL password
                database="registation"  # Your database name
            )
            cursor = connection.cursor()

            # Insert new user into the database
            query = "INSERT INTO users (first_name, last_name, contact_no, email, security_question, security_answer, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (first_name, last_name, contact_no, email, security_question, security_answer, hashed_password))
            connection.commit()

            messagebox.showinfo("Success", "Registration successful!")
            cursor.close()
            connection.close()
            self.redirect_to_login()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {str(err)}")

    def redirect_to_login(self):
        self.root.destroy()  # Close the registration window
        root = Tk()
        app = Login_Window(root)
   
  


if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
