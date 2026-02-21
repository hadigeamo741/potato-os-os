import tkinter as tk
from tkinter import ttk, messagebox
import os
import sys
import subprocess
import time

# --- جعل المسارات ديناميكية (تشتغل عند أي حد) ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# البحث عن مجلد "ملفات النظام" في نفس مكان هذا الملف
SYSTEM_FILES_PATH = os.path.join(BASE_DIR, "ملفات النظام")

class BatataLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Batata OS - Bootloader")
        self.root.geometry("500x300")
        self.root.configure(bg="#111")
        self.root.overrideredirect(True)
        
        # تمركز النافذة
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (500 // 2)
        y = (screen_height // 2) - (300 // 2)
        self.root.geometry(f"500x300+{x}+{y}")

        self.setup_ui()
        self.root.after(500, self.start_check_sequence)

    def setup_ui(self):
        tk.Label(self.root, text="🥔 BATATA OS", font=("Arial", 24, "bold"), fg="gold", bg="#111").pack(pady=40)
        self.status_lbl = tk.Label(self.root, text="Initializing Bootloader...", fg="white", bg="#111", font=("Arial", 10))
        self.status_lbl.pack(pady=10)
        
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=20)

    def start_check_sequence(self):
        # مصفوفة الفحص
        checks = [
            ("Verifying System Directory...", 30),
            ("Checking Main Kernel...", 60),
            ("Preparing APScell Environment...", 90),
            ("Starting Batata OS...", 100)
        ]
        
        for text, val in checks:
            self.status_lbl.config(text=text)
            self.progress['value'] = val
            self.root.update()
            time.sleep(0.6)
            
            if val == 30 and not os.path.exists(SYSTEM_FILES_PATH):
                messagebox.showerror("Error", "Critical: 'ملفات النظام' folder not found!")
                self.root.destroy()
                return

        self.launch_main_system()

    def launch_main_system(self):
        main_script = os.path.join(SYSTEM_FILES_PATH, "main_os.py")
        if os.path.exists(main_script):
            try:
                # تشغيل النظام باستدعاء مفسر بايثون الحالي
                subprocess.Popen([sys.executable, main_script])
                self.root.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to launch: {e}")
        else:
            messagebox.showerror("Error", "main_os.py is missing!")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BatataLauncher(root)
    root.mainloop()
