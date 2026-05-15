import tkinter as tk


class SearchApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuração da janela
        self.title("Britney Search")
        self.geometry("850x550")
        self.configure(bg="#EDE7E3")
        self.minsize(500, 350)

        # Frame principal
        main_frame = tk.Frame(self, bg="#F8F5F2")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # ---------------- TÍTULO ----------------
        title_frame = tk.Frame(main_frame, bg="#F8F5F2")
        title_frame.pack(pady=(0, 35))

        # Cores suaves e elegantes
        colors = [
            "#7C6A9A",
            "#B08BBB",
            "#C9ADA7",
            "#A26769",
            "#6D597A",
            "#9A8C98",
            "#7F5539"
        ]

        text = "Britney"

        for i, char in enumerate(text):
            tk.Label(
                title_frame,
                text=char,
                font=("Georgia", 54, "bold"),
                fg=colors[i],
                bg="#F8F5F2"
            ).pack(side="left")

        # ---------------- BARRA DE PESQUISA ----------------
        search_container = tk.Frame(
            main_frame,
            bg="#FFFFFF",
            bd=0
        )
        search_container.pack(ipadx=12, ipady=8)

        # Sombra suave
        shadow = tk.Frame(
            search_container,
            bg="#D8D2CC",
            padx=1,
            pady=1
        )
        shadow.pack()

        search_frame = tk.Frame(
            shadow,
            bg="#FFFFFF",
            padx=10,
            pady=5
        )
        search_frame.pack()

        # Ícone lupa
        search_icon = tk.Label(
            search_frame,
            text="🔍",
            bg="#FFFFFF",
            fg="#8D8D8D",
            font=("Segoe UI Emoji", 14)
        )
        search_icon.pack(side="left", padx=(5, 8))

        # Placeholder
        self.placeholder_text = "Digite sua dúvida..."
        self.search_var = tk.StringVar()

        # Entrada
        self.search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=("Arial", 14),
            width=42,
            bd=0,
            bg="#FFFFFF",
            fg="#9A9A9A",
            insertbackground="#5C5470"
        )

        self.search_entry.pack(side="left", pady=6)

        self.search_entry.insert(0, self.placeholder_text)

        # Ícone microfone
        mic_icon = tk.Label(
            search_frame,
            text="🎙",
            bg="#FFFFFF",
            fg="#8D8D8D",
            font=("Segoe UI Emoji", 14)
        )
        mic_icon.pack(side="right", padx=(8, 5))

        # Eventos
        self.search_entry.bind("<FocusIn>", self.on_entry_click)
        self.search_entry.bind("<FocusOut>", self.on_focus_out)
        self.search_entry.bind("<Return>", self.perform_search)

        # ---------------- BOTÕES ----------------
        buttons_frame = tk.Frame(main_frame, bg="#F8F5F2")
        buttons_frame.pack(pady=30)

        # Estilo dos botões
        button_style = {
            "font": ("Arial", 11),
            "bg": "#D8CFC4",
            "fg": "#4A4A4A",
            "activebackground": "#CBBFB3",
            "activeforeground": "#2E2E2E",
            "relief": "flat",
            "cursor": "hand2",
            "padx": 18,
            "pady": 9,
            "bd": 0
        }

        search_button = tk.Button(
            buttons_frame,
            text="Pesquisar",
            command=self.perform_search,
            **button_style
        )
        search_button.pack(side="left", padx=10)

        lucky_button = tk.Button(
            buttons_frame,
            text="Estou com sorte",
            **button_style
        )
        lucky_button.pack(side="left", padx=10)

    # ---------------- FUNÇÕES ----------------

    def on_entry_click(self, event):
        if self.search_entry.get() == self.placeholder_text:
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(fg="#333333")

    def on_focus_out(self, event):
        if self.search_entry.get() == "":
            self.search_entry.insert(0, self.placeholder_text)
            self.search_entry.config(fg="#9A9A9A")

    def perform_search(self, event=None):
        query = self.search_entry.get()

        if query and query != self.placeholder_text:
            print(f"Buscando por: {query}")


# Inicialização
if __name__ == "__main__":
    app = SearchApp()
    app.mainloop()