# Importing Libraries
import ttkbootstrap as ttk
from appCode.config import AppConfig 
from PIL import ImageTk

class MhabPortal(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title(AppConfig.title)
        self.master.geometry(f"{master.winfo_screenwidth()}x{master.winfo_screenheight()}")
        self.master.configure(bg=AppConfig.primary_white_color)


if __name__ == "__main__":
    # Initilise application window
    root = ttk.Window()
    portal_app = MhabPortal(root)

    root.mainloop()
