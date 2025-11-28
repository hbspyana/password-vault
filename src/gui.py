import tkinter as tk
from tkinter import messagebox
from logic import UserAuth, PassVault, check_pwned


class PassVaultGUI:
    def __init__(self):
        self.auth = UserAuth()
        self.root = tk.Tk()
        self.root.title('Password Vault')
        self.root.geometry('400x600')
        self.root.configure(bg='#07052A')
        self.login_screen()

    def login_screen(self):
        frame = tk.Frame(self.root)
        frame.pack()
        
        tk.Label(
            frame, text='password_vault', font=('Arial Black', 28, 'bold', 'italic')).pack()

        tk.Label(frame, text='Username:').pack()
        user_entry = tk.Entry(frame)
        user_entry.pack()

        tk.Label(frame, text='Password:').pack()
        pass_entry = tk.Entry(frame, show='*')
        pass_entry.pack()

        def user_login():
            ok, msg = self.auth.login(user_entry.get(), pass_entry.get())
            if ok:
                self.vault_screen(user_entry.get())
            else:
                messagebox.showerror('Error', msg)

        def user_signup():
            ok, msg = self.auth.signup(user_entry.get(), pass_entry.get())
            messagebox.showinfo('Info', msg)

        tk.Button(frame, text='Login', command=user_login).pack()
        tk.Button(frame, text='Sign up', command=user_signup).pack()

    def vault_screen(self, username):
        vault = PassVault(username)

        win = tk.Toplevel(self.root)
        win.title(f'Vault - {username}')

        tk.Label(win, text='Site:').pack()
        site_entry = tk.Entry(win)
        site_entry.pack()

        tk.Label(win, text='Password:').pack()
        key_entry = tk.Entry(win)
        key_entry.pack()

        def add_key():
            site = site_entry.get()
            key = key_entry.get()
            vault.add_password(site, key)
            messagebox.showinfo('Saved', 'Password stored.')
            
        def check_leak():
            key = key_entry.get()
            count = check_pwned(key)

            if count == False:
                messagebox.showerror('Error', 'Was not able to check.')

            elif count == True:
                messagebox.showinfo('Safe!', 'Password not found in any leaks.')

            else:
                messagebox.showwarning('Uh oh!',
                    f'This password has been leaked {count} time(s)!')


        def show_pass():
            
            data = vault.get_all()
            text = '\n'.join([f'{s}: {p}' for s, p in data])
            messagebox.showinfo('Stored Passwords', text)

        tk.Button(win, text='Save Password', command=add_key).pack()
        tk.Button(win, text='Show Saved Passwords', command=show_pass).pack()
        tk.Button(win, text='Check if Leaked', command=check_leak).pack()

    def run(self):
        self.root.mainloop()
