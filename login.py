import tkinter as tk
from functools import partial

class LoginApp(tk.Frame):
    """ The Login Form Class. """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        # Username field
        self.usernameLabel = tk.Label(self.master, text='Username')
        self.usernameLabel.grid(row=0, column=0)
        self.username = tk.StringVar()
        self.usernameEntry = tk.Entry(
            self.master, 
            textvariable=self.username
        ).grid(row=0, column=1)

        # Password field
        self.passwordLabel = tk.Label(self.master, text='Password')
        self.passwordLabel.grid(row=1, column=0)
        self.password = tk.StringVar()
        self.passwordEntry = tk.Entry(
            self.master, 
            textvariable=self.password
        ).grid(row=1, column=1)

        # Set parameters to the function
        self.validateLogin = partial(
            self.validateLogin,
            self.username, 
            self.password
        )

        # Login button
        self.loginButton = tk.Button(
            self.master, 
            text='Login', 
            command=self.validateLogin
        ).grid(row=4, column=0)

    def validateLogin(self, username, password):
        """ Prints the username and password to the console. """
        print("Username:", username.get())
        print("Password:", password.get())


# Tk window
root = tk.Tk()
window = LoginApp(master=root)

window.master.geometry('300x100')
window.master.title("Tkinter Login Form")

window.mainloop()