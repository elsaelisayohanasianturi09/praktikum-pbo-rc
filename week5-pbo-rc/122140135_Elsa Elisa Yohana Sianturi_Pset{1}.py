#Nama : Elsa Elisa Yohana Sianturi
#NIM : 122140135
import tkinter as tk
from tkinter import messagebox
user_database = {}

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in user_database and user_database[username] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        login_window.destroy() 
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def register():
    register_window = tk.Toplevel(root)
    register_window.title("Register")

    def register_user():
        new_username = new_username_entry.get()
        new_password = new_password_entry.get()
        confirm_password = confirm_password_entry.get()

        # Validasi
        if not new_username or not new_password or not confirm_password:
            messagebox.showerror("Registration Failed", "Please fill in all fields")
            return

        if new_username in user_database:
            messagebox.showerror("Registration Failed", "Username already exists")
            return

        if new_password != confirm_password:
            messagebox.showerror("Registration Failed", "Passwords do not match")
            return

        user_database[new_username] = new_password
        print(f"Registered new user: {new_username}")

        messagebox.showinfo("Registration Successful", "You have successfully registered!")
        register_window.destroy()

   
    registration_frame = tk.Frame(register_window)
    registration_frame.pack(padx=20, pady=10)

    new_username_label = tk.Label(registration_frame, text="New Username:")
    new_username_label.grid(row=0, column=0, sticky=tk.E)

    new_username_entry = tk.Entry(registration_frame)
    new_username_entry.grid(row=0, column=1, padx=5, pady=5)

    new_password_label = tk.Label(registration_frame, text="New Password:")
    new_password_label.grid(row=1, column=0, sticky=tk.E)

    new_password_entry = tk.Entry(registration_frame, show="*")
    new_password_entry.grid(row=1, column=1, padx=5, pady=5)

    confirm_password_label = tk.Label(registration_frame, text="Confirm Password:")
    confirm_password_label.grid(row=2, column=0, sticky=tk.E)

    confirm_password_entry = tk.Entry(registration_frame, show="*")
    confirm_password_entry.grid(row=2, column=1, padx=5, pady=5)

    register_button = tk.Button(register_window, text="Register", command=register_user)
    register_button.pack(pady=10)


root = tk.Tk()
root.title("Login System")

login_frame = tk.Frame(root)
login_frame.pack(padx=20, pady=10)

username_label = tk.Label(login_frame, text="Username:")
username_label.grid(row=0, column=0, sticky=tk.E)

username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(login_frame, text="Password:")
