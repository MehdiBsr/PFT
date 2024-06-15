import tkinter as tk
from tkinter import *
import json
import os
import random
from tkcalendar import DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt

#creating a window for a login page 
login_window = tk.Tk()
login_window.title("Login page")
login_window.geometry("800x400")

#this is an empty frame to hold all the widgets in the middle of the window
center_frame = tk.Frame(login_window)
center_frame.grid(row = 0, column = 1, sticky='nsew')
login_window.rowconfigure(0, weight= 10)
login_window.columnconfigure(0, weight = 1)

#user name label
username = tk.Label(login_window, text="User Name", font=("calibri", 16))
username.grid(row = 0, column = 0, padx= (20, 0), pady= (20, 10))

#user name enter space
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

#function to show the password and hide it
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

    #to check if the file exists
    if os.path.isfile("user_data.json"):
        # load the existing data into a dictionary
        with open("user_data.json", "r") as file:
            data = json.load(file)

        #initializing the "users" key with an empty list if it doesn't exist
        if "users" not in data:
            data["users"] = []

        #now we add the new user to the dictionary
        data["users"].append(new_user)
    else:
        #create a new dictionary with an empty list of users
        data = {"users": []}

        #add the new user to the list
        data["users"].append(new_user)

    #convert the dictionary to a JSON string
    json_data = json.dumps(data)

    #write the JSON string to the file
    with open("user_data.json", "w") as file:
        file.write(json_data)

    print("Data stored successfully")
    print("Now you may login")

#sign in button
signin_btn = tk.Button(login_window, text="Sign in", font=("calibri", 14),height= 1, width = 8, command=sign_in )
signin_btn.config (bg="blue", fg="white", borderwidth = 4)
signin_btn.grid(row = 4, column = 0, padx= (200, 0), pady= (20, 10))

#function to clear the entry space
def clear_all():            
    ent_space.delete(0, tk.END)
    mdp_space.delete(0, tk.END)
    
# delete button
del_btn= tk.Button(login_window, text="Clear", font =("Calibri", 14),height= 1, width = 8, command = clear_all)
del_btn.config(bg="red", fg="white", borderwidth = 4)
del_btn.grid(row = 5, column = 0, padx= (20,200), pady= (20, 10))

def exit_window():
    login_window.destroy()
#exit button
exit_btn= tk.Button(login_window, text= "Exit", font =("Calibri", 14),height= 1, width = 8, command = exit_window)
exit_btn.config(bg="black", fg="white")
exit_btn.grid(row = 5, column = 0, padx= (200, 0), pady= (20, 10))

def holding_data():
    name_user = ent_space.get()
    password_user = mdp_space.get()

    #reading the data from the file
    with open("user_data.json", "r") as file:
        json_data = file.read()

    #converting the json string to a dictionary
    data = json.loads(json_data)

    #checking if the entered username and password match any of the users in the list
    for user in data["users"]:
        if user["username"] == name_user and user["password"] == password_user:
            print("user name:", name_user)
            print("password:", password_user)
            right_user(user, name_user, data)
            
            return 

        else:
            print("login failed")

# login button
login_btn = tk.Button(login_window, text="Login", font=("calibri", 14),height= 1, width = 8, command=holding_data )
login_btn.config (bg="green", fg="white", borderwidth = 4)
login_btn.grid(row = 4, column = 0, padx= (20,200), pady= (20, 10))


def right_user(user, name_user, data):
    #Create a new window for the welcoming page     
            menu_window = tk.Tk()
            menu_window.title("Personal Finance Tracker")
            menu_window.geometry("1920x1080")
     
            welcome_label = tk.Label(menu_window, text=f"Hello {name_user} and welcome to your personal finance tracker!",font=("Arial", 20))
            welcome_label.pack()
    
            login_window.destroy()
            
            #balance widgets
            balance = user.get("balance", 0.0)
            balance_label = tk.Label(menu_window, text= f"Your current balance is: ${balance:.2f} ",font=("Arial", 16) )
            balance_label.pack(pady = (40,40))
            
            history = tk.Label(menu_window, text = "This is the summary of your last transaction",font=("Arial", 16) )
            history.pack()
            
            #check if there is a last transaction of not
            if len(user["transactions"]) > 0:
                #if there is transactions we show the information of the last transaction that we get from the json file
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
                #if there no transactions we show none and zero value.
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
                
            
            #function to add a transaction to the json file used as a database
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
                
                #call the update_categories function whenever the value of type_var changes
                type_var.trace("w", update_categories)
                
                #Call theupdate_categories once to set the initial categories
                update_categories()
                
                #creating a new frame to add in it the transaction window to put all the widgets in the middle 
                input_frame = tk.Frame(transaction_window)
                input_frame.pack(pady=(10,0))
                
                # Define a function to valide the input of the amount
                def validate_input(input):
                    if input == "" or input.isdigit():
                        return True
                    else:
                        #if it's not a digit, a window error will appear
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

                #call the update_field function whenever the value of type_var changes
                type_var.trace("w", update_field)
                update_field()

                # add a calendar input field for the transaction date
                date_frame = tk.Frame(transaction_window)
                date_frame.pack(pady=(20,0))

                date_label = tk.Label(date_frame, text="Date: ")
                date_label.pack(side=tk.LEFT)

                date_var = tk.StringVar()
                date_entry = DateEntry(date_frame, textvariable=date_var, date_pattern='y-mm-dd')
                date_entry.pack(side=tk.RIGHT)
                
                #create function to add every thing in the data base
                def finish_add():
                    nonlocal balance #this refer to the balance variable in the outer function
                    
                    #validate the amount input
                    if not amount_entry.get() or not amount_entry.get().isdigit():
                        messagebox.showerror("Error", "Please enter a valid amount")
                        return

                    #create a new list of transactions if the user doesn't have one
                    if "transactions" not in user:
                        user["transactions"] = []

                    #add the new transaction
                    new_transaction = {
                        "transaction_id": random.randint(1000, 9999),
                        "type": type_var.get(),
                        "category": category_var.get(),
                        "amount": float(amount_entry.get()),
                        "date": date_var.get(),
                        "payee": payee_entry.get()
                    }

                    #add the new transaction to the user's list
                    user["transactions"].append(new_transaction)

                    #update the account balance based on the transaction type
                    if new_transaction["type"] == "Income":
                        balance += new_transaction["amount"]
                    else:
                        balance -= new_transaction["amount"]

                    print("New balance: ", balance)
                    
                    #create a list with the new updated data
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

                    # Updating the last transaction information in the main window
                    transaction_id.config(text=f"Transaction ID: {new_transaction['transaction_id']}")
                    type_transaction.config(text=f"Type of the transaction: {new_transaction['type']}")
                    category.config(text=f"Category: {new_transaction['category']}")
                    amount.config(text=f"Transaction amount: ${new_transaction['amount']:.2f}")
                    date_transaction.config(text=f"Date of the transaction: {new_transaction['date']}")

                    print("Transaction added successfully")

                    # Close the transaction window
                    transaction_window.destroy()

            
                #creating a button to use the finish_add function which will end the process of adding a transactionin the json file
                finish_btn = tk.Button(transaction_window, text="Finish", font=("Arial", 14), height=1, width=8, command=finish_add)
                finish_btn.config(bg="blue", fg="white", borderwidth=4)
                finish_btn.pack(pady=(20, 10))


            add_btn = tk.Button(menu_window, text="Add Transaction", command=lambda: add_transaction(balance_label), font=("Arial", 16))#this lambda function calls the add_transaction function with balance_label as an argument
            add_btn.pack()

            #function of the summary (Dashboard) window
            def summary_window():
                #creating a new window for the summary
                summary_window = tk.Tk()
                summary_window.title("Dashboard")
                summary_window.geometry("900x700")

                # View Transactions
                view_transactions_label = tk.Label(summary_window, text="View Transactions", font=("Arial", 16))
                view_transactions_label.pack()

                # Filter by time range
                time_range_label = tk.Label(summary_window, text="Time Range:", font=("Arial", 12))
                time_range_label.pack()
                start_date_label = tk.Label(summary_window, text="Start Date:", font=("Arial", 12))
                start_date_label.pack()
                start_date_entry = DateEntry(summary_window, date_pattern='y-mm-dd')
                start_date_entry.pack()
                end_date_label = tk.Label(summary_window, text="End Date:", font=("Arial", 12))
                end_date_label.pack()
                end_date_entry = DateEntry(summary_window, date_pattern='y-mm-dd')
                end_date_entry.pack()

                #filter by class (income/expense)
                class_label = tk.Label(summary_window, text="Class:", font=("Arial", 12))
                class_label.pack()
                class_var = tk.StringVar()
                class_menu = tk.OptionMenu(summary_window, class_var, "Income", "Expenses")
                class_menu.pack()
                

                #filter by category
                category_label = tk.Label(summary_window, text="Category:", font=("Arial", 12))
                category_label.pack()
                category_var = tk.StringVar()
                category_menu = tk.OptionMenu(summary_window, category_var, * ["Food"] + ["Rent"] + ["Clothing"] + ["Car"] +  ["Health"] + ["Salary"] + ["Pension"] + ["Interest"])
                category_menu.pack()

                #filter by payee/source name
                payee_label = tk.Label(summary_window, text="Payee/Source:", font=("Arial", 12))
                payee_label.pack()
                payee_entry = tk.Entry(summary_window)
                payee_entry.pack()
                global transaction_text_box  # declare it as global
                transaction_text_box = tk.Text(summary_window, width=60, height=10)
                transaction_text_box.pack()

                #show transaction function
                def show_transactions():
                    start_date = start_date_entry.get()
                    end_date = end_date_entry.get()
                    class_type = class_var.get()
                    category = category_var.get()
                    payee = payee_entry.get()

                    filtered_transactions = []
                    for transaction in user["transactions"]:
                        #cheking if the transaction meet all the filtered criteria
                        if (start_date <= transaction["date"] <= end_date and
                            transaction["type"] == class_type and
                            transaction["category"] == category and
                            transaction["payee"] == payee):
                            #if it meets them all then add it to the to filtered_transactions list
                            filtered_transactions.append(transaction)

                    transaction_text_box.delete(1.0, tk.END)  #clear the text box
                    #creating an empty string to store the transaction data
                    transaction_text = ""
                    
                    #iterate over each transaction in the filtered_transactions list and append each detail into the empty string
                    for transaction in filtered_transactions:
                        transaction_text += f"Transaction ID: {transaction['transaction_id']}\n"
                        transaction_text += f"Type: {transaction['type']}\n"
                        transaction_text += f"Category: {transaction['category']}\n"
                        transaction_text += f"Amount: ${transaction['amount']:.2f}\n"
                        transaction_text += f"Date: {transaction['date']}\n"
                        transaction_text += f"Payee/Source: {transaction['payee']}\n\n"

                    
                    transaction_text_box.insert(tk.END, transaction_text)

                #Show transaction button
                show_btn = tk.Button(summary_window, text="Show", command=show_transactions)
                show_btn.pack()

                #function to print the filtered transaction in the external .txt file
                def print_transactions():
                    start_date = start_date_entry.get()
                    end_date = end_date_entry.get()
                    class_type = class_var.get()
                    category = category_var.get()
                    payee = payee_entry.get()

                    filtered_transactions = []
                    for transaction in user["transactions"]:
                        if (start_date <= transaction["date"] <= end_date and
                            transaction["type"] == class_type and
                            transaction["category"] == category and
                            transaction["payee"] == payee):
                            filtered_transactions.append(transaction)

                    transaction_text = ""
                    for transaction in filtered_transactions:
                        transaction_text += f"Transaction ID: {transaction['transaction_id']}\n"
                        transaction_text += f"Type: {transaction['type']}\n"
                        transaction_text += f"Category: {transaction['category']}\n"
                        transaction_text += f"Amount: ${transaction['amount']:.2f}\n"
                        transaction_text += f"Date: {transaction['date']}\n"
                        transaction_text += f"Payee/Source: {transaction['payee']}\n\n"

                    if transaction_text:
                        with open("transactions.txt", "w") as file:
                            file.write(transaction_text)
                    else:
                        messagebox.showerror("Error", "You have to filter the transactions first")

                #creating a button to use the print_transaction function
                print_btn = tk.Button(summary_window, text="Print", command=print_transactions)
                print_btn.pack()

                #bar Chart label
                bar_chart_label = tk.Label(summary_window, text="Bar Chart", font=("Arial", 16))
                bar_chart_label.pack()

                #creating a function to draw the bar chart using the library matplotlib
                def create_bar_chart():
                    #creating two empty lists to store the categories and corresponding amounts
                    categories = []
                    amounts = []
                    
                    #iterate over each transaction in the user's transactions
                    for transaction in user["transactions"]:
                        #check if the transaction type matches the selected class
                        if transaction["type"] == class_var.get():
                            #if it matches then it append the transaction category to the categories list and append the transaction amount to the amounts list
                            categories.append(transaction["category"])
                            amounts.append(transaction["amount"])

                    #create a bar chart using the collected categories and amounts
                    plt.bar(categories, amounts)
                    #set the x-axis label to "Category"
                    plt.xlabel("Category")
                    #set the y-axis label to "Amount"
                    plt.ylabel("Amount")
                    #set the title of the bar chart
                    plt.title("Bar Chart of " + class_var.get())
                    #display the bar chart
                    plt.show()

                #button to create the bar chart
                bar_chart_btn = tk.Button(summary_window, text="Create Bar Chart", command=create_bar_chart)
                bar_chart_btn.pack()

                #pie Chart label
                pie_chart_label = tk.Label(summary_window, text="Pie Chart", font=("Arial", 16))
                pie_chart_label.pack()

                #function to create the pie chart
                def create_pie_chart():
                    #creating an empty dictionary to store categories and their corresponding total amounts
                    categories = {}
                    
                    #iterate through each transaction in the users transactions
                    for transaction in user["transactions"]:
                        #check if the transaction type matches the selected class
                        if transaction["type"] == class_var.get():
                            #get the category and amount of the transaction
                            category = transaction["category"]
                            amount = transaction["amount"]
                            #if the category already exists in the dictionary, add the amount to the existing total
                            if category in categories:
                                categories[category] += amount
                            else:
                                #if the category doesn't exist, add it to the dictionary with the current amount
                                categories[category] = amount
                    
                     #this creates a list of category labels from the keys of the dictionary
                    labels = list(categories.keys())
                    #this create a list of sizes from the values of the dictionary
                    sizes = list(categories.values())
                    
                    # Create a pie chart using the sizes and labels
                    plt.pie(sizes, labels=labels, autopct='%1.1f%%') #"autopct='%1.1f%%'" displays the percentage value with one decimal place
                    #set the title of the pie chart, including the selected class
                    plt.title("Pie Chart of " + class_var.get())
                    #display the pie chart
                    plt.show()

                #creating a button to use the create_pie_chart function
                pie_chart_btn = tk.Button(summary_window, text="Create Pie Chart", command=create_pie_chart)
                pie_chart_btn.pack()

                summary_window.mainloop()

            summary_btn = tk.Button(menu_window, text="Summary", command=summary_window, font=("Arial", 16))
            summary_btn.pack()
            
            def all_transaction_window():
                # create a new window to display the transactions summary
                all_transaction_window = tk.Tk()
                all_transaction_window.title("Transactions Summary")
                all_transaction_window.geometry("800x600")

                summary_label = tk.Label(all_transaction_window, text="Transactions Summary", font=("Arial", 16))
                summary_label.pack()

                # define transaction_text_box as global to access in print_transactions
                global transaction_text_box
                
                transaction_text_box = tk.Text(all_transaction_window, height=20, width=80)
                transaction_text_box.pack(pady=10)

                # displaying the transactions in the text box
                for transaction in user["transactions"]:
                    transaction_text_box.insert(tk.END, f"Transaction ID: {transaction['transaction_id']}\n")
                    transaction_text_box.insert(tk.END, f"Type: {transaction['type']}\n")
                    transaction_text_box.insert(tk.END, f"Category: {transaction['category']}\n")
                    transaction_text_box.insert(tk.END, f"Amount: ${transaction['amount']:.2f}\n")
                    transaction_text_box.insert(tk.END, f"Date: {transaction['date']}\n")
                    transaction_text_box.insert(tk.END, "-"*40 + "\n") #add a separator line for clarity

                #delete transaction label
                delete_label = tk.Label(all_transaction_window, text="Delete Transaction (Enter the ID of the transaction)", font=("Arial", 14))
                delete_label.pack()

                #delete transaction entry
                delete_entry = tk.Entry(all_transaction_window, width=20)
                delete_entry.pack()

                #function to delete a transaction
                def delete_transaction():
                    #get the transaction ID entered by the user in the delete_entry widget and asign it to a variable named transaction_id
                    transaction_id = delete_entry.get()
                    #iterate over each transaction in the transactions list
                    for transaction in user["transactions"]:
                        #check if the current transaction's ID matches the entered transaction ID
                        if str(transaction["transaction_id"]) == transaction_id:
                            #if it does it removes the matching transaction from the transactions list
                            user["transactions"].remove(transaction)
                            with open("user_data.json", "w") as file:
                                #write the updated user data to the file, formatted with indentation for readability
                                file.write(json.dumps(data, indent=4))
                            #display a success message to inform the user that the transaction was deleted
                            messagebox.showinfo("Success", "Transaction deleted successfully")
                            all_transaction_window.destroy()
                            return
                    messagebox.showerror("Error", "Transaction not found")

                delete_btn = tk.Button(all_transaction_window, text="Delete Transaction", command=delete_transaction)
                delete_btn.pack()

                all_transaction_window.mainloop()
         
            all_transaction_btn = tk.Button(menu_window, text="See all Transactions",font=("Arial", 16), command = all_transaction_window)
            all_transaction_btn.pack()

            menu_window.mainloop()



login_window.mainloop()