import os
import time
from colorama import init, Fore, Style
from cryptography.fernet import Fernet

# Initialize colorama
init()

class MultiLayerEncryption:
    def __init__(self):
        self.master_key = Fernet.generate_key()
        self.cipher = Fernet(self.master_key)

    def encrypt(self, message):
        encrypted = self.cipher.encrypt(message.encode())
        decrypt_code = self.master_key.decode()  # La clé sert de code de décryptage
        return encrypted.decode(), decrypt_code

    def decrypt(self, encrypted_data, decrypt_code, master_key=None):
        try:
            # Utilise la clé fournie ou celle de l'instance
            key = decrypt_code.encode() if decrypt_code else self.master_key
            cipher = Fernet(key)
            decrypted = cipher.decrypt(encrypted_data.encode())
            return decrypted.decode()
        except Exception as e:
            return f"Erreur de décryptage : {e}"

def print_banner():
    banner = f"""
    {Fore.CYAN}╔══════════════════════════════════════════╗
    ║  {Fore.YELLOW}Multi-Layer Encryption System v2.0{Fore.CYAN}        ║
    ║  {Fore.WHITE}Created by k0zei{Fore.CYAN}                         ║
    ╚══════════════════════════════════════════╝{Style.RESET_ALL}
    """
    print(banner)

def loading_animation(duration=2):
    animation = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    start_time = time.time()
    i = 0
    while (time.time() - start_time) < duration:
        print(f"\r{Fore.CYAN}Initializing system... {animation[i % len(animation)]}", end="")
        time.sleep(0.1)
        i += 1
    print(f"\r{Fore.GREEN}System initialized successfully!{Style.RESET_ALL}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    print_banner()
    loading_animation()
    
    encryptor = MultiLayerEncryption()
    
    while True:
        print(f"\n{Fore.CYAN}[1]{Fore.WHITE} Encrypt a message")
        print(f"{Fore.CYAN}[2]{Fore.WHITE} Decrypt a message")
        print(f"{Fore.CYAN}[3]{Fore.WHITE} Exit")
        
        choice = input(f"\n{Fore.YELLOW}Choose an option (1-3): {Style.RESET_ALL}")
        
        if choice == "1":
            message = input(f"\n{Fore.GREEN}Enter message to encrypt: {Style.RESET_ALL}")
            print(f"\n{Fore.CYAN}Encrypting...{Style.RESET_ALL}")
            time.sleep(1)
            
            encrypted_data, decrypt_code = encryptor.encrypt(message)
            print(f"\n{Fore.GREEN}Encrypted data:{Style.RESET_ALL} {encrypted_data}")
            print(f"{Fore.GREEN}Decryption code:{Style.RESET_ALL} {decrypt_code}")
            
        elif choice == "2":
            encrypted_data = input(f"\n{Fore.GREEN}Enter encrypted data: {Style.RESET_ALL}")
            decrypt_code = input(f"{Fore.GREEN}Enter decryption code: {Style.RESET_ALL}")
            
            print(f"\n{Fore.CYAN}Decrypting...{Style.RESET_ALL}")
            time.sleep(1)
            
            decrypted = encryptor.decrypt(encrypted_data, decrypt_code)
            print(f"\n{Fore.GREEN}Decrypted result:{Style.RESET_ALL} {decrypted}")
            
        elif choice == "3":
            print(f"\n{Fore.YELLOW}Exiting...{Style.RESET_ALL}")
            time.sleep(1)
            break
            
        input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")
        os.system('cls' if os.name == 'nt' else 'clear')
        print_banner()