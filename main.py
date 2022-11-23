# this is a simple user input data
from tkinter import *
import sqlite3 as db

# Creating database and tables
conn = db.connect('Sample.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS DATA
    (
     Fname TEXT,
     Lname TEXT,
     Course TEXT,
     Score TEXT
     )''')
cur.close()
conn.commit()
conn.close()


# creating method for inputing data in database
# get method extract values from variables
def put():
    conn = db.connect('Sample.db')
    cur = conn.cursor()
    cur.execute(
        "insert into DATA values('%s', '%s', '%s', '%s')" % (fname.get(), lname.get(), Course.get(), Score.get()))
    cur.close()
    conn.commit()
    conn.close()
    status.set('Data Added Successfully')


# creating method for FETCHING  data in database
# Storing data in tuples
# converting it to string for better visuals
def fetchdata():
    conn = db.connect('Sample.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM DATA")
    list0 = cur.fetchall()
    cur.close()
    conn.close()
    print(list0)
    output = ''
    for x in list0:
        output = output + x[0] + ' ' + x[1] + ' ' + x[2] + ' ' + x[3] + '\n'
    return output


# Creating UserInterface
tk = Tk()

# Creating variables for accessing entry boxes and labels
fname = StringVar()
lname = StringVar()
status = StringVar()
Course = StringVar()
Score = StringVar()
# Score = IntVar()

# labels creation
Label(tk, text='Firstname: ').grid(row=0, column=0)
Label(tk, text='Lastname: ').grid(row=1, column=0)
Label(tk, text='', textvariable=status).grid(row=6, columnspan=2)
Label(tk, text='Course: ').grid(row=2, column=0)
Label(tk, text='Score: ').grid(row=3, column=0)

# labels textfield

Entry(tk, textvariable=fname).grid(row=0, column=1)
Entry(tk, textvariable=lname).grid(row=1, column=1)
Entry(tk, textvariable=Course).grid(row=2, column=1)
Entry(tk, textvariable=Score).grid(row=3, column=1)

# creating text box for display
# Using Objects for better heading
text = Text(tk, height=10, width=24)
text.grid(row=4, columnspan=2)
# add button for data submission
# Columnspan decides how much space is to be given
# command specifies button action
# Using lambda function to add row in display

Button(tk, text='Submit', command=put).grid(row=5, columnspan=1)
Button(tk, text='Fetch', command=lambda: (text.delete(1.0, END), text.insert(END, fetchdata()))).grid(row=5,
                                                                                                      columnspan=3)

mainloop()  # KEEPS THE GUI RUNNIING
