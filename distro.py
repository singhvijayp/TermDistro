import time, os, sys
# Coded by github.com/singhvijayp
# Copy with credits

# code
os.system("clear")
time.sleep(2)

# colors
R="\033[91m"
G="\033[92m"

# code
print("\033[1;36mPlease Wait... Installing Requirements.")
time.sleep(3)
os.system("apt install python git -y")
time.sleep(2)
print(" ")
print("\033[0;0m Setup Finished... Launching the tool...")
time.sleep(2)
os.system("clear")

print (R+"""
     .___..___.__ .  ..__ ._. __..___..__ .__.
       |  [__ [__)|\/||  \ | (__   |  [__)|  |
       |  [___|  \|  ||__/_|_.__)  |  |  \|__|
                 """+G+"""   Dev: @singhvijayp """)
time.sleep(2)
print("\033[92m 1. Kali Linux ")
print(" 2. Parrot ")
print(" 3. Arch")
print(" 4. Kali Nethunter ")
print(" 5. Backbox")
print(" 6. Alpine")
print(" 7. Opensuse-tumbelweed ")
print(" 8. Black Arch")
print(" 9. Opensuse-leap ")
print(" 10. Ubuntu")
print(" 11. Debian ")
print(" 12. Fedora ")
print(" 13. Centos \033[0m ")
op = input("\033[1;33mChoose your desired O.S : ")
if op == "1" :
   print("\033[91m Installing kali... \033[0m")
   os.system("cd ~")
   time.sleep(1.5)
   os.system("apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh")
elif op == "2" :
   print("\033[91m Installing Parrot... \033[0m")
   os.system("cd ~")
   time.sleep(1.5)
   os.system("apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Parrot/parrot.sh && bash parrot.sh")
elif op == "3" :
   print("\033[91m Installing Arch... \033[0m ")
   os.system("cd ~")
   time.sleep(1.5)
   os.system("apt install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Arch/armhf/arch.sh && bash arch.sh ")
elif op == "4" :
   print("\033[91m Installing Nethunter... \033[0m")
   os.system("cd ~")
   time.sleep(1.5)
   os.system("apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Nethunter/nethunter.sh && bash nethunter.sh")
elif op == "5" :
   print("\033[91m Installing Blackbox.. \033[0m")
   os.system("cd ~")
   time.sleep(1.5)
   os.system("apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/BackBox/backbox.sh && bash backbox.sh")
elif op == "6" :
   print("\033[91m Installing Alpine... \033[0m")
   os.system("cd ~")
   time.sleep(1.5)
   os.system("apy install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Alpine/alpine.sh && bash alpine.sh")
elif op == "7" :
   print("\033[91m Installing tumbelweed... \033[0m")
   os.system("cd ~")
   time.sleep(1.5)
   os.system("apt install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Tumbleweed/opensuse-tumbleweed.sh && bash opensuse-tumbleweed.sh")
elif op == "8" :
   print("\033[91m Installing black arch... \033[0m")
   os.system("cd ~")
   time.sleep(1.5)
   os.system("pacman-key --init && pacman-key --populate archlinuxarm && pacman -Sy --noconfirm curl && curl -O https://blackarch.org/strap.sh && chmod +x strap.sh && ./strap.sh")
elif op == "9" :
   print("\033[91m Installing opensuse-leap... \033[0m ")
   os.system("cd ~")
   time.sleep(1.5)
   os.system("apt install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Leap/opensuse-leap.sh && bash opensuse-leap.sh")
elif op == "10" :
   print("\033[91m Installing Ubuntu...\033[0m")
   os.system("cd ~")
   time.sleep(1.5)
   os.system("apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh")
elif op == "11" :
   print("\033[91m Installing Debian... \033[0m ")
   os.system("cd")
   time.sleep(1.5)
   o9s.system("apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh")
elif op == "12" :
   print("\033[91m Installing Fedora... \033[0m ")
   os.system("cd")
   time.sleep(1.5)
   os.system("apt install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Fedora/fedora.sh && bash fedora.sh")
elif op == "13" :
   print("\033[91m Installing centos... \033[0m ")
   os.system("cd")
   time.sleep(1.5)
   os.system("apt install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh && bash centos.sh")
else :
   print(" Enter a valid option... ")
