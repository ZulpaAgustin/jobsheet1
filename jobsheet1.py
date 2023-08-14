import random
from guess import cek

class TebakAngka:
    def __init__(self):
        self.jawaban=random.randint(1,10)
        
    def tebak(self, tebakan):
         self.tebakan=tebakan
         if self.tebakan == self.jawaban:
            print ("Jawabanmu benar!")
         else:
         	print ("Jawabanmu salah!")
	
objek=TebakAngka( )

tebakan=int(input("Tebak angka dari 1s.d 10 : "))
obj=objek.tebak(tebakan)
print(obj)