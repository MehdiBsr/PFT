"""
    Programmer : Mehdi Boussoura
    Date : june 2024
    program : Assignment 3, Personal Finance Tracker 
"""



import tkinter as tk
from tkinter import *
import json
import os
import random
from tkcalendar import DateEntry
from tkinter import messagebox
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
                "transactions" : [],
                "balance" : 0}

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

    # checking if the entered username and password match any of the users in the list
    for user in data["users"]:
        if user["username"] == name_user and user["password"] == password_user:
            print("user name:", name_user)
            print("password:", password_user)

            
            #Create a new window for the welcoming page     
            menu_window = tk.Tk()
            menu_window.title("Personal Finance Tracker")
            menu_window.geometry("1920x1080")
     
            welcome_label = tk.Label(menu_window, text=f"Hello {name_user} and welcome to your personal finance tracker!",font=("Arial", 20))
            welcome_label.pack()
    
            login_window.destroy()
            
            balance = user.get("balance", 0.0)
            balance_label = tk.Label(menu_window, text= f"Your current balance is: ${balance:.2f} ",font=("Arial", 16) )
            balance_label.pack(pady = (40,40))
            
            history = tk.Label(menu_window, text = "This is the summary of your last transaction",font=("Arial", 16) )
            history.pack()
            
            if len(user["transactions"]) > 0:
                last_transaction = user["transactions"][-1]

                transaction_id = tk.Label(menu_window, text = f"Transaction ID : {last_transaction['transaction_id']}",font=("Arial", 16) )
                transaction_id.pack()

                type_transaction = tk.Label(menu_window, text = f"Type of the transaction: {last_transaction['type']}",font=("Arial", 16) )
                type_transaction.pack()

                category = tk.Label(menu_window, text = f"category : {last_transaction['category']}",font=("Arial", 16) )
                category.pack()

                amount = tk.Label(menu_window, text = f"Transaction amount : ${last_transaction['amount']}",font=("Arial", 16) )
                amount.pack()

                date_transaction = tk.Label(menu_window, text = f"Date of the transaction : {last_transaction['date']}",font=("Arial", 16) )
                date_transaction.pack()

            else:
                transaction_id = tk.Label(menu_window, text = "Transaction ID : None",font=("Arial", 16) )
                transaction_id.pack()

                type_transaction = tk.Label(menu_window, text = "Type of the transaction: None",font=("Arial", 16) )
                type_transaction.pack()

                category = tk.Label(menu_window, text = "category : None",font=("Arial", 16) )
                category.pack()

                amount = tk.Label(menu_window, text = "Transaction amount : $0",font=("Arial", 16) )
                amount.pack()

                date_transaction = tk.Label(menu_window, text = "Date of the transaction : None",font=("Arial", 16) )
                date_transaction.pack()
                
            
            def add_transaction(balance_label):
                # creating a window for the add transaction process
                transaction_window = tk.Tk()
                transaction_window.title("Add Transaction")
                transaction_window.geometry("800x400")
                
                type_label = tk.Label(transaction_window, text="Transaction Type: ",font=("Arial", 12))
                type_label.pack()
                
                #create a dropdown menu for the type of the transaction
                type_var = tk.StringVar(value ="Income")
                type_menu = tk.OptionMenu(transaction_window, type_var, "Income", "Expenses")
                type_menu.pack()

                category_label = tk.Label(transaction_window, text="Category: ",font=("Arial", 12))
                category_label.pack()
                
                #function to update the dropdown of categories
                def update_categories(*args):
                    if type_var.get() == "Income":
                        categories = ["Salary", "Pension", "Interest", "Others"]
                    else:
                        categories = ["Food", "Rent", "Clothing", "Car", "Health", "Others"]
                    
                    category_menu['menu'].delete(0, 'end')  # Clear existing categories
                    for category in categories:
                        category_menu['menu'].add_command(label=category, command=tk._setit(category_var, category))
                    category_var.set(categories[0])
                category_var = tk.StringVar()
                category_menu = tk.OptionMenu (transaction_window, category_var, category_var)
                category_menu.pack()
                
                # call the update_categories function whenever the value of type_var changes
                type_var.trace("w", update_categories)
                
                # Call theupdate_categories once to set the initial categories
                update_categories()
                
                #creating a new frame to add in it the transaction window to put all the widgets in the middle 
                input_frame = tk.Frame(transaction_window)
                input_frame.pack(pady=(10,0))
                
                # Define a function to valide the input of the amount
                def validate_input(input):
                    if input == "" or input.isdigit():
                        return True
                    else:
                        messagebox.showerror("Error", "Please enter a number")
                        return False
                
                # Create a label widget for amount and add it to the input_frame 
                amount_label = tk.Label(input_frame, text="Amount: ")
                amount_label.pack(side=tk.LEFT)
                
                #Register the validate_input function with the input_frame frame
                vcmd = input_frame.register(validate_input)
                
                # Creating a new entry widget and add it to the input_frame
                amount_entry = tk.Entry(input_frame, validate = "key", validatecommand = (vcmd, '%P')) # Set the validate option to "key" and the validate command option to the registered function validate_input
                amount_entry.pack(side=tk.RIGHT)
                
                second_input_frame = tk.Frame(transaction_window)
                second_input_frame.pack(pady=(20,0))

                def update_field(*args):
                    if type_var.get() == "Income":
                        label_text = "Source:"
                    else:
                        label_text = "Payee:"

                    payee_var.set(label_text)

                payee_var = tk.StringVar()
                payee_label = tk.Label(second_input_frame, textvariable=payee_var)
                payee_label.pack(side=tk.LEFT)
                payee_entry = tk.Entry(second_input_frame)
                payee_entry.pack(side = tk.RIGHT)

                type_var.trace("w", update_field)
                update_field()

                # Add a calendar input field for the transaction date
                date_frame = tk.Frame(transaction_window)
                date_frame.pack(pady=(20,0))

                date_label = tk.Label(date_frame, text="Date: ")
                date_label.pack(side=tk.LEFT)

                date_var = tk.StringVar()
                date_entry = DateEntry(date_frame, textvariable=date_var, date_pattern='y-mm-dd')
                date_entry.pack(side=tk.RIGHT)
                
                #Create function to add every thing in the data base
                def finish_add(balance, user, balance_label, transaction_id, type_transaction, category, amount, date_transaction):
                    # Create a new list of transactions if the user doesn't have one
                    if "transactions" not in user:
                        user["transactions"] = []

                    # Add the new transaction
                    new_transaction = {
                        "transaction_id": random.randint(1000, 9999),
                        "type": type_var.get(),
                        "category": category_var.get(),
                        "amount": float(amount_entry.get()),
                        "date": date_var.get()
                    }

                    # Add the new transaction to the user's list
                    user["transactions"].append(new_transaction)

                    # Update the account balance based on the transaction type
                    if new_transaction["type"] == "Income":
                        balance += new_transaction["amount"]
                    else:
                        balance -= new_transaction["amount"]

                    # Check if the amount is less than 0
                    if new_transaction["amount"] < 0:
                        messagebox.showerror("Error", "Amount cannot be less than 0")
                        return

                    # Create a new dictionary with the updated user information
                    updated_user = {
                        "username": user["username"],
                        "password": user["password"],
                        "transactions": user["transactions"],
                        "balance": balance
                    }

                    # Update the data dictionary with the new user dictionary
                    data["users"] = [u for u in data["users"] if u["username"] != user["username"]]
                    data["users"].append(updated_user)

                    # Write the updated data to the JSON file
                    with open("user_data.json", "w") as file:
                        file.write(json.dumps(data, indent=4))

                    # Update the balance label in the main window
                    balance_label.config(text=f"Your current balance is: ${balance:.2f}")

                    # Update the last transaction information in the main window
                    transaction_id.config(text=f"Transaction ID: {new_transaction['transaction_id']}")
                    type_transaction.config(text=f"Type of the transaction: {new_transaction['type']}")
                    category.config(text=f"Category: {new_transaction['category']}")
                    amount.config(text=f"Transaction amount: ${new_transaction['amount']:.2f}")
                    date_transaction.config(text=f"Date of the transaction: {new_transaction['date']}")

                    print("Transaction added successfully")

                    # Close the transaction window
                    transaction_window.destroy()

            
                
                add_transaction_btn = tk.Button (transaction_window, text="Add Transaction",font=("Arial", 16), command =lambda: finish_add(balance, user, balance_label, transaction_id, type_transaction, category, amount, date_transaction) )
                add_transaction_btn.pack(pady = (20,20))
                # Create a function to finish the transaction process
                def finish_transaction():
                    # Validate the amount input
                    if not amount_entry.get() or not amount_entry.get().isdigit():
                        messagebox.showerror("Error", "Please enter a valid amount")
                        return

                    # Finish the transaction process
                    finish_add(balance, user, balance_label, transaction_id, type_transaction, category, amount, date_transaction)

                # Bind the "Add Transaction" button to the finish_transaction() function
                add_transaction_btn.config(command=finish_transaction)
                
            add_btn = tk.Button(menu_window, text="Add Transaction", command=lambda: add_transaction(balance_label), font=("Arial", 16))
            add_btn.pack()
            
            
            menu_window.mainloop()
            return 
        
        else:
            print("login failed")
            
   
# login button
login_btn = tk.Button(login_window, text="Login", font=("calibri", 14),height= 1, width = 8, command=holding_data )
login_btn.config (bg="green", fg="white", borderwidth = 4)
login_btn.grid(row = 4, column = 0, padx= (20,200), pady= (20, 10))

login_window.mainloop()