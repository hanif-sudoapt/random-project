from os import system, name
from time import sleep

# So welcome, what this file / module can do is like a basic loading stuff, 
# and for me it's like a cool animation that can be used in the terminal :)


class Loading:
    # the core of this class is in here actually 
    def __init__(self, firstCount, manyCount, sleep_time):
        self.firstCount = firstCount
        self.manyCount = manyCount
        self.sleep_time = sleep_time

    # I'm using staticmethod, because this function didn't use any argumen / parameters
    @staticmethod
    def clear():

        # for windows os
        if name == "nt":
            _ = system("cls")
        # for linux or mac os
        else:
            _ = system('clear')

    def loadingText(self):

        # clearing the terminal screen
        Loading(self.firstCount, self.manyCount, self.sleep_time).clear()

        # print text loadingnya, dengan jumlah titik yang ditentukan
        print("loading" + " . " * self.firstCount)

    def loadingAnimation(self):

        # jadi, gw buat kloningannya firstCount variable. 
        # Karena klo ga di buat kloningannya, nnti si firsCount nya jadi ikut nambah angkanya saat di increment dalam while loop di bawah
        # akibatnya apa jika ga di clone atau di buat variabel yang baru ?

        # nanti jika manggil fungsi loadingAnimation sekali, masih bisa normal loadingnya. Nah yang masalah klo kita manggil lagi fungsinya
        # bakal gaada loading textnya yang titik" nambah. Karena di anggep sama komputer bahwa firstCount ini, nilai nya udah setara sama manyCount
        # jadinya, cuma keluar loading dan titik" dengan sejumlah manyCount tersebut. Sorry klo belibet jelasinnya 
        FirstCountClone = self.firstCount

        # Nah makanya disini gw pake variabel patokan awal loopnya, dari si variabel firstCountClone, biar ga ngefek ke seluruh class
        while FirstCountClone <= self.manyCount:
            # ini buat panggil si loadingText nya
            Loading(FirstCountClone, self.manyCount, self.sleep_time).loadingText()

            # jeda waktu sebelum titik bertambah
            sleep(self.sleep_time)

            # increment the firstCountClone
            FirstCountClone += 1

        # clearing the terminal screen
        Loading(self.firstCount, self.manyCount, self.sleep_time).clear()