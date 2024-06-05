import tkinter as tk
from tkinter import *
import json
import os
import datetime
import matplotlib.pyplot as plt

login_window = tk.Tk()
login_window.title("Login page")
login_window.geometry("800x400")

#this is an empty frame to hold all the widgets
center_frame = tk.Frame(login_window)
center_frame.grid(row = 0, column = 1, sticky='nsew')
login_window.rowconfigure(0, weight= 10)
login_window.columnconfigure(0, weight = 1)

# User name label
username = tk.Label(login_window, text="User Name", font=("calibri", 16))
username.grid(row = 0, column = 0, padx= (20, 0), pady= (20, 10))
# User name enter space
ent_space = tk.Entry(login_window, width = 25, font=("Arial", 14))
ent_space.grid(row = 1, column = 0, padx= (20, 0), pady= (20, 10))
#Password Label
mdp = tk.Label(login_window, text ="Password",font=("calibri", 16))
mdp.grid(row = 2, column = 0, padx= (20, 0), pady= (20, 10))
# Password enter space
mdp_space = tk.Entry(login_window, width = 25, font=("Arial", 14), show ="*")
mdp_space.grid(row = 3, column = 0, padx= (20,0), pady= (20, 10))

#this is a variable to hold the state of the checkbox (if it's clicked or not)
show_password = tk.IntVar()

def password_visible():
    if show_password.get() == 1:
        mdp_space.config(show="")
    else:
        mdp_space.config(show="*")
#Create a checkbox to be able to see the password
password_checkbox = tk.Checkbutton(login_window, text="show  password", variable = show_password, onvalue=1, offvalue=0, command = password_visible)
password_checkbox.grid(row = 3, column = 0, padx= (450, 0), pady= (20, 10))



def sign_in():
    name_user = ent_space.get()
    password_user = mdp_space.get()

    # creating a dictionary to store the username and password
    new_user = {"username": name_user,
                "password": password_user,
                "transactions" : []}

    #to chock if the file exists
    if os.path.isfile("user_data.json"):
        # load the existing data into a dictionary
        with open("user_data.json", "r") as file:
            data = json.load(file)

        # initialize the "users" key with an empty list if it doesn't exist
        if "users" not in data:
            data["users"] = []

        # now we add the new user to the dictionary
        data["users"].append(new_user)
    else:
        # create a new dictionary with an empty list of users
        data = {"users": []}

        # add the new user to the list
        data["users"].append(new_user)

    # convert the dictionary to a JSON string
    json_data = json.dumps(data)

    # write the JSON string to the file
    with open("user_data.json", "w") as file:
        file.write(json_data)

    print("Data stored successfully")
    print("Now you may login")

#sign in button
signin_btn = tk.Button(login_window, text="Sign in", font=("calibri", 14),height= 1, width = 8, command=sign_in )
signin_btn.config (bg="blue", fg="white", borderwidth = 4)
signin_btn.grid(row = 4, column = 0, padx= (200, 0), pady= (20, 10))



def clear_all():
    ent_space.delete(0, tk.END)
    mdp_space.delete(0, tk.END)
# delete button
del_btn= tk.Button(login_window, text="Clear", font =("Calibri", 14),height= 1, width = 8, command = clear_all)
del_btn.config(bg="red", fg="white", borderwidth = 4)
del_btn.grid(row = 5, column = 0, padx= (20,200), pady= (20, 10))

def exit_window():
    login_window.destroy()
# exit button
exit_btn= tk.Button(login_window, text= "Exit", font =("Calibri", 14),height= 1, width = 8, command = exit_window)
exit_btn.config(bg="black", fg="white")
exit_btn.grid(row = 5, column = 0, padx= (200, 0), pady= (20, 10))

def holding_data():
    name_user = ent_space.get()
    password_user = mdp_space.get()

    # reading the data from the file
    with open("user_data.json", "r") as file:
        json_data = file.read()

    # converting the json string to a dictionary
    data = json.loads(json_data)

    #creating a flag to check if the user is logged in or not 

    # checking if the entered username and password match any of the users in the list
    for user in data["users"]:
        if user["username"] == name_user and user["password"] == password_user:
            print("user name:", name_user)
            print("password:", password_user)

                
            menu_window = tk.Tk()
            menu_window.title("Personal Finance Tracker")
            menu_window.geometry("1920x1080")
     
            welcome_label = tk.Label(menu_window, text=f"Hello {name_user}, welcome your personal finance tracker!",font=("Arial", 20))
            welcome_label.pack()
    
            login_window.destroy()
            
            balance = 0
            balance_label = tk.Label(menu_window, text= f"Your current balance is: ${balance} ",font=("Arial", 16) )
            balance_label.pack(pady = (40,40))
            
            history = tk.Label(menu_window, text = "This is the summary of your last transaction",font=("Arial", 16) )
            history.pack()
            
            last_transaction = tk.Label(menu_window, text = "Last transaction : None",font=("Arial", 16) )
            last_transaction.pack()
            
            transaction_id = tk.Label(menu_window, text = "Transaction ID : None",font=("Arial", 16) )
            transaction_id.pack()
            
            type_transaction = tk.Label(menu_window, text = "Type of the transaction",font=("Arial", 16) )
            type_transaction.pack()
            
            category = tk.Label(menu_window, text = "category : None",font=("Arial", 16) )
            category.pack()
            
            amount = tk.Label(menu_window, text = "Transaction amount : $0",font=("Arial", 16) )
            amount.pack()
            
            date_transaction = tk.Label(menu_window, text = "Date of the transaction : None",font=("Arial", 16) )
            date_transaction.pack()
            
            
            
            
            
            
            
            
            
            menu_window.mainloop()
            return 
        
        else:
            print("login failed")
            
   
# login button
login_btn = tk.Button(login_window, text="Login", font=("calibri", 14),height= 1, width = 8, command=holding_data )
login_btn.config (bg="green", fg="white", borderwidth = 4)
login_btn.grid(row = 4, column = 0, padx= (20,200), pady= (20, 10))

login_window.mainloop()