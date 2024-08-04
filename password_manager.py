from cryptography.fernet import Fernet


'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) '''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            # rstrip enable not to read an empty line
            data = line.rstrip()
            user, password = data.split("|")
            print(user, fer.decrypt(password.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', "a") as f:
        f.write("name: " + name + " | " + "password: " +
                fer.encrypt(pwd.encode()) + "\n")  # encrypt the password


while True:
    mode = input(
        "Would you like to view password or add a new one?(view / add / press q to quite) ")
    if mode == "q":
        print("you quited")
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()
    else:
        print("Invalide Mode")
        continue
