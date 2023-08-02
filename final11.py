from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from tkcalendar import Calendar
from PIL import ImageTk, Image
import time

 

  
# Create object 
root = Tk()


#============================VARIABLES===================================
FIRSTNAME = StringVar()
LASTNAME = StringVar()
GENDER = StringVar()
AGE = StringVar()
ADDRESS = StringVar()
CONTACT = StringVar()
DEPT = StringVar()
YEAR = StringVar()
AADHAR = StringVar()
ROLL = StringVar()
REG = StringVar()




def Clear():
    for item in tree.get_children():
      tree.delete(item)
    
def Database():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

    
def cse1Database():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='CSE' AND `year`='First' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    
def cse2Database():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='CSE' AND `year`='Second' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def cse3Database():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='CSE' AND `year`='Third' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def cse4Database():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='CSE' AND `year`='Fourth' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def cseexDatabase():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='CSE' AND `year`='EX_STUDENT' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    
def ece1Database():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='ECE' AND `year`='First' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    
def ece2Database():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='ECE' AND `year`='Second' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def ece3Database():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='ECE' AND `year`='Third' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def ece4Database():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='ECE' AND `year`='Fourth' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def eceexDatabase():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='ECE' AND `year`='EX_STUDENT' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    
def ee1Database():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='EE' AND `year`='First' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    
def ee2Database():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='EE' AND `year`='Second' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def ee3Database():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='EE' AND `year`='Third' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def ee4Database():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='EE' AND `year`='Fourth' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def eeexDatabase():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='EE' AND `year`='EX_STUDENT' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    
def me1Database():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='ME' AND `year`='First' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    
def me2Database():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='ME' AND `year`='Second' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def me3Database():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='ME' AND `year`='Third' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def me4Database():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='ME' AND `year`='Fourth' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def meexDatabase():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='ME' AND `year`='EX_STUDENT' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    
def ce1Database():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='CE' AND `year`='First' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    
def ce2Database():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='CE' AND `year`='Second' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def ce3Database():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='CE' AND `year`='Third' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def ce4Database():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='CE' AND `year`='Fourth' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def ceexDatabase():
    for item in tree.get_children():
      tree.delete(item)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member1` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, dept TEXT, year TEXT, aadhar TEXT, roll TEXT, reg TEXT)")
    cursor.execute("SELECT * FROM `member1` WHERE `dept`='CE' AND `year`='EX_STUDENT' ORDER BY `mem_id` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()





def SubmitData():
    if  FIRSTNAME.get() == "" or LASTNAME.get() == "" or GENDER.get() == "" or AGE.get() == "" or ADDRESS.get() == "" or CONTACT.get() == "" or DEPT.get() == "" or YEAR.get() == "" or AADHAR.get() == "" or ROLL.get() == "" or REG.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `member1` (firstname, lastname, gender, age, address, contact, dept, year, aadhar, roll, reg) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(FIRSTNAME.get()),str(LASTNAME.get()), str(GENDER.get()), int(AGE.get()), str(ADDRESS.get()), str(CONTACT.get()), str(DEPT.get()), str(YEAR.get()), str(AADHAR.get()), str(ROLL.get()), str(REG.get())))
        conn.commit()
        cursor.execute("SELECT * FROM `member1` ORDER BY `lastname` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        FIRSTNAME.set("")
        LASTNAME.set("")
        GENDER.set("")
        AGE.set("")
        ADDRESS.set("")
        CONTACT.set("")
        DEPT.set("")
        YEAR.set("")
        AADHAR.set("")
        ROLL.set("")
        REG.set("")
        
    
   

def UpdateData():
    if GENDER.get() == "":
       result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE `member1` SET `firstname` = ?, `lastname` = ?, `gender` =?, `age` = ?,  `address` = ?, `contact` = ?, `dept` = ?, `year` = ?, `aadhar` = ?,`roll` = ?, `reg` = ? WHERE `mem_id` = ?", (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), str(AGE.get()), str(ADDRESS.get()), str(CONTACT.get()), str(DEPT.get()), str(YEAR.get()), str(AADHAR.get()), str(ROLL.get()), str(REG.get()), int(mem_id)))
        conn.commit()
        cursor.execute("SELECT * FROM `member1` ORDER BY `mem_id` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        FIRSTNAME.set("")
        LASTNAME.set("")
        GENDER.set("")
        AGE.set("")
        ADDRESS.set("")
        CONTACT.set("")
        DEPT.set("")
        YEAR.set("")
        AADHAR.set("")
        ROLL.set("")
        REG.set("")
        
    
def OnSelected(event):
    global mem_id, UpdateWindow
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    mem_id = selecteditem[0]
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    AGE.set("")
    ADDRESS.set("")
    CONTACT.set("")
    DEPT.set("")
    YEAR.set("")
    AADHAR.set("")
    ROLL.set("")
    REG.set("")
    FIRSTNAME.set(selecteditem[1])
    LASTNAME.set(selecteditem[2])
    AGE.set(selecteditem[4])
    ADDRESS.set(selecteditem[5])
    CONTACT.set(selecteditem[6])
    DEPT.set(selecteditem[7])
    YEAR.set(selecteditem[8])
    AADHAR.set(selecteditem[9])
    ROLL.set(selecteditem[10])
    REG.set(selecteditem[11])
    UpdateWindow = Toplevel()
    UpdateWindow.title("Contact List")
    width = 1200
    height = 650
    UpdateWindow.config(bg="#000000")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) + 450) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    UpdateWindow.resizable(0, 0)
    UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'NewWindow' in globals():
        NewWindow.destroy()

    #===================FRAMES==============================
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)
    ContactForm.config(bg="#000000")
    RadioGroup = Frame(ContactForm)
    RadioGroup1 = Frame(ContactForm)
    RadioGroup2 = Frame(ContactForm)
    RadioGroup3 = Frame(ContactForm)
    #=====================================================================================================================
    Male = Radiobutton(RadioGroup, text="MALE", variable=GENDER, value="Male",font=('Eras Bold ITC', 14), indicator = 0, background = "#FFFF00"  ).pack(ipadx = 110,ipady = 5)

    Female = Radiobutton(RadioGroup, text="FEMALE", variable=GENDER, value="Female", font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00"  ).pack( fill = X,ipady = 5)

    Others = Radiobutton(RadioGroup, text="OTHERS", variable=GENDER, value="Others", font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00"  ).pack( fill = X,ipady = 5)
   
    #=====================================================================================================================
    CSE = Radiobutton(RadioGroup1, text="CSE", variable=DEPT, value="CSE",font=('Eras Bold ITC', 14) , indicator = 0, background = "#FFFF00" ).pack(ipadx = 115,ipady = 5)
    
    ECE = Radiobutton(RadioGroup1, text="ECE", variable=DEPT, value="ECE",font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00"  ).pack(fill = X,ipady = 5)
    
    EE = Radiobutton(RadioGroup1, text="EE", variable=DEPT, value="EE",  font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00").pack( fill = X,ipady = 5)
   
    ME = Radiobutton(RadioGroup1, text="ME", variable=DEPT, value="ME",  font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00").pack( fill = X,ipady = 5)
  
    CE = Radiobutton(RadioGroup1, text="CE", variable=DEPT, value="CE",  font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00").pack( fill = X,ipady = 5)
  
    #====================================================================================================================
    First = Radiobutton(RadioGroup2, text="FIRST", variable=YEAR, value="First",  font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00").pack( ipadx = 110,ipady = 5)
   
    Second = Radiobutton(RadioGroup2, text="SECOND", variable=YEAR, value="Second",  font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00").pack( fill = X,ipady = 5)
    
    Third = Radiobutton(RadioGroup2, text="THIRD", variable=YEAR, value="Third",  font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00").pack(fill = X,ipady = 5)
  
    Fourth = Radiobutton(RadioGroup2, text="FOURTH", variable=YEAR, value="Fourth",  font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00").pack( fill = X,ipady = 5)
    
    EX_STUDENT = Radiobutton(RadioGroup2, text="EX_STUDENT", variable=YEAR, value="EX_STUDENT",  font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00").pack( fill = X,ipady = 5)
  
     


 

        
    #===================LABELS==============================
    lbl_title = Label(FormTitle, text="UPDATING EXISTING STUDENT DATA", font=('Cooper Std Black', 30,'bold'), bg="#FFFFFA",fg="#0000FF",  width = 300)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactForm, text="FIRST  NAME", font=('Eras Bold ITC', 16,'bold'), bd=5,bg="#000000", fg="#FFFFFA")
    lbl_firstname.grid(row=0, column=0, sticky=W)
    lbl_lastname = Label(ContactForm, text="LAST  NAME", font=('Eras Bold ITC', 16,'bold'), bd=5,bg="#000000", fg="#FFFFFA")
    lbl_lastname.grid(row=0,column=2, sticky=W)
    lbl_gender = Label(ContactForm, text="GENDER", font=('Eras Bold ITC', 16,'bold'), bd=5,bg="#000000", fg="#FFFFFA")
    lbl_gender.grid(row=2,column=0, sticky=W)
    lbl_age = Label(ContactForm, text="AGE", font=('Eras Bold ITC', 16,'bold'), bd=5,bg="#000000", fg="#FFFFFA")
    lbl_age.grid(row=8,column=2, sticky=W)
    lbl_address = Label(ContactForm, text="ADDRESS", font=('Eras Bold ITC', 16,'bold'), bd=5,bg="#000000", fg="#FFFFFA")
    lbl_address.grid(row=3,column=0, sticky=W)
    lbl_contact = Label(ContactForm, text="CONTACT", font=('Eras Bold ITC', 16,'bold'), bd=5,bg="#000000", fg="#FFFFFA")
    lbl_contact.grid(row=3,column=2, sticky=W)
    lbl_dept = Label(ContactForm, text="DEPARTMENT", font=('Eras Bold ITC', 16,'bold'), bd=5,bg="#000000", fg="#FFFFFA")
    lbl_dept.grid(row=4,column=0, sticky=W)
    lbl_year = Label(ContactForm, text="YEAR", font=('Eras Bold ITC', 16,'bold'), bd=5,bg="#000000", fg="#FFFFFA")
    lbl_year.grid(row=4, column=2,sticky=W)
    lbl_aadhar = Label(ContactForm, text="AADHAR  NO", font=('Eras Bold ITC', 16,'bold'), bd=5,bg="#000000", fg="#FFFFFA")
    lbl_aadhar.grid(row=8, column =0, sticky=W)
    lbl_roll = Label(ContactForm, text="ROLL  NO", font=('Eras Bold ITC', 16,'bold'), bd=5,bg="#000000", fg="#FFFFFA")
    lbl_roll.grid(row=9, column =0, sticky=W)
    lbl_reg = Label(ContactForm, text="UNIVERSITY  REGISTRATION  NO", font=('Eras Bold ITC', 16,'bold'),bg="#000000", fg="#FFFFFA")
    lbl_reg.grid(row=9, column =2, sticky=W)
     
   



    #===================ENTRY===============================
    firstname = Entry(ContactForm, textvariable=FIRSTNAME, font=('Eras Bold ITC', 16),bg="#FFFFFA", fg="#0000FF")
    firstname.grid(row=0, column=1)
    lastname = Entry(ContactForm, textvariable=LASTNAME, font=('Eras Bold ITC', 16),bg="#FFFFFA", fg="#0000FF")
    lastname.grid(row=0, column=3)
    RadioGroup.grid(row=2, column=1)
    
    address = Entry(ContactForm, textvariable=ADDRESS,  font=('Eras Bold ITC', 16),bg="#FFFFFA", fg="#0000FF")
    address.grid(row=3, column=1)
    contact = Entry(ContactForm, textvariable=CONTACT,  font=('Eras Bold ITC', 16),bg="#FFFFFA", fg="#0000FF")
    contact.grid(row=3, column=3)
    RadioGroup1.grid(row=4, column=1)
    RadioGroup2.grid(row=4, column=3)
    age = Entry(ContactForm, textvariable=AGE, font=('Eras Bold ITC', 16),bg="#FFFFFA", fg="#0000FF")
    age.grid(row=8,  column=3)
    aadhar = Entry(ContactForm, textvariable=AADHAR, font=('Eras Bold ITC', 16),bg="#FFFFFA", fg="#0000FF")
    aadhar.grid(row=8,  column=1)
    roll = Entry(ContactForm, textvariable=ROLL, font=('Eras Bold ITC', 16),bg="#FFFFFA", fg="#0000FF")
    roll.grid(row=9,  column=1)
    reg = Entry(ContactForm, textvariable=REG, font=('Eras Bold ITC', 16),bg="#FFFFFA", fg="#0000FF")
    reg.grid(row=9,  column=3)
    
    

    #==================BUTTONS==============================
  
    btn_updatecon = Button(ContactForm, text="UPDATE DATA", width=86,font=('Eras Bold ITC', 15),bg="#FFFF00",fg="#000000", command=UpdateData)
    btn_updatecon.grid(row=11, columnspan=5, pady=0)
  
    


#fn1353p    
def DeleteData():
    if not tree.selection():
       result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
    else:
        result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            conn = sqlite3.connect("pythontut.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `member1` WHERE `mem_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
            

   

    
def AddNewWindow():
    global NewWindow
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    AGE.set("")
    ADDRESS.set("")
    CONTACT.set("")
    DEPT.set("")
    YEAR.set("")
    AADHAR.set("")
    ROLL.set("")
    REG.set("")
      
    NewWindow = Toplevel()
    NewWindow.title("Contact List")
    width = 1200
    height = 650
    NewWindow.resizable(0, 0)
    NewWindow.config(bg="#000000")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) - 455) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    
    
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()
    
    #===================FRAMES==============================
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=10)
    ContactForm.config(bg="#000000")
    RadioGroup = Frame(ContactForm)
    RadioGroup1 = Frame(ContactForm)
    RadioGroup2 = Frame(ContactForm)
    RadioGroup3 = Frame(ContactForm)

    Male = Radiobutton(RadioGroup, text="MALE", variable=GENDER, value="Male",font=('Eras Bold ITC', 14), indicator = 0, background = "#FFFF00"  ).pack(ipadx = 110,ipady = 5)

    Female = Radiobutton(RadioGroup, text="FEMALE", variable=GENDER, value="Female", font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00"  ).pack( fill = X,ipady = 5)

    Others = Radiobutton(RadioGroup, text="OTHERS", variable=GENDER, value="Others", font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00"  ).pack( fill = X,ipady = 5)
   
    #=====================================================================================================================
    CSE = Radiobutton(RadioGroup1, text="CSE", variable=DEPT, value="CSE",font=('Eras Bold ITC', 14) , indicator = 0, background = "#FFFF00" ).pack(ipadx = 115,ipady = 5)
    
    ECE = Radiobutton(RadioGroup1, text="ECE", variable=DEPT, value="ECE",font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00"  ).pack(fill = X,ipady = 5)
    
    EE = Radiobutton(RadioGroup1, text="EE", variable=DEPT, value="EE",  font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00").pack( fill = X,ipady = 5)
   
    ME = Radiobutton(RadioGroup1, text="ME", variable=DEPT, value="ME",  font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00").pack( fill = X,ipady = 5)
  
    CE = Radiobutton(RadioGroup1, text="CE", variable=DEPT, value="CE",  font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00").pack( fill = X,ipady = 5)
  
    #====================================================================================================================
    First = Radiobutton(RadioGroup2, text="FIRST", variable=YEAR, value="First",  font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00").pack( ipadx = 110,ipady = 5)
   
    Second = Radiobutton(RadioGroup2, text="SECOND", variable=YEAR, value="Second",  font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00").pack( fill = X,ipady = 5)
    
    Third = Radiobutton(RadioGroup2, text="THIRD", variable=YEAR, value="Third",  font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00").pack(fill = X,ipady = 5)
  
    Fourth = Radiobutton(RadioGroup2, text="FOURTH", variable=YEAR, value="Fourth",  font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00").pack( fill = X,ipady = 5)
    
    EX_STUDENT = Radiobutton(RadioGroup2, text="EX_STUDENT", variable=YEAR, value="EX_STUDENT",  font=('Eras Bold ITC', 14), indicator = 0,background = "#FFFF00").pack( fill = X,ipady = 5)
  
     


 

        
    #===================LABELS==============================
    lbl_title = Label(FormTitle, text="ADD NEW STUDENT", font=('Cooper Std Black', 30,'bold'), bg="#FFFFFA",fg="#0000FF",  width = 300)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactForm, text="FIRST  NAME", font=('Eras Bold ITC', 16,'bold'), bd=5,bg="#000000", fg="#FFFFFA")
    lbl_firstname.grid(row=0, column=0, sticky=W)
    lbl_lastname = Label(ContactForm, text="LAST  NAME", font=('Eras Bold ITC', 16,'bold'), bd=5,bg="#000000", fg="#FFFFFA")
    lbl_lastname.grid(row=0,column=2, sticky=W)
    lbl_gender = Label(ContactForm, text="GENDER", font=('Eras Bold ITC', 16,'bold'), bd=5,bg="#000000", fg="#FFFFFA")
    lbl_gender.grid(row=2,column=0, sticky=W)
    lbl_age = Label(ContactForm, text="AGE", font=('Eras Bold ITC', 16,'bold'), bd=5,bg="#000000", fg="#FFFFFA")
    lbl_age.grid(row=8,column=2, sticky=W)
    lbl_address = Label(ContactForm, text="ADDRESS", font=('Eras Bold ITC', 16,'bold'), bd=5,bg="#000000", fg="#FFFFFA")
    lbl_address.grid(row=3,column=0, sticky=W)
    lbl_contact = Label(ContactForm, text="CONTACT", font=('Eras Bold ITC', 16,'bold'), bd=5,bg="#000000", fg="#FFFFFA")
    lbl_contact.grid(row=3,column=2, sticky=W)
    lbl_dept = Label(ContactForm, text="DEPARTMENT", font=('Eras Bold ITC', 16,'bold'), bd=5,bg="#000000", fg="#FFFFFA")
    lbl_dept.grid(row=4,column=0, sticky=W)
    lbl_year = Label(ContactForm, text="YEAR", font=('Eras Bold ITC', 16,'bold'), bd=5,bg="#000000", fg="#FFFFFA")
    lbl_year.grid(row=4, column=2,sticky=W)
    lbl_aadhar = Label(ContactForm, text="AADHAR  NO", font=('Eras Bold ITC', 16,'bold'), bd=5,bg="#000000", fg="#FFFFFA")
    lbl_aadhar.grid(row=8, column =0, sticky=W)
    lbl_roll = Label(ContactForm, text="ROLL  NO", font=('Eras Bold ITC', 16,'bold'), bd=5,bg="#000000", fg="#FFFFFA")
    lbl_roll.grid(row=9, column =0, sticky=W)
    lbl_reg = Label(ContactForm, text="UNIVERSITY  REGISTRATION  NO", font=('Eras Bold ITC', 16,'bold'),bg="#000000", fg="#FFFFFA")
    lbl_reg.grid(row=9, column =2, sticky=W)
     
   



    #===================ENTRY===============================
    firstname = Entry(ContactForm, textvariable=FIRSTNAME, font=('Eras Bold ITC', 16),bg="#FFFFFA", fg="#0000FF")
    firstname.grid(row=0, column=1)
    lastname = Entry(ContactForm, textvariable=LASTNAME, font=('Eras Bold ITC', 16),bg="#FFFFFA", fg="#0000FF")
    lastname.grid(row=0, column=3)
    RadioGroup.grid(row=2, column=1)
    
    address = Entry(ContactForm, textvariable=ADDRESS,  font=('Eras Bold ITC', 16),bg="#FFFFFA", fg="#0000FF")
    address.grid(row=3, column=1)
    contact = Entry(ContactForm, textvariable=CONTACT,  font=('Eras Bold ITC', 16),bg="#FFFFFA", fg="#0000FF")
    contact.grid(row=3, column=3)
    RadioGroup1.grid(row=4, column=1)
    RadioGroup2.grid(row=4, column=3)
    age = Entry(ContactForm, textvariable=AGE, font=('Eras Bold ITC', 16),bg="#FFFFFA", fg="#0000FF")
    age.grid(row=8,  column=3)
    aadhar = Entry(ContactForm, textvariable=AADHAR, font=('Eras Bold ITC', 16),bg="#FFFFFA", fg="#0000FF")
    aadhar.grid(row=8,  column=1)
    roll = Entry(ContactForm, textvariable=ROLL, font=('Eras Bold ITC', 16),bg="#FFFFFA", fg="#0000FF")
    roll.grid(row=9,  column=1)
    reg = Entry(ContactForm, textvariable=REG, font=('Eras Bold ITC', 16),bg="#FFFFFA", fg="#0000FF")
    reg.grid(row=9,  column=3)
    
    

    #==================BUTTONS==============================
    btn_addcon = Button(ContactForm, text="SAVE  DATA", width=86,font=('Eras Bold ITC', 15),bg="#FFFF00",fg="#000000", command=SubmitData)
    btn_addcon.grid(row=11, columnspan=5, pady=0)
   

# Adjust size 
root.geometry("1600x800")
root.config(bg="#000000")
root.title('DATABASE')
root.resizable(0,0)
  
Left = Frame(root, width=1600, height=400)
Left.pack(side=TOP)

TopLeft = Frame(Left, width=1050, height=400)
TopLeft.pack(side=LEFT)

TopLeftL = Frame(TopLeft, width=1000, height=400)
TopLeftL.pack(side=LEFT)

TopLeftR = Frame(TopLeft, width=150, height=400,bg="#000000")
TopLeftR.pack(side=RIGHT)

TopLeftRT = Frame(TopLeftR, width=150, height=260,bg="#000000")
TopLeftRT.pack(side=TOP)

TopLeftRB = Frame(TopLeftR, width=150, height=130,bg="#000000")
TopLeftRB.pack()

BottomLeft = Frame(Left, width=450, height=400)
BottomLeft.pack(side=RIGHT)

BottomLeftT = Frame(BottomLeft, width=450, height=335)
BottomLeftT.pack(side=TOP)

BottomLeftB = Frame(BottomLeft, width=450, height=20)
BottomLeftB.pack(side=BOTTOM)
label = Label(BottomLeftB, font=("Digital-7", 45, 'bold'), bg="blue", fg="white",width=400)
label.pack()
def digitalclock():
   text_input = time.strftime("%H:%M:%S")
   label.config(text=text_input)
   label.after(200, digitalclock)
digitalclock()


bg11 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View2\\01.jpg").resize((450,335)))
bg22 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View2\\02.jpg").resize((450,335)))
bg33 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View2\\03.jpg").resize((450,335)))
bg44 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View2\\04.jpg").resize((450,335)))
bg55 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View2\\05.jpg").resize((450,335)))
bg66 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View2\\06.jpg").resize((450,335)))
bg77 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View2\\07.jpg").resize((450,335)))
bg88 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View2\\08.jpg").resize((450,335)))
bg99 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View2\\09.jpg").resize((450,335)))
bg100 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View2\\10.jpg").resize((450,335)))

image_list1=[bg11, bg22, bg33, bg44, bg55, bg66, bg77, bg88, bg99, bg100]


#Create a label
l1=Label(BottomLeftT,font="bold")
l1.pack()
#take a variable
x1=1


#create a function for moving a picture
def move1():#name anything but meaningful
    global x1
    if x1>=10:
        x1=1
    value=range(35)
    for i1 in value:
        a1=1
    l1.config(image=image_list1[x1])
    
    #you can do it for thousands of images
    #now increase the count by one
    x1+=1
    #set images to work automatically by "after" feature in tkinter
    BottomLeftT.after(3000,move1)
    

move1()


bg1 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\01.jpg").resize((1000,400)))
bg2 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\02.jpg").resize((1000,400)))
bg3 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\03.jpg").resize((1000,400)))
bg4 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\04.jpg").resize((1000,400)))
bg5 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\05.jpg").resize((1000,400)))
bg6 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\06.jpg").resize((1000,400)))
bg7 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\07.jpg").resize((1000,400)))
bg8 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\08.jpg").resize((1000,400)))
bg9 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\09.jpg").resize((1000,400)))
bg10 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\10.jpg").resize((1000,400)))
bg11 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\11.jpg").resize((1000,400)))
bg12 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\12.jpg").resize((1000,400)))
bg13 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\13.jpg").resize((1000,400)))
bg14 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\14.jpg").resize((1000,400)))
bg15 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\15.jpg").resize((1000,400)))
bg16 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\16.jpg").resize((1000,400)))
bg17 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\17.jpg").resize((1000,400)))
bg18 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\18.jpg").resize((1000,400)))
bg19 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\19.jpg").resize((1000,400)))
bg20 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\20.jpg").resize((1000,400)))
bg21 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\21.jpg").resize((1000,400)))
bg22 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\22.jpg").resize((1000,400)))
bg23 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\23.jpg").resize((1000,400)))
bg24 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\24.jpg").resize((1000,400)))
bg25 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\25.jpg").resize((1000,400)))
bg26 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\26.jpg").resize((1000,400)))
bg27 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\27.jpg").resize((1000,400)))
bg28 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\28.jpg").resize((1000,400)))
bg29 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\29.jpg").resize((1000,400)))
bg30 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\30.jpg").resize((1000,400)))
bg31 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\31.jpg").resize((1000,400)))
bg32 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\32.jpg").resize((1000,400)))
bg33 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\33.jpg").resize((1000,400)))
bg34 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\34.jpg").resize((1000,400)))
bg35 = ImageTk.PhotoImage(Image.open("C:\\Project1\\View\\35.jpg").resize((1000,400)))

image_list=[bg1, bg2, bg3, bg4, bg5, bg6, bg7, bg8, bg9, bg10, bg11, bg12, bg13, bg14, bg15, bg16, bg17, bg18, bg19, bg20, bg21, bg22, bg23, bg24, bg25, bg26, bg27, bg28, bg29, bg30, bg31, bg32,bg33, bg34 ,bg35]


#Create a label
l=Label(TopLeftL)
l.pack()
#take a variable
x=1


#create a function for moving a picture
def move():#name anything but meaningful
    global x
    if x>=35:
        x=1
    value=range(35)
    for i in value:
        a=1
    l.config(image=image_list[x])
    
    #you can do it for thousands of images
    #now increase the count by one
    x+=1
    #set images to work automatically by "after" feature in tkinter
    TopLeft.after(3000,move)
    

move()



photo = ImageTk.PhotoImage(Image.open("C:\\Project1\\refresh1.png").resize((120,130)))
photo1 = ImageTk.PhotoImage(Image.open("C:\\Project1\\clear1.png").resize((120,130)))
photo2 = ImageTk.PhotoImage(Image.open("C:\\Project1\\quit.png").resize((120,130)))

btn_add = Button(TopLeftRT, image = photo, command=Database)
btn_add.pack(side=TOP)

btn_add = Button(TopLeftRT, image = photo1, command=Clear)
btn_add.pack(side= BOTTOM)

btn_quit = Button(TopLeftRB, image = photo2, command=Clear )
btn_quit.pack()









    
#============================FRAMES======================================
Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width=500,  bg="#000000")
Mid.pack(side=TOP)
MidLeft = Frame(Mid, width=100)
MidLeft.pack(side=LEFT, pady=10)
MidLeftPadding = Frame(Mid, width=370, bg="#000000")
MidLeftPadding.pack(side=LEFT)
MidRight = Frame(Mid, width=100)
MidRight.pack(side=RIGHT, pady=10)
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
#============================LABELS======================================



#============================BUTTONS=====================================



#============================TABLES======================================
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("MemberID", "FIRST  NAME", "LAST  NAME", "GENDER", "AGE", "ADDRESS", "CONTACT", "DEPARTMENT", "CURRENT  YEAR", "AADHAR  NO", "ROLL  NO", "UNIVERSITY REGISTRATION  NO"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('MemberID', text="MemberID", anchor=W)
tree.heading('FIRST  NAME', text="FIRST  NAME", anchor=W)
tree.heading('LAST  NAME', text="LAST  NAME", anchor=W)
tree.heading('GENDER', text="GENDER", anchor=W)
tree.heading('AGE', text="AGE", anchor=W)
tree.heading('ADDRESS', text="ADDRESS", anchor=W)
tree.heading('CONTACT', text="CONTACT", anchor=W)
tree.heading('DEPARTMENT', text="DEPARTMENT", anchor=W)
tree.heading('CURRENT  YEAR', text="CURRENT  YEAR", anchor=W)
tree.heading('AADHAR  NO', text="AADHAR  NO", anchor=W)
tree.heading('ROLL  NO', text="ROLL  NO", anchor=W)
tree.heading('UNIVERSITY REGISTRATION  NO', text="UNIVERSITY REGISTRATION  NO", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=120)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=120)
tree.column('#5', stretch=NO, minwidth=0, width=90)
tree.column('#6', stretch=NO, minwidth=0, width=180)
tree.column('#7', stretch=NO, minwidth=0, width=120)
tree.column('#8', stretch=NO, minwidth=0, width=90)
tree.column('#9', stretch=NO, minwidth=0, width=120)
tree.column('#10', stretch=NO, minwidth=0, width=160)
tree.column('#11', stretch=NO, minwidth=0, width=120)
tree.column('#12', stretch=NO, minwidth=0, width=180)
tree.pack()
tree.bind('<Double-Button-1>', OnSelected)

menubar = Menu(root)
first = PhotoImage(file = r"C:\Project1\First.png")
second = PhotoImage(file = r"C:\Project1\Second.png")
third = PhotoImage(file = r"C:\Project1\Third.png")
fourth = PhotoImage(file = r"C:\Project1\Fourth.png")
ex = PhotoImage(file = r"C:\Project1\Ex.png")
add = PhotoImage(file = r"C:\Project1\add.png")
delete = PhotoImage(file = r"C:\Project1\delete.png")
contact = PhotoImage(file = r"C:\Project1\contact.png")
quit1 = PhotoImage(file = r"C:\Project1\quit.png")

csemenu = Menu(menubar, tearoff=0)
csemenu.add_command(image = first, command=cse1Database)
csemenu.add_command(image = second, command=cse2Database)
csemenu.add_command(image = third, command=cse3Database)
csemenu.add_command(image = fourth,command=cse4Database)
csemenu.add_command(image = ex,command=cseexDatabase)
csemenu.add_separator()
menubar.add_cascade(label="        COMPUTER      SCIENCE            ",menu=csemenu)

ecemenu = Menu(menubar, tearoff=0)
ecemenu.add_command(image = first, command=ece1Database)
ecemenu.add_command(image = second, command=ece2Database)
ecemenu.add_command(image = third, command=ece3Database)
ecemenu.add_command(image = fourth,command=ece4Database)
ecemenu.add_command(image = ex,command=eceexDatabase)
ecemenu.add_separator()
menubar.add_cascade(label="ELECTRONICS & COMMUNICATION", menu=ecemenu)

eemenu = Menu(menubar, tearoff=0)
eemenu.add_command(image = first,command=ee1Database)
eemenu.add_command(image = second, command=ee2Database)
eemenu.add_command(image = third,command=ee3Database)
eemenu.add_command(image = fourth,command=ee4Database)
eemenu.add_command(image = ex,command=eeexDatabase)
eemenu.add_separator()
menubar.add_cascade(label="                     ELECTRICAL                    ", menu=eemenu)



memenu = Menu(menubar, tearoff=0)
memenu.add_command(image = first, command=me1Database)
memenu.add_command(image = second, command=me2Database)
memenu.add_command(image = third, command=me3Database)
memenu.add_command(image = fourth, command=me4Database)
memenu.add_command(image = ex,command=meexDatabase)
memenu.add_separator()
menubar.add_cascade(label="               MECHANICAL                      ", menu=memenu)

cemenu = Menu(menubar, tearoff=0)
cemenu.add_command(image = first, command=ce1Database)
cemenu.add_command(image = second, command=ce2Database)
cemenu.add_command(image = third,command=ce3Database)
cemenu.add_command(image = fourth,command=ce4Database)
cemenu.add_command(image = ex,command=ceexDatabase)
cemenu.add_separator()
menubar.add_cascade(label="                            CIVIL                          ", menu=cemenu)

othermenu = Menu(menubar, tearoff=0)
othermenu.add_command(image = add, command=AddNewWindow)
othermenu.add_command(image = delete, command=DeleteData)

othermenu.add_separator()
menubar.add_cascade(label="              MANAGE              ", menu=othermenu)

root.config(menu=menubar)





root.mainloop()



