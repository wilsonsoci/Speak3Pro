import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3
from datetime import datetime
import hashlib
import re
import subprocess
import sys

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('usuarios.db')
        self.criar_tabela()
    
    def criar_tabela(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL UNIQUE,
                data_nascimento DATE NOT NULL,
                nacionalidade TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL
            );
            """)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao criar tabela: {e}")
    
    def inserir_usuario(self, usuario):
        sql = """INSERT INTO usuarios(nome, cpf, data_nascimento, nacionalidade, email, senha)
                 VALUES(?, ?, ?, ?, ?, ?)"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, usuario)
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Erro de integridade: {e}")
            return None
        except sqlite3.Error as e:
            print(f"Erro ao inserir usuário: {e}")
            return None
    
    def verificar_login(self, email, senha):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT senha FROM usuarios WHERE email = ?", (email,))
            resultado = cursor.fetchone()
            if resultado:
                # Compara o hash da senha inserida com o hash armazenado
                return resultado[0] == hash_password(senha)
            return False
        except sqlite3.Error as e:
            print(f"Erro ao verificar login: {e}")
            return False
    
    def email_existe(self, email):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT 1 FROM usuarios WHERE email = ?", (email,))
            return cursor.fetchone() is not None
        except sqlite3.Error as e:
            print(f"Erro ao verificar email: {e}")
            return False
    
    def cpf_existe(self, cpf):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT 1 FROM usuarios WHERE cpf = ?", (cpf,))
            return cursor.fetchone() is not None
        except sqlite3.Error as e:
            print(f"Erro ao verificar CPF: {e}")
            return False

class Speak3ProApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Speak3Pro")
        self.geometry("800x500")
        self.resizable(False, False)
        self.db = Database()

        # Load logo image
        try:
            image = Image.open("logo.png")
            image = image.resize((80, 80), Image.Resampling.LANCZOS)
            self.logo = ImageTk.PhotoImage(image)
        except:
            # Caso a imagem não exista, cria uma placeholder
            self.logo = ImageTk.PhotoImage(Image.new('RGB', (80, 80), color='gray'))

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
        self.senha_entry = tk.Entry(left, show="*", width=30)
        self.senha_entry.pack(pady=5)

        tk.Button(left, text="Login", width=25, command=self.fazer_login).pack(pady=20)

        tk.Label(left, text="Do not have an account?", bg="#edf0f2").pack()
        tk.Button(left, text="Sign up", command=lambda: controller.show_frame(RegisterPageStep1)).pack()

        # Right logo
        right = tk.Frame(self, bg="#0b1e33")
        right.place(relx=0.65, rely=0, relwidth=0.35, relheight=1)

        tk.Label(right, image=controller.logo, bg="#0b1e33").pack(pady=30)
        tk.Label(right, text="Speak3Pro", font=("Helvetica", 18, "bold"), fg="white", bg="#0b1e33").pack()
        tk.Label(right, text="Proactivity\nProductivity\nProficiency", fg="white", bg="#0b1e33", font=("Georgia", 12)).pack(pady=10)

    def fazer_login(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        
        if not email or not senha:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos")
            return
        
        if self.controller.db.verificar_login(email, senha):
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            subprocess.Popen(["python", "main.py"])
            self.master.destroy()
            sys.exit()
        else:
            messagebox.showerror("Erro", "E-mail ou senha incorretos")

# ---------------- REGISTER STEP 1 -------------------
class RegisterPageStep1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.dados_step1 = {}

        left = tk.Frame(self, bg="#edf0f2")
        left.place(relx=0, rely=0, relwidth=0.65, relheight=1)

        tk.Label(left, text="Full name", bg="#edf0f2").pack(pady=5)
        self.nome_entry = tk.Entry(left)
        self.nome_entry.pack()

        tk.Label(left, text="Date of birth (DD/MM/YYYY)", bg="#edf0f2").pack(pady=5)
        self.data_nasc_entry = tk.Entry(left)
        self.data_nasc_entry.pack()

        tk.Label(left, text="CPF/SSN", bg="#edf0f2").pack(pady=5)
        self.cpf_entry = tk.Entry(left)
        self.cpf_entry.pack()

        tk.Label(left, text="Nationality", bg="#edf0f2").pack(pady=5)
        self.nacionalidade_combo = ttk.Combobox(left, values=["Brazil", "USA", "Other"])
        self.nacionalidade_combo.pack()

        tk.Button(left, text="← Back", command=lambda: controller.show_frame(LoginPage)).pack(side="left", padx=20, pady=30)
        tk.Button(left, text="Continue", command=self.validar_step1).pack(side="right", padx=20)

        # Right panel
        right = tk.Frame(self, bg="#0b1e33")
        right.place(relx=0.65, rely=0, relwidth=0.35, relheight=1)

        tk.Label(right, image=controller.logo, bg="#0b1e33").pack(pady=30)
        tk.Label(right, text="Speak3Pro", font=("Helvetica", 18, "bold"), fg="white", bg="#0b1e33").pack()
        tk.Label(right, text="Register to have\nfull access to the\nplatform!", fg="white", bg="#0b1e33", font=("Georgia", 12)).pack(pady=10)

    def validar_step1(self):
        cpf = self.cpf_entry.get()
        if not cpf.isdigit() or len(cpf) != 11:
            messagebox.showerror("Erro", "CPF deve conter 11 dígitos numéricos")
            return
        nome = self.nome_entry.get()
        data_nasc = self.data_nasc_entry.get()
        cpf = self.cpf_entry.get()
        nacionalidade = self.nacionalidade_combo.get()
        
        if not all([nome, data_nasc, cpf, nacionalidade]):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos")
            return
        
        # No RegisterPageStep1, adicione validação adicional:
        try:
            data_obj = datetime.strptime(data_nasc, "%d/%m/%Y")
            if data_obj > datetime.now():
                messagebox.showerror("Erro", "Data de nascimento não pode ser no futuro")
                return
        except ValueError:
            messagebox.showerror("Erro", "Formato de data inválido! Use DD/MM/AAAA")
            return
        
        # Salva os dados para usar no próximo passo
        self.dados_step1 = {
            'nome': nome,
            'data_nasc': data_nasc,
            'cpf': cpf,
            'nacionalidade': nacionalidade
        }
        
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
        self.senha_entry = tk.Entry(left, show="*")
        self.senha_entry.pack()

        tk.Label(left, text="Confirm Password", bg="#edf0f2").pack(pady=5)
        self.confirm_senha_entry = tk.Entry(left, show="*")
        self.confirm_senha_entry.pack()

        tk.Button(left, text="← Back", command=lambda: controller.show_frame(RegisterPageStep1)).pack(side="left", padx=20, pady=30)
        tk.Button(left, text="Continue", command=self.validar_step2).pack(side="right", padx=20)

        right = tk.Frame(self, bg="#0b1e33")
        right.place(relx=0.65, rely=0, relwidth=0.35, relheight=1)

        tk.Label(right, image=controller.logo, bg="#0b1e33").pack(pady=30)
        tk.Label(right, text="Speak3Pro", font=("Helvetica", 18, "bold"), fg="white", bg="#0b1e33").pack()
        tk.Label(right, text="Register to have\nfull access to the\nplatform!", fg="white", bg="#0b1e33", font=("Georgia", 12)).pack(pady=10)

    def validar_step2(self):
        email = self.email_entry.get()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Erro", "Formato de e-mail inválido")
            return
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        confirm_senha = self.confirm_senha_entry.get()
        
        if not all([email, senha, confirm_senha]):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos")
            return
        
        if senha != confirm_senha:
            messagebox.showerror("Erro", "As senhas não coincidem")
            return
        
        if len(senha) < 6:
            messagebox.showerror("Erro", "A senha deve ter pelo menos 6 caracteres")
            return
        
        if self.controller.db.email_existe(email):
            messagebox.showerror("Erro", "E-mail já cadastrado")
            return
        
        # Recupera os dados do passo 1
        dados_step1 = self.controller.frames[RegisterPageStep1].dados_step1
        
        # Converte a data para formato SQL
        data_obj = datetime.strptime(dados_step1['data_nasc'], "%d/%m/%Y")
        data_sql = data_obj.strftime("%Y-%m-%d")
        
        # Cria o usuário no banco de dados
       # Substitua a linha onde o usuário é criado:
        usuario = (
            dados_step1['nome'],
            dados_step1['cpf'],
            data_sql,
            dados_step1['nacionalidade'],
            email,
            hash_password(senha)  # Armazena o hash da senha
        )
        
        user_id = self.controller.db.inserir_usuario(usuario)
        
        if user_id:
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            self.controller.show_frame(RegisterCompletePage)
        else:
            messagebox.showerror("Erro", "Não foi possível completar o cadastro")

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
