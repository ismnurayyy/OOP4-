class hesab():
    def __init__(self,hesabnomresi,balans):
        self.hesabnomresi = hesabnomresi
        self.balans = balans

    def balansartirmaq(self,daxiledilenmebleg):
        self.balans += daxiledilenmebleg
        self.daxiledilenmebleg = daxiledilenmebleg
        print(self.balans)
    def pulcixarmaq(self,cekilecekmebleg):
        if self.balans > cekilecekmebleg:
            self.balans -= cekilecekmebleg
            print("isteiyniz ugurla yerine yetirildi")
        else:
            print("Balansinizda kifayet qeder mebleg yoxdur")
        
    def balansgostermek(self):
        print("Balansinizda {} azn mebleg var".format(self.balans))


class kredit(hesab):
    def __init__(self,hesabnomresi,balans,kreditpulu):
        super().__init__(hesabnomresi,balans)
        self.kreditpulu = kreditpulu

    def kreditgotur(self):
        self.balans += self.kreditpulu

    def kreditodemek(self):
        ayliqmebleg = self.kreditpulu % 12
        self.pulcixarmaq(ayliqmebleg)


# def hesabtest():
#     hesabnomresi1 = hesab("256654",5000)
#     hesabnomresi1.balansartirmaq(1000)
#     hesabnomresi1.pulcixarmaq(1200)
#     hesabnomresi1.pulcixarmaq(8000)
#     hesabnomresi1.balansgostermek()
    



def kredit_test():
    hesabnomresi1 = kredit("328963",6300,15000)
    hesabnomresi1.balansgostermek()
    hesabnomresi1.kreditgotur()
    hesabnomresi1.balansgostermek()
    hesabnomresi1.kreditodemek()
    hesabnomresi1.balansgostermek()

if __name__ == "__main__":
    # hesabtest()
    kredit_test()



