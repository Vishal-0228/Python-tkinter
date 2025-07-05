from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from time import strftime
from datetime import datetime 

class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        
        lbl_title=Label(self.root,text="RoomBooking DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1295,height=50)

        img2=Image.open(r"D:\Hotel Management\logohotel.png")
        img2=img2.resize((100,50),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        lblimg=Label(self.root,image=self.photoimg2,bd=4)
        lblimg.place(x=5,y=2,width=100,height=50)

        
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)
       ##Floor
        lbl_floor=Label(labelframeleft,text="Floor:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_Floor=StringVar()
        enty_floor=ttk.Entry(labelframeleft,textvariable=self.var_Floor,width=20,font=("times new roman",13,"bold"))
        enty_floor.grid(row=0,column=1,sticky=W)

        ##ROOM NO

        lbl_RoomNo=Label(labelframeleft,text="Room No:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)

        self.var_RoomNo=StringVar()

        enty_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_RoomNo,width=20,font=("times new roman",13,"bold"))
        enty_RoomNo.grid(row=1,column=1,sticky=W)

        ## ROOM TYPE
        lbl_RoomType=Label(labelframeleft,text="Room Type:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)

        self.var_RoomType=StringVar()

        enty_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,width=20,font=("times new roman",13,"bold"))
        enty_RoomType.grid(row=2,column=1,sticky=W)

         #Buttons 
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        btnReset.grid(row=0,column=3,padx=1)
                            ##Table Frame

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details ",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=600,y=55,width=600,height=350)

        ##Scroll Bar 

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_Frame,column=("Floor","RoomNo","RoomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)


        self.room_table.heading("Floor",text="Floor")
        self.room_table.heading("RoomNo",text="RoomNo")
        self.room_table.heading("RoomType",text="RoomType")

        self.room_table["show"]="headings"

        self.room_table.column("Floor",width=100)
        self.room_table.column("RoomNo",width=100)
        self.room_table.column("RoomType",width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
               if self.var_Floor.get()==""or self.var_RoomType.get()=="":
                    messagebox.showerror("Error","All fields are required",parent=self.root)
               else:
                   try:
                            conn=mysql.connector.connect(host="localhost",username="root",password="vishal0228",database="management")
                            my_cursor=conn.cursor()
                            sql="""INSERT INTO details (`Floor`,`RoomNo`,`RoomType`) VALUES ( %s, %s, %s)"""
                            values= ( 
                                                                               self.var_Floor.get(),
                                                                               self.var_RoomNo.get(),
                                                                               self.var_RoomType.get(),
                                                                                                                
                                                                         
                                                                                        
                                                                                           
                                                                       

                                                                                    )
                            print("SQL Query:", sql)
                            print("Values:", values)
                            my_cursor.execute(sql,values)

                            conn.commit()
                            self.fetch_data()
                            conn.close()

                            messagebox.showinfo("Success","New Room Added Successfully ",parent=self.root)
                   except mysql.connector.Error as err:
                           messagebox.showwarning("Warning", f"Database error: {str(err)}", parent=self.root)
                   except Exception as es:
                           messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)  

    def fetch_data(self):
           conn=mysql.connector.connect(host="localhost",username="root",password="vishal0228",database="management")
           my_cursor=conn.cursor()
           my_cursor.execute("select*from details")
           rows=my_cursor.fetchall()
           if len(rows)!=0:
                   self.room_table.delete(*self.room_table.get_children())
                   for i in rows:
                           self.room_table.insert("",END,values=i)
                   conn.commit() 
                   conn.close() 

    def get_cursor(self,event=""):
            cursor_row=self.room_table.focus()
            content=self.room_table.item(cursor_row)
            row=content["values"]
            
            self.var_Floor.set(row[0])
            self.var_RoomNo.set(row[1]),
            self.var_RoomType.set(row[2])
            

    
    def update(self):
       if self.var_Floor.get() == "" or self.var_RoomType.get() == "":
        messagebox.showerror("Error", "Please enter Floor Number ", parent=self.root)
       else:
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="vishal0228", database="management")
            my_cursor = conn.cursor()

            # Correct SQL query with backticks around column names
            sql = """UPDATE details SET `Floor`=%s, `RoomType`=%s WHERE `RoomNo`=%s"""
            values = (self.var_Floor.get(), self.var_RoomType.get(), self.var_RoomNo.get())

            # Execute the query
            my_cursor.execute(sql, values)

            # Check how many rows were affected
            if my_cursor.rowcount == 0:
                messagebox.showwarning("Warning", "No rows were updated. Check the Room No.", parent=self.root)
            else:
                conn.commit()  # Commit the transaction
                messagebox.showinfo("Success", "Room Details Updated Successfully", parent=self.root)

            conn.close()

        except mysql.connector.Error as err:
            messagebox.showwarning("Warning", f"Database error: {str(err)}", parent=self.root)
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def delete(self):
            delete=messagebox.askyesno("Hotel Management Sysytem","Do you want to delete this Room details ",parent=self.root)
            if delete>0:
                     conn = mysql.connector.connect(host="localhost", username="root", password="vishal0228", database="management")
                     my_cursor = conn.cursor()
                     query="delete from details where RoomNo=%s"
                     values=(self.var_RoomNo.get(),)
                     my_cursor.execute(query,values)
            else:
                if not delete:
                        return
            conn.commit()
            self.fetch_data()
            conn.close()   

          ##Reset data 
    def reset(self):
          self.var_Floor.set("  "),
          self.var_RoomNo.set("  "),
          self.var_RoomType.set("  ")
             




if __name__ == '__main__':
                     root = Tk()
                     obj = DetailsRoom(root)
                     root.mainloop()
()

