#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
# Registartion function
def registration ():
    temp=0
    pattern = '^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
 # Registering email id and password for the user
 # validating user email id
    username=input('Enter Email :')
    with open('sample.txt','r') as f2:
        if re.search(pattern, username):
            for line in f2:
                if username in line:
                    print("Username already Exsits")
                    temp=1
                    break
        else:
            print('Enter valid email address')
            temp=1
     # validating user password
    specials = ['@','!','#','^','%','$','&','*','(',')']
    if temp != 1:
        password=input('Enter password :')
        if len(password) <16 and len(password) >5:
            if re.search('[0-9]',password):
                if re.search('[A-Z]',password):
                    if re.search('[a-z]',password):
                        if any(char in specials for char in password):
                            with open('sample.txt', 'a') as f:
                                f.write(f"\n{username},{password}")
                                print("Registration Successful")
                        else:
                            print("Password must have special letter")
                    else:
                        print("Password must have lower case letter")
                else:
                    print("Password must have capital letter") 
            else:
                print("Password must have Number")
        else:
            print('password length must be between 8 to 16')                   
 # forgot password function
def forgot_password ():
    forgot_mail=input('Enter the registered Email id:\n')
    with open('sample.txt','r') as f3:
        for line in f3:
            if forgot_mail in line:
                pas=line.split(',')
                print("The Registered password is",pas[-1])
                break
        else:
            print("Email Id is not valid")
                
# login function
def login():
    login_mail=input('Login E-mail:')
    login_pass=input('Login Password:')
    
    with open('sample.txt','r') as f1:
        for line in f1:
            if login_mail and login_pass in line:
                                 # removing escape sequence from line 
                escape = re.sub(r"(\\n|\\r|\\t|\\)", "", line).strip()
                check=escape.split(',')
                if login_mail ==check[0] and login_pass == check[-1]:
                    print("login Sucessful")
                    break
        else:
            new_input=int(input("Incorrect Credentials ,select the following: \n 1.Registration \n 2.Forget Password"))
            
            if new_input == 1:
                registration()
            elif new_input == 2:
                forgot_password()
            else:
                print("Please register to continue !")

                            # Main Program
user_input=int(input("Enter your action \n 1.Registration \n 2.Login \n 3.Forget Password"))
new_input =0
if user_input == 1:
    registration()
elif user_input == 2:
    login()
elif user_input == 3:
    forgot_password()
else:
    print("Enter valid input !")


# In[ ]:




