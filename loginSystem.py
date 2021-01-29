# Komentar Berbahasa Campuran (English and Indonesian)!

# import only system and name from os
from os import system, name

# import sleep to show output for some time period
from time import sleep 

# ini dictionary untuk menyimpan data akun user
user_data = {}

# ini password rahasia hehe
secret_password = "kopinya enak banget"

def welcome():
    # for clear entire screen before
    clear(0.5)

    choice = input("Welcome\n1. Sign Up\n2. Login\n3. All Data\n(press enter for exit)\n--> ")

    if choice == "1" or choice == "Sign Up":
        # masuk ke fungsi sign_up
        sign_up()
    elif choice == "2" or choice == "Login":
        # masuk ke fungsi login
        login()
    elif choice == "3" or choice == "All Data":
        # masuk ke fungsi all_data
        all_data()
    else:
        print("\nLoading . . . ")

        # for clear entire screen before
        clear(2)

        # keluar dari program, jika user menekan enter :)

    
def sign_up():
    # for clear entire screen before
    clear(0.5)

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

    # for clear entire screen
    clear(2)

    # kembali ke fungsi welcome
    welcome()


# Fungsi ini ga terlalu penting sih hehe
def login():
    # for clear entire screen before
    clear(0.5)

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

    # for clear entire screen
    clear(2)

    # kembali ke fungsi welcome
    welcome()


def all_data():
    # for clear entire screen before
    clear(0.5)

    # di sini, kita bisa akses semua data yang telah tersimpan di dalam dictionary "user_data"
    secret_input = input("Enter the secret password: ")

    if user_data == {}:
        # new feature
        print("\n*Empty")
    else:

        if secret_input == secret_password:
            print("\nUser Data:")
            for username, password in user_data.items():
                print(f"- {username} >>> {password}")
        else:
            print("\n*Invalid password")

    if input("\npress ENTER if you done") == "":
        # for clear entire screen
        clear(2)

    # kembali ke fungsi welcome
    welcome()

def clear(sleep_time):

    # sleep time
    sleep(sleep_time)

    # this is for windows
    if name == "nt":
        _ = system('cls')

    # this is for mac and linux (os.name called "posix")
    else:
        _ = system('clear')

# start program
welcome()


# Program ini belum selesai tuntas, masih banyak yang bisa di improve kedepannya