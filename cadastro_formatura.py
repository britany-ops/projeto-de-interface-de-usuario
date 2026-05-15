import tkinter as tk
from tkinter import ttk, messagebox


class AppVanGogh(tk.Tk):
    def __init__(self):
        super().__init__()

        # ---------------- JANELA ----------------
        self.title("Galeria Van Gogh")
        self.geometry("920x680")
        self.configure(bg="#1B263B")
        self.resizable(False, False)

        # ---------------- PALETA VAN GOGH ----------------
        # Inspirada em Noite Estrelada
        self.bg_color = "#1B263B"        # Azul escuro
        self.card_color = "#243B55"      # Azul profundo
        self.gold = "#F4B942"            # Dourado estrelado
        self.light_gold = "#FFD166"      # Amarelo claro
        self.text_color = "#F8F1E5"      # Creme claro
        self.input_bg = "#324A5F"        # Azul suave
        self.border = "#4F6D7A"
        self.muted = "#C9C9C9"

        # ---------------- ESTILO COMBOBOX ----------------
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "TCombobox",
            fieldbackground=self.input_bg,
            background=self.card_color,
            foreground=self.text_color,
            bordercolor=self.gold,
            arrowcolor=self.gold,
            padding=6
        )

        self.create_widgets()

    def create_widgets(self):

        # ---------------- CABEÇALHO ----------------
        header = tk.Frame(self, bg=self.bg_color)
        header.pack(fill="x", pady=(35, 20))

        title = tk.Label(
            header,
            text="GALERIA IMERSIVA",
            font=("Georgia", 13, "bold"),
            bg=self.bg_color,
            fg=self.light_gold
        )
        title.pack()

        subtitle = tk.Label(
            header,
            text="VAN GOGH EXPERIENCE",
            font=("Georgia", 34, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        subtitle.pack(pady=(5, 0))

        line = tk.Frame(
            header,
            bg=self.gold,
            width=140,
            height=3
        )
        line.pack(pady=15)

        desc = tk.Label(
            header,
            text="Cadastro para visitação das pinturas clássicas de Vincent van Gogh",
            font=("Segoe UI", 11),
            bg=self.bg_color,
            fg=self.muted
        )
        desc.pack()

        # ---------------- CARD PRINCIPAL ----------------
        card = tk.Frame(
            self,
            bg=self.card_color,
            bd=0
        )
        card.pack(
            padx=90,
            pady=20,
            fill="both",
            expand=True
        )

        # ---------------- FUNÇÃO INPUT ----------------
        def create_input(parent, text, row, col, width=30):

            lbl = tk.Label(
                parent,
                text=text,
                font=("Georgia", 10, "bold"),
                bg=self.card_color,
                fg=self.light_gold
            )
            lbl.grid(
                row=row,
                column=col,
                sticky="w",
                padx=20,
                pady=(18, 0)
            )

            entry = tk.Entry(
                parent,
                font=("Segoe UI", 13),
                bg=self.input_bg,
                fg=self.text_color,
                insertbackground=self.gold,
                relief="flat",
                width=width,
                highlightthickness=1,
                highlightbackground=self.border,
                highlightcolor=self.gold
            )

            entry.grid(
                row=row + 1,
                column=col,
                sticky="we",
                padx=20,
                pady=(6, 8),
                ipady=9
            )

            return entry

        # ---------------- CAMPOS ----------------
        self.ent_nome = create_input(card, "NOME COMPLETO", 0, 0, 35)
        self.ent_cpf = create_input(card, "CPF / DOCUMENTO", 0, 1, 25)

        self.ent_email = create_input(card, "E-MAIL", 2, 0, 35)
        self.ent_telefone = create_input(card, "TELEFONE", 2, 1, 25)

        # ---------------- COMBOBOX ----------------
        lbl_tipo = tk.Label(
            card,
            text="EXPERIÊNCIA ESCOLHIDA",
            font=("Georgia", 10, "bold"),
            bg=self.card_color,
            fg=self.light_gold
        )
        lbl_tipo.grid(
            row=4,
            column=0,
            sticky="w",
            padx=20,
            pady=(18, 0)
        )

        self.combo_tipo = ttk.Combobox(
            card,
            values=[
                "Noite Estrelada",
                "Girassóis",
                "Quarto em Arles",
                "Campo de Trigo",
                "Auto Retratos"
            ],
            font=("Segoe UI", 12),
            state="readonly"
        )

        self.combo_tipo.grid(
            row=5,
            column=0,
            sticky="we",
            padx=20,
            pady=(6, 10)
        )

        self.combo_tipo.set("Noite Estrelada")

        # Cores do menu dropdown
        self.option_add('*TCombobox*Listbox.background', self.input_bg)
        self.option_add('*TCombobox*Listbox.foreground', self.text_color)
        self.option_add('*TCombobox*Listbox.selectBackground', self.gold)
        self.option_add('*TCombobox*Listbox.selectForeground', "#000000")

        # Grid
        card.columnconfigure(0, weight=1)
        card.columnconfigure(1, weight=1)

        # ---------------- BOTÃO ----------------
        btn_frame = tk.Frame(self, bg=self.bg_color)
        btn_frame.pack(pady=(10, 35))

        def on_enter(e):
            self.btn.config(bg="#FFD166")

        def on_leave(e):
            self.btn.config(bg=self.gold)

        self.btn = tk.Button(
            btn_frame,
            text="CONFIRMAR VISITA",
            font=("Georgia", 12, "bold"),
            bg=self.gold,
            fg="#1B263B",
            activebackground="#FFD166",
            activeforeground="#1B263B",
            relief="flat",
            cursor="hand2",
            padx=45,
            pady=14,
            command=self.cadastrar
        )

        self.btn.pack()

        self.btn.bind("<Enter>", on_enter)
        self.btn.bind("<Leave>", on_leave)

        # ---------------- STATUS ----------------
        self.status_lbl = tk.Label(
            self,
            text="",
            font=("Segoe UI", 11),
            bg=self.bg_color,
            fg=self.light_gold
        )
        self.status_lbl.pack()

    # ---------------- FUNÇÃO CADASTRO ----------------
    def cadastrar(self):

        nome = self.ent_nome.get()
        obra = self.combo_tipo.get()

        if not nome:
            messagebox.showwarning(
                "Atenção",
                "Preencha o nome do visitante!",
                parent=self
            )
            return

        self.status_lbl.config(
            text="Preparando sua experiência artística..."
        )

        self.update()
        self.after(700)

        primeiro_nome = nome.split()[0]

        self.status_lbl.config(
            text=f"✓ Entrada confirmada! Bem-vindo(a), {primeiro_nome}. Aproveite a obra '{obra}'.",
            fg=self.light_gold
        )

        # Limpar campos
        self.ent_nome.delete(0, tk.END)
        self.ent_cpf.delete(0, tk.END)
        self.ent_email.delete(0, tk.END)
        self.ent_telefone.delete(0, tk.END)

        self.combo_tipo.set("Noite Estrelada")

        self.ent_nome.focus()


# ---------------- EXECUÇÃO ----------------
if __name__ == "__main__":
    app = AppVanGogh()
    app.mainloop()