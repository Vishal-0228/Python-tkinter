from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox 


class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1150x550+230+220") ##Width , Height , X axis , Y axis 
        ##SQL variable 
        self.var_cust_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_cust_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_cust_mother=StringVar()
        self.var_cust_gender=StringVar()
        self.var_cust_postcode =StringVar()
        self.var_cust_mobile=StringVar()
        self.var_cust_email=StringVar()
        self.var_cust_nationality=StringVar()
        self.var_cust_address=StringVar()
        self.var_cust_Idproof=StringVar()
        #self.var_cust_idnumber=StringVar()


               ##Title Label and image 

        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1295,height=50)

        img2=Image.open(r"D:\Hotel Management\logohotel.png")
        img2=img2.resize((100,50),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img2)


        lblimg=Label(self.root,image=self.photoimg1,bd=4)
        lblimg.place(x=5,y=2,width=100,height=50)


        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

       ##Cust REff
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_cust_ref,width=29,font=("times new roman",13,"bold"),state="readonly")
        enty_ref.grid(row=0,column=1)

 ##Cust name
        cname=Label(labelframeleft,text="Customer Name",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
    

        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=29,font=("arial",13,"bold"))
        txtcname.grid(row=1,column=1)


 ##Mother name 
        lblmname=Label(labelframeleft,text="Mother Name",font=("arial",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)

        txtmname=ttk.Entry(labelframeleft, textvariable=self.var_cust_mother,width=29,font=("arial",13,"bold"))
        txtmname.grid(row=2,column=1)

 ##Gender  combbox
        label_gender=Label(labelframeleft,text="Gender",font=("arial",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_cust_gender,font=("arial",13,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        


 ##Postcode 
        lblPostCode=Label(labelframeleft,text="PostCode",font=("arial",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)

        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_cust_postcode,width=29,font=("arial",13,"bold"))
        txtPostCode.grid(row=4,column=1)


         ##Mobile Number
        lblMobile=Label(labelframeleft,text="Mobile Number",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)

        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_cust_mobile,width=29,font=("arial",13,"bold"))
        txtMobile.grid(row=5,column=1)



         ##Email 
        lblEmail=Label(labelframeleft,text="Email",font=("arial",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)

        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_cust_email,width=29,font=("arial",13,"bold"))
        txtEmail.grid(row=6,column=1)

        #Nationality
        lblNationality=Label(labelframeleft,text="Nationality",font=("arial",12,"bold"),padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_cust_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Nationality["value"]=("Indian","Americian","Austrilian")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)


  ##idproff type combobox
        lblIdproof=Label(labelframeleft,text="Id proof Type",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdproof.grid(row=8,column=0,sticky=W)

        combo_Id=ttk.Combobox(labelframeleft,textvariable=self.var_cust_Idproof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Id["value"]=("Addhar Card","Pan Card","Driving License")
        combo_Id.current(0)
        combo_Id.grid(row=8,column=1)




          ##id number 
        #lblIdNumber=Label(labelframeleft,text="Id Number",font=("arial",12,"bold"),padx=2,pady=6)
        #lblIdNumber.grid(row=9,column=0,sticky=W)

        #txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_cust_idnumber,width=29,font=("arial",13,"bold"))
        #txtIdNumber.grid(row=9,column=1)



          ##Address
        lblAddress=Label(labelframeleft,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)

        txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_cust_address,width=29,font=("arial",13,"bold"))
        txtAddress.grid(row=10,column=1)


    #Buttons 
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=350,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #Tabel Frame
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=50,width=860,height=490)


        lblSearchBy=Label(Table_Frame,text="SearchBy:",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.search_var=StringVar()


        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=17,state="readonly")
        combo_Search["value"]=("Mobile","Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1)

        self.txt_search=StringVar

        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)


        ## Show Data Table 

        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350) 

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","postcode","mobile","email","nationality","Idproof","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("postcode",text="Postcode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        #self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")
        self.Cust_Details_Table.heading("Idproof",text="Idproof")


        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("postcode",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        #self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)
        self.Cust_Details_Table.column("Idproof",width=100)
        


        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
               if self.var_cust_mobile.get()==""or self.var_cust_mother.get()=="":
                    messagebox.showerror("Error","All fields are required",parent=self.root)
               else:
                   try:
                            conn=mysql.connector.connect(host="localhost",username="root",password="vishal0228",database="management")
                            my_cursor=conn.cursor()
                            sql="""INSERT INTO customer (ref, name, mother,gender,postcode, mobile, email,nationality,Idproof,address) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"""
                            values= (                                                      self.var_cust_ref.get(),
                                                                                           self.var_cust_name.get(),
                                                                                           self.var_cust_mother.get(),
                                                                                           self.var_cust_gender.get(),
                                                                                           self.var_cust_postcode.get(),
                                                                                           self.var_cust_mobile.get(),
                                                                                           self.var_cust_email.get(),
                                                                                           self.var_cust_nationality.get(),
                                                                                           self.var_cust_Idproof.get(),
                                                                                           #self.var_cust_idnumber.get(),
                                                                                           self.var_cust_address.get(),
                                                                                           

                                                                                    )
                            print("SQL Query:", sql)
                            print("Values:", values)
                            my_cursor.execute(sql,values)

                            conn.commit()
                            self.fetch_data()
                            conn.close()

                            messagebox.showinfo("Success","customer has been added",parent=self.root)
                   except mysql.connector.Error as err:
                           messagebox.showwarning("Warning", f"Database error: {str(err)}", parent=self.root)
                   except Exception as es:
                           messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
           conn=mysql.connector.connect(host="localhost",username="root",password="vishal0228",database="management")
           my_cursor=conn.cursor()
           my_cursor.execute("select*from customer")
           rows=my_cursor.fetchall()
           if len(rows)!=0:
                   self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                   for i in rows:
                           self.Cust_Details_Table.insert("",END,values=i)
                   conn.commit()
           conn.close()

    def get_cursor(self,event=""):
            cursor_row=self.Cust_Details_Table.focus()
            content=self.Cust_Details_Table.item(cursor_row)
            row=content["values"]
            
            self.var_cust_ref.set(row[0]),
            self.var_cust_name.set(row[1]),
            self.var_cust_mother.set(row[2]),
            self.var_cust_gender.set(row[3]),

            self.var_cust_postcode.set(row[4]),
            self.var_cust_mobile.set(row[5]),
            self.var_cust_email.set(row[6]),
            self.var_cust_nationality.set(row[7]),
            self.var_cust_Idproof.set(row[8]),
            #self.var_cust_idnumber.set(row[9]),
            self.var_cust_address.set(row[10])
            

          
    
    def update(self):
             if self.var_cust_mobile.get()=="":
                     messagebox.showerror("Error","Please enter mobile number",parent=self.root)
             else:
                 
                     conn = mysql.connector.connect(host="localhost", username="root", password="vishal0228", database="management")
                     my_cursor = conn.cursor()
                     my_cursor.execute(
        """UPDATE customer 
           SET name=%s, mother=%s, gender=%s, postcode=%s, mobile=%s, email=%s, nationality=%s, idproof=%s, idnumber=%s, address=%s 
           WHERE ref=%s""",
             (   
                    self.var_cust_name.get(),
                    self.var_cust_mother.get(),
                    self.var_cust_gender.get(),
                    self.var_cust_postcode.get(),
                    self.var_cust_mobile.get(),
                    self.var_cust_email.get(),
                    self.var_cust_nationality.get(),
                    self.var_cust_Idproof.get(),
                    #self.var_cust_idnumber.get(),
                    self.var_cust_address.get(),
                    self.var_cust_ref.get()
            
        )
    )
             conn.commit()
             self.fetch_data()
             conn.close()
             messagebox.showinfo("Update", "Customer details have been updated successfully", parent=self.root)

    def delete(self):
            delete=messagebox.askyesno("Hotel Management Sysytem","Do you want to delete this customer",parent=self.root)
            if delete>0:
                     conn = mysql.connector.connect(host="localhost", username="root", password="vishal0228", database="management")
                     my_cursor = conn.cursor()
                     query="delete from customer where Ref=%s"
                     values=(self.var_cust_ref.get(),)
                     my_cursor.execute(query,values)
            else:
                if not delete:
                        return
            conn.commit()
            self.fetch_data()
            conn.close()

    def reset(self):
          
            #self.var_cust_ref.set(" ")
            self.var_cust_name.set(" "),
            self.var_cust_mother.set(" "),
            #self.var_cust_gender.set(" "),

            self.var_cust_postcode.set(" "),
            self.var_cust_mobile.set(" "),
            self.var_cust_email.set(" "),
            #self.var_cust_nationality.set(" "),
            #self.var_cust_Idproof.set(" "),
            #self.var_cust_idnumber.set(" "),
            self.var_cust_address.set(" "),
            
            
            x=random.randint(1000,9999)
            self.var_cust_ref.set(str(x))

    def search(self):
        try:
              conn = mysql.connector.connect(host="localhost", username="root", password="vishal0228", database="management")
              my_cursor = conn.cursor()

              query="Select*from customer where "+str(self.search_var.get())+"LIKE'%"+str(self.txt_search.get())+"%'"
              my_cursor.execute(query)
              rows=my_cursor.fetchall()
              if len(rows)!=0:
                      self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                      for i in rows:
                              self.Cust_Details_Table.insert("",END,values=i)
                      conn.commit()
        except Exception as e:
                      messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)
        finally:
                conn.close()



if __name__ == '__main__':
                     root = Tk()
                     obj = Cust_Win(root)
                     root.mainloop()
()