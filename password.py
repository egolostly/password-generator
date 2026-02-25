import random
import time
import string
import os

def password():
    while True:
        try:
            os.system("cls" if os.name == "nt" else "clear")
            user_input = input("🧾 Enter your password length (1-100): ").strip()
            if not user_input:
                print("⚠️ You cannot leave it empty!")
                time.sleep(1.5)
                continue
            length = int(user_input)
            if length < 1 or length > 100:
                print("⚠️ Please enter a length between 1 and 100.")
                time.sleep(2)
                continue
            print("👾 Generating your password...")
            time.sleep(1)
            characters = string.ascii_letters + string.digits + "!@#$%^&*"
            generated_password = "".join(random.choice(characters) for _ in range(length))
            os.system("cls" if os.name == "nt" else "clear")
            print(f"✅ Your password is: {generated_password}")
            print("-" * 30)
            while True:
                confirm = input("🔄 Would you like to create another password? (y/n): ").lower().strip()
                if confirm == "y":
                    print("🚀 Redirecting to start...")
                    time.sleep(1)
                    break 
                elif confirm == "n":
                    print("👋 Have a great day!")
                    time.sleep(1.5)
                    return
                else:
                    print("⚠️ Please enter a valid response (y/n).")
                    time.sleep(1.5)
                    # Buradaki hatırlatıcı print'i koruduk
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f"✅ Your password was: {generated_password}")
        except ValueError:
            # Harf veya geçersiz sembol girilirse burası kurtarır
            print("⚠️ Invalid input! Please enter a WHOLE NUMBER.")
            time.sleep(2)
if __name__ == "__main__":
    password()