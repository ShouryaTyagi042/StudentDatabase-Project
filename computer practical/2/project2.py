import mysql.connector
import time
import sys
from tabulate import tabulate

say = "Login"
print("=" * len(say.center(156, ".")))
print(say.center(156, "."))
print("=" * len(say.center(156, ".")))
print()

# getting user credentials
user_name = input("Enter your mysql username:  ")
mysql_passwd =  input("Enter your mysql password:  ")
host_name = input("Enter your host name:  ")


# checking user credentials
try:
    myconnection = mysql.connector.connect(host=host_name,user=user_name,passwd=mysql_passwd)
    mycursorconnection = myconnection.cursor()
    try :
        mycursorconnection.execute("CREATE DATABASE School_Management_System")
        print()
        print("DATABASE School_Management_System CREATED")
    except mysql.connector.errors.DatabaseError :
        print()
        print("Databse School_Management_System already exists ! ")
    mydb = mysql.connector.connect(host=host_name,user=user_name,passwd=mysql_passwd,database="School_Management_System")
    mycursor = mydb.cursor()

    def create_student_table():
        mycursor.execute(" CREATE TABLE student (UID int auto_increment , Roll_No int(15) ,Name varchar(30) , Class varchar(10) , Section varchar(10) , Phone_No varchar(255) , Email varchar(166) , Primary key (UID));")
        mydb.commit()
    def create_library_table() :
        mycursor.execute("CREATE TABLE Library (BID int auto_increment , Book_Code varchar(55) ,Book_Name varchar(230) , Author_Name varchar(166) , Subject varchar(166) ,Issued varchar(25) ,UID int(22) , Return_Date Date , Return_Status varchar(20) , Primary key (BID)); ")
        mydb.commit()
    def create_attendance_table() :
        mycursor.execute("CREATE TABLE Attendance (AID int auto_increment , Student_UID int(25) ,Date_ date ,  Subject varchar(166) ,Status  varchar(35) ,Time_of_Join time, Time_of_Leave time , Primary key (AID)); ")
        mydb.commit()

    def main() :

        try :
            create_attendance_table()
            create_library_table()
            create_student_table()

            print("Required tables created !")
            print()

        except :
            print("Required tables already exists")
            print()

        while True :
            heading = "SCHOOL MANAGEMENT SYSTEM"
            print("="*len(heading.center(156,"-")))
            print("+"*len(heading.center(156,"-")))
            print(heading.center(156,"-"))
            print("+"*len(heading.center(156,"-")))
            print("="*len(heading.center(156,"-")))
            print()
            print("1. Students ")
            print("2. Attendance")
            print("3. Library")
            print("4. Exit")
            print()
            choice = input("Enter your choice: ")
            print()
            if choice == "1" :
                student_menu()
            elif choice == "2" :
                attendance_menu()
            elif choice == "3" :
                library_menu()
            elif choice == "4" :
                confirm = input("Do YOU REALLY WANT TO EXIT Y OR N")
                if confirm == "Y" :
                    print("BYE")
                    break
                elif confirm == "N" :
                    print("YOU CAN CONTINUE ")

                else :
                    print("INVALID choice")
    def student_menu() :
        while True :
            heading = "SCHOOL MANAGEMENT SYSTEM "
            sub_1 = "<STUDENT>"
            print("="*len(heading.center(156,"-")))
            # print("+"*len(heading.center(156,"-")))
            print(heading.center(156,"-"))
            print(sub_1.center(156,"-"))
            # print("+"*len(heading.center(156,"-")))
            print("="*len(heading.center(156,"-")))
            print()
            print("1. Add Student")
            print("2. Update Student")
            print("3. Show Student")
            print("4. Remove Student")
            print("5. Return ")
            print()
            choice = input("Enter your choice: ")
            print()

            if choice == "1" :
                student_menu_add()
            elif choice == "2" :
                student_menu_update()
            elif choice == "3" :
                student_menu_show()
            elif choice == "4" :
                student_menu_remove()
            elif choice == "5" :
                break
            else :
                print("Invalid Choice")
    def student_menu_add() :
        heading = "SCHOOL MANAGEMENT SYSTEM "
        sub_1 = "STUDENT"
        sub_2 = "<ADD>"
        print("="*len(heading.center(156,"-")))
        # print("+"*len(heading.center(156,"-")))
        print(heading.center(156,"-"))
        print(sub_1.center(156,"-"))
        print(sub_2.center(156,"-"))
        # print("+"*len(heading.center(156,"-")))
        print("="*len(heading.center(156,"-")))
        print()

        roll_no = int(input("Enter Roll no :"))
        name = input("Enter your name :")
        clas = input("Enter Class :")
        section = input("Enter section :")
        phone_no = input("Enter phone_no :")
        email = input("Enter email:")

        query = "insert into student(Roll_No,Name,Class,Section,Phone_No,Email) values(%s,%s,%s,%s,%s,%s)"
        values = (roll_no,name,clas,section,phone_no,email)
        mycursor.execute(query,values)
        mydb.commit()
    def student_menu_show() :
        while True :
            heading = "SCHOOL MANAGEMENT SYSTEM "

            sub_1 = "STUDENT"
            sub_2 = "<SHOW>"
            print("="*len(heading.center(156,"-")))
        # print("+"*len(heading.center(156,"-")))
            print(heading.center(156,"-"))
            print(sub_1.center(156,"-"))
            print(sub_2.center(156,"-"))
        # print("+"*len(heading.center(156,"-")))
            print("="*len(heading.center(156,"-")))
            print()

            mycursor.execute("SELECT * FROM student ")
            rec = mycursor.fetchall()
            print("-"*136)

            # data = [row[0],row[1],row[2],row[3]]



            print(tabulate(rec , headers= ["UID","Roll_No","Name","Class","Section","Phone_No","Email"]))
            print("-"*136)
            print()
            break
    def student_menu_update() :
        while  True :
            heading = "SCHOOL MANAGEMENT SYSTEM "

            sub_1 = "STUDENT"
            sub_2 = "<UPDATE>"
            print("="*len(heading.center(156,"-")))
        # print("+"*len(heading.center(156,"-")))
            print(heading.center(156,"-"))
            print(sub_1.center(156,"-"))
            print(sub_2.center(156,"-"))
        # print("+"*len(heading.center(156,"-")))
            print("="*len(heading.center(156,"-")))
            print()

            print("1. UPDATE ROLL NUMBER ")
            print("2. UPDATE NAME ")
            print("3. UPDATE CLASS")
            print("4. UPDATE SECTION")
            print("5. UPADATE PHONE NUMBER ")
            print("6. UPDATE EMAIL ")
            print("7. RETURN")
            print()

            choice = int(input("Enter your choice: "))
            print()
            exists = False
            if choice >= 1 and choice <= 6 :
                uid = int(input("Enter UID of student :"))
                if choice == 1:
                    mycursor.execute("SELECT * FROM student")
                    result = mycursor.fetchall()
                    for r_col in result :
                        if r_col[0] == uid :
                            exists = True
                            new_rno = input("Enter new roll_no :")
                            query = "Update student set Roll_No=(%s) where UID = (%s)"
                            value = (new_rno,uid)
                            mycursor.execute(query,value)
                            mydb.commit()
                            print("Roll no updated")

                elif choice == 2 :
                    mycursor.execute("SELECT * FROM student")
                    result = mycursor.fetchall()
                    for r_col in result :
                        if r_col[0] == uid :
                            exists = True
                            new_name = input("Enter new Name :")
                            query = "Update student set Name =(%s) where UID = (%s)"
                            value = (new_name,uid)
                            mycursor.execute(query,value)
                            mydb.commit()
                            print("Name updated")
                elif choice == 3 :
                    mycursor.execute("SELECT * FROM student")
                    result = mycursor.fetchall()
                    for r_col in result :
                        if r_col[0] == uid :
                            exists = True
                            new_class = input("Enter new class :")
                            query = "Update student set Class=(%s) where UID = (%s)"
                            value = (new_class,uid)
                            mycursor.execute(query,value)
                            mydb.commit()
                            print(" Class updated")
                elif choice == 4:
                    mycursor.execute("SELECT * FROM student")
                    result = mycursor.fetchall()
                    for r_col in result :
                        if r_col[0] == uid :
                            exists = True
                            new_section = input("Enter new Section :")
                            query = "Update student set Section=(%s) where UID = (%s)"
                            value = (new_section,uid)
                            mycursor.execute(query,value)
                            mydb.commit()
                            print("Section updated")
                elif choice == 5 :
                    mycursor.execute("SELECT * FROM student")
                    result = mycursor.fetchall()
                    for r_col in result :
                        if r_col[0] == uid :
                            exists = True
                            new_phone = input("Enter new Phone_No :")
                            query = "Update student set Phone_No=(%s) where UID = (%s)"
                            value = (new_phone,uid)
                            mycursor.execute(query,value)
                            mydb.commit()
                            print("Phone_No  updated")
                elif choice == 6 :
                    mycursor.execute("SELECT * FROM student")
                    result = mycursor.fetchall()
                    for r_col in result :
                        if r_col[0] == uid :
                            exists = True
                            new_email = input("Enter new email :")
                            query = "Update student set Email=(%s) where UID = (%s)"
                            value = (new_email,uid)
                            mycursor.execute(query,value)
                            mydb.commit()
                            print("Email updated")
            elif choice == 7 :
                break
            else :
                print("Invalid Choice")
            if not exists and choice >= 1 and choice <= 6 :
                print("Invalid Details")
    def student_menu_remove():
        heading = "SCHOOL MANAGEMENT SYSTEM "

        sub_1 = "STUDENT"
        sub_2 = "<REMOVE>"
        print("="*len(heading.center(156,"-")))
        print(heading.center(156,"-"))
        print(sub_1.center(156,"-"))
        print(sub_2.center(156,"-"))
        # print("+"*len(heading.center(156,"-")))
        print("="*len(heading.center(156,"-")))
        print()

        ask_uid = int(input("Enter UID of Student you want to remove : "))
        sql = "SELECT * FROM student WHERE UID = (%s) "
        val = (ask_uid,)
        mycursor.execute(sql,val)
        rec= mycursor.fetchall()
        if len(rec) <= 0 :
            print("WRONG UID")
        else :
            confirm_name = input("Confirm by entering name  ")
            for row in rec :
                if confirm_name == row[2] :
                    query = "DELETE FROM student WHERE UID = (%s) "
                    value = (ask_uid,)
                    mycursor.execute(query,value)
                    mydb.commit()
                    print(row[2], " WAS  REMOVED")
                else :
                    print("Incorrect NAME")
    def library_menu() :
        while True() :
            heading = "SCHOOL MANAGEMENT SYSTEM "
            sub_1 = "<library>"
            print("="*len(heading.center(156,"-")))
            # print("+"*len(heading.center(156,"-")))
            print(heading.center(156,"-"))
            print(sub_1.center(156,"-"))
            # print("+"*len(heading.center(156,"-")))
            print("="*len(heading.center(156,"-")))
            print()
            print("1. Add Book")
            print("2. Update Book")
            print("3. Show Book")
            print("4. Remove Book")

            print("5. Search Book ")
            print("6. Return ")
            print()
            choice = input("Enter your choice: ")
            print()

            if choice == "1" :
                library_menu_add()
            elif choice == "2 " :
                library_menu_update()
            elif choice == " 3" :
                library_menu_show()
            elif choice == "4" :
                library_menu_delete()
            elif choice == "6" :

                break
            elif choice =="5" :
                library_menu_search()
            else :
                print("Invalid Choice")
    def library_menu_add():
        heading = "SCHOOL MANAGEMENT SYSTEM "

        sub_1 = "LIBRARY"
        sub_2 = "<ADD>"
        print("="*len(heading.center(156,"-")))

        print(heading.center(156,"-"))
        print(sub_1.center(156,"-"))
        print(sub_2.center(156,"-"))

        print("="*len(heading.center(156,"-")))
        print()
        book_code = input("Enter your book code: ")
        book_name = input("Enter book name : ")
        author_name = input("Enter Author Name ")
        subject = input("Enter subject : ")
        issued = input("Enter is your book issued Yes or No : ")
        if issued == "Yes" or issued == "Y" :
            st_uid = int(input("Enter Student's UID : "))
            mycursor.execute("SELECT * FROM student ")
            rec = mycursor.fetchall()
            for row in rec :
                if row[0] == st_uid  :
                    return_date = input("Enter Assigned return date (YYYY-MM-DD): ")
                    return_status = input("Is this book returned (Y or N) :")
                    sql = "INSERT INTO library(Book_Code,Book_Name,Author_Name,Subject,Issued,UID,Return_Date,Return_Status) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                    val  = (book_code,book_name,author_name,subject,issued,st_uid,return_date,return_status)
                    try :
                        mycursor.execute(sql,val)
                        mydb.commit()
                        exists = True
                        sql_1 = "SELECT * FROM library WHERE Book_Code = (%s) and Book_Name = (%s) and Author_Name = (%s) and Subject = (%s) "
                        val_1 = (book_code,book_name,author_name,subject)
                        mycursor.execute(sql_1,val_1)
                        result = mycursor.fetchall()
                        print()
                        print(tabulate(result , headers= ["BID","Book_Code","Book_Name","Author_Name","Subject","Issued","UID","Return_Date","Return_Status"]))
                    except mysql.connector.errors.DataError as e:
                        print()
                        print("Error",e)
                        print()
            if not exists :
                print("Student's UID is incorrect ")
                print("Go to Student section to see ")
                print()
        elif issued == "N" or issued == "No" :
            sql = "INSERT INTO library(Book_Code,Book_Name,Author_Name,Subject,Issued,) values(%s,%s,%s,%s,%s,'No')"
            val  = (book_code,book_name,author_name,subject)
            mycursor.execute(sql,val)
            mydb.commit()
            sql_1 = "SELECT * FROM library WHERE Book_Code = (%s) and Book_Name = (%s) and Author_Name = (%s) and Subject = (%s) "
            val_1 = (book_code,book_name,author_name,subject)
            mycursor.execute(sql_1,val_1)
            result = mycursor.fetchall()
            print()
            print(tabulate(result , headers= ["BID","Book_Code","Book_Name","Author_Name","Subject","Issued","UID","Return_Date","Return_Status"]))
        else :
            print("Invalid Option")
            print()
    def library_menu_show() :
        while True :
            heading = "SCHOOL MANAGEMENT SYSTEM "
            sub_1 = "LIBRARY"
            sub_2 = "<SHOW>"
            print("="*len(heading.center(156,"-")))
            print(heading.center(156,"-"))
            print(sub_1.center(156,"-"))
            print(sub_2.center(156,"-"))
            print("="*len(heading.center(156,"-")))
            print()
            mycursor.execute("SELECT * FROM library ")
            rec = mycursor.fetchall()
            print("-"*156)
            print(tabulate(rec , headers= ["BID","Book_Code","Book_Name","Author_Name","Subject","Issued","UID","Return_Date","Return_Status"]))
            print("-"*156)
    def library_menu_search() :
        while  True :
            heading = "SCHOOL MANAGEMENT SYSTEM "
            sub_1 = "LIBRARY"
            sub_2 = "<SEARCH>"
            print("="*len(heading.center(156,"-")))
            print(heading.center(156,"-"))
            print(sub_1.center(156,"-"))
            print(sub_2.center(156,"-"))
            print("="*len(heading.center(156,"-")))
            print()

            print("1. SEARCH WITH BID :")
            print("2. SEARCH WITH Book Code: ")
            print("3. SEARCH WITH Book Name ")
            print("4. SEARCH WITH Author Name ")
            print('5. SEARCH WITH SUBJECT')
            print("6. SEARCH WITH ISSUED ")
            print("7. SEARCH WITH UID")
            print("8. SEARCH WITH Return Date")
            print("9. SEARCH WITH Return Status")
            print("10. Return ")

            print()
            choice = int(input("Enter your Choice : "))
            print()

            if choice == 1 :
                ask_bid = input("Enter BID:")
                sql = "SELECT * FROM library WHERE BID =(%s) "
                val = (ask_bid,)
                mycursor.execute(sql,val)
                rec = mycursor.fetchall()
                if len(rec) >= 1 :
                    print(tabulate(rec , headers= ["BID","Book_Code","Book_Name","Author_Name","Subject","Issued","UID","Return_Date","Return_Status"]))
                    print()
                else :
                    print("Any record with bid ",ask_bid," not found ! ")
            elif choice == 2 :
                ask_bcode = input("Enter Book_Code:")
                sql = "SELECT * FROM library WHERE Book_Code =(%s) "
                val = (ask_bcode,)
                mycursor.execute(sql,val)
                rec = mycursor.fetchall()
                if len(rec) >= 1 :
                    print(tabulate(rec , headers= ["BID","Book_Code","Book_Name","Author_Name","Subject","Issued","UID","Return_Date","Return_Status"]))
                    print()
                else :
                    print("Any record with Book code ",ask_bcode," not found ! ")
            elif choice == 3 :
                ask_bname = input("Enter Book_Name:")
                sql = "SELECT * FROM library WHERE Book_Name =(%s) "
                val = (ask_bname,)
                mycursor.execute(sql,val)
                rec = mycursor.fetchall()
                if len(rec) >= 1 :
                    print(tabulate(rec , headers= ["BID","Book_Code","Book_Name","Author_Name","Subject","Issued","UID","Return_Date","Return_Status"]))
                    print()
                else :
                    print("Any record with Book_Name ",ask_bname," not found ! ")
            elif choice == 4 :
                ask_aname = input("Enter Author_Name:")
                sql = "SELECT * FROM library WHERE Author_Name =(%s) "
                val = (ask_aname,)
                mycursor.execute(sql,val)
                rec = mycursor.fetchall()
                if len(rec) >= 1 :
                    print(tabulate(rec , headers= ["BID","Book_Code","Book_Name","Author_Name","Subject","Issued","UID","Return_Date","Return_Status"]))
                    print()
                else :
                    print("Any record with Author_Namer ",ask_aname," not found ! ")
            elif choice == 5 :
                ask_sub = input("Enter Subject:")
                sql = "SELECT * FROM library WHERE Subject =(%s) "
                val = (ask_sub,)
                mycursor.execute(sql,val)
                rec = mycursor.fetchall()
                if len(rec) >= 1 :
                    print(tabulate(rec , headers= ["BID","Book_Code","Book_Name","Author_Name","Subject","Issued","UID","Return_Date","Return_Status"]))
                    print()
                else :
                    print("Any record with subject ",ask_sub," not found ! ")
            elif choice == 6 :
                ask_istatus = input("Enter Issued:")
                sql = "SELECT * FROM library WHERE Issued =(%s) "
                val = (ask_istatus,)
                mycursor.execute(sql,val)
                rec = mycursor.fetchall()
                if len(rec) >= 1 :
                    print(tabulate(rec , headers= ["BID","Book_Code","Book_Name","Author_Name","Subject","Issued","UID","Return_Date","Return_Status"]))
                    print()
                else :
                    print("Any record with issued status ",ask_istatus," not found ! ")
            elif choice == 7 :
                ask_suid = input("Enter UID:")
                sql = "SELECT * FROM library WHERE UID =(%s) "
                val = (ask_suid,)
                mycursor.execute(sql,val)
                rec = mycursor.fetchall()
                if len(rec) >= 1 :
                    print(tabulate(rec , headers= ["BID","Book_Code","Book_Name","Author_Name","Subject","Issued","UID","Return_Date","Return_Status"]))
                    print()
                else :
                    print("Any record with UID ",ask_suid," not found ! ")
            elif choice == 8 :
                ask_rd = input("Enter Return_Date:")
                sql = "SELECT * FROM library WHERE Return_Date =(%s) "
                val = (ask_rd,)
                mycursor.execute(sql,val)
                rec = mycursor.fetchall()
                if len(rec) >= 1 :
                    print(tabulate(rec , headers= ["BID","Book_Code","Book_Name","Author_Name","Subject","Issued","UID","Return_Date","Return_Status"]))
                    print()
                else :
                    print("Any record with Return_Date ",ask_rd," not found ! ")
            elif choice == 9 :
                ask_rs = input("Enter Return_Status:")
                sql = "SELECT * FROM library WHERE Return_Status =(%s) "
                val = (ask_rs,)
                mycursor.execute(sql,val)
                rec = mycursor.fetchall()
                if len(rec) >= 1 :
                    print(tabulate(rec , headers= ["BID","Book_Code","Book_Name","Author_Name","Subject","Issued","UID","Return_Date","Return_Status"]))
                    print()
                else :
                    print("Any record with Return_Status ",ask_rs," not found ! ")
            elif choice == 10 :
                break
            else :
                print("Invalid choice")
    def library_menu_update() :
        while  True :
            heading = "SCHOOL MANAGEMENT SYSTEM "
            sub_1 = "LIBRARY"
            sub_2 = "<UPDATE>"
            print("="*len(heading.center(156,"-")))
            print(heading.center(156,"-"))
            print(sub_1.center(156,"-"))
            print(sub_2.center(156,"-"))
            print("="*len(heading.center(156,"-")))
            print()

            # print("1. UPDATE BID :")
            print("1. UPDATE Book Code: ")
            print("2. UPDATE Book Name ")
            print("3. UPDATE Author Name ")
            print('4. UPDATE SUBJECT')
            print("5. UPDATE ISSUED ")
            # print("7. UPDATE UID")
            # print("8. UPDATE Return Date")
            # print("9. SEARCH WITH Return Status")
            print("6. Return ")
            print()

            if choice >= 1 and choice <= 5 :
                bid = int(input("Enter BID of book :"))
                if choice == 1:
                    mycursor.execute("SELECT * FROM library")
                    result = mycursor.fetchall()
                    for r_col in result :
                        if r_col[0] == bid :
                            exists = True
                            new_rno = input("Enter new Book_Code :")
                            query = "Update library set Book_Code=(%s) where BID = (%s)"
                            value = (new_rno,bid)
                            mycursor.execute(query,value)
                            mydb.commit()
                            print("Book_Code updated")

                elif choice == 2 :
                    mycursor.execute("SELECT * FROM library")
                    result = mycursor.fetchall()
                    for r_col in result :
                        if r_col[0] == bid :
                            exists = True
                            new_name = input("Enter new Book_Name :")
                            query = "Update library set Book_Name =(%s) where BID = (%s)"
                            value = (new_name,bid)
                            mycursor.execute(query,value)
                            mydb.commit()
                            print("BOOK Name updated")
                elif choice == 3 :
                    mycursor.execute("SELECT * FROM library")
                    result = mycursor.fetchall()
                    for r_col in result :
                        if r_col[0] == bid :
                            exists = True
                            new_class = input("Enter new Author_Name :")
                            query = "Update library set Author_Name=(%s) where BID = (%s)"
                            value = (new_class,bid)
                            mycursor.execute(query,value)
                            mydb.commit()
                            print("Author_Name updated")
                elif choice == 4:
                    mycursor.execute("SELECT * FROM library")
                    result = mycursor.fetchall()
                    for r_col in result :
                        if r_col[0] == bid :
                            exists = True
                            new_section = input("Enter new Subject  :")
                            query = "Update library set Subject =(%s) where BID = (%s)"
                            value = (new_section,bid)
                            mycursor.execute(query,value)
                            mydb.commit()
                            print("Subject updated")
                elif choice == 5 :
                    mycursor.execute("SELECT * FROM library")
                    result = mycursor.fetchall()
                    for r_col in result :
                        if r_col[0] == bid :
                            exists = True
                            new_status = input("Enter new Issued Status Y or N :")
                            if new_status == "Y" :
                                st_uid = int(input("Enter students UID : "))
                                mycursor.execute("select * from student ")
                                rec = mycursor.fetchall()
                                exists = False

                                for row in rec :
                                    if row[0] == st_uid :
                                        return_date = input("Enter assigned date (YYYY-MM-DD): ")
                                        return_status = input("Is this book returned? Y or N ")
                                        sql = "UPDATE library set Issued ='YES' , UID =(%s) ,Return_Date =(%s) , Return_Status = (%s) WHERE BID = (%s) "
                                        val = (st_uid,return_date,return_status,bid)
                                        try :
                                            mycursor.execute(sql,val)
                                            mydb.commit()
                                            exists = True
                                            print("Book Updated")
                                            break
                                        except mysql.connector.errors.DataError as e :
                                            print()
                                            print("Error",e)
                                            print()
                                    if not exists :
                                        print("Students UID is incorrect ")
                                        print()
                            else :
                                sql = "UPDATE library set Issued ='NO' , UID =(%s) ,Return_Date =(%s) , Return_Status = (%s) WHERE BID = (%s) "
                                val = (None,None,None,bid)
                                mycursor.execute(sql,val)
                                mydb.commit()
                                exists = True
                                print("Book Updated ")
                elif choice == 6 :
                    break
                else :
                    print("Invalid Choice")
                if not exists and choice >= 1 and choice <= 5 :
                    print("Invalid Details")
    def library_menu_delete() :
        heading = "SCHOOL MANAGEMENT SYSTEM "

        sub_1 = "LIBRARY"
        sub_2 = "<DELETE>"
        print("="*len(heading.center(156,"-")))
        print(heading.center(156,"-"))
        print(sub_1.center(156,"-"))
        print(sub_2.center(156,"-"))
        # print("+"*len(heading.center(156,"-")))
        print("="*len(heading.center(156,"-")))
        print()

        ask_bid = int(input("Enter BID of BOOK you want to remove : "))
        sql = "SELECT * FROM library WHERE UID = (%s) "
        val = (ask_bid,)
        mycursor.execute(sql,val)
        rec= mycursor.fetchall()
        if len(rec) <= 0 :
            print("WRONG BID")
        else :
            confirm_name = input("Confirm by entering Books NAME  ")
            for row in rec :
                if confirm_name == row[2] :
                    query = "DELETE FROM Library WHERE UID = (%s) "
                    value = (ask_bid,)
                    mycursor.execute(query,value)
                    mydb.commit()
                    print(tabulate(rec , headers= ["BID","Book_Code","Book_Name","Author_Name","Subject","Issued","UID","Return_Date","Return_Status"]))
                    print()
                    print("was REMOVED ! ")
                    print()
                else :
                    print("Incorrect NAME")
    def attendance_menu() :
        while True :
            heading = "SCHOOL MANAGEMENT SYSTEM "
            sub_1 = "<attendance>"
            print("="*len(heading.center(156,"-")))
            # print("+"*len(heading.center(156,"-")))
            print(heading.center(156,"-"))
            print(sub_1.center(156,"-"))
            # print("+"*len(heading.center(156,"-")))
            print("="*len(heading.center(156,"-")))
            print()
            print("1. Add attendance")
            print("2. Update attendance")
            print("3. Show attendance")
            print("4. Remove attendance")
            print("5. Return ")
            print()
            choice = input("Enter your choice: ")
            print()

            if choice == "1" :
                attendance_menu_add()
            elif choice == "2 " :
                attendance_menu_update()
            elif choice == " 3" :
                attendance_menu_show()
            elif choice == "4" :
                attendance_menu_delete()
            elif choice == "5" :
                break
            else :
                print("Invalid Choice")
    def attendance_menu_add():
        heading = "SCHOOL MANAGEMENT SYSTEM "

        sub_1 = "ATTENDANCE"
        sub_2 = "<ADD>"
        print("="*len(heading.center(156,"-")))

        print(heading.center(156,"-"))
        print(sub_1.center(156,"-"))
        print(sub_2.center(156,"-"))
        print("="*len(heading.center(156,"-")))
        print()

        st_uid = int(input("Enter Student's UID : "))
        # exists = False
        mycursor.execute("SELECT * FROM student ")
        rec = mycursor.fetchall()
        for row in rec :
            if row[0] == st_uid  :
                exists = True
                date = input("Enter Assigned date (YYYY-MM-DD): ")
                subject  = input("Enter subject: ")
                status = input("Enter status ( P = Present , A = Absent ):")
                if status in "Pp" :
                    time_of_Join = input("Enter time_of_Join :")
                    time_of_Leave = input("Enter time of leave :")
                    sql = "INSERT INTO attendance(Student_UID,Date_,Subject,Status,Time_of_Join,Time_of_Leave) values(%s,%s,%s,%s,%s,%s)"
                    val  = (st_uid,date,subject,status,time_of_Join,time_of_Leave)
                    try :
                        mycursor.execute(sql,val)
                        mydb.commit()

                    except mysql.connector.errors.DataError as e:
                        print()
                        print("Error",e)
                        print("Enter in HH:MM:SS format ! ")
                        print()
                    sql_1 = "SELECT FROM attendance WHERE Student_UID = (%s) and Date_ = (%s) and Status = (%s) and Time_of_Join = (%s) and Time_of_Leave = (%s)  "
                    val_1 = (st_uid,date,status,time_of_Join,time_of_Leave)
                    mycursor.execute(sql_1,val_1)
                    r = mycursor.fetchall()
                    print(tabulate(r,headers = ["AID","Student_UID","Date","Subject","Status","Time_of_Join","Time_of_Leave"]))
                    print()
                elif status in "Aa" :
                    sql = "INSERT INTO attendance(Student_UID,Date_,Subject,Status,Time_of_Join,Time_of_Leave) values(%s,%s,%s,%s,%s,%s)"
                    val = (st_uid,date,subject,"A",None,None)
                    mycursor.execute(sql,val)
                    mydb.commit()
                    sql_1 = "SELECT FROM attendance WHERE Student_UID = (%s) and Date_ = (%s) and Status = (%s)"
                    val_1 = (st_uid,date,"A")
                    mycursor.execute(sql_1,val_1)
                    r = mycursor.fetchall()
                    print(tabulate(r,headers=["AID","Student_UID","Date","Status","Time_of_Join","Time_of_Leave"]))
                    print()
                else :
                    print("Invalid choice")
            if not exists :
                print()
                print("Incorrect Student_UID")
                print("Check Student_UID  go to student section ")
                print()
    def attendance_menu_update() :
        while  True :
            heading = "SCHOOL MANAGEMENT SYSTEM "
            sub_1 = "ATTENDANCE"
            sub_2 = "<UPDATE>"
            print("="*len(heading.center(156,"-")))
            print(heading.center(156,"-"))
            print(sub_1.center(156,"-"))
            print(sub_2.center(156,"-"))
            print("="*len(heading.center(156,"-")))
            print()
            # print("1. UPDATE BID :")
            print("1. UPDATE Date: ")
            print("2. UPDATE Subject ")
            print("3. UPDATE Status ")
            print('4. UPDATE Student_UID')
            print("5. Return")
            # print("7. UPDATE UID")
            # print("8. UPDATE Return Date")
            # print("9. SEARCH WITH Return Status")
            # print("10. Return ")
            print()

            if choice >= 1 and choice <= 4 :
                aid = int(input("Enter AID of ATTENDANCE :"))
                if choice == 1:
                    mycursor.execute("SELECT * FROM attendance")
                    result = mycursor.fetchall()
                    for r_col in result :
                        if r_col[0] == aid :
                            exists = True
                            new_ac = input("Enter new Date :")
                            query = "Update attendance set Date_=(%s) where AID = (%s)"
                            value = (new_ac,aid)
                            mycursor.execute(query,value)
                            mydb.commit()
                            print("Date updated")

                elif choice == 2 :
                    mycursor.execute("SELECT * FROM attendance")
                    result = mycursor.fetchall()
                    for r_col in result :
                        if r_col[0] == aid :
                            exists = True
                            new_name = input("Enter new SUBJECT :")
                            query = "Update library set Subject =(%s) where AID = (%s)"
                            value = (new_name,aid)
                            mycursor.execute(query,value)
                            mydb.commit()
                            print("Subject updated")
                elif choice == 3 :
                    mycursor.execute("SELECT * FROM attendance")
                    result = mycursor.fetchall()
                    for r_col in result :
                        if r_col[0] == aid :
                            exists = True
                            new_class = input("Enter new Status P = Present and A = Absent  :")
                            if new_class in "Pp" :
                                time_of_Join = input("Enter time_of_Join (HH:MM:SS) : ")
                                time_of_Leave = input("Enter Time_of_Leave (HH:MM:SS) :")
                                sql = "UPDATE attendance set Status = (%s) , Time_of_Join = (%s) , Time_of_Leave = (%s) ,WHERE AID = (%s) "
                                val = ("P",time_of_Join,time_of_Leave,aid)
                                mycursor.execute(sql,val)
                                try :
                                    mydb.commit()
                                    exists = True
                                    print("Status Updated")
                                    print()
                                    break
                                except mysql.connector.errors.DataError as e :
                                    print()
                                    print("Error",e)
                                    print()
                            elif new_class in "Aa" :
                                sql = "UPDATE attendance set Status = (%s) , Time_of_Join = (%s) , Time_of_Leave = (%s) ,WHERE AID = (%s) "
                                val = ("A",None,None,aid)
                                mycursor.execute(sql,val)
                                mydb.commit()
                                exists = True
                                print("Updated")
                                print()
                            else :
                                print("Invalid Choice ")
                                print()



                elif choice == 4:
                    mycursor.execute("SELECT * FROM attendance")
                    result = mycursor.fetchall()
                    for r_col in result :
                        if r_col[0] == aid :
                            exists = True
                            new_section = input("Enter new Student_UID  :")
                            query = "Update attendance set Student_UID =(%s) where AID = (%s)"
                            value = (new_section,aid)
                            mycursor.execute(query,value)
                            mydb.commit()
                            print("Student_UID updated")
                elif choice == 5 :
                     break
                else :
                    print("Invalid Choice")
                if not exists and choice >= 1 and choice <= 4 :
                    print("Invalid Details")
    def attendance_menu_show() :
        while True :
            heading = "SCHOOL MANAGEMENT SYSTEM "
            sub_1 = "ATTENDANCE"
            sub_2 = "<SHOW>"
            print("="*len(heading.center(156,"-")))
            print(heading.center(156,"-"))
            print(sub_1.center(156,"-"))
            print(sub_2.center(156,"-"))
            print("="*len(heading.center(156,"-")))
            print()
            mycursor.execute("SELECT * FROM attendance ")
            rec = mycursor.fetchall()
            print("-"*156)
            print(tabulate(rec,headers = ["AID","Student_UID","Date","Subject","Status","Time_of_Join","Time_of_Leave"]))
            print("-"*156)
    def attendance_menu_delete() :
        heading = "SCHOOL MANAGEMENT SYSTEM "

        sub_1 = "ATTENDANCE"
        sub_2 = "<DELETE>"
        print("="*len(heading.center(156,"-")))
        print(heading.center(156,"-"))
        print(sub_1.center(156,"-"))
        print(sub_2.center(156,"-"))
        # print("+"*len(heading.center(156,"-")))
        print("="*len(heading.center(156,"-")))
        print()

        ask_aid = int(input("Enter AID of ATTENDANCE you want to remove : "))
        sql = "SELECT * FROM attendance WHERE AID = (%s) "
        val = (ask_aid,)
        mycursor.execute(sql,val)
        rec = mycursor.fetchall()
        if len(rec) <= 0 :
            print("WRONG AID")
        else :
            confirm_name = input("Confirm by entering Subject  ")
            for row in rec :
                if confirm_name == row[3] :
                    query = "DELETE FROM attendance WHERE AID = (%s) "
                    value = (ask_aid,)
                    mycursor.execute(query,value)
                    mydb.commit()
                    print(tabulate(rec , headers= ["AID","Student_UID","Date","Subject","Status","Time_of_Join","Time_of_Leave"]))
                    print()
                    print("was REMOVED ! ")
                    print()
                else :
                    print("Incorrect NAME")
    main()
except mysql.connector.errors.ProgrammingError as e :
    print()
    print("Error",e)
    print("Incorrect User or password")










































