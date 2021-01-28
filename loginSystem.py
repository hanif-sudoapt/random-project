# Komentar Berbahasa Indonesia !

# ini dictionary untuk menyimpan data akun user
user_data = {}

# ini password rahasia hehe
secret_password = "kopinya enak banget"

def welcome():
    choice = input("\nWelcome\n1. Sign Up\n2. Login\n3. All Data\n(press enter for exit)\n--> ")
    print()
    if choice == "1":
        # masuk ke fungsi sign_up
        sign_up()
    elif choice == "2":
        # masuk ke fungsi login
        login()
    elif choice == "3":
        # masuk ke fungsi all_data
        all_data()
    else:
        pass
        # keluar dari program, jika user menekan enter :)

    
def sign_up():
    # sign up untuk akun baru
    new_username = input("Input new username: ")
    new_password = input("Input new password: ")

    # algoritma untuk cek apakah ada spasi di dalam username ataupun password
    if " " in new_username:
        print("\n*No space allowed in username")
    elif " " in new_password:
        print("\n*No space allowed in password")
    # jika sudah benar tidak ada spasi pada username maupun password, maka username dan password dapat dilanjut ke tahap berikutnya
    else:
        # jika username sudah pernah di input sebelumnya, maka username tidak akan bisa diterima komputer
        if new_username in user_data.keys():
            print("\n*This account is already exist")
        else:
            # mentransfer data ke dictionary "user_data"
            user_data[new_username] = new_password
            print("\n*Account added")

    # kembali ke fungsi welcome
    welcome()


def login():
    # meminta input untuk login user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # logika untuk cek keberadaan akun
    if username in user_data.keys():
        if password in user_data.values():
            print("\n*Login successfully")
        else:
            print("\n*This account is doesn't exist")
    else:
        print("\n*This account is doesn't exist")

    # kembali ke fungsi welcome
    welcome()


def all_data():
    # di sini, kita bisa akses semua data yang telah tersimpan di dalam dictionary "user_data"
    secret_input = input("Enter the secret password: ")
    if secret_input == secret_password:
        print("\nUser Data:")
        for username, password in user_data.items():
            print(f"- {username} == {password}")
    else:
        print("\n*Invalid password")

    # kembali ke fungsi welcome
    welcome()


# start program
welcome()


# Program ini belum selesai tuntas, masih banyak yang bisa di improve kedepannya