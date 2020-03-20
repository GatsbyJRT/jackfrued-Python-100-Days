name = {"rick","summer"}
password = {"123","000"}
while 1 :
    try:
        new_name = input("name is: ")
        new_password = input("password is : ")
        if new_name in name:
            if new_password in password:
                print("you are right")
                break
    except:
        print("your name or password is not correct!")
        continue
