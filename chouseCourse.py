import tkinter as tk
from PIL import Image, ImageTk

# Main colors
BG_COLOR = "#f9fff9"
PRIMARY_COLOR = "#002b4d"
ACCENT_COLOR = "#aab8c2"
TEXT_COLOR = "#333333"
CARD_BG = "#d2dee7"
BUTTON_BG = "white"

# Dummy function
def dummy():
    print("Button clicked")

# Main window
root = tk.Tk()
root.title("Speak3Pro - English Course")
root.geometry("1000x750")
root.configure(bg=BG_COLOR)

# ===== HEADER =====
header = tk.Frame(root, bg=PRIMARY_COLOR, height=60)
header.pack(fill="x")

left_header = tk.Frame(header, bg=PRIMARY_COLOR)
left_header.pack(side="left", padx=15)
tk.Label(left_header, text="\U0001F3E0", bg=PRIMARY_COLOR, fg="white", font=("Segoe UI Emoji", 18)).pack(side="left", padx=10)
for item in ["Courses", "Units", "About us", "My learning"]:
    tk.Label(left_header, text=item, bg=PRIMARY_COLOR, fg="white", font=("Segoe UI", 11, "bold")).pack(side="left", padx=15)

center_header = tk.Frame(header, bg=PRIMARY_COLOR)
center_header.pack(side="left", expand=True, fill="x", padx=20)
search_var = tk.StringVar(value="Search")
search = tk.Entry(center_header, textvariable=search_var, font=("Segoe UI", 11), fg="gray")
search.pack(pady=10, fill="x")

search.bind('<FocusIn>', lambda e: (search_var.set(''), search.config(fg='black')) if search_var.get() == 'Search' else None)
search.bind('<FocusOut>', lambda e: (search_var.set('Search'), search.config(fg='gray')) if search_var.get() == '' else None)

right_header = tk.Frame(header, bg=PRIMARY_COLOR)
right_header.pack(side="right", padx=20)
tk.Button(right_header, text="Login", bg=BUTTON_BG, fg=PRIMARY_COLOR, font=("Segoe UI", 10, "bold"), relief="flat", width=10).pack(side="right", padx=5, pady=10)
tk.Button(right_header, text="Register", bg=BUTTON_BG, fg=PRIMARY_COLOR, font=("Segoe UI", 10, "bold"), relief="flat", width=10).pack(side="right", padx=5, pady=10)

# ===== MAIN BODY =====
content = tk.Frame(root, bg=BG_COLOR)
content.pack(fill="both", expand=True, padx=40, pady=30)

# ---- Left side
left_content = tk.Frame(content, bg=BG_COLOR)
left_content.pack(side="left", fill="both", expand=True)

tk.Label(left_content, text="English Course", font=("Georgia", 22, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).pack(anchor="w")

# Carrega e exibe a bandeira abaixo do título
flag_img = Image.open("img/us.png")
flag_img = flag_img.resize((500, 120))  # Ajuste de tamanho conforme necessário
flag_photo = ImageTk.PhotoImage(flag_img)
flag_label = tk.Label(left_content, image=flag_photo, bg=BG_COLOR)
flag_label.image = flag_photo
flag_label.pack(anchor="w", pady=(10, 20))

tk.Label(left_content, text="Highest Rated\nUS/UK Teachers (BES)", font=("Arial", 10), bg=BG_COLOR, fg=TEXT_COLOR).pack(anchor="w", pady=(10, 5))
tk.Label(left_content, text="240+ students", font=("Arial", 10), bg=BG_COLOR, fg=TEXT_COLOR).pack(anchor="w")
tk.Label(left_content, text="Teacher Evaluation", font=("Arial", 10), bg=BG_COLOR, fg=TEXT_COLOR).pack(anchor="w")

tk.Label(left_content, text="Included:", font=("Segoe UI", 12, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).pack(anchor="w", pady=(20, 5))

for item in ["100 hours of course", "guides", "daily exercises", "feedback", "certificate of completion"]:
    tk.Label(left_content, text="✔ " + item, font=("Arial", 10), bg=BG_COLOR, fg=TEXT_COLOR).pack(anchor="w", padx=10)

tk.Label(left_content, text="Course division:", font=("Segoe UI", 12, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).pack(anchor="w", pady=(20, 5))
for mod in ["Module 1", "Module 2", "Mini", "Module 3", "Final Test"]:
    tk.Label(left_content, text=mod, bg="white", fg=PRIMARY_COLOR, font=("Arial", 10), bd=1, relief="solid", width=30, anchor="w", padx=10).pack(anchor="w", pady=2)

# ---- Right side (card)
right_card = tk.Frame(content, bg=CARD_BG, width=250, height=250, relief="flat", bd=1)
right_card.pack(side="right", padx=30, pady=10)
right_card.pack_propagate(False)

tk.Label(right_card, text="$ 17,90", font=("Georgia", 22, "bold"), bg=CARD_BG, fg=PRIMARY_COLOR).pack(pady=(30, 0))
tk.Label(right_card, text="Per month", font=("Arial", 10), bg=CARD_BG, fg=TEXT_COLOR).pack()

tk.Button(right_card, text="Buy", bg=BUTTON_BG, fg=PRIMARY_COLOR, font=("Segoe UI", 10, "bold"), relief="flat", width=20).pack(pady=10)
tk.Button(right_card, text="Add to backpack", bg=BUTTON_BG, fg=PRIMARY_COLOR, font=("Segoe UI", 10, "bold"), relief="flat", width=20).pack()

tk.Label(right_card, text="30-Day Money Back Guarantee\nNote: Classes will be from Monday\nto Friday in the unit you chose",
         font=("Arial", 8), bg=CARD_BG, fg=TEXT_COLOR, justify="center").pack(pady=10)

# ===== FOOTER =====
footer = tk.Frame(root, bg=PRIMARY_COLOR, height=100)
footer.pack(fill="x", side="bottom", pady=(20, 0))

tk.Label(footer, text="Speak3Pro", font=("Arial", 12, "bold"), fg="white", bg=PRIMARY_COLOR).pack(side="left", padx=40, pady=30)
tk.Label(footer, text="Questions\nPortal do aluno\nOpen Source", font=("Arial", 9), fg="white", bg=PRIMARY_COLOR, justify="left").pack(side="left", padx=40)
tk.Label(footer, text="Contact\n📧 ✉️", font=("Arial", 9), fg="white", bg=PRIMARY_COLOR).pack(side="left", padx=40)
tk.Label(footer, text="Follow us on social media\n🔗", font=("Arial", 9), fg="white", bg=PRIMARY_COLOR).pack(side="right", padx=40)

# Run the application
root.mainloop()
