import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

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
        tk.Entry(left, width=30).pack(pady=5)

        tk.Label(left, text="Password:", bg="#edf0f2").pack()
        tk.Entry(left, show="*", width=30).pack(pady=5)

        tk.Button(left, text="Login", width=25).pack(pady=20)

        tk.Label(left, text="Do not have an account?", bg="#edf0f2").pack()
        tk.Button(left, text="Sign up", command=lambda: controller.show_frame(RegisterPageStep1)).pack()

        # Right logo
        right = tk.Frame(self, bg="#0b1e33")
        right.place(relx=0.65, rely=0, relwidth=0.35, relheight=1)

        tk.Label(right, image=controller.logo, bg="#0b1e33").pack(pady=30)
        tk.Label(right, text="Speak3Pro", font=("Helvetica", 18, "bold"), fg="white", bg="#0b1e33").pack()
        tk.Label(right, text="Proactivity\nProductivity\nProficiency", fg="white", bg="#0b1e33", font=("Georgia", 12)).pack(pady=10)


# ---------------- REGISTER STEP 1 -------------------
class RegisterPageStep1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        left = tk.Frame(self, bg="#edf0f2")
        left.place(relx=0, rely=0, relwidth=0.65, relheight=1)

        tk.Label(left, text="Full name", bg="#edf0f2").pack(pady=5)
        tk.Entry(left).pack()

        tk.Label(left, text="Date of birth", bg="#edf0f2").pack(pady=5)
        tk.Entry(left).pack()

        tk.Label(left, text="CPF/SSN", bg="#edf0f2").pack(pady=5)
        tk.Entry(left).pack()

        tk.Label(left, text="Nationality", bg="#edf0f2").pack(pady=5)
        ttk.Combobox(left, values=["Brazil", "USA", "Other"]).pack()

        tk.Button(left, text="← Back", command=lambda: controller.show_frame(LoginPage)).pack(side="left", padx=20, pady=30)
        tk.Button(left, text="Continue", command=lambda: controller.show_frame(RegisterPageStep2)).pack(side="right", padx=20)

        # Right panel
        right = tk.Frame(self, bg="#0b1e33")
        right.place(relx=0.65, rely=0, relwidth=0.35, relheight=1)

        tk.Label(right, image=controller.logo, bg="#0b1e33").pack(pady=30)
        tk.Label(right, text="Speak3Pro", font=("Helvetica", 18, "bold"), fg="white", bg="#0b1e33").pack()
        tk.Label(right, text="Register to have\nfull access to the\nplatform!", fg="white", bg="#0b1e33", font=("Georgia", 12)).pack(pady=10)


# ---------------- REGISTER STEP 2 -------------------
class RegisterPageStep2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        left = tk.Frame(self, bg="#edf0f2")
        left.place(relx=0, rely=0, relwidth=0.65, relheight=1)

        tk.Label(left, text="E-mail", bg="#edf0f2").pack(pady=5)
        tk.Entry(left).pack()

        tk.Label(left, text="Password", bg="#edf0f2").pack(pady=5)
        tk.Entry(left, show="*").pack()

        tk.Label(left, text="Confirm Password", bg="#edf0f2").pack(pady=5)
        tk.Entry(left, show="*").pack()

        tk.Button(left, text="← Back", command=lambda: controller.show_frame(RegisterPageStep1)).pack(side="left", padx=20, pady=30)
        tk.Button(left, text="Continue", command=lambda: controller.show_frame(RegisterCompletePage)).pack(side="right", padx=20)

        right = tk.Frame(self, bg="#0b1e33")
        right.place(relx=0.65, rely=0, relwidth=0.35, relheight=1)

        tk.Label(right, image=controller.logo, bg="#0b1e33").pack(pady=30)
        tk.Label(right, text="Speak3Pro", font=("Helvetica", 18, "bold"), fg="white", bg="#0b1e33").pack()
        tk.Label(right, text="Register to have\nfull access to the\nplatform!", fg="white", bg="#0b1e33", font=("Georgia", 12)).pack(pady=10)


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
