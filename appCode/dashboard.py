import ttkbootstrap as ttk
from appCode.config import AppConfig

class Dashboard(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.winfo_toplevel().title(AppConfig.title + " | Dashboard")
        self.winfo_toplevel().geometry(f"{int(master.winfo_screenwidth() * AppConfig.initial_window_scale)}x{int(master.winfo_screenheight() * AppConfig.initial_window_scale)}")

        # Configure the style for the dashboard frame
        style = ttk.Style()
        style.configure(
            "Dashboard.TFrame",
            background=AppConfig.primary_black_color,
        )

        self.configure(style="Dashboard.TFrame")

        ttk.Label(
            self,
            text="Dashboard",
            font=("Arial", 24),
            background=AppConfig.primary_black_color,
            foreground=AppConfig.primary_white_color
        ).pack(pady=20)

        ttk.Button(
            self,
            text="Go to Login",
            command=self.go_to_login
        ).pack(pady=10)

    def go_to_login(self):
        self.master.show_page("login")