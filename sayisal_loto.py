import random
import time 

class SayisalLoto():
    baslik = "SAYISAL LOTO PROGRAMI"

    def __init__(self):
        # Programı doğrudan başlatmak için
        self.giris()

    def sayibelirleme(self):
        while True:
            try:
                kolonsayisi = int(input("Kaç tane kolon üretelim? : "))
                return kolonsayisi
            except ValueError:
                print("Bir tam sayı girilmedi. Tekrar deneyin...")

    def giris(self):
        # Başlık formatı düzeltildi
        print("*" * len(self.baslik), self.baslik, "*" * len(self.baslik), sep="\n")
        
        while True:
            istek = input("\nProgramdan çıkmak için 1'e, devam etmek için herhangi bir tuşa basınız: ")

            if istek == "1":
                print("Program kapatılıyor...")
                time.sleep(1)
                break
            
            sayi_adedi = self.sayibelirleme()
            kolonlar = []
            sayac = 0

            while sayac < sayi_adedi:
                kolon = []
                while len(kolon) < 6:
                    numara = random.randint(1, 49) # Sayısal loto genelde 1-49 arasıdır
                    if numara not in kolon:
                        kolon.append(numara)
                
                kolon.sort()
                
                if kolon not in kolonlar:
                    kolonlar.append(kolon)
                    sayac += 1
                    print(f"{sayac}. kolon = {kolon}")

if __name__ == "__main__":
    sl = SayisalLoto()