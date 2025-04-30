import qrcode
from termcolor import colored
import pyfiglet
import os
os.system("clear")
banner = pyfiglet.figlet_format("ScanicToxin", font="poison")


print(colored(banner, "red", attrs=["bold"]))

print(colored(f"Tools Name  : \033[45mScanic Toxin\033[0m", attrs=["bold"]))
print(colored(f"Author      : \033[46mXERATHIL\033[0m", attrs=["bold"]))
print(colored(f"YouTube     :https://YouTube.com/@xerathil", "red", attrs=["bold"]))
print(colored("=======================================================", "green", attrs=["bold"]))





user = input(colored("[~] Enter Your Phishing Link/Data: ", "yellow", attrs=["bold"]))

img = qrcode.make(user)

img.save("/storage/emulated/0/phishing_Qr.png")

print(colored("\033[42m~Your Qr Code Created Successfully in Your Internal Storage\nImg Name:phishing_Qr.png\033[0m", attrs=["bold"]))

os.system("xdg-open https://youtube.com/@xerathil?si=ypSv6hyl4yJKGlTH")
