import tkinter as tk
from tkinter import messagebox, ttk
import os
import subprocess
from time import strftime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class BatataOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Batata OS Pro")
        self.root.state('zoomed') # تشغيل فول سكرين
        self.root.configure(bg="#1a1a1a")
        
        self.start_menu = None # متغير لتخزين نافذة القائمة
        
        self.setup_ui()

    def setup_ui(self):
        # --- 1. الأيقونات الذكية ---
        self.create_smart_icon("Terminal", "📟", 0.08, 0.1, self.open_terminal, "#00FF00")
        self.create_smart_icon("Browser", "🌐", 0.08, 0.25, self.open_browser, "#4285F4")
        self.create_smart_icon("Files", "📁", 0.08, 0.40, lambda: os.startfile(BASE_DIR), "#F1C40F")

        # --- 2. شريط المهام ---
        self.taskbar = tk.Frame(self.root, bg="#111111", height=50)
        self.taskbar.pack(side="bottom", fill="x")

        # زر ابدأ
        self.start_btn = tk.Button(self.taskbar, text="🥔 Start", font=("Arial", 11, "bold"),
                                  bg="#FFD700", fg="black", padx=20, bd=0, 
                                  command=self.toggle_start_menu)
        self.start_btn.pack(side="left", padx=10, pady=5)

        # الساعة
        self.clock_lbl = tk.Label(self.taskbar, font=('Arial', 11, 'bold'), bg="#111111", fg="white")
        self.clock_lbl.pack(side="right", padx=20)
        self.update_clock()

    def toggle_start_menu(self):
        # إذا كانت القائمة موجودة، احذفها
        if self.start_menu and self.start_menu.winfo_exists():
            self.start_menu.destroy()
            self.start_menu = None
        else:
            # إنشاء القائمة كـ Toplevel
            self.start_menu = tk.Toplevel(self.root)
            self.start_menu.overrideredirect(True) # بدون حواف
            self.start_menu.configure(bg="#1e1e1e", bd=2, relief="flat")
            
            # حساب الأبعاد والموقع (فوق التاسك بار بالضبط)
            screen_height = self.root.winfo_height()
            self.start_menu.geometry(f"300x400+5+{screen_height - 455}")
            
            # التأكد من ظهورها فوق كل شيء
            self.start_menu.attributes("-topmost", True)
            
            # محتويات القائمة
            tk.Label(self.start_menu, text="BATATA OS MENU", bg="#FFD700", fg="black", 
                     font=("Arial", 10, "bold"), pady=10).pack(fill="x")
            
            def add_item(text, icon, cmd):
                tk.Button(self.start_menu, text=f"{icon} {text}", bg="#1e1e1e", fg="white",
                          font=("Arial", 11), bd=0, anchor="w", padx=20, pady=10,
                          activebackground="#333", command=lambda: [cmd(), self.toggle_start_menu()]).pack(fill="x")

            add_item("Terminal", "📟", self.open_terminal)
            add_item("Browser", "🌐", self.open_browser)
            add_item("Settings", "⚙️", lambda: print("Settings"))
            tk.Frame(self.start_menu, bg="#333", height=1).pack(fill="x", pady=10)
            add_item("Shutdown", "🔴", self.root.destroy)

    # --- وظائف مساعدة ---
    def create_smart_icon(self, name, icon, relx, rely, command, color):
        btn = tk.Button(self.root, text=icon, font=("Arial", 35), bg="#1a1a1a", fg=color, 
                        bd=0, cursor="hand2", activebackground="#333", command=command)
        btn.place(relx=relx, rely=rely, anchor="center")
        lbl = tk.Label(self.root, text=name, font=("Arial", 11, "bold"), bg="#1a1a1a", fg="white")
        lbl.place(relx=relx, rely=rely + 0.07, anchor="center")

    def open_terminal(self):
        bat_file = os.path.join(BASE_DIR, "batata_term.bat")
        if os.path.exists(bat_file):
            subprocess.Popen(['cmd.exe', '/k', bat_file], creationflags=subprocess.CREATE_NEW_CONSOLE)

    def open_browser(self):
        webbrowser.open("https://www.google.com")

    def update_clock(self):
        self.clock_lbl.config(text=strftime('%I:%M %p'))
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    import webbrowser
    root = tk.Tk()
    app = BatataOS(root)
    root.mainloop()
