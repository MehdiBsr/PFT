import tkinter as tk
from tkinter import * 

login_window = tk.Tk()
login_window.title("Login page")
login_window.geometry("800x400")

#this is an empty frame to hold all the widgets
center_frame = tk.Frame(login_window)
center_frame.grid(row = 0, column = 1, sticky='nsew')
login_window.rowconfigure(0, weight= 1)
login_window.columnconfigure(0, weight = 1)


username = tk.Label(login_window, text="User Name", font=("calibri", 16))
username.grid(row = 0, column = 0, padx= (20, 0), pady= (20, 10))

ent_space = tk.Entry(login_window, width = 25, font=("Arial", 14))
ent_space.grid(row = 1, column = 0, padx= (20, 0), pady= (20, 10))

mdp = tk.Label(login_window, text ="Password",font=("calibri", 16))
mdp.grid(row = 2, column = 0, padx= (20, 0), pady= (20, 10))

mdp_space = tk.Entry(login_window, width = 25, font=("Arial", 14), show ="*")
mdp_space.grid(row = 3, column = 0, padx= (20, 0), pady= (20, 10))

#this is a variable to hold the state of the checkbox (if it's clicked or not)
show_password = tk.IntVar()

def password_visible():
    if show_password.get() == 1:
        mdp_space.config(show="")
    else:
        mdp_space.config(show="*")
#Create a checkbox to be able to see the password
password_checkbox = tk.Checkbutton(login_window, text="show  password", variable = show_password, onvalue=1, offvalue=0, command = password_visible)
password_checkbox.grid(row = 3, column =0,padx=(10, 0), pady=(20, 10), sticky='w')

def holding_data():
    name_user= ent_space.get()
    password_user= mdp_space.get()
    print("user name:",name_user)
    print("password:", password_user)
    
btn = tk.Button(login_window, text="Login", font=("calibri", 14),height= 1, width = 8, command=holding_data )
btn.config (bg="green", fg="white")
btn.grid(row = 4, column = 0, padx= (20,200), pady= (20, 10))


def clear_all():
    ent_space.delete(0, tk.END)
    mdp_space.delete(0, tk.END)

del_btn= tk.Button(login_window, text="Clear", font =("Calibri", 14),height= 1, width = 8, command = clear_all)
del_btn.config(bg="red", fg="white")
del_btn.grid(row = 4, column = 0, padx= (200, 0), pady= (20, 10))

def exit_window():
    login_window.destroy()

exit_btn= tk.Button(login_window, text= "Exit", font =("Calibri", 14),height= 1, width = 8, command = exit_window)
exit_btn.config(bg="black", fg="white")
exit_btn.grid(row = 5, column = 0,columnspan= 2, padx= (20, 0), pady= (20, 10))


login_window.mainloop()