import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import webbrowser
from time import strftime

# --- تحديد المسارات بشكل ديناميكي داخل المجلد ---
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# نفترض وجود مجلد Assets داخل ملفات النظام للصور
ASSETS_PATH = os.path.join(CURRENT_DIR, "Assets")

class BatataOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Batata OS Pro - GitHub Edition")
        self.root.state('zoomed')
        self.root.configure(bg="#1a1a1a")
        self.start_menu = None
        self.setup_ui()

    def setup_ui(self):
        # محاولة تحميل الخلفية
        try:
            bg_path = os.path.join(ASSETS_PATH, "wallpaper.png")
            if os.path.exists(bg_path):
                self.bg_img = tk.PhotoImage(file=bg_path)
                tk.Label(self.root, image=self.bg_img).place(relwidth=1, relheight=1)
        except: pass

        # أيقونات سطح المكتب (النسب المئوية تضمن ثباتها في GitHub للكل)
        self.create_icon("Terminal", "📟", 0.08, 0.15, self.open_terminal, "#00FF00")
        self.create_icon("Browser", "🌐", 0.08, 0.30, self.open_browser, "#4285F4")
        self.create_icon("System", "📁", 0.08, 0.45, lambda: os.startfile(CURRENT_DIR), "#F1C40F")

        # شريط المهام
        taskbar = tk.Frame(self.root, bg="#111", height=50)
        taskbar.pack(side="bottom", fill="x")

        tk.Button(taskbar, text="🥔 Start", font=("Arial", 11, "bold"), bg="#FFD700", 
                  bd=0, padx=20, command=self.toggle_start_menu).pack(side="left", padx=10, pady=5)

        self.clock_lbl = tk.Label(taskbar, font=('Arial', 11), bg="#111", fg="white")
        self.clock_lbl.pack(side="right", padx=20)
        self.update_clock()

    def create_icon(self, name, icon, relx, rely, cmd, color):
        btn = tk.Button(self.root, text=icon, font=("Arial", 35), bg="#1a1a1a", fg=color, 
                        bd=0, cursor="hand2", activebackground="#333", command=cmd)
        btn.place(relx=relx, rely=rely, anchor="center")
        tk.Label(self.root, text=name, font=("Arial", 10, "bold"), bg="#1a1a1a", fg="white").place(relx=relx, rely=rely+0.07, anchor="center")

    def toggle_start_menu(self):
        if self.start_menu and self.start_menu.winfo_exists():
            self.start_menu.destroy()
            self.start_menu = None
        else:
            self.start_menu = tk.Toplevel(self.root)
            self.start_menu.overrideredirect(True)
            self.start_menu.configure(bg="#1e1e1e", bd=1, relief="solid")
            h = self.root.winfo_height()
            self.start_menu.geometry(f"280x400+5+{h-455}")
            self.start_menu.attributes("-topmost", True)
            
            tk.Label(self.start_menu, text="BATATA MENU", bg="#333", fg="gold", pady=10).pack(fill="x")
            items = [("Terminal", "📟", self.open_terminal), ("Browser", "🌐", self.open_browser)]
            for text, icon, cmd in items:
                tk.Button(self.start_menu, text=f"{icon} {text}", bg="#1e1e1e", fg="white", bd=0, 
                          anchor="w", padx=20, pady=10, command=lambda c=cmd:[c(), self.start_menu.destroy()]).pack(fill="x")
            
            tk.Button(self.start_menu, text="🔴 Shutdown", bg="#1e1e1e", fg="red", bd=0, command=self.root.destroy).pack(fill="x", side="bottom")

    def open_terminal(self):
        # البحث عن ملف الباتش في نفس مجلد main_os
        term_path = os.path.join(CURRENT_DIR, "batata_term.bat")
        if os.path.exists(term_path):
            subprocess.Popen(['cmd.exe', '/k', term_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:
            messagebox.showerror("System Error", "Terminal Script missing!")

    def open_browser(self):
        webbrowser.open("https://www.google.com")

    def update_clock(self):
        self.clock_lbl.config(text=strftime('%I:%M %p'))
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    app = BatataOS(root)
    root.mainloop()
