import re
import hashlib
def hash(value):
    return hashlib.sha256(value.encode()).hexdigest()
def main():
    def menu():
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choice: ")
        def handle():
            if choice == "1":
                register()
            elif choice == "2":
                login()
            elif choice == "3":
                exit()
            else:
                print("Invalid choice!")
                menu()
        handle()
    def register():
        usr0 = input("Username: ")
        pas0 = input("Password: ")
        ema0 = input("Email: ")
        def checksum():
            def pas0check():
                if len(pas0) <= 7:
                    print("Password too short!")
                    exit()
                def ema0check():
                    pattern = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
                    if not re.match(pattern, ema0):
                        print("Invalid email!")
                        exit()

                    def duplicatecheck():
                        try:
                            with open("data.txt", "r") as f:
                                for line in f:
                                    stored_usr = line.strip().split("+")[0]
                                    if stored_usr == usr0:
                                        print("Username already taken!")
                                        exit()
                        except FileNotFoundError:
                            pass  
                        def finalcheck():
                            with open("data.txt", "a") as f:
                                f.write(f"{usr0}+{hash(pas0)}+{hash(ema0)}\n")
                            print("Account created!")
                            menu()

                        finalcheck()
                    duplicatecheck()
                ema0check()
            pas0check()
        checksum()
    def login():
        usr0 = input("Username: ")
        pas0 = input("Password: ")
        def attempt():
            try:
                with open("data.txt", "r") as f:
                    for line in f:
                        parts = line.strip().split("+")
                        stored_usr = parts[0]
                        stored_pas = parts[1]
                        def compare():
                            if stored_usr == usr0 and stored_pas == hash(pas0):
                                print(f"Welcome, {usr0}!")
                                menu()                      
                        compare()
                print("Invalid username or password!")
            except FileNotFoundError:
                print("No accounts found!")
        attempt()
    menu()
main()