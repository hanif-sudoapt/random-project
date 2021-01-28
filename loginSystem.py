# Komentar Berbahasa Indonesia !

# ini dictionary untuk menyimpan data akun user
user_data = {}

def welcome():
    choice = input("\nWelcome\n1. Sign Up\n2. Login\n3. Exit\n== ")
    if choice == "1":
        # masuk ke fungsi sign_up
        sign_up()
    elif choice == "2":
        # masuk ke fungsi login
        login()
    else:
        pass
        # keluar dari program, jika user input angka untuk exit

    
def sign_up():
    # sign up untuk akun baru
    new_username = input("Input new username: ")
    new_password = input("Input new password: ")

    # store the data to the dictionary
    user_data[new_username] = new_password

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

            # kembali ke fungsi welcome
            welcome()
        else:
            print("\n*This account is doesn't exist")

            # kembali ke fungsi welcome
            welcome()
    else:
        print("\n*This account is doesn't exist")

        # kembali ke fungsi welcome
        welcome()

# start program
welcome()


# Program ini belum selesai tuntas, masih banyak yang bisa di improve kedepannya