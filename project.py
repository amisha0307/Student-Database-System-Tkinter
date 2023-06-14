import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import tkinter
from tkinter.font import Font
from PIL import ImageTk,Image

def GetValue(event):
	e1.delete(0, END)
	e2.delete(0, END)
	e3.delete(0, END)
	e4.delete(0, END)
	e5.delete(0, END)
	e6.delete(0,END)

	row_id = listBox.selection()[0]
	select = listBox.set(row_id)
	e1.insert(0,select['Student Name'])
	e2.insert(0,select['Branch'])
	e3.insert(0,select['Course Name'])
	e4.insert(0,select['Fees'])
	e5.insert(0,select['Contact No.'])
	e6.insert(0,select['Gender'])


def Add():
	studname = e1.get()
	studbranch = e2.get()
	coursename = e3.get()
	feee = e4.get()
	contactno = e5.get()
	studgender = e6.get()
	mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="xiepro")
	mycursor=mysqldb.cursor()
	try:
		sql = "INSERT INTO record (stname,branch,course,fee,Contact_no,Gender)  VALUES (%s, %s, %s, %s, %s, %s)"
		val = (studname,studbranch,coursename,feee,contactno,studgender)
		mycursor.execute(sql, val)
		mysqldb.commit()
		lastid = mycursor.lastrowid
		messagebox.showinfo("information", "Record inserted successfully...")
		e1.delete(0, END)
		e2.delete(0, END)
		e3.delete(0, END)
		e4.delete(0, END)
		e5.delete(0, END)
		e6.delete(0,END)


		e1.focus_set()
		show(1)
	except Exception  as e:
		print(e)
		mysqldb.rollback()
		mysqldb.close()


def update():
	studname = e1.get()
	studbranch = e2.get()
	coursename = e3.get()
	feee = e4.get()
	contactno = e5.get()
	studgender = e6.get()
	mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="xiepro")
	mycursor = mysqldb.cursor()
	
	try:
		sql = "Update record set branch= %s,course= %s,fee= %s, Contact_no= %s, Gender= %s where stname= %s"
		val = (studbranch,coursename,feee,contactno,studgender,studname)
		mycursor.execute(sql, val)
		mysqldb.commit()
		lastid = mycursor.lastrowid
		messagebox.showinfo("information", "Record Updated Successfully...")
	
		e1.delete(0, END)
		e2.delete(0, END)
		e3.delete(0, END)
		e4.delete(0, END)
		e5.delete(0, END)
		e6.delete(0,END)
		
		e1.focus_set()
		show(1)
	except Exception as e:
	
			print(e)
			mysqldb.rollback()
			mysqldb.close()

def delete():
	studname = e1.get()

	mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="xiepro")
	mycursor=mysqldb.cursor()

	try:
		sql="delete from record where stname=%s"
		val=(studname,)
		mycursor.execute(sql,val)
		mysqldb.commit()
		lastid=mycursor.lastrowid
		messagebox.showinfo("information","Record Delete successfully")

		e1.delete(0, END)
		e2.delete(0, END)
		e3.delete(0, END)
		e4.delete(0, END)
		e5.delete(0, END)
		e6.delete(0,END)
		e1.focus_set()

		show(1)

	except Exception as e:

		print(e)
		mysqldb.rollback()
		mysqldb.close()	


def show(call_from):
	mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="xiepro")
	mycursor=mysqldb.cursor()
	mycursor.execute("SELECT stname,branch,course,fee,Contact_no,Gender FROM record")
	records=mycursor.fetchall()
	print(records)
	


	if call_from==1:
		for i in listBox.get_children():
			listBox.delete(i)
			
	for i, (stname,branch,course,fee,Contact_no,Gender) in enumerate(records,start=1):
		listBox.insert("","end",values=(stname,branch,course,fee,Contact_no,Gender))
	mysqldb.close()

root = tk.Tk()

root.geometry("1650x900")
root.title('Python Project :- Student Register')
bigFont = Font(
	family = "Times",
	size = 35,
	weight = "bold",
	slant="italic",
	underline = 5)

tk.Label(root, text="STUDENT REGISTER", fg="black", font=bigFont, bg="#49A").place(x=515, y=40)

my_pic1 = Image.open("C:/Users/Stepheny Lucas/Desktop/python/pic1.png")
resized1 = my_pic1.resize((520, 175), Image.ANTIALIAS)
new_pic1 = ImageTk.PhotoImage(resized1)

my_label1 = Label(root, image=new_pic1,bg="#49A").place(x=1000,y=1)

my_pic2 = Image.open("C:/Users/Stepheny Lucas/Desktop/python/pic2.png")
resized2 = my_pic2.resize((680, 250), Image.ANTIALIAS)
new_pic2 = ImageTk.PhotoImage(resized2)
my_label2 = Label(root, image=new_pic2,bg="#49A").place(x=400,y=540)


my_pic3 = Image.open("C:/Users/Stepheny Lucas/Desktop/python/pic3.png")
resized3 = my_pic3.resize((500, 158), Image.ANTIALIAS)
new_pic3 = ImageTk.PhotoImage(resized3)
my_label3 = Label(root, image=new_pic3,bg="#49A").place(x=0,y=0)

my_pic4 = Image.open("C:/Users/Stepheny Lucas/Desktop/python/pic5.png")
resized4 = my_pic4.resize((200, 400), Image.ANTIALIAS)
new_pic4 = ImageTk.PhotoImage(resized4)
my_label4 = Label(root, image=new_pic4,bg="#49A").place(x=1330,y=325)

my_pic5 = Image.open("C:/Users/Stepheny Lucas/Desktop/python/pic6.png")
resized5 = my_pic5.resize((200, 420), Image.ANTIALIAS)
new_pic5 = ImageTk.PhotoImage(resized5)
my_label5 = Label(root, image=new_pic5,bg="#49A").place(x=0,y=330)

labelFont = Font(
	family = "Times",
	size = 14,
	weight = "bold")	

tk.Label(root, text="Student Name:", font=labelFont, bg="#49A").place(x=60, y=160)
tk.Label(root, text="Branch:", font=labelFont, bg="#49A").place(x=60, y=210) 
tk.Label(root, text="Course Name:", font=labelFont, bg="#49A").place(x=380, y=160)
tk.Label (root, text="Fees:", font=labelFont, bg="#49A").place(x=380, y=210)
tk.Label (root, text="Contact Number:", font=labelFont, bg="#49A").place(x=680, y=160)
tk.Label (root, text="Gender:", font=labelFont, bg="#49A").place(x=680, y=210)

e1=Entry(root)
e1.place(x=198, y=165)

e2=ttk.Combobox(root, values=["Computer Engineering","IT Engineering","EXTC Engineering"])
e2.set("Select")
e2.place(x=198, y=215)

e3=ttk.Combobox(root, values=["Python", "Java", "AI", "SQL","IOT", "Cyber Security"])
e3.set("Select")
e3.place(x=508, y=165)

e4=Entry(root)
e4.place(x=508, y=215)

e5=Entry(root)
e5.place(x=828, y=165)

e6=ttk.Combobox(root, values=["Male","Female"])
e6.set("Select")
e6.place(x=828, y=215)

buttonFont = Font(
	family = "Times",
	size = 16,
	weight = "bold"
	)

Button(root, text="ADD", command = Add, height=2, width= 8, font=buttonFont).place(x=1020, y=185)
Button(root, text="UPDATE", command = update, height=2, width= 8, font=buttonFont).place(x=1140, y=185) 
Button(root, text="DELETE", command = delete,height=2, width= 8, font=buttonFont).place(x=1260, y=185)


cols= ('Student Name','Branch','Course Name','Fees', 'Contact No.', 'Gender') 
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
	listBox.heading (col, text=col)
	listBox.place(x=130, y=260)

show(0)
listBox.bind('<Double-Button-1>', GetValue)

root['bg'] = '#49A'

button_quit = Button(root, text="EXIT", height=1, width=10, font=buttonFont, command=root.quit).place(x=650, y=510)
root.mainloop()