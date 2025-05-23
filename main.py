import tkinter as tk
from tkinter import ttk

class HomePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SpeakThreePro - Home")
        self.geometry("1024x720")
        self.configure(bg="#edf0f2")

        # Configurar grid da janela para expandir
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Frame container que vai conter o canvas e scrollbar
        container = tk.Frame(self, bg="#edf0f2")
        container.grid(row=0, column=0, sticky="nsew")

        # Canvas com scroll vertical
        self.canvas = tk.Canvas(container, bg="#edf0f2", highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.canvas.configure(yscrollcommand=scrollbar.set)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Frame dentro do canvas que conterá todo conteúdo e será centralizado
        self.content_frame = tk.Frame(self.canvas, bg="#edf0f2")
        self.content_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Criar janela no canvas para o frame
        self.canvas_window = self.canvas.create_window((0, 0), window=self.content_frame, anchor="n")

        # Centralizar o content_frame dentro do canvas na largura
        self.canvas.bind("<Configure>", self.resize_content_frame)

        # Criar conteúdo
        self.create_header()
        self.create_course_cards()
        self.create_additional_sections()


    def resize_content_frame(self, event):
        # Centraliza o content_frame e limita largura máxima em 900
        canvas_width = event.width
        max_width = 900
        width = min(canvas_width, max_width)
        self.canvas.itemconfig(self.canvas_window, width=width)
        # Centralizar: atualizar o x da janela para ficar no meio
        x = (canvas_width - width) // 2
        self.canvas.coords(self.canvas_window, x, 0)

    def create_header(self):
        header = tk.Frame(self.content_frame, bg="#0b1e33", height=60)
        header.pack(fill="x", pady=(0, 10))

        header.grid_columnconfigure(0, weight=1)
        header.grid_rowconfigure(0, weight=1)

        title = tk.Label(header, text="SpeakThreePro", font=("Georgia", 16, "bold"), fg="white", bg="#0b1e33")
        title.grid(row=0, column=0, padx=20, sticky="w")

        btn_frame = tk.Frame(header, bg="#0b1e33")
        btn_frame.grid(row=0, column=1, padx=10)

        for name in ["Courses", "Units", "About us", "My learning"]:
            btn = tk.Button(btn_frame, text=name, bg="#0b1e33", fg="white", border=0,
                            font=("Helvetica", 10), activebackground="#1a2e52", activeforeground="white")
            btn.pack(side="left", padx=8)

        search_frame = tk.Frame(header, bg="#0b1e33")
        search_frame.grid(row=0, column=2, padx=10, sticky="e")

        search_entry = ttk.Entry(search_frame, width=20)
        search_entry.pack(side="left", padx=(0, 5))
        search_btn = ttk.Button(search_frame, text="Search")
        search_btn.pack(side="left")

        login_frame = tk.Frame(header, bg="#0b1e33")
        login_frame.grid(row=0, column=3, padx=20)

        login_btn = tk.Button(login_frame, text="Login", bg="#0b1e33", fg="white", borderwidth=1,
                              relief="solid", font=("Helvetica", 10), activebackground="#1a2e52", activeforeground="white")
        login_btn.pack(side="left", padx=5)
        register_btn = tk.Button(login_frame, text="Register", bg="#0b1e33", fg="white", borderwidth=1,
                                 relief="solid", font=("Helvetica", 10), activebackground="#1a2e52", activeforeground="white")
        register_btn.pack(side="left", padx=5)

    def create_course_cards(self):
        title = tk.Label(self.content_frame, text="Where you really learn!", font=("Georgia", 20, "bold"),
                         bg="#edf0f2", fg="#0b1e33")
        title.pack(pady=(10, 15))

        cards_frame = tk.Frame(self.content_frame, bg="#edf0f2")
        cards_frame.pack(padx=30, fill="x")

        courses = ["English", "Spanish", "Germany", "Italian", "French", "Portuguese"]

        for i in range(3):
            cards_frame.grid_columnconfigure(i, weight=1, uniform="col")

        for i, course in enumerate(courses):
            card = tk.Frame(cards_frame, bg="#7a8ea1", bd=0, relief="ridge", padx=15, pady=15)
            card.grid(row=i // 3, column=i % 3, padx=15, pady=15, sticky="nsew")

            emoji = tk.Label(card, text="🏳️", font=("Arial", 30), bg="#7a8ea1")
            emoji.pack(pady=(0, 10))

            course_label = tk.Label(card, text=course, font=("Georgia", 14, "bold"), bg="#7a8ea1", fg="white")
            course_label.pack(pady=(0, 10))

            desc_label = tk.Label(card, text="Find out about the course", font=("Helvetica", 10), bg="#7a8ea1",
                                  fg="white")
            desc_label.pack()

    def create_additional_sections(self):
        motivational = tk.Label(self.content_frame, text="Achieve fluency once and for all!",
                               font=("Georgia", 18, "bold"),
                               fg="#0b1e33", bg="#edf0f2")
        motivational.pack(pady=(30, 20))

        info_frame = tk.Frame(self.content_frame, bg="#edf0f2")
        info_frame.pack(padx=20, fill="x")

        for i in range(3):
            info_frame.grid_columnconfigure(i, weight=1, uniform="benefit")

        info_data = [
            ("In-person classes", "Estude presencialmente... Clique aqui", "👥"),
            ("Cost benefit", "Aprenda o idioma... Clique aqui", "💰"),
            ("Networking", "Crie uma rede... Clique aqui", "🌐")
        ]

        for i, (title, text, emoji) in enumerate(info_data):
            box = tk.Frame(info_frame, bg="#f4f7fa", bd=1, relief="solid", padx=15, pady=15)
            box.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")

            tk.Label(box, text=emoji, font=("Arial", 30), bg="#f4f7fa").pack(pady=(0, 10))
            tk.Label(box, text=title, font=("Georgia", 14, "bold"), fg="#a52a2a", bg="#f4f7fa").pack(pady=(0, 5))
            tk.Label(box, text=text, wraplength=200, justify="center", font=("Helvetica", 11), bg="#f4f7fa").pack()

        dropdown_label = tk.Label(self.content_frame,
                                  text="Choose the unit and find out about the available classes",
                                  font=("Georgia", 13), bg="#edf0f2")
        dropdown_label.pack(pady=(40, 15))

        sel_frame = tk.Frame(self.content_frame, bg="#edf0f2")
        sel_frame.pack(padx=20, fill="x")

        sel_frame.grid_columnconfigure(0, weight=1)
        sel_frame.grid_columnconfigure(1, weight=1)

        tk.Label(sel_frame, text="Select a unit:", bg="#edf0f2", font=("Helvetica", 11)).grid(row=0, column=0,
                                                                                            sticky="w", padx=10, pady=5)
        tk.Label(sel_frame, text="Select the desired period:", bg="#edf0f2", font=("Helvetica", 11)).grid(row=0, column=1,
                                                                                                         sticky="w",
                                                                                                         padx=10, pady=5)

        unit_box = ttk.Combobox(sel_frame, values=["Unit A", "Unit B", "Unit C"])
        unit_box.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

        period_box = ttk.Combobox(sel_frame, values=["Morning", "Afternoon", "Evening"])
        period_box.grid(row=1, column=1, sticky="ew", padx=10, pady=10)

        note = tk.Label(self.content_frame,
                        text="Note: The class may be cancelled or have changes in the number of places, dates and times.",
                        font=("Helvetica", 9), fg="white", bg="#5a6a7a", wraplength=900, pady=8)
        note.pack(pady=30, padx=20, fill="x")

        register = tk.Button(self.content_frame, text="Register Interest", bg="#0b1e33", fg="white",
                             font=("Helvetica", 12, "bold"), padx=20, pady=10, activebackground="#152a4f",
                             activeforeground="white")
        register.pack(pady=(0, 30))

        who_are_we_btn = tk.Button(self.content_frame, text="Who Are We", bg="#0b1e33", fg="white",
                            font=("Helvetica", 12, "bold"), padx=20, pady=10,
                            activebackground="#152a4f", activeforeground="white",
                            command=self.open_who_are_we)
        who_are_we_btn.pack(pady=(10, 30))
        
        profile_btn = tk.Button(self.content_frame, text="Go to Profile", bg="#0b1e33", fg="white",
                        font=("Helvetica", 12, "bold"), padx=20, pady=10,
                        command=self.open_user_profile)
        profile_btn.pack(pady=(10, 30))


        courses_btn = tk.Button(self.content_frame, text="View Courses", bg="#0b1e33", fg="white",
                                font=("Helvetica", 12, "bold"), padx=20, pady=10,
                                activebackground="#152a4f", activeforeground="white",
                                command=self.open_courses_window)
        courses_btn.pack(pady=(10, 30))


    def open_who_are_we(self):
        WhoAreWeWindow(self)

    def open_user_profile(self):
        UserProfile(self)

    def open_courses_window(self):
        CoursesWindow(self)


    



class WhoAreWeWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Who Are We")
        self.geometry("800x600")
        self.configure(bg="#edf0f2")
        
        title = tk.Label(self, text="Developing Potential,\nTransforming Futures", 
                         font=("Georgia", 20, "bold"), fg="#0b1e33", bg="#edf0f2", justify="center")
        title.pack(pady=(20, 10))
        
        intro = tk.Label(self, text="At [Company Name], we believe that people of all ages deserve opportunities to grow. "
                                    "We provide quality education at affordable prices because growth shouldn't be a privilege, it's a right for everyone.",
                         font=("Helvetica", 11), wraplength=700, bg="#edf0f2", justify="center")
        intro.pack(pady=(0, 20))
        
        mission_title = tk.Label(self, text="Our Mission", font=("Georgia", 16, "bold"), bg="#edf0f2", fg="#0b1e33")
        mission_title.pack(pady=(10, 5))
        
        mission = tk.Label(self, text="Our goal is to provide the best teaching method, combining quality, personal development and affordable investment, "
                                      "so that each student can expand their possibilities.", 
                           font=("Helvetica", 11), wraplength=700, bg="#edf0f2", justify="center")
        mission.pack(pady=(0, 20))
        
        why_title = tk.Label(self, text="Why Do We Choose In-Person Teaching?", 
                             font=("Georgia", 14, "bold"), bg="#edf0f2", fg="#0b1e33")
        why_title.pack(pady=(10, 10))
        
        benefits = [
            ("Deeper learning", "Direct interaction with teachers and peers increases student achievement.", "🧑‍🏫"),
            ("Practical experience", "In-person classes allow for dynamics that online teaching cannot replace.", "🎓"),
            ("Focus and discipline", "The physical environment reduces distractions and strengthens commitment.", "⚙️")
        ]
        
        for title, desc, icon in benefits:
            frame = tk.Frame(self, bg="#edf0f2")
            frame.pack(anchor="w", padx=50, pady=5)
            emoji = tk.Label(frame, text=icon, font=("Arial", 14), bg="#edf0f2")
            emoji.pack(side="left")
            text = tk.Label(frame, text=f"{title} – {desc}", font=("Helvetica", 11), bg="#edf0f2", wraplength=650, justify="left")
            text.pack(side="left", padx=(10, 0))
        
        human_contact = tk.Label(self, text="We believe that human contact is irreplaceable in education.",
                                 font=("Helvetica", 11, "italic"), bg="#edf0f2", fg="#0b1e33")
        human_contact.pack(pady=(20, 10))
        
        access_title = tk.Label(self, text="More Units, More Access", font=("Georgia", 14, "bold"), bg="#edf0f2", fg="#0b1e33")
        access_title.pack(pady=(20, 10))
        
        commitment = [
            "Bring quality education to more regions",
            "Offering a modern and welcoming structure",
            "Ensuring that cost is not a barrier"
        ]
        
        for item in commitment:
            frame = tk.Frame(self, bg="#edf0f2")
            frame.pack(anchor="w", padx=50, pady=2)
            diamond = tk.Label(frame, text="♦", font=("Arial", 12), bg="#edf0f2")
            diamond.pack(side="left")
            text = tk.Label(frame, text=item, font=("Helvetica", 11), bg="#edf0f2")
            text.pack(side="left", padx=(5, 0))
        
        join = tk.Label(self, text="Come be part of this journey", font=("Georgia", 16, "bold"), bg="#edf0f2", fg="#0b1e33")
        join.pack(pady=(30, 10))
        
        learn_more = tk.Label(self, text="Learn about our courses and find the unit closest to you!", 
                              font=("Helvetica", 11), bg="#edf0f2")
        learn_more.pack()
        
        btn_frame = tk.Frame(self, bg="#edf0f2")
        btn_frame.pack(pady=20)
        
        matriculate_btn = tk.Button(btn_frame, text="🟢 Matriculate Now", bg="#0b1e33", fg="white", font=("Helvetica", 11, "bold"))
        matriculate_btn.pack(side="left", padx=10)
        
        find_unit_btn = tk.Button(btn_frame, text="📍 Find a unit", bg="#7a8ea1", fg="white", font=("Helvetica", 11, "bold"))
        find_unit_btn.pack(side="left", padx=10)


class UserProfile(tk.Toplevel):
    def __init__(self, parent, user_name="Murillo"):
        super().__init__(parent)
        self.title("User Profile")
        self.geometry("900x700")
        self.configure(bg="#dfe8ea")

        # Header
        header = tk.Frame(self, bg="#0b1e33", height=60)
        header.pack(fill="x")

        tk.Label(header, text="Speak3Pro", font=("Georgia", 16, "bold"),
                 fg="white", bg="#0b1e33").pack(side="left", padx=20)

        for name in ["Courses", "Units", "About us", "My learning"]:
            tk.Button(header, text=name, bg="#0b1e33", fg="white", border=0,
                      font=("Helvetica", 10), activebackground="#1a2e52").pack(side="left", padx=8)

        search_frame = tk.Frame(header, bg="#0b1e33")
        search_frame.pack(side="right", padx=20)
        ttk.Entry(search_frame, width=20).pack(side="left", padx=(0, 5))
        ttk.Button(search_frame, text="Search").pack(side="left")

        tk.Button(header, text="Login", bg="#0b1e33", fg="white", borderwidth=1, relief="solid").pack(side="right", padx=5)
        tk.Button(header, text="Register", bg="#0b1e33", fg="white", borderwidth=1, relief="solid").pack(side="right", padx=5)

        # Main area
        main_frame = tk.Frame(self, bg="#91a3b0", bd=2, relief="groove")
        main_frame.pack(padx=40, pady=30, fill="both", expand=True)

        # Top section: Logo, back, search
        top_frame = tk.Frame(main_frame, bg="#91a3b0")
        top_frame.pack(fill="x", pady=10)

        tk.Button(top_frame, text="←", font=("Helvetica", 12), bg="#91a3b0", border=0).pack(side="left", padx=10)

        logo_label = tk.Label(top_frame, text="Speak3Pro", font=("Georgia", 18, "bold"), bg="#91a3b0", fg="white")
        logo_label.pack(side="left", padx=20)

        user_btn = tk.Button(top_frame, text="Me", bg="#b33e3e", fg="white", border=0, font=("Helvetica", 10, "bold"))
        user_btn.pack(side="right", padx=10, pady=10)

        bell_icon = tk.Label(top_frame, text="🔔", bg="#91a3b0")
        bell_icon.pack(side="right", padx=10)

        search_entry = ttk.Entry(top_frame, width=30)
        search_entry.pack(side="top", pady=10)

        # Greeting
        tk.Label(main_frame, text=f"Hello {user_name}", font=("Georgia", 20, "bold"), bg="#91a3b0", fg="white").pack(pady=10)
        tk.Label(main_frame, text="You are doing very well !!!", font=("Helvetica", 12), bg="#91a3b0", fg="white").pack(pady=5)

        # Graph (simulado com Canvas)
        graph_frame = tk.Frame(main_frame, bg="#91a3b0")
        graph_frame.pack(pady=10)

        graph_canvas = tk.Canvas(graph_frame, width=400, height=200, bg="white")
        graph_canvas.pack()

        # Simulação de gráfico
        skills = ["Listening", "Grammar", "Vocabulary", "Reading"]
        values = [24, 30, 35, 45]
        max_value = max(values)
        bar_width = 50

        for idx, (skill, value) in enumerate(zip(skills, values)):
            x0 = idx * (bar_width + 20) + 50
            y0 = 200 - (value / max_value) * 150
            x1 = x0 + bar_width
            y1 = 200
            graph_canvas.create_rectangle(x0, y0, x1, y1, fill="#324c70")
            graph_canvas.create_text(x0 + bar_width / 2, y0 - 10, text=f"{value}", font=("Helvetica", 8))
            graph_canvas.create_text(x0 + bar_width / 2, 210, text=skill, font=("Helvetica", 8))

        # Current courses
        tk.Label(main_frame, text="Current courses", font=("Georgia", 16, "bold"), bg="#91a3b0", fg="white").pack(pady=10)

        courses_frame = tk.Frame(main_frame, bg="#91a3b0")
        courses_frame.pack()

        # Dados de cursos
        courses = [
            ("🇺🇸", "English Course", "A2", "20/100 apprenticeship"),
            ("🇪🇸", "Spanish Course", "B1", "45/100 apprenticeship"),
            ("🇯🇵", "Japanese Course", "Level", "38/100 apprenticeship")
        ]

        for flag, title, level, progress in courses:
            self.create_course_card(courses_frame, flag, title, level, progress)

    def create_course_card(self, parent, flag, title, level, progress):
        card = tk.Frame(parent, bg="#943737", padx=10, pady=10, bd=2, relief="groove")
        card.pack(side="left", padx=10, pady=10)

        tk.Label(card, text=flag, font=("Arial", 20), bg="#943737", fg="white").pack(anchor="w")
        tk.Label(card, text=title, font=("Georgia", 12, "bold"), bg="#943737", fg="white").pack(anchor="w", pady=5)

        tk.Label(card, text=level, font=("Helvetica", 10, "bold"), bg="#943737", fg="white").pack(anchor="w")

        progress_label = tk.Label(card, text=progress, font=("Helvetica", 10), bg="#943737", fg="white")
        progress_label.pack(anchor="w", pady=5)

        ttk.Progressbar(card, length=120, value=int(progress.split("/")[0]), maximum=100).pack(anchor="w", pady=5)


class CoursesWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Courses")
        self.geometry("1024x720")
        self.configure(bg="#edf0f2")

        # Header
        header = tk.Frame(self, bg="#0b1e33", height=60)
        header.pack(fill="x")

        tk.Label(header, text="SpeakThreePro", font=("Georgia", 16, "bold"),
                 fg="white", bg="#0b1e33").pack(side="left", padx=20)

        for name in ["Courses", "Units", "About us", "My learning"]:
            tk.Button(header, text=name, bg="#0b1e33", fg="white", border=0,
                      font=("Helvetica", 10), activebackground="#1a2e52").pack(side="left", padx=8)

        search_frame = tk.Frame(header, bg="#0b1e33")
        search_frame.pack(side="right", padx=20)
        ttk.Entry(search_frame, width=20).pack(side="left", padx=(0, 5))
        ttk.Button(search_frame, text="Search").pack(side="left")

        tk.Button(header, text="Login", bg="#0b1e33", fg="white", borderwidth=1, relief="solid").pack(side="right", padx=5)
        tk.Button(header, text="Register", bg="#0b1e33", fg="white", borderwidth=1, relief="solid").pack(side="right", padx=5)

        # Main frame
        main_frame = tk.Frame(self, bg="#edf0f2")
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Sidebar filters
        sidebar = tk.Frame(main_frame, bg="#edf0f2", width=200)
        sidebar.pack(side="left", fill="y", padx=(0, 20))

        tk.Label(sidebar, text="Filter by", font=("Georgia", 14, "bold"), bg="#edf0f2", fg="#0b1e33").pack(anchor="w", pady=(0, 10))

        self.create_filter_section(sidebar, "Classification", ["★★★★★", "★★★★☆", "★★★☆☆", "★★☆☆☆", "★☆☆☆☆"])
        self.create_filter_section(sidebar, "Language", ["Brazil", "English", "French", "German", "Italian", "Japan", "Spain"])
        self.create_filter_section(sidebar, "Level", ["Beginner", "Intermediate", "Advanced", "All levels"])
        self.create_filter_section(sidebar, "Cost", ["Buy", "Free"])

        # Course list
        course_list_frame = tk.Frame(main_frame, bg="#edf0f2")
        course_list_frame.pack(side="left", fill="both", expand=True)

        # Scrollable canvas for courses
        canvas = tk.Canvas(course_list_frame, bg="#edf0f2", highlightthickness=0)
        scrollbar = ttk.Scrollbar(course_list_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#edf0f2")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Courses data
        courses = [
            ("🇺🇸", "English Course", "36 lessons\n4.5 hours in total\nTaboão da Serra - SP\nBasic Level", "4.1", "8650"),
            ("🇪🇸", "Spanish Course", "45 lessons\n6 hours in total\nEmbu das Artes - SP\nBasic Level", "3.7", "6255"),
            ("🇩🇪", "Germany Course", "50 lessons\n7.5 hours in total\nItapecerica da Serra - SP\nBasic Level", "3.8", "4372"),
            ("🇮🇹", "Italian Course", "25 lessons\n4 hours in total\nCampo Limpo - SP\nBasic Level", "4.2", "3243"),
            ("🇫🇷", "French Course", "75 lessons\n10 hours in total\nSão Paulo - SP\nBasic Level", "4.9", "7558"),
            ("🇧🇷", "Portuguese Course", "35 lessons\n4.5 hours in total\nTaboão da Serra - SP\nBasic Level", "1.7", "2355"),
            ("🇯🇵", "Japanese Course", "100 lessons\n20 hours in total\nCajueiro Redondo - SP\nBasic Level", "5.0", "8374"),
        ]

        for flag, title, desc, rating, students in courses:
            self.create_course_card(scrollable_frame, flag, title, desc, rating, students)

    def create_filter_section(self, parent, title, options):
        section = tk.Frame(parent, bg="#edf0f2")
        section.pack(anchor="w", pady=10, fill="x")
        tk.Label(section, text=title, font=("Georgia", 12, "bold"), bg="#edf0f2").pack(anchor="w", pady=5)

        for opt in options:
            cb = tk.Checkbutton(section, text=opt, bg="#edf0f2", anchor="w")
            cb.pack(anchor="w")

    def create_course_card(self, parent, flag, title, desc, rating, students):
        card = tk.Frame(parent, bg="white", bd=1, relief="solid", padx=10, pady=10)
        card.pack(fill="x", pady=5)

        flag_label = tk.Label(card, text=flag, font=("Arial", 40), bg="white")
        flag_label.pack(side="left", padx=10)

        info_frame = tk.Frame(card, bg="white")
        info_frame.pack(side="left", fill="both", expand=True)

        title_label = tk.Label(info_frame, text=title, font=("Georgia", 14, "bold"), bg="white")
        title_label.pack(anchor="w")

        desc_label = tk.Label(info_frame, text=desc, font=("Helvetica", 10), bg="white", justify="left")
        desc_label.pack(anchor="w", pady=5)

        rating_label = tk.Label(info_frame, text=f"{rating} ★ ({students})", font=("Helvetica", 10), bg="white")
        rating_label.pack(anchor="w")

        price_label = tk.Label(card, text="$17.90", font=("Helvetica", 12, "bold"), bg="white")
        price_label.pack(side="right", padx=10)


if __name__ == "__main__":
    app = HomePage()
    app.mainloop()
