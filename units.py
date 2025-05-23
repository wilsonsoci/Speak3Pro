import tkinter as tk
from tkinter import ttk

# Cores principais do design
BG_COLOR = "#f9fff9"
PRIMARY_COLOR = "#002b4d"
BUTTON_COLOR = "#c6d4e1"

# Cores do cabeçalho
header_bg = PRIMARY_COLOR
header_fg = "white"

# Janela principal
root = tk.Tk()
root.title("Speak3Pro - Find the unit closest to you")
root.geometry("1000x700")
root.configure(bg=BG_COLOR)

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

# Título principal
title = tk.Label(root, text="Find the unit closest to you", font=("Georgia", 24, "bold"), fg=PRIMARY_COLOR, bg=BG_COLOR)
title.pack(pady=(40, 20))

# Frame dos selects
select_frame = tk.Frame(root, bg=BG_COLOR)
select_frame.pack(pady=20)

# Select 1
unit_label = tk.Label(select_frame, text="Select a unit:", font=("Georgia", 16), fg=PRIMARY_COLOR, bg=BG_COLOR)
unit_label.grid(row=0, column=0, padx=40, pady=10)
unit_combo = ttk.Combobox(select_frame, values=["Click on the unit of interest"], state="readonly", width=40)
unit_combo.current(0)
unit_combo.grid(row=1, column=0, padx=40)

# Select 2
period_label = tk.Label(select_frame, text="Select the desired period:", font=("Georgia", 16), fg=PRIMARY_COLOR, bg=BG_COLOR)
period_label.grid(row=0, column=1, padx=40, pady=10)
period_combo = ttk.Combobox(select_frame, values=["Click on the period of interest"], state="readonly", width=40)
period_combo.current(0)
period_combo.grid(row=1, column=1, padx=40)

# Nota
note = tk.Label(root, text="Note: The class may be canceled or have changes in the number of places, dates and times.",
                font=("Arial", 10), fg=PRIMARY_COLOR, bg=BG_COLOR)
note.pack(pady=(30, 10))

# Botão
def on_register():
    print("Interest registered!")

register_frame = tk.Frame(root, bg=BG_COLOR)
register_frame.pack()

register_text = tk.Label(register_frame, text="Receive a notification via WhatsApp if new classes open.",
                         font=("Arial", 10), fg=PRIMARY_COLOR, bg=BG_COLOR)
register_text.pack(side=tk.LEFT)

register_btn = tk.Button(register_frame, text="Register interest", command=on_register,
                         bg=BUTTON_COLOR, fg=PRIMARY_COLOR, relief="flat", font=("Arial", 9))
register_btn.pack(side=tk.LEFT, padx=10)

# Rodapé (simples)
footer = tk.Frame(root, bg=PRIMARY_COLOR, height=100)
footer.pack(fill=tk.X, side=tk.BOTTOM, pady=(40, 0))

footer_label = tk.Label(footer, text="Speak3Pro", font=("Arial", 12, "bold"), fg="white", bg=PRIMARY_COLOR)
footer_label.pack(pady=20)

root.mainloop()
