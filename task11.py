color = ""
secret = ["sininen", "punainen", "keltainen", "vihreä"]
while(color not in secret):
    color = str(input("Syötä salainen väri: "))
    if color in secret:
     print("Löysit salaisen värin!")
    else:
     print("Et läytänyt salaista väriä! Yritä uudelleen!")
