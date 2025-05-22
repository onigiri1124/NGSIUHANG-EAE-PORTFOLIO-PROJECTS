username = input("set your username :")
print(f"{username} is your set username")

password = input("set your password :")
print(f"{password} is your set password")

print("enter username and password")
while True:
    input_username = input("username :")
    if input_username != username:
        print("incorrect username")
        continue

    else:
        input_password = input("password :")
        if input_password == password:
            print("access granted")
            break
        else:
            print("access blocked")