# importing modules/libraries
import sqlite3 as sq
from sqlite3.dbapi2 import Cursor
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox


# Connecting with DB and creating tables
try:
    con = sq.connect(database="database/main.sqlite")
    cursor = con.cursor()
    cursor.execute(
        "create table customer(name text, address text, mobile text, nationality text, aadhar integer, email text, gender text, father_name text)")
    con.commit()
    # print("Table created")
except:
    print("table already exists")
con.close()

# Creating Tk class object
win = Tk()

width = win.winfo_screenwidth()  # get Windows width size
height = win.winfo_screenheight()  # get Windows height size

win.geometry("%dx%d" % (width, height))
win.resizable('False', 'False')
win.state('zoomed')
win.title('Add Customer Details')


# loading images and converting to tkinter format
logo_img = Image.open('images/logo.jpg').resize((120, 89))
logo_img_tk = ImageTk.PhotoImage(logo_img, master=win)


logo_img_lb = Label(win, image=logo_img_tk, bg='black')
logo_img_lb.place(x=0, y=0)

title_lb = Label(win, text="Add Customer Details", bg='#000000',fg='#FFFFFF', font=('Ariel', 47), width=40)
title_lb.place(relx=.05, rely=0)


# Customer details frame
cus_detail_frame = Frame(win)
cus_detail_frame.place(relx=.01, rely=.1, relwidth=.4, relheight=.85)


# Details inside Customer details frame
cus_detail_lbl = Label(cus_detail_frame, text="Customer Details", font=('Ariel', 18, "bold"))
cus_detail_lbl.place(relx=.01, rely=.01)

cus_name = Label(cus_detail_frame, text="Name:", font=('Ariel', 14))
cus_name.place(relx=.01, rely=.1)

cus_address = Label(cus_detail_frame, text="Address:", font=('Ariel', 14))
cus_address.place(relx=.01, rely=.2)

cus_mobile = Label(cus_detail_frame, text="Mobile No.:", font=('Ariel', 14))
cus_mobile.place(relx=.01, rely=.3)

cus_nationality = Label(cus_detail_frame, text="Nationality:", font=('Ariel', 14))
cus_nationality.place(relx=.01, rely=.4)

cus_aadhar = Label(cus_detail_frame, text="Aadhar Number:", font=('Ariel', 14))
cus_aadhar.place(relx=.01, rely=.5)

cus_email = Label(cus_detail_frame, text="Email:", font=('Ariel', 14))
cus_email.place(relx=.01, rely=.6)

cus_gender = Label(cus_detail_frame, text="Gender:", font=('Ariel', 14))
cus_gender.place(relx=.01, rely=.7)

cus_father = Label(cus_detail_frame, text="Father's name:", font=('Ariel', 14))
cus_father.place(relx=.01, rely=.8)

# Input boxes for Customer details
name_e = Entry(cus_detail_frame, font=('Ariel', 14), bd=5, fg='black')
name_e.place(relx=.5, rely=.1)

add_e = Entry(cus_detail_frame, font=('Ariel', 14), bd=5, fg='black')
add_e.place(relx=.5, rely=.2)

mobile_e = Entry(cus_detail_frame, font=('Ariel', 14), bd=5, fg='black')
mobile_e.place(relx=.5, rely=.3)

nationality_e = Entry(cus_detail_frame, font=('Ariel', 14), bd=5, fg='black')
nationality_e.place(relx=.5, rely=.4)

aadhar_e = Entry(cus_detail_frame, font=('Ariel', 14), bd=5, fg='black')
aadhar_e.place(relx=.5, rely=.5)

email_e = Entry(cus_detail_frame, font=('Ariel', 14), bd=5, fg='black')
email_e.place(relx=.5, rely=.6)

cus_gender_e = Combobox(cus_detail_frame, values=['Male', 'Female', "Prefer not to say"], font=('Ariel', 14))
cus_gender_e.place(relx=.5, rely=.7)

father_e = Entry(cus_detail_frame, font=('Ariel', 14), bd=5, fg='black')
father_e.place(relx=.5, rely=.8)


# function to add detials to DB
def add(event):
    """
    Add operation to add all the input details to SQL database table
    """
    n = name_e.get()
    ad = add_e.get()
    mob = mobile_e.get()
    nat = nationality_e.get()
    aadhar = aadhar_e.get()
    email = email_e.get()
    gender = cus_gender_e.get()
    father = father_e.get()

    if (len(n) or len(ad) or len(mob) or len(nat) or len(aadhar) or len(email) or len(gender) or len(father)) == 0:
        messagebox.showerror("Error", "Fields cannot be blank")
    else:
        try:
            con = sq.connect(database="database/main.sqlite")
            cursor = con.cursor()
            cursor.execute("insert into customer values(?,?,?,?,?,?,?,?)",
                           (n, ad, mob, nat, aadhar, email, gender, father))
            con.commit()
            messagebox.showinfo("Success", "Details added")
        except:
            messagebox.showerror(
                "Error", "Error occured. Try again after sometime")

        con.close()


# Function to update customer details on the basis of their name
def update(event):
    """
    Event listener to update Customer record on the basis on name
    """
    n = name_e.get()
    ad = add_e.get()
    mob = mobile_e.get()
    nat = nationality_e.get()
    aadhar = aadhar_e.get()
    email = email_e.get()
    gender = cus_gender_e.get()
    father = father_e.get()

    response = messagebox.askyesno(
        "Update Details", "Update details for {}?".format(n))

    if response:
        try:
            con = sq.connect(database="database/main.sqlite")
            cursor = con.cursor()
            cursor.execute("UPDATE customer SET address=?, mobile=?, nationality=?, aadhar=?, email=?, father_name=? WHERE name=?",
                           (ad, mob, nat, aadhar, email, father, n))
            con.commit()
            con.close()
            messagebox.showinfo("Updated", "Details updated!")
        except:
            messagebox.showerror(
                "Error", "Error occured updating the record. Try again after sometime")
    else:
        messagebox.showinfo("Update Details", "Details not updated!")


# Function to delete customer record on the basis of their name
def delete(event):
    """"
    Event listner to delete the customer record on the basis of their Mobile number
    """
    n = name_e.get()
    ad = add_e.get()
    mob = mobile_e.get()
    nat = nationality_e.get()
    aadhar = aadhar_e.get()
    email = email_e.get()
    gender = cus_gender_e.get()
    father = father_e.get()

    if (len(n) and len(mob)) == 0:
        messagebox.showerror(
            "Error", "Name and Mobile number field cannot be blank ")
    else:
        response = messagebox.askyesno(
            "Delete Details", "Do you want to delete record for {}? ".format(n))

        if response:
            try:
                con = sq.connect(database="database/main.sqlite")
                cursor = con.cursor()
                cursor.execute("DELETE from customer WHERE mobile=?", (mob,))
                con.commit()
                messagebox.showinfo("Deleted", "Deleted Successfully")
            except:
                messagebox.showerror(
                    "Error", "Record could not be deleted. Try again after sometime")

            con.close()


#Function to reset all the input fields to blank
def reset(event):
    """"
    Event listener for reset button. 
    Resets all the values in the input field to blank
    """

    name_e.delete(0, "end")
    add_e.delete(0, "end")
    mobile_e.delete(0, "end")
    nationality_e.delete(0, "end")
    aadhar_e.delete(0, "end")
    email_e.delete(0, "end")
    cus_gender_e.delete(0, "end")
    father_e.delete(0, "end")

    name_e.focus()


#CRUD Buttons
add_btn = Button(cus_detail_frame, text="Add", font=(
    'Ariel', 12, 'bold'), bg='black', fg='yellow', width=12)
add_btn.place(relx=.01, rely=.9)
add_btn.bind("<Button>", add)  # Todo

update_btn = Button(cus_detail_frame, text="Update", font=(
    'Ariel', 12, 'bold'), bg='black', fg='yellow', width=12)
update_btn.place(relx=.25, rely=.9)
update_btn.bind("<Button>", update)  # Todo

delete_btn = Button(cus_detail_frame, text="Delete", font=(
    'Ariel', 12, 'bold'), bg='black', fg='yellow',  width=12)
delete_btn.place(relx=.49, rely=.9)
delete_btn.bind("<Button>", delete)  # Todo

reset_btn = Button(cus_detail_frame, text="Reset", font=(
    'Ariel', 12, 'bold'), bg='black', fg='yellow',  width=12)
reset_btn.place(relx=.73, rely=.9)
reset_btn.bind("<Button>", reset)  # Todo


# Show Customer detail frame
search_view_frame = Frame(win)
search_view_frame.place(relx=0.43, rely=.1, relwidth=.55, relheight=.85)

view_detail_lbl = Label(
    search_view_frame, text="View Detail and Search System", font=('Ariel', 18, "bold"))
view_detail_lbl.place(relx=.01, rely=.01)

search_by = Label(search_view_frame, text="Search By",
                  font=('Ariel', 18, "bold"), bg='red', fg='white')
search_by.place(relx=.01, rely=.1)

search_combo = Combobox(search_view_frame, values=[
                        'Name', 'Mobile', "Email", "Aadhar"], font=('Ariel', 18, 'bold'), width=10)
search_combo.place(relx=.2, rely=.1)

search_input = Entry(search_view_frame, font=('Ariel', 18), width=17)
search_input.place(relx=.4, rely=.1)


#Function to display records of customer according to Category select and input provided by user in the input field
def search(event):
    """"
    Search event listner to display records according category and input provided by user
    """
    category = search_combo.get()
    u_input = str(search_input.get())

    if len(u_input) == 0:
        messagebox.showerror("Error!", "Input Field cannot be blank")
    else:
        con = sq.connect(database="database/main.sqlite")
        cursor = con.cursor()
        if category == "Name":
            cursor.execute("select * from customer where name=?", (u_input,))
        elif category == "Mobile":
            cursor.execute("select * from customer where mobile=?", (u_input,))
        elif category == "Aadhar":
            cursor.execute("select * from customer where aadhar=?", (u_input,))
        elif category == "Email":
            cursor.execute("select * from customer where email=?", (u_input,))

        info = ""
        for row in cursor:
            info = info + "\n" + "\t" + row[0] + "\t\t" + row[1] + "\t\t" + row[2] + "\t\t" + row[3] + \
                "\t\t\t" + str(row[4]) + "\t\t\t" + row[5] + \
                "\t\t\t" + row[6] + "\t\t\t" + row[7] + "\t"

        st.insert("end", info)


def showall(event):
    """
    Event listner to display all records from the database
    """
    con = sq.connect(database="database/main.sqlite")
    cursor = con.cursor()
    cursor.execute("SELECT * from customer")

    info = ""
    for row in cursor:
        info = info + "\n" + "\t" + row[0] + "\t\t" + row[1] + "\t\t" + row[2] + "\t\t" + row[3] + \
            "\t\t\t" + str(row[4]) + "\t\t\t" + row[5] + \
            "\t\t\t" + row[6] + "\t\t\t" + row[7] + "\t"

    st.insert("end", info)


search_btn = Button(search_view_frame, text="Search", font=(
    'Ariel', 12, 'bold'), bg='black', fg='yellow',  width=12)
search_btn.place(relx=.7, rely=.1)
search_btn.bind("<Button>", search)  # Todo

showall_btn = Button(search_view_frame, text="Show all", font=(
    'Ariel', 12, 'bold'), bg='black', fg='yellow',  width=12)
showall_btn.place(relx=.85, rely=.1)
showall_btn.bind("<Button>", showall)

hori_scroll = Scrollbar(search_view_frame, orient='horizontal')
hori_scroll.pack(side=BOTTOM, fill='x')


st = Text(search_view_frame, height=28, width=90, wrap="none",
          xscrollcommand=hori_scroll.set, font=("Arial", 12, "bold"))
st.place(relx=.04, rely=.2)
# st.pack()
st.insert("end", "\tName\t\tAddress\t\tMobile\t\tNationality\t\t\tAadhar\t\t\tEmail\t\t\tGender\t\tFather's name\t\n")
st.insert("end", "------------------------------------------------------------------------------------------------------------"
          "--------------------------------------------------------------------------------------------------------------------------------------------")
hori_scroll.config(command=st.xview)

win.mainloop()
