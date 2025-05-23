import tkinter as tk
from tkinter import ttk, messagebox

def pagar():
    metodo = selected.get()
    if metodo in ["Credit card", "Debit card"]:
        f = frames_metodos[metodo]
        n = f.num_cartao.get().strip()
        v = f.validade.get().strip()
        c = f.cvv.get().strip()

        if not (n and v and c):
            messagebox.showwarning("Warning", "Please fill all the card details.")
            return

        f.pack_forget()
        pay_button.pack_forget()

        confirmation_label.config(text="Thank you for your purchase!\nYou will receive an email with details.")
        confirmation_label.pack(pady=20)

        root.after(5000, show_continue_options)

    else:
        messagebox.showinfo("Payment", "You will receive an email when your class starts!")

def show_continue_options():
    confirmation_label.pack_forget()
    continue_frame.pack(pady=20)

def continue_shopping():
    continue_frame.pack_forget()
    for f in frames_metodos.values():
        f.num_cartao.delete(0, tk.END)
        f.validade.delete(0, tk.END)
        f.cvv.delete(0, tk.END)
    metodo = selected.get()
    if metodo in ["Credit card", "Debit card"]:
        frames_metodos[metodo].pack(fill="x", padx=10, pady=(0,10))
    pay_button.pack(pady=15)

def go_home():
    messagebox.showinfo("Home", "Going back to home page...")
    root.destroy()

# Cores
header_bg = "#0d2a4a"
header_fg = "white"
gray = "#dddddd"
bg = "#ffffff"
summary_bg = "#e2e2e2"
dark1 = "#6a11cb"
dark2 = "#2575fc"
dark1_hover = "#7b2ff7"
dark2_hover = "#5f5fc7"

root = tk.Tk()
root.title("Checkout")
root.geometry("1100x700")
root.configure(bg=bg)

# Cabeçalho
header = tk.Frame(root, bg=header_bg, height=50)
header.pack(fill="x")
left_header = tk.Frame(header, bg=header_bg)
left_header.pack(side="left")
tk.Label(left_header, text="\U0001F3E0", bg=header_bg, fg=header_fg, font=("Segoe UI Emoji", 18)).pack(side="left", padx=15)
for txt in ["Courses", "Units", "About us", "My learning"]:
    tk.Label(left_header, text=txt, bg=header_bg, fg=header_fg, font=("Segoe UI", 12, "bold")).pack(side="left", padx=15)

def dummy():
    print("Button clicked!")

def criar_botao_cabecalho(parent, texto, comando):
    return tk.Button(parent, text=texto, bg="white", fg=header_bg,
                     font=("Segoe UI", 11, "bold"), width=10, relief="flat", command=comando)

center_header = tk.Frame(header, bg=header_bg)
center_header.pack(side="left", expand=True, fill="x", padx=20)
search_var = tk.StringVar(value="Search")
search = tk.Entry(center_header, textvariable=search_var, font=("Segoe UI", 12), fg="gray")
search.pack(pady=8, fill="x")

search.bind('<FocusIn>', lambda e: (search_var.set(''), search.config(fg='black')) if search_var.get() == 'Search' else None)
search.bind('<FocusOut>', lambda e: (search_var.set('Search'), search.config(fg='gray')) if search_var.get() == '' else None)

right_header = tk.Frame(header, bg=header_bg)
right_header.pack(side="right", padx=20)
criar_botao_cabecalho(right_header, "Register", dummy).pack(side="right", padx=10, pady=8)
criar_botao_cabecalho(right_header, "Login", dummy).pack(side="right", pady=8)

# Título
tk.Label(root, text="Checkout", font=("Georgia", 28, "bold"), bg=bg, fg="#0d2a4a").pack(pady=25)

main = tk.Frame(root, bg=bg)
main.pack(padx=30, fill="both", expand=True)
left = tk.Frame(main, bg=bg)
left.pack(side="left", padx=20, fill="both", expand=True)
right = tk.Frame(main, bg=summary_bg, width=300, bd=1, relief="ridge")
right.pack(side="right", padx=20, fill="y")

# -------------------- Conteúdo Principal --------------------
main = tk.Frame(root, bg=bg)
main.pack(padx=30, fill="both", expand=True)

left = tk.Frame(main, bg=bg)
left.pack(side="left", padx=20, fill="both", expand=True)

right = tk.Frame(main, bg=summary_bg, width=300, bd=1, relief="ridge")
right.pack(side="right", padx=20, fill="y")

# ----- Billing Address -----
tk.Label(left, text="Billing Address", font=("Georgia", 14, "bold"), bg=bg).pack(anchor="w")
tk.Label(left, text="Country", font=("Arial", 11), bg=bg).pack(anchor="w", pady=(10, 0))

country = ttk.Combobox(left, values=["Brazil", "USA", "Portugal", "Germany"], width=30)
country.set("Brazil")
country.pack(pady=5)

# ----- Payment Method -----
frame_pm = tk.Frame(left, bg=bg)
frame_pm.pack(anchor="w", pady=25)

selected = tk.StringVar(value="Pix")
methods = [
    ("Pix", "10% discount for cash payment!"),
    ("Credit card", ""),
    ("Debit card", ""),
    ("Bank slip", "")
]

frames_metodos = {}

def mostrar_formulario_cartao():
    metodo = selected.get()
    for f in frames_metodos.values():
        f.pack_forget()
    if metodo in ["Credit card", "Debit card"]:
        frames_metodos[metodo].pack(fill="x", padx=10, pady=(0,10))

tk.Label(frame_pm, text="Payment Method", font=("Georgia", 14, "bold"), bg=bg).grid(row=0, column=0, sticky="w")
tk.Label(frame_pm, text="Secure and encrypted 🔐", font=("Arial", 9), bg=bg).grid(row=0, column=1, sticky="e", padx=20)

for i, (method, note) in enumerate(methods):
    box = tk.Frame(left, bg=gray, relief="solid", bd=1)
    box.pack(fill="x", pady=2)

    rb = tk.Radiobutton(box, variable=selected, value=method, bg=gray, command=mostrar_formulario_cartao)
    rb.pack(side="left", padx=5)
    tk.Label(box, text=method, font=("Arial", 11), bg=gray, fg="#0d2a4a").pack(side="left")
    if note:
        tk.Label(box, text=note, font=("Arial", 9), bg=gray, fg="#2c3e50").pack(side="right", padx=5)

    if method in ["Credit card", "Debit card"]:
        f = tk.Frame(left, bg="#f5f5f5", bd=1, relief="solid", padx=10, pady=10)
        frames_metodos[method] = f

        tk.Label(f, text="Card number:", font=("Arial", 11), bg="#f5f5f5").pack(anchor="w")
        num_cartao = tk.Entry(f, width=30)
        num_cartao.pack(pady=2)

        tk.Label(f, text="Expiry date (MM/YY):", font=("Arial", 11), bg="#f5f5f5").pack(anchor="w", pady=(10,2))
        validade = tk.Entry(f, width=10)
        validade.pack(pady=2)

        tk.Label(f, text="CVV:", font=("Arial", 11), bg="#f5f5f5").pack(anchor="w", pady=(10,2))
        cvv = tk.Entry(f, width=5, show="*")
        cvv.pack(pady=2)

        f.num_cartao = num_cartao
        f.validade = validade
        f.cvv = cvv

mostrar_formulario_cartao()

# ----- Order details -----
tk.Label(left, text="Order details   (Number of courses)", font=("Arial", 10), fg="gray", bg=bg).pack(anchor="w", pady=10)
tk.Label(left, bg=gray, height=2, width=60).pack(pady=(0, 20))

# -------------------- Right: Order Summary --------------------
tk.Label(right, text="Order Summary", font=("Georgia", 16), bg=summary_bg, fg="black").pack(pady=20)

summary_content = [
    ("Price:", "R$ 99,99"),
    ("Discount (10% off):", "R$ 10,00")
]

for label, value in summary_content:
    row = tk.Frame(right, bg=summary_bg)
    row.pack(fill="x", pady=5, padx=20)
    tk.Label(row, text=label, font=("Arial", 12), bg=summary_bg).pack(side="left")
    tk.Label(row, text=value, font=("Arial", 12), bg=summary_bg).pack(side="right")

tk.Frame(right, height=1, bg="black").pack(fill="x", padx=20, pady=10)

tk.Label(right, text="Total (Number of courses):", font=("Arial", 12), bg=summary_bg).pack(anchor="w", padx=20)
tk.Label(right, text="R$ 89,99", font=("Georgia", 14, "bold"), bg=summary_bg, fg="#2c3e50").pack(anchor="w", padx=20, pady=5)

# ------ Botão customizado com hover ------
def criar_botao_pagamento(parent, texto, comando):
    canvas = tk.Canvas(parent, width=220, height=45, highlightthickness=0, bg=summary_bg)
    canvas.pack(pady=15)

    fundo1 = canvas.create_rectangle(0, 0, 220, 45, outline="", fill=dark1)
    fundo2 = canvas.create_rectangle(0, 0, 220, 45, outline="", fill=dark2)
    texto_id = canvas.create_text(110, 23, text=texto, fill="white", font=("Arial", 12, "bold"))

    def clique(event):
        comando()

    def ao_passar_mouse(event):
        canvas.itemconfig(fundo1, fill=dark1_hover)
        canvas.itemconfig(fundo2, fill=dark2_hover)

    def ao_sair_mouse(event):
        canvas.itemconfig(fundo1, fill=dark1)
        canvas.itemconfig(fundo2, fill=dark2)

    canvas.bind("<Button-1>", clique)
    canvas.tag_bind(texto_id, "<Button-1>", clique)
    canvas.bind("<Enter>", ao_passar_mouse)
    canvas.bind("<Leave>", ao_sair_mouse)

    return canvas

pay_button = criar_botao_pagamento(right, "Pay   R$ 89,99", pagar)

# Aviso e garantia
tk.Label(right, text="Not happy? Get a full refund within\n30 days. Simple and easy!",
         font=("Arial", 9), bg=summary_bg, fg="black", justify="center").pack(pady=5)

warning = tk.Frame(right, bg="#d6d6d6", bd=1, relief="solid", padx=10, pady=10)
warning.pack(pady=15, padx=20)
tk.Label(warning, text="⚠️", font=("Arial", 16), bg="#d6d6d6", fg="red").pack()
tk.Label(warning, text="We will send you an\nemail when your\nclass starts", font=("Arial", 10),
         bg="#d6d6d6", justify="center").pack()

# Confirmação e continuar
confirmation_label = tk.Label(left, text="", font=("Arial", 14), fg="green", bg=bg)
continue_frame = tk.Frame(left, bg=bg)
tk.Label(continue_frame, text="Do you want to continue shopping or go back to the home page?", font=("Arial", 12), bg=bg).pack(pady=10)

btn_continue = tk.Button(continue_frame, text="Continue Shopping", command=continue_shopping, bg="#4CAF50", fg="white", width=20)
btn_continue.pack(side="left", padx=20, pady=10)

btn_home = tk.Button(continue_frame, text="Go to Home", command=go_home, bg="#f44336", fg="white", width=20)
btn_home.pack(side="right", padx=20, pady=10)

root.mainloop()
