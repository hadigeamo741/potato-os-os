import os
import platform

def batata_os():
    print("-----------------------------------")
    print("      مرحباً بكم في نظام بطاطس OS      ")
    print("   أول نظام تشغيل كربوهيدراتي في العالم  ")
    print("-----------------------------------")
    
    while True:
        # مكان إدخال الأوامر
        command = input("Batata_User > ").strip().lower()

        if command == "exit":
            print("إغلاق نظام بطاطس... وداعاً!")
            break
        
        elif command == "help":
            print("الأوامر المتاحة:")
            print("- info: معلومات النظام")
            print("- fry: تحويل الملفات إلى بطاطس مقلية (مزحة)")
            print("- hello: ترحيب")
            print("- exit: الخروج")

        elif command == "info":
            print(f"النظام يعمل على: {platform.system()}")
            print("الإصدار: 1.0.0 (نسخة النشا)")

        elif command == "hello":
            print("أهلاً بك! نظام بطاطس يتمنى لك يوماً سعيداً.")

        else:
            print("عذراً، هذا الأمر غير موجود في قاموس البطاطس.")

if __name__ == "__main__":
    batata_os()
