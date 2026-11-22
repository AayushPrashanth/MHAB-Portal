import ttkbootstrap as ttk
from appCode.config import AppConfig

class LoginPage(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.winfo_toplevel().title(AppConfig.title + " | Login")
        self.winfo_toplevel().geometry(f"{int(master.winfo_screenwidth() * AppConfig.initial_window_scale)}x{int(master.winfo_screenheight() * AppConfig.initial_window_scale)}")

        # Configure the style for the login frame
        style = ttk.Style()
        style.configure(
            "Login.TFrame",
            background=AppConfig.primary_white_color,
        )
        self.configure(style="Login.TFrame")

        style.configure(
            "Login.TButton",
            font=(AppConfig.default_font, AppConfig.medium_font_size),
            background=AppConfig.primary_black_color,
            foreground=AppConfig.primary_white_color
        )

        # Login Page Title 
        ttk.Label(
            self, 
            text="Login Page", 
            font=(AppConfig.default_font, AppConfig.large_font_size), 
            background=AppConfig.primary_white_color
        ).pack(pady=40)

        # Username Label and Entry
        ttk.Label(
            self,
            text = "Username:",
            font=(AppConfig.default_font, AppConfig.medium_font_size),
            background=AppConfig.primary_white_color,
            foreground=AppConfig.primary_black_color
        ).pack(pady=5)

        self.usernameEntry = ttk.Entry(
            self,
            font=(AppConfig.default_font, AppConfig.medium_font_size),
            width=30
        ).pack(pady=5)

        # Password Label and Entry
        ttk.Label(
            self,
            text="Password:",
            font=(AppConfig.default_font, AppConfig.medium_font_size),
            background=AppConfig.primary_white_color,
            foreground=AppConfig.primary_black_color
        ).pack(pady=5)

        self.passwordEntry = ttk.Entry(
            self,
            font=(AppConfig.default_font, AppConfig.medium_font_size),
            width=30,
            show="*"
        ).pack(pady=5)

        # Login Button
        ttk.Button(
            self,
            text="Login",
            style="Login.TButton",
            command=self.go_to_dashboard
        ).pack(pady=5)

    def go_to_dashboard(self):
        self.master.show_page("dashboard")