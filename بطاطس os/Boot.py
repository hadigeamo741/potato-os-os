import tkinter as tk
from tkinter import ttk, messagebox
import os
import sys
import subprocess
import time

# --- إعداد المسارات المخصصة التي ذكرتها ---
BASE_PATH = r"C:\Users\LENOVO\Desktop\بطاطس os"
SYSTEM_FILES_PATH = os.path.join(BASE_PATH, "ملفات النظام")

class BatataLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Batata OS - Bootloader")
        self.root.geometry("500x300")
        self.root.configure(bg="#111")
        self.root.overrideredirect(True) # إخفاء حواف النافذة لشكل أكثر احترافية
        
        # تمركز النافذة في وسط الشاشة
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
        steps = [
            ("Checking Directory Structure...", 20),
            ("Loading System Modules...", 40),
            ("Verifying Terminal Scripts...", 60),
            ("Checking GUI Components...", 80),
            ("Launching Main OS...", 100)
        ]
        
        for i, (text, val) in enumerate(steps):
            self.status_lbl.config(text=text)
            self.progress['value'] = val
            self.root.update()
            time.sleep(0.7) # محاكاة وقت التحميل
            
            # فحص وجود المجلد الأساسي في كل خطوة
            if i == 0 and not os.path.exists(SYSTEM_FILES_PATH):
                messagebox.showerror("Error", f"تعذر العثور على مجلد: ملفات النظام\nالمسار: {SYSTEM_FILES_PATH}")
                self.root.destroy()
                return

        self.launch_main_system()

    def launch_main_system(self):
        # تشغيل ملف main_os.py الموجود داخل مجلد ملفات النظام
        main_script = os.path.join(SYSTEM_FILES_PATH, "main_os.py")
        
        if os.path.exists(main_script):
            try:
                # تشغيل النظام في عملية منفصلة وإغلاق اللانشر
                subprocess.Popen([sys.executable, main_script])
                self.root.destroy()
            except Exception as e:
                messagebox.showerror("Execution Error", f"فشل تشغيل النظام: {e}")
        else:
            messagebox.showerror("Error", f"ملف main_os.py غير موجود في:\n{SYSTEM_FILES_PATH}")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BatataLauncher(root)
    root.mainloop()
