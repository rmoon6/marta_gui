# CS4400 Project
# Bryan Jackisch, Matthew Munns, Matthew Cover, Jag Gangemi

from tkinter import *
from tkinter import messagebox
import tktable
import datetime
import pymysql
import random
import hashlib
import re
from random import randint


class MARTA():
    def __init__(self, root):
        self.root = root
        self.login()
        self.connect()

    def connect(self):
        try:
            self.db = pymysql.connect(host='academic-mysql.cc.gatech.edu', passwd='72ogsOcy', user='cs4400_Group_84',
                                      db='cs4400_Group_84')
        except:
            messagebox.showerror('Connection Error', 'Cannot connect to database')

    def login(self):
        self.root.title('Log In')
        self.e1Var = StringVar()
        self.e2Var = StringVar()
        self.l1 = Label(self.root, text='Username:')
        self.l2 = Label(self.root, text='Password:')
        self.e1 = Entry(self.root, textvariable=self.e1Var, width=30)
        self.e2 = Entry(self.root, textvariable=self.e2Var, width=30)
        self.b1 = Button(self.root, text='Register', command=self.displayRegister)
        self.b2 = Button(self.root, text='Login', command=self.loginTry)
        self.l1.grid(row=0, column=0, padx=3)
        self.l2.grid(row=1, column=0, padx=3)
        self.e1.grid(row=0, column=1, columnspan=2, padx=7, pady=2)
        self.e2.grid(row=1, column=1, columnspan=2, padx=7, pady=2)
        self.b1.grid(row=2, column=1, pady=4)
        self.b2.grid(row=3, column=1, pady=4)

    def displayPassenger(self):
        self.root.withdraw()
        self.root10 = Toplevel()
        self.root10.deiconify()
        self.passenger()

    def displayRegister(self):
        self.root.withdraw()
        self.root2 = Toplevel()
        self.root2.deiconify()
        self.register()

    def displayLogin10(self):
        self.root10.withdraw()
        self.root = Toplevel()
        self.root.deiconify()
        self.login()

    def displayAdmin(self):
        self.root.withdraw()
        self.root4 = Toplevel()
        self.root4.deiconify()
        self.admin()

    def displayStatMan(self):
        self.root4.withdraw()
        self.root5 = Toplevel()
        self.root5.deiconify()
        self.statMan()

    def displaySusCard(self):
        self.root4.withdraw()
        self.root6 = Toplevel()
        self.root6.deiconify()
        self.susCard()

    def displayCardMan(self):
        self.root4.withdraw()
        self.root7 = Toplevel()
        self.root7.deiconify()
        self.cardMan()

    def displayFlowRep(self):
        self.root4.withdraw()
        self.root8 = Toplevel()
        self.root8.deiconify()
        self.flowRep()

    def displayCreate(self):
        self.root5.withdraw()
        self.root9 = Toplevel()
        self.root9.deiconify()
        self.createStat()

    def passenger(self):
        self.root10.title('Welcome to MARTA')
        self.p1 = Label(self.root10, text='Breeze Card')
        self.pVar = StringVar()
        self.pVar2 = StringVar()
        self.pVar3 = StringVar()
        self.pVar4 = StringVar()
        self.pVar5 = StringVar()
        self.pVar3.set('Placeholder')
        self.pVar4.set('Another Placeholder')
        self.p2 = OptionMenu(self.root10, self.pVar, " Card one", "Card two", "Card three")
        self.p3 = Label(self.root10, text='Manage Cards')
        self.p3.bind("<ButtonRelease-1>", self.ButtonClickOne)
        self.p1.grid(row=0, column=0, padx=3, pady=3)
        self.p2.grid(row=0, column=1, padx=3, pady=3)
        self.p3.grid(row=0, column=2, padx=3, pady=3)
        self.p4 = Label(self.root10, text='Balance')
        self.p5 = Label(self.root10, textvariable=self.pVar3)
        self.p6 = Label(self.root10, text='Starts At')
        self.p7 = OptionMenu(self.root10, self.pVar2, "station 1", 'Station 2', 'Station 3')
        self.p8 = Label(self.root10, textvariable=self.pVar4)
        self.p4.grid(row=1, column=0, padx=3, pady=3)
        self.p5.grid(row=1, column=1, padx=3, pady=3)
        self.p6.grid(row=2, column=0, padx=3, pady=3)
        self.p7.grid(row=2, column=1, padx=3, pady=3)
        self.p8.grid(row=2, column=2, padx=3, pady=3)
        self.p9 = Label(self.root10, text='Ending at')
        self.p10 = OptionMenu(self.root10, self.pVar5, 'end station 1', 'endstation2', 'endstation3')
        self.p11 = Label(self.root10, text='End Trip')
        self.p11.bind('<ButtonRelease-1>', self.ButtonClickTwo)
        self.p12 = Button(self.root10, text='View Trip History', command=self.viewHist)
        self.p13 = Button(self.root10, text='Log Out', command=self.displayLogin10)
        self.p9.grid(row=3, column=0, padx=3, pady=3)
        self.p10.grid(row=3, column=1, padx=3, pady=3)
        self.p11.grid(row=3, column=2, padx=3, pady=3)
        self.p12.grid(row=4, column=0, pady=10, padx=3)
        self.p13.grid(row=4, column=2, pady=10, padx=3)

    def ButtonClickOne(self, printThis):
        print('Button One was clicked. Should open Manage Cards')

    def ButtonClickTwo(self, printThis):
        print('Button Two was clicked. Should do something with End Trip')

    def viewHist(self):
        print('View History button clicked')

    def createStat(self):
        self.root9.title('Create New Station')
        self.cs2Var = StringVar()
        self.cs4Var = StringVar()
        self.cs6Var = StringVar()
        self.cs11Var = StringVar()
        self.cs1 = Label(self.root9, text='Station Name')
        self.cs2 = Entry(self.root9, width=30, textvariable=self.cs2Var)
        self.cs3 = Label(self.root9, text='Stop ID')
        self.cs4 = Entry(self.root9, width=30, textvariable=self.cs4Var)
        self.cs5 = Label(self.root9, text='Entry Fare')
        self.cs6 = Entry(self.root9, width=30, textvariable=self.cs6Var)
        self.cs7 = Label(self.root9, text='Station Type')
        self.csVar = StringVar(value='bus')
        self.csVar2 = IntVar()
        self.cs8 = Radiobutton(self.root9, text='Bus Station', variable=self.csVar, value='bus')
        self.cs9 = Radiobutton(self.root9, text='Train Station', variable=self.csVar, value='train')
        self.cs10 = Label(self.root9, text='Nearest Intersection', font=('Times', 8))
        self.cs11 = Entry(self.root9, width=20, textvariable=self.cs11Var)
        self.cs12 = Checkbutton(self.root9, text='Open Station', variable=self.csVar2)
        self.cs13 = Label(self.root9, text='When checked, passengers can enter at this station.', font=('Times', 8))
        self.cs14 = Button(self.root9, text='Create Station', command=self.createStation)
        self.cs1.grid(row=0, column=0, padx=1)
        self.cs2.grid(row=0, column=1, padx=1)
        self.cs3.grid(row=1, column=0, padx=1)
        self.cs4.grid(row=1, column=1, padx=1)
        self.cs5.grid(row=2, column=0, padx=1)
        self.cs6.grid(row=2, column=1, padx=1)
        self.cs7.grid(row=3, column=0, rowspan=4)
        self.cs8.grid(row=3, column=1)
        self.cs9.grid(row=6, column=1)
        self.cs10.grid(row=4, column=1)
        self.cs11.grid(row=5, column=1)
        self.cs12.grid(row=7, column=0, columnspan=2)
        self.cs13.grid(row=8, column=0, columnspan=2)
        self.cs14.grid(row=9, column=0, columnspan=2)

    def flowRep(self):
        self.root8.title('Passenger Flow Report')
        self.fr2Var = StringVar()
        self.fr6Var = StringVar()
        self.fr1 = Label(self.root8, text='Start Time')
        self.fr2 = Entry(self.root8, width=20, textvariable=self.fr2Var)
        self.fr3 = Button(self.root8, text='Update', command=self.updateFlowRep)
        self.fr4 = Button(self.root8, text='Reset')
        self.fr5 = Label(self.root8, text='End Time')
        self.fr6 = Entry(self.root8, width=20, textvariable=self.fr6Var)
        self.fr1.grid(row=0, column=0, padx=5)
        self.fr2.grid(row=0, column=1, padx=3)
        self.fr3.grid(row=0, column=2, padx=2, rowspan=2)
        self.fr4.grid(row=0, column=3, padx=2, rowspan=2)
        self.fr5.grid(row=1, column=0, padx=5)
        self.fr6.grid(row=1, column=1, padx=3)

    def cardMan(self):
        self.root7.title('Breeze Card Management')
        self.cm1 = Label(self.root7, text='Breeze Cards', font=('Times', 16, 'bold'))
        self.cm2 = Label(self.root7, text='Search/Filter', font=('Times', 10))
        self.cm3 = Label(self.root7, text='Owner')
        self.cm4Var = StringVar()
        self.cm7Var = StringVar()
        self.cm10Var = StringVar()
        self.cm12Var = StringVar()
        self.cm14Var = StringVar()
        self.cm16Var = StringVar()
        self.cm4 = Entry(self.root7, width=30, textvariable=self.cm4Var)
        self.cmVar = IntVar()
        self.cmF = Frame(self.root7)
        self.cm5 = Checkbutton(self.root7, text='Show Suspended Cards', variable=self.cmVar)
        self.cm6 = Label(self.root7, text='Card Number')
        self.cm7 = Entry(self.root7, width=30, textvariable=self.cm7Var)
        self.cm8 = Button(self.root7, text='Reset')
        self.cm9 = Label(self.root7, text='Value Between')
        self.cm10 = Entry(self.cmF, width=10, textvariable=self.cm10Var)
        self.cm11 = Label(self.cmF, text='and')
        self.cm12 = Entry(self.cmF, width=10, textvariable=self.cm12Var)
        self.cm13 = Button(self.root7, text='Update Filter', command=self.updateFilter)
        self.cm14 = Entry(self.root7, width=15, textvariable=self.cm14Var)
        self.cm15 = Button(self.root7, text='Set Value of Selected Card', command=self.setVal)
        self.cm16 = Entry(self.root7, width=15, textvariable=self.cm16Var)
        self.cm17 = Button(self.root7, text='Transfer Selected Card', command=self.tranCard)
        self.cm1.grid(row=0, column=0, pady=3)
        self.cm2.grid(row=1, column=0, pady=3)
        self.cm3.grid(row=2, column=0, padx=2)
        self.cm4.grid(row=2, column=1, padx=2)
        self.cm5.grid(row=2, column=2, padx=2)
        self.cm6.grid(row=3, column=0, padx=2)
        self.cm7.grid(row=3, column=1, padx=2)
        self.cm8.grid(row=3, column=2, padx=2)
        self.cm9.grid(row=4, column=0, padx=2)
        self.cmF.grid(row=4, column=1, padx=2)
        self.cm10.grid(row=0, column=0, padx=2)
        self.cm11.grid(row=0, column=1, padx=2)
        self.cm12.grid(row=0, column=2, padx=2)
        self.cm13.grid(row=4, column=2, padx=2)
        self.cm14.grid(row=5, column=0, padx=2)
        self.cm15.grid(row=5, column=1, padx=2)
        self.cm16.grid(row=6, column=0, padx=2)
        self.cm17.grid(row=6, column=1, padx=2)

    def susCard(self):
        self.root6.title('Suspended Cards')
        self.sc1 = Button(self.root6, text='Assign Selected Card to New Owner')
        self.sc2 = Button(self.root6, text='Assign Selected Card to Previous Owner')
        self.sc1.grid(row=0, column=0, padx=5, pady=5)
        self.sc2.grid(row=1, column=0, pady=5, padx=5)

    def statMan(self):
        self.root5.title('Station Listing')
        self.make_table()

        self.sm1 = Button(self.root5, text='Create New Station', command=self.displayCreate)
        self.sm2 = Button(self.root5, text='View Station')

        self.sm1.grid(row=1, column=0, pady=3, padx=3)
        self.sm2.grid(row=1, column=1, pady=3, padx=3)

    def make_table(self, column=""):
        for widget in self.root5.winfo_children():
            widget.destroy()

        canvas = Canvas(self.root5, borderwidth=0, background="#ffffff")
        canvas.grid(row=0, column=0, columnspan=2, pady=3, padx=3)

        cursor = self.db.cursor()
        sql = '''SELECT * from `Station`'''
        if len(column) != 0:
            sql += ''' order by `''' + column + '`'
        cursor.execute(sql)

        print(sql)

        self.set_column_headers(canvas, cursor.description)
        self.set_data(canvas, cursor)

    def set_column_headers(self, canvas, description):
        i = 0
        for desc in description:
            Button(canvas, text=desc[0], width=30, command=lambda d=desc[0]: self.make_table(d)).grid(row=0, column=i, padx=2, pady=2)
            i += 1

    def set_data(self, canvas, cursor):
        r = 1
        c = 0
        for elementList in cursor:
            for each in elementList:
                Label(canvas, text=str(each)).grid(row=r, column=c, padx=2, pady=2)
                c += 1
            r += 1
            c = 0

    def admin(self):
        self.root4.title('Administrator')
        self.la1 = Button(self.root4, text='Station Management', command=self.displayStatMan)
        self.la2 = Button(self.root4, text='Suspended Cards', command=self.displaySusCard)
        self.la3 = Button(self.root4, text='Breeze Card Management', command=self.displayCardMan)
        self.la4 = Button(self.root4, text='Passenger Flow Report', command=self.displayFlowRep)
        self.la5 = Button(self.root4, text='Log Out', command=self.displayLogin3)
        self.la1.grid(row=0, column=0, pady=3)
        self.la2.grid(row=1, column=0, pady=3)
        self.la3.grid(row=2, column=0, pady=3)
        self.la4.grid(row=3, column=0, pady=3)
        self.la5.grid(row=4, column=0, pady=6)

    def register(self):
        self.root2.title('Create a MARTA Account')
        self.frame1 = Frame(self.root2, borderwidth=5, relief=SUNKEN)
        self.l3 = Label(self.root2, text='Username:')
        self.l4 = Label(self.root2, text='Email Address:')
        self.l5 = Label(self.root2, text='Password:')
        self.l6 = Label(self.root2, text='Confirm Password:')
        self.e3Var = StringVar()
        self.e4Var = StringVar()
        self.e5Var = StringVar()
        self.e6Var = StringVar()
        self.e7Var = StringVar()

        self.e3 = Entry(self.root2, width=30, textvariable=self.e3Var)
        self.e4 = Entry(self.root2, width=30, textvariable=self.e4Var)
        self.e5 = Entry(self.root2, width=30, textvariable=self.e5Var)
        self.e6 = Entry(self.root2, width=30, textvariable=self.e6Var)
        self.b3 = Button(self.root2, text='Create Account', command=self.createAccount)
        self.l3.grid(row=0, column=0, pady=3)
        self.l4.grid(row=1, column=0, pady=3)
        self.l5.grid(row=2, column=0, pady=3)
        self.l6.grid(row=3, column=0, pady=3)
        self.e3.grid(row=0, column=1, columnspan=2, pady=3, padx=5)
        self.e4.grid(row=1, column=1, columnspan=2, pady=3, padx=5)
        self.e5.grid(row=2, column=1, columnspan=2, pady=3, padx=5)
        self.e6.grid(row=3, column=1, columnspan=2, pady=3, padx=5)
        self.b3.grid(row=6, column=0, pady=3, columnspan=2)
        self.l7 = Label(self.frame1, text='Breeze Card')

        self.frame1.grid(row=5, column=0, pady=8, padx=3, columnspan=2)
        self.e7 = Entry(self.frame1, width=30, textvariable=self.e7Var, )
        self.l8 = Label(self.frame1, text='Card Number')
        self.strVar = StringVar(value='existing')
        self.l7.grid(row=0, column=0, pady=5)
        self.radio1 = Radiobutton(self.frame1, text="Use my existing Breeze Card", variable=self.strVar,
                                  value="existing")
        self.radio1.grid(row=1, column=0)
        self.e7.grid(row=2, column=1)
        self.l8.grid(row=2, column=0)
        self.radio2 = Radiobutton(self.frame1, text="Get a new Breeze Card", variable=self.strVar, value="new")
        self.radio2.grid(row=3, column=0)

    def displayLogin(self):
        self.root2.withdraw()
        self.root.deiconify()
        self.login()

    def displayLogin2(self):
        self.root3.withdraw()
        self.root.deiconify()
        self.login()

    def displayLogin3(self):
        self.root4.withdraw()
        self.root.deiconify()
        self.login()

    def loginTry(self):
        self.username = self.e1.get()
        self.m = hashlib.md5()
        self.password = self.e2.get()
        self.m.update(self.password.encode('utf-8'))
        cursor = self.db.cursor()
        sql = '''SELECT Username, Password, IsAdmin FROM User WHERE Username =%s and Password=%s'''
        cursor.execute(sql, (self.username, self.m.hexdigest()))
        self.s = 0
        for each in cursor:

            if int(each[2]) == 1:

                self.displayAdmin()
                self.s = 1
            elif int(each[2]) == 0:
                self.s = 1
                self.displayPassenger()

        if self.s == 0:
            messagebox.showerror('Login Error', 'Username and Password are incorrect')

    def createAccount(self):

        self.userTry = self.e3.get()
        self.emailTry = self.e4.get()
        self.passwordTry = self.e5.get()
        self.passwordConfirm = self.e6.get()

        cursor2 = self.db.cursor()

        if self.userTry != '' and self.emailTry != '' and self.passwordTry != '':

            if len(self.passwordTry) > 7 and self.passwordTry == self.passwordConfirm:

                ##                rgx = rgx3 = r'[0-9]{2,3}\.[0-9]{2}[BM]{1}'
                ##                self.it = re.finditer(rgx, self.emailTry)
                ##                for each in self.it:
                self.encodePass = hashlib.md5()
                self.encodePass.update(self.passwordConfirm.encode('utf-8'))
                sql1 = '''SELECT 1 FROM User WHERE Username=%s'''
                cursor2.execute(sql1, (self.userTry))
                if cursor2.fetchone() is None:
                    sql2 = '''SELECT 1 FROM Passenger WHERE Email = %s'''
                    cursor2 = self.db.cursor()
                    cursor2.execute(sql2, (self.emailTry))
                    if cursor2.fetchone() is None:
                        if self.strVar.get() == 'existing':
                            cursor2 = self.db.cursor()
                            sql3 = '''SELECT 1 FROM Breezecard WHERE BreezecardNum =%s'''
                            cursor2.execute(sql3, (self.e7Var.get()))
                            if cursor2.fetchone() is None:
                                messagebox.showerror('Breezecard Error', 'That Breezecard does not exist')
                            else:
                                sql4 = '''SELECT BelongsTo From Breezecard WHERE BreezecardNum = %s'''
                                cursor2.execute(sql4, (self.e7Var.get()))
                                if cursor2.fetchone() is None:
                                    sql5 = '''INSERT INTO User VALUES (%s,%s,"0")'''
                                    sql6 = '''INSERT INTO Passenger VALUES (%s, %s)'''
                                    sql7 = '''INSERT INTO Breezecard VALUES (%s, "0.00", %s)'''
                                    cursor2.execute(sql5, (self.userTry, self.encodePass.hexdigest()))
                                    cursor2.execute(sql6, (self.userTry, self.emailTry))
                                    cursor2.execute(sql7, (self.e7Var.get(), self.userTry()))
                                    self.db.commit()
                                else:
                                    self.s = 0
                                    while self.s == 0:
                                        self.randCard = randint(1000000000000000, 9999999999999999)
                                        sql8 = '''SELECT 1 FROM Breezecard WHERE BreezecardNum = %s'''
                                        cursor2.execute(sql8, (self.randCard))
                                        if cursor2.fetchone() is None:
                                            self.s = 1
                                    sql9 = '''INSERT INTO User VALUES (%s,%s,"0")'''
                                    sql10 = '''INSERT INTO Passenger VALUES (%s, %s)'''
                                    sql11 = '''INSERT INTO Breezecard VALUES (%s, "0.00", %s)'''
                                    sql12 = '''INSERT INTO Conflict VALUES (%s, %s, 'curent time')'''
                                    cursor2.execute(sql9, (self.userTry, self.encodePass.hexdigest()))
                                    cursor2.execute(sql10, (self.userTry, self.emailTry))
                                    cursor2.execute(sql11, (self.randCard, self.userTry))
                                    cursor2.execute(sql12, (self.userTry, self.randCard))
                                    self.db.commit()


                        else:
                            print('Trying to insert new 1')

                            self.s = 0
                            while self.s == 0:
                                self.randCard = randint(1000000000000000, 9999999999999999)
                                sql16 = '''SELECT 1 FROM Breezecard WHERE BreezecardNum = %s'''
                                cursor2.execute(sql16, (self.randCard))
                                if cursor2.fetchone() is None:
                                    self.s = 1

                            sql13 = '''INSERT INTO User VALUES (%s,%s,"0")'''
                            sql14 = '''INSERT INTO Passenger VALUES (%s, %s)'''
                            sql15 = '''INSERT INTO Breezecard VALUES (%s, "0.00", %s)'''
                            cursor2.execute(sql13, (self.userTry, self.encodePass.hexdigest()))
                            cursor2.execute(sql14, (self.userTry, self.emailTry))
                            cursor2.execute(sql15, (self.randCard, self.userTry))
                            self.db.commit()



                    else:
                        messagebox.showerror('Email Error', 'Email is taken. Please choose another')

                else:
                    messagebox.showerror('Username Error', 'Username is taken. Please choose another')
            else:
                messagebox.showerror('Password Error',
                                     'Password must be at least 8 characters and must match what is entered in Conifrm Password')

        else:
            messagebox.showerror('Registration Error', 'Make sure all fields are filled out.')

    def createStation(self):
        print('Trying to create station....')
        cursor = self.db.cursor()
        if self.csVar2.get() == 1:
            self.csVar2 = 0
        else:
            self.csVar2 = 1
        if self.csVar.get() == 'train':
            self.trainVar = 1
        else:
            self.trainVar = 0
        print('Station Name:', self.cs2Var.get())
        print('Stop ID:', self.cs4Var.get())
        print('Entry Fare:', self.cs6Var.get())
        if self.cs2Var.get() != '' and self.cs4Var.get() != '' and self.cs6Var.get() != '':
            sql1 = '''SELECT 1 FROM Station WHERE StopID=%s'''
            cursor.execute(sql1, (self.cs4Var.get()))
            if cursor.fetchone() is None:
                sql2 = '''SELECT 1 FROM Station WHERE Name = %s and IsTrain = %s'''
                cursor.execute(sql2, (self.cs2Var.get(), self.csVar2))
                if cursor.fetchone() is None:
                    if self.csVar.get() == 'train':
                        sql3 = '''INSERT INTO Station VALUES(%s,%s,%s, %s, %s)'''
                        cursor.execute(sql3, (
                        self.cs4Var.get(), self.cs2Var.get(), self.cs6Var.get(), self.csVar2, self.trainVar,))
                        self.db.commit()
                    else:
                        sql4 = '''INSERT INTO Station VALUES(%s,%s,%s, %s, %s)'''
                        cursor.execute(sql4, (
                        self.cs4Var.get(), self.cs2Var.get(), self.cs6Var.get(), self.csVar2, self.trainVar,))
                        sql5 = '''INSERT INTO BusStationIntersection VALUES(%s, %s)'''
                        cursor.execute(sql5, (self.cs4Var.get(), self.cs11Var.get()))
                        self.db.commit()




                else:
                    messagebox.showerror('Create Station Error', 'This station already exists.')

            else:
                messagebox.showerror('Create Station Error', 'This Stop ID already exists.')
        else:
            messagebox.showerror('Create Station Error', 'Please make sure all fields are filled out.')

    def updateFilter(self):
        print('Updating Filter...')
        if self.cm4Var.get() != '':
            print('Owner: ', self.cm4Var.get())
        if self.cm7Var.get() != '':
            print('Card Number: ', self.cm7Var.get())
        if self.cm10Var.get() != '' and self.cm12Var.get() != '':
            print('Value Between: ', self.cm10Var.get(), 'and', self.cm12Var.get())
        if self.cmVar.get() == 1:
            print('SHOWING SUSPENDED CARDS')

    def updateFlowRep(self):
        print('Update flow report for start time:', self.fr2Var.get(), 'and end time:', self.fr6Var.get())

    def setVal(self):
        print('Set value of selected card to', self.cm14Var.get())

    def tranCard(self):
        print('Transfer selected card to', self.cm16Var.get())


root = Tk()
app = MARTA(root)
root.mainloop()