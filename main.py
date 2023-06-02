import subprocess

def change_mac_address():
    interface = "eth0"  # اسم الواجهة التي تريد تغيير عنوان MAC الخاص بها
    new_mac = "00:11:22:33:44:55"  # العنوان الماك الجديد الذي ترغب في استخدامه

    # إيقاف واجهة الشبكة
    subprocess.call(["ifconfig", interface, "down"])

    # تغيير عنوان MAC
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

    # تشغيل واجهة الشبكة
    subprocess.call(["ifconfig", interface, "up"])

# استدعاء الدالة عند إعادة التشغيل
change_mac_address()
