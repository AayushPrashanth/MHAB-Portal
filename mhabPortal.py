# Importing Libraries
import ttkbootstrap as ttk
from appCode.config import AppConfig 
from appCode.login import LoginPage
from appCode.dashboard import Dashboard 

class MhabPortal(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title(AppConfig.title)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.pages = {
            "login": LoginPage(self),
            "dashboard": Dashboard(self)
        }

        for page in self.pages.values():
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page("login")

    def show_page(self, pageName):
        page = self.pages[pageName]
        page.tkraise()


if __name__ == "__main__":
    # Initilise application window
    root = ttk.Window()
    portal_app = MhabPortal(root)
    portal_app.pack(fill="both", expand=True)

    root.mainloop()
