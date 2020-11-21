# -----------------------------------------Create Connection----------------------------------
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="EVCDATABASE"
)
# ----------------------------------------Create Table--------------------------------------------
mycursor = mydb.cursor()


#mycursor.execute("CREATE DATABASE EVCDATABASE")  #check Table Already Created
#mycursor.execute("CREATE TABLE USERS (NAME  CHAR(255) NOT NULL,USER_ID INTEGER AUTO_INCREMENT PRIMARY KEY,EMAIL CHAR(255) NULL ,PASSWORD INT NOT NULL)")


# -------------------------------Error----------------------------------------------------------
def Error():
    print("you Entered Wrong Values!")


# ----------------------------------------------------Add Data In Database---------------------------------

def add_user(uname, uid, uemail, upassword):
    sql = "INSERT INTO USERS (NAME,USER_ID,Email,PASSWORD) VALUES (%s, %s,%s,%s)"
    val = [(uname), (uid), (uemail), (upassword)]
    try:
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "was inserted.")
    except:
        mydb.rollback()
        Error()


# -------------------------------------------Data In the DataBase-------------------------------------------
def show_data():
    try:
        mycursor.execute("SELECT NAME FROM USERS")
        myresult = mycursor.fetchall()
        return myresult
    except:
        mydb.rollback()
        Error()


# -------------------------------------------Delete Data from Table--------------------------------

def Delete_User_From_Table(uid):
    sql = "DELETE FROM USERS WHERE USER_ID = %s"
    adr = (uid,)
    if (int(uid) == 1):
        print("you can't Delete Default User")
        return 0
    elif (int(uid) > 1):
        try:
            mycursor.execute(sql, adr)
            mydb.commit()
            print(mycursor.rowcount, "record(s) deleted")
        except:
            mydb.rollback()
            Error()


#--------------------------------------------------Authenticate User--------------------------
# def Authenticate_Custom_User(uid):
#     sql = " SELECT * from USERS WHERE USER_ID like %s "
#     adr = (uid,)
#     try:
#         mycursor.execute(sql, adr)
#         User_Info = mycursor.fetchone()
#         return User_Info[]
#     except:
#         mydb.rollback()
#         Error()


def Authenticate_User(uPassword):
    sql = " SELECT * from USERS WHERE PASSWORD like %s "
    global User_Info
    adr=(uPassword,)
    try:
        mycursor.execute(sql, adr)
        User_Info = mycursor.fetchone()
        if (str(User_Info[3])== uPassword):
            print("you Entered Correct Password")
            if(int(User_Info[1])>1):
                print('you are not default User')
                return User_Info[0]
            elif(int(User_Info[1])==1):
                print("you are Not Custom User")
                return User_Info[0]
        else:
            print("you Entered wrong Password ")


    except:
         mydb.rollback()
         Error()


# --------------------------------------------Authenticate Default User--------------------------------

# def Authenticate_Default_User(uPassword):
#     sql = " SELECT * from USERS WHERE USER_ID like %s "
#     adr = (uPassword,)
#     global User_Info
#     if (int(uid) > 1):
#         print("you are not Default User")
#     elif (int(uid) == 1):
#         try:
#             mycursor.execute(sql, adr)
#             User_Info = mycursor.fetchone()
#             Password = User_Info[3]
#             if (Password == int(uPassword)):
#                 print("you Entered Correct Password")
#             else:
#                 print("you Entered wrong Password ")
#         except:
#             mydb.rollback()
#             Error()


# --------------------------------------Update User information-----------------------------

def Update_information(CurrentUser_Id="",New_Email="", New_Name="", New_Password=""):
    # print(New_Name)
    print(type(CurrentUser_Id))
    User_id = int(CurrentUser_Id)
    if (len(New_Email) != 0):
        print(New_Email)
        sql = "UPDATE USERS SET EMAIL = %s WHERE USER_ID = %s"
        val = (New_Email, User_id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
    if (len(New_Name) != 0):
        if (New_Name == 'Default'):
            print("you can't change the Name")
            return 0
        else:
            sql = "UPDATE USERS SET NAME = %s WHERE USER_ID = %s"
            val = (New_Name, User_id)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
    if (len(New_Password) != 0):
        sql = "UPDATE USERS SET PASSWORD = %s WHERE USER_ID = %s"
        val = (New_Password, User_id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
    else:
        return 0
