import EVC
#------------------------------------------Function for User Input--------------------------------
def take_input_from_user():
    username = input("Enter username:")
    Id = input("Enter User Id in Integer froms:")
    email = input("Enter User Email:")
    password = input("Enter User password in Integer form:")
    EVC.add_user(username,Id,email,password)

#-------------------------------------------Delete Data from Table--------------------------------

def Delete_user():
    Id = input("Enter User Id in Integer froms:")
    EVC.Delete_User_From_Table(Id)




def Authenticate_User():
    user_id=input("Enter user_id !")
    password=input("Enter password !")
    EVC.Authenticate_Custom_User(user_id,password)
    #EVC.Authenticate_Default_User(user_id,password)



def main():
    #Authenticate_User()2
    #EVC.Authenticate_User('5555')
    take_input_from_user()
    #Delete_user()
    #EVC.Update_user_information()
    #EVC.Update_information(New_Name='Custom3')
    #list=EVC.show_data()
    print(list)

if __name__ == "__main__":
    main()