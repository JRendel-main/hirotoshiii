import mysql.connector as mysql

db = mysql.connect(
  host="localhost",
  user="root",
  password="",
  db="college"
)
command_handler = db.cursor(buffered=True)

def admin_session():
    while 1:
        print("")
        print("Admin Dashboard")
        print("1. Registr for Student")
        print("2. Register of Teacher")
        print("3. Delete Student")
        print("4. Delete Teacher")
        print("5. Logout")
        
        user_option = input(str("Option: "))
        if user_option == "1":
            print("")
            print("Regsiter a Student's Account")
            username = input(str("Student Username: "))
            password = input(str("Student Password: "))
            query_vals = (username,password)
            command_handler.execute("INSERT INTO users(username, password, privilage) VALUES(%s,%s,'student')", query_vals)
            db.commit()
            print(username + " has been registed")
        elif user_option == "2":
            print("")
            print("Regsiter a Teacher's Account")
            username = input(str("Teacher Username: "))
            password = input(str("Teacher Password: "))
            query_vals = (username,password)
            command_handler.execute("INSERT INTO users(username, password, privilage) VALUES(%s,%s,'teacher')", query_vals)
            db.commit()
            print(username + " has been registed")
        elif user_option == "3":
            print("")
            print("Delete Stundent's Account")
            username = input(str("Stundets Username: "))
            query_vals = (username, "student")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilage = %s ", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not Found!")
            else:
                print(username + " has been deleted!")
        elif user_option == "4":
            print("")
            print("Delete Teacher's Account")
            username = input(str("Teacher's Username: "))
            query_vals = (username, "teacher")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilage = %s ", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not Found!")
            else:
                print(username + " has been deleted!")
        elif user_option == "5":
            break
        else:
            print("Invalid option! Try Again!")
        
        

def auth_admin():
    print("Admin Login")
    username = input(str("Username: "))
    password = input(str("Password: "))
    
    if username == "admin":
        if password == "pass":
            admin_session()
        else:
            print("Wrong Try again!")
    else:
        print("Try Again!")
def main():
    while 1:
        print("Welcome to College System!")
        print("/*****************************/")
        print("1 for Login as Student")
        print("2 for Teacher")
        print("3 for Admin")
        print("/*****************************/")

        user_option = input(str("Option: "))
        if user_option == "1":
            print("Hello Stud3ent")
        elif user_option == "2":
            print("Hello Teacher!")
        elif user_option == "3":
            auth_admin()
        else:
            print("Error! Try Again")
            break
        
main()