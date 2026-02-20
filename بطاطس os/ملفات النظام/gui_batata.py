import tkinter as tk
from time import strftime

def start_batata_os():
    root = tk.Tk()
    root.title("Batata OS - Desktop Edition")
    root.geometry("800x500")

    # --- وظيفة الساعة ---
    def update_time():
        string = strftime('%H:%M:%S %p')
        clock_label.config(text=string)
        clock_label.after(1000, update_time)

    # --- إضافة صورة خلفية (اختياري) ---
    # إذا كان لديك صورة، قم بإلغاء التعليق عن الأسطر التالية:
    # try:
    #     bg_image = tk.PhotoImage(file="potato_bg.png")
    #     bg_label = tk.Label(root, image=bg_image)
    #     bg_label.place(relwidth=1, relheight=1)
    # except:
    #     root.configure(bg="#D2B48C") # لو لم توجد صورة، استعمل اللون البني

    # شريط المهام السفلي (Taskbar)
    taskbar = tk.Frame(root, bg="#3e2723", height=40)
    taskbar.pack(side="bottom", fill="x")

    # الساعة في شريط المهام
    clock_label = tk.Label(taskbar, font=('Arial', 12, 'bold'), bg="#3e2723", fg="white")
    clock_label.pack(side="right", padx=10)
    update_time()

    # زر "ابدأ" (البطاطسة الكبيرة)
    def start_menu():
        print("قائمة ابدأ مفتوحة!")
        
    start_btn = tk.Button(taskbar, text="🥔 Start", command=start_menu, bg="#FFD700", font=("Arial", 10, "bold"))
    start_btn.pack(side="left", padx=5)

    # أيقونة تجريبية على سطح المكتب
    def open_folder():
        print("فتح مجلد الصور...")

    folder_btn = tk.Button(root, text="📁 ملفات النشا", command=open_folder, 
                           bg="white", relief="flat", padx=10)
    folder_btn.place(x=20, y=20)

    root.mainloop()

if __name__ == "__main__":
    start_batata_os()
