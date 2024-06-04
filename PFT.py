import tkinter as tk
from tkinter import *
import json
import os

login_window = tk.Tk()
login_window.title("Login page")
login_window.geometry("800x400")

#this is an empty frame to hold all the widgets
center_frame = tk.Frame(login_window)
center_frame.grid(row = 0, column = 1, sticky='nsew')
login_window.rowconfigure(0, weight= 10)
login_window.columnconfigure(0, weight = 1)


username = tk.Label(login_window, text="User Name", font=("calibri", 16))
username.grid(row = 0, column = 0, padx= (20, 0), pady= (20, 10))

ent_space = tk.Entry(login_window, width = 25, font=("Arial", 14))
ent_space.grid(row = 1, column = 0, padx= (20, 0), pady= (20, 10))

mdp = tk.Label(login_window, text ="Password",font=("calibri", 16))
mdp.grid(row = 2, column = 0, padx= (20, 0), pady= (20, 10))

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

def holding_data():
    name_user = ent_space.get()
    password_user = mdp_space.get()

    # reading the data from the file
    with open("user_data.json", "r") as file:
        json_data = file.read()

    # converting the json string to a dictionary
    data = json.loads(json_data)

    # checking if the entered username and password match any of the users in the list
    for user in data["users"]:
        if user["username"] == name_user and user["password"] == password_user:
            print("user name:", name_user)
            print("password:", password_user)
            return

    print("login failed")
    
    
login_btn = tk.Button(login_window, text="Login", font=("calibri", 14),height= 1, width = 8, command=holding_data )
login_btn.config (bg="green", fg="white", borderwidth = 4)
login_btn.grid(row = 4, column = 0, padx= (20,200), pady= (20, 10))

def sign_in():
    name_user = ent_space.get()
    password_user = mdp_space.get()

    # creating a dictionary to store the username and password
    new_user = {"username": name_user,
                "password": password_user}

    # check if the file exists
    if os.path.isfile("user_data.json"):
        # load the existing data into a dictionary
        with open("user_data.json", "r") as file:
            data = json.load(file)

        # initialize the "users" key with an empty list if it doesn't exist
        if "users" not in data:
            data["users"] = []

        # add the new user to the dictionary
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


signin_btn = tk.Button(login_window, text="Sign in", font=("calibri", 14),height= 1, width = 8, command=sign_in )
signin_btn.config (bg="blue", fg="white", borderwidth = 4)
signin_btn.grid(row = 4, column = 0, padx= (200, 0), pady= (20, 10))



def clear_all():
    ent_space.delete(0, tk.END)
    mdp_space.delete(0, tk.END)

del_btn= tk.Button(login_window, text="Clear", font =("Calibri", 14),height= 1, width = 8, command = clear_all)
del_btn.config(bg="red", fg="white", borderwidth = 4)
del_btn.grid(row = 5, column = 0, padx= (20,200), pady= (20, 10))

def exit_window():
    login_window.destroy()

exit_btn= tk.Button(login_window, text= "Exit", font =("Calibri", 14),height= 1, width = 8, command = exit_window)
exit_btn.config(bg="black", fg="white")
exit_btn.grid(row = 5, column = 0, padx= (200, 0), pady= (20, 10))


login_window.mainloop()