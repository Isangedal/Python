import random, string, os
version = "10"
key_format = f"nlln-lnnnl-V{version}-nn-llln-nlllnn"
admin_key_format = f"llnln-nnnlll-llnnn-V{version}-llln-n-nlln-nnnnn-ll"
user = 0 # 0 = Guest | 1 = User | 2 = Admin
last_user = 0
valid_keys = []
invalid_keys = []
valid_admin_keys = []
invalid_admin_keys = []
def generate_key():
    key = ""
    for letter in key_format:
        if letter == "n":
            key += str(random.randint(0, 9))
        elif letter == "l":
            key += random.choice(string.ascii_uppercase)
        else: key += letter
    valid_keys.append(key)
    input(f"{key}\n")
    start()
def generate_admin_key():
    key = ""
    for letter in admin_key_format:
        if letter == "n":
            key += str(random.randint(0, 9))
        elif letter == "l":
            key += random.choice(string.ascii_uppercase)
        elif letter == "-": key += letter
        else: key += letter
    valid_admin_keys.append(key)
    input(f"{key}\n")
    start()
def find_key(key):
    global user
    os.system("cls")
    if key in valid_admin_keys:
        input("Found admin key.\n")
        user = 2
        user_stuff()
    elif key in invalid_keys or key in invalid_admin_keys:
        input("This is an invalid key. Either this key has been used before, or someone has disabled it.\n")
        if last_user != 0:
            login = input("Since you already have entered a valid key, you may log in. Do you want to log in?\n(Y / N)\n")
            if login.lower() == "y":
                user = last_user
                user_stuff()
            else:
                start()
        else:
            start()
    elif key in valid_keys:
        input("Found key.\n")
        user = 1
        invalid_keys.append(key)
        del valid_keys[valid_keys.index(key)]
        user_stuff()
    else:
        input("Could not find the key. Try again.\n")
        if last_user != 0:
            login = input("Since you already have entered a valid key, you may log in. Do you want to log in?\n(Y / N)\n")
            if login.lower() == "y":
                user = last_user
                user_stuff()
            else:
                start()
        start()
def start():
    os.system("cls")
    has_key = input("\nDo you have a key?\n(Y / N)\n")
    if has_key == "keys":
        os.system("cls")
        print("Keys:\n")
        for key in valid_keys:
            print(key)
        print("\nAdmin Keys:\n")
        for key in valid_admin_keys:
            print(key)
        input()
        start()
    elif has_key == "4DMIN":
        os.system("cls")
        print("Debug:")
        generate_admin_key()
    elif has_key.lower() == "n":
        os.system("cls")
        print(f"\nGo to www.example.com/key/{version} to get a key.\n")
        print("Debug:")
        generate_key()
    elif has_key.lower() == "y":
        os.system("cls")
        key = input("Please type in your key.\n")
        find_key(key)
    elif has_key == "exit": exit()
    else:
        os.system("cls")
        input("That is not an option.\n")
        start()
def user_stuff():
    global user, last_user
    last_user = user
    os.system("cls")
    if user == 1:
        stuff = input("What to do?\n\n0: Logout\n")
        if stuff == "0":
            os.system("cls")
            input("Logging out...\n")
            user = 0
            start()
        else:
            input("That is not a valid option.\n")
            user_stuff()
    elif user == 2:
        stuff = input("What to do?\n1: Disable a key\n2: Enable a key\n\n0: Logout\n")
        if stuff == "1":
            disable_key()
        if stuff == "2":
            enable_key()
        if stuff == "0":
            os.system("cls")
            input("Logging out...\n")
            user = 0
            start()
        else:
            input("That is not a valid option.\n")
            user_stuff()
def disable_key():
    os.system("cls")
    print("Keys:\n")
    for key in valid_keys:
        print(key)
    print("\nAdmin Keys:\n")
    for key in valid_admin_keys:
        print(key)
    key = input("\nWhich key do you want to disable?\n")
    if key in valid_keys:
        os.system("cls")
        invalid_keys.append(key)
        del valid_keys[valid_keys.index(key)]
        input(f"Disabled key: {key}\n")
        user_stuff()
    if key in valid_admin_keys:
        os.system("cls")
        invalid_admin_keys.append(key)
        del valid_admin_keys[valid_admin_keys.index(key)]
        input(f"Disabled admin key: {key}\n")
        user_stuff()
    else:
        input("That is not a valid key\n")
        user_stuff()
def enable_key():
    os.system("cls")
    print("Keys:\n")
    for key in invalid_keys:
        print(key)
    print("\nAdmin Keys:\n")
    for key in invalid_admin_keys:
        print(key)
    key = input("\nWhich key do you want to enable?\n")
    if key in invalid_keys:
        os.system("cls")
        valid_keys.append(key)
        del invalid_keys[invalid_keys.index(key)]
        input(f"Enabled key: {key}\n")
        user_stuff()
    if key in invalid_admin_keys:
        os.system("cls")
        valid_admin_keys.append(key)
        del invalid_admin_keys[invalid_admin_keys.index(key)]
        input(f"Enabled admin key: {key}\n")
        user_stuff()
    else:
        os.system("cls")
        input("That is not a valid key\n")
        user_stuff()
start()