def szepnapvan():
    szoveg: str = "Szép nap vann!"

    # Írd ki a szöveg első karakterét!
    print("1. ",szoveg[0])

    # Írd ki a szöveg 2. karakterét!
    print("2. ",szoveg[1])

    # Írd ki a szöveg hosszát!
    print("A hossz: ", len(szoveg))

    # Írd ki a szöveg utolsó karakterét!
    print("utolsó ", szoveg[len(szoveg)-1])

    # Írd ki a szöveg karaktereit egymás után betűnként!
    i:int=0
    while i< len(szoveg):
        print(szoveg[i])
        i+=1

def szovegkezeles():
    szoveg:str = "Ez egy teszt szöveg"
    print(szoveg)
    print(szoveg.upper())

    # van-e a szövegben 'teszt' szöveg
    x:int =szoveg.find("teszt")
    if x>=0:
        print("van benne teszt szöveg")
    else:
        print("nincs benne teszt szöveg")

    # a szoveg váltoróban hol szerepel először az s betű
    print(szoveg.find("s"), ". helyen szerepel s betű!")

    # alakítsd át minden szó kezdőbetűjé nagybetűssé
    print(szoveg.title())

    # cseréld ki a teszt szót 'próba'-ra
    print(szoveg.replace("teszt", "próba"))

def aszoveg_visszafele(szoveg:str):
    # a paraméterben kapott szöveg visszafelé kiírva egymás mellé betű
    i:int=len(szoveg)
    while i!=0:
        print(szoveg[i-1], end="")
        i -= 1
    
def a_betuk_szama(szoveg:str):
    #hány 'a' betű van a szövegben?
    #print(szoveg.count("a"), " alkalommal szerepel a betű a szövegben.")
    i:int = 0
    a_szamlalo: int = 0
    while i<len(szoveg):
        if szoveg[i]== 'a':
            a_szamlalo +=1
        i +=1
    print("A betűk száma: ", a_szamlalo)
