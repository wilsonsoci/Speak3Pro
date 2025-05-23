import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


class Speak3ProApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Speak3Pro")
        self.geometry("800x500")
        self.resizable(False, False)

        # Load logo image
        image = Image.open("logo.png")
        image = image.resize((80, 80), Image.Resampling.LANCZOS)
        self.logo = ImageTk.PhotoImage(image)

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (LoginPage, RegisterPageStep1, RegisterPageStep2, RegisterCompletePage):
            frame = F(parent=self.container, controller=self)
            self.frames[F] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame(LoginPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


# ---------------- LOGIN PAGE -------------------
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        left = tk.Frame(self, bg="#edf0f2")
        left.place(relx=0, rely=0, relwidth=0.65, relheight=1)

        tk.Label(left, text="Welcome back!", font=("Georgia", 22, "bold"), bg="#edf0f2", fg="#1c1c1c").pack(pady=30)

        tk.Label(left, text="E-mail:", bg="#edf0f2").pack()
        self.email_entry = tk.Entry(left, width=30)
        self.email_entry.pack(pady=5)

        tk.Label(left, text="Password:", bg="#edf0f2").pack()
        self.password_entry = tk.Entry(left, show="*", width=30)
        self.password_entry.pack(pady=5)

        tk.Button(left, text="Login", width=25, command=self.validate_login).pack(pady=20)

        tk.Label(left, text="Do not have an account?", bg="#edf0f2").pack()
        tk.Button(left, text="Sign up", command=lambda: controller.show_frame(RegisterPageStep1)).pack()

        right = tk.Frame(self, bg="#0b1e33")
        right.place(relx=0.65, rely=0, relwidth=0.35, relheight=1)

        tk.Label(right, image=controller.logo, bg="#0b1e33").pack(pady=30)
        tk.Label(right, text="Speak3Pro", font=("Helvetica", 18, "bold"), fg="white", bg="#0b1e33").pack()
        tk.Label(right, text="Proactivity\nProductivity\nProficiency", fg="white", bg="#0b1e33", font=("Georgia", 12)).pack(pady=10)

    def validate_login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        if not email or not password:
            messagebox.showerror("Validation Error", "Please fill in all fields.")
            return
        # Adicione sua lógica de autenticação aqui
        messagebox.showinfo("Login", "Login successful!")



# ---------------- REGISTER STEP 1 -------------------
class RegisterPageStep1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        left = tk.Frame(self, bg="#edf0f2")
        left.place(relx=0, rely=0, relwidth=0.65, relheight=1)

        tk.Label(left, text="Full name", bg="#edf0f2").pack(pady=5)
        self.name_entry = tk.Entry(left)
        self.name_entry.pack()

        tk.Label(left, text="Date of birth", bg="#edf0f2").pack(pady=5)
        self.dob_entry = tk.Entry(left)
        self.dob_entry.pack()

        tk.Label(left, text="CPF/SSN", bg="#edf0f2").pack(pady=5)
        self.cpf_entry = tk.Entry(left)
        self.cpf_entry.pack()

        tk.Label(left, text="Nationality", bg="#edf0f2").pack(pady=5)
        self.nationality_cb = ttk.Combobox(left, values=["Brazil", "USA", "Other"])
        self.nationality_cb.pack()

        tk.Button(left, text="← Back", command=lambda: controller.show_frame(LoginPage)).pack(side="left", padx=20, pady=30)
        tk.Button(left, text="Continue", command=self.validate_step1).pack(side="right", padx=20)

        right = tk.Frame(self, bg="#0b1e33")
        right.place(relx=0.65, rely=0, relwidth=0.35, relheight=1)

        tk.Label(right, image=controller.logo, bg="#0b1e33").pack(pady=30)
        tk.Label(right, text="Speak3Pro", font=("Helvetica", 18, "bold"), fg="white", bg="#0b1e33").pack()
        tk.Label(right, text="Register to have\nfull access to the\nplatform!", fg="white", bg="#0b1e33", font=("Georgia", 12)).pack(pady=10)

    def validate_step1(self):
        if not all([self.name_entry.get(), self.dob_entry.get(), self.cpf_entry.get(), self.nationality_cb.get()]):
            messagebox.showerror("Validation Error", "Please fill in all fields.")
            return
        self.controller.show_frame(RegisterPageStep2)


# ---------------- REGISTER STEP 2 -------------------
class RegisterPageStep2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        left = tk.Frame(self, bg="#edf0f2")
        left.place(relx=0, rely=0, relwidth=0.65, relheight=1)

        tk.Label(left, text="E-mail", bg="#edf0f2").pack(pady=5)
        self.email_entry = tk.Entry(left)
        self.email_entry.pack()

        tk.Label(left, text="Password", bg="#edf0f2").pack(pady=5)
        self.password_entry = tk.Entry(left, show="*")
        self.password_entry.pack()

        tk.Label(left, text="Confirm Password", bg="#edf0f2").pack(pady=5)
        self.confirm_entry = tk.Entry(left, show="*")
        self.confirm_entry.pack()

        tk.Button(left, text="← Back", command=lambda: controller.show_frame(RegisterPageStep1)).pack(side="left", padx=20, pady=30)
        tk.Button(left, text="Continue", command=self.validate_step2).pack(side="right", padx=20)

        right = tk.Frame(self, bg="#0b1e33")
        right.place(relx=0.65, rely=0, relwidth=0.35, relheight=1)

        tk.Label(right, image=controller.logo, bg="#0b1e33").pack(pady=30)
        tk.Label(right, text="Speak3Pro", font=("Helvetica", 18, "bold"), fg="white", bg="#0b1e33").pack()
        tk.Label(right, text="Register to have\nfull access to the\nplatform!", fg="white", bg="#0b1e33", font=("Georgia", 12)).pack(pady=10)

    def validate_step2(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm = self.confirm_entry.get()

        if not all([email, password, confirm]):
            messagebox.showerror("Validation Error", "Please fill in all fields.")
            return
        if '@' not in email or '.' not in email:
            messagebox.showerror("Validation Error", "Please enter a valid email address.")
            return
        if password != confirm:
            messagebox.showerror("Validation Error", "Passwords do not match.")
            return
        messagebox.showinfo("Success", "Registration completed!")
        self.controller.show_frame(RegisterCompletePage)


# ---------------- REGISTER COMPLETE -------------------
class RegisterCompletePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        left = tk.Frame(self, bg="#edf0f2")
        left.place(relx=0, rely=0, relwidth=0.65, relheight=1)

        tk.Label(left, text="You have completed\nyour registration!", font=("Georgia", 20, "bold"), fg="#822222", bg="#edf0f2").pack(pady=30)
        tk.Label(left, text="Now, log in to access\nall the content on\nour platform.", font=("Georgia", 12), bg="#edf0f2").pack(pady=10)

        tk.Button(left, text="Login", command=lambda: controller.show_frame(LoginPage)).pack(pady=40)

        right = tk.Frame(self, bg="#0b1e33")
        right.place(relx=0.65, rely=0, relwidth=0.35, relheight=1)

        tk.Label(right, image=controller.logo, bg="#0b1e33").pack(pady=30)
        tk.Label(right, text="Speak3Pro", font=("Helvetica", 18, "bold"), fg="white", bg="#0b1e33").pack()
        tk.Label(right, text="Register to have\nfull access to the\nplatform!", fg="white", bg="#0b1e33", font=("Georgia", 12)).pack(pady=10)


# ---------------------- RUN --------------------------
if __name__ == "__main__":
    app = Speak3ProApp()
    app.mainloop()
