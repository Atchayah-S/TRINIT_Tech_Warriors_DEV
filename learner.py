import hashlib
import os
def signup():
    email = input("")
    pwd = input()
    conf_pwd = input()
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.txt", "w") as f:
             f.write(email + "\n")
             f.write(hash1)
        f.close()
        login(email,pwd)
    else:
        print("Password is not same as above! \n")
def login(email,pwd):
   
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.txt", "r") as f:
        
        stored_email, stored_pwd = f.read().split("\n")
    f.close()
    if email == stored_email and auth_hash == stored_pwd:
         print("Login successfully")
         print("Welcome Learner! \nMake a move to upgrade yourself with current world")
    else:
         print("Login failed! \n")
while 1:
  #  print("********** Login System **********")
    ch=input()
    if ch == "signup":
        signup()
    elif ch == "login":
        login(input(),input())
        break
    elif ch == "exit":
        break
    else:
        print("Wrong Choice!")