number = ""
while(number != 0):
    number = int(input("Syötä luku: "))
    answer = number % 3
    if answer == 0:
        print("Lukusi on jaollinen kolmella")
    else:
        print("Lukusi ei ole jaollinen kolmella")
print("Ohjelma loppui")