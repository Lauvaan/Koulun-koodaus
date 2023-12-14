number = int(input("Syötä positiivinen kokonaisluku: "))
if number < 1:
    print("Syöttämäsi luku ei ole kokonaisluku, syötä uusi luku:")
else:
    for k in range(1,number + 1):
        print(k)
    print("Loppu!")