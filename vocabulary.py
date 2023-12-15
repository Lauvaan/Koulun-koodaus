# importing libraries and intializing variables(all vars initialized in the start)

import random 
word = ""
entry = ""
aswer = ""
index = int()
yesno = ""
esfi = ""
# lists of vocabulary in Spanish and Finnish, wordses = Spanish, wordsfi = Finnish

wordses = ["que bien nos lo pasamos", 
           "medio dormido", 
           "menos mal", 
           "no me digas", 
           "extrano", 
           "aunque tenia que hacerlo", 
           "a lo mejor", 
           "ponerse malo", 
           "enfermo", 
           "una insolacion", 
           "resfriarse", 
           "pillar una gripe", 
           "acabo de enterarme", 
           "torcerse",
           "caerse",
           "se le ha roto", 
           "escaylado",
           "pobre",
           "que molesto",
           "mejorarse",
           "pronto",
           "la suerte",
           "ademas",
           "que pena",
           ]
wordsfi = ["olipa meillä hauskaa",
           "puolinukuksissa",
           "onneksi",
           "ihanko totta",
           "outo",
           "vaikka hänen piti tehdä se",
           "ehkä",
           "sairastua",
           "sairas",
           "auringonpistos",
           "vilustua",
           "saada flunssa",
           "sain juuri tietää",
           "nyrjäyttää",
           "kaatua",
           "häneltä rikkoutui",
           "kipsattu",
           "raukka",
           "miten harmillista",
           "parantua",
           "pian",
           "onni",
           "lisäksi",
           "voi harmi",
           ]

# Instructs the user to use only lower case letters, so that the program fucntions correctly

print("Kirjoita kaikki pienillä kirjaimilla, äläkä käytä aksenttimerkkejä tai muita symboleja, jotta ohjelma toimii oikein.")

# Input field that asks the user if they want to translate to English or Finnish

esfi = str(input("Haluatko kääntää sanoja espanjaksi vai suomeksi(espanja/suomi)? "))

# The actual excersise. If clauses for Spanish and Finnish translations.
# Inside them, while loops that run as long as the user doesn't input "en", meaning "not"
# Asks the user if they want to play
# Prints a divider and chooses the origin word using the random librarys "choice" function
# Prints the origin word, and asks user to translate it
# Finds the index of the origin word, and checks if the user inputted answer is the same as the corresponding entry in the answer words list
# If the word is correct, it tells the user the word was correct, and prints a few dividers
# If user inputs "en tiedä", meaning "I don't know", it tells them the correct answer
# If the word was incorrect, it tells the user the word was incorrect and the correct word, so the user can learn. Also prints a few dividers

if esfi == "suomi":
    while(yesno != "en"):
        print("------------------")
        entry = random.choice(wordses)
        print("'", entry, "'", end=" ", sep="")
        word = str(input("tarkoittaa mitä? "))
        index = wordses.index(entry)
        if word == wordsfi[index]:
            print("Oikein!")
            print("------------------")
            print("------------------")
            yesno = str(input("Haluatko pelata(kyllä/en)? "))
        elif word == "en tiedä":
            print("Ei se mitään, oikea vastaus on ", "'", (wordsfi[index]), "'", sep="")
            print("Ensi kerralla sitten osaat!")
            yesno = str(input("Haluatko pelata(kyllä/en)? "))
        else:
            print("Väärin! Oikea vastaus olisi ollut ", "'", (wordsfi[index]), "'", sep="")
            print("------------------")
            print("------------------")
            yesno = str(input("Haluatko pelata(kyllä/en)? "))

elif esfi == "espanja":
    while(yesno != "en"):
        print("------------------")
        entry = random.choice(wordsfi)
        print("'", entry, "'", end=" ", sep="")
        word = str(input("tarkoittaa mitä? "))
        index = wordsfi.index(entry)
        if word == wordses[index]:
            print("Oikein!")
            print("------------------")
            print("------------------")
            yesno = str(input("Haluatko pelata(kyllä/en)? "))
        elif word == "en tiedä":
            print("Ei se mitään, oikea vastaus on ", "'", (wordses[index]), "'", sep="")
            print("Ensi kerralla sitten osaat!")
            print("------------------")
            yesno = str(input("Haluatko pelata(kyllä/en)? "))
        else:
            print("Väärin! Oikea vastaus olisi ollut ", "'", (wordses[index]), "'", sep="")
            print("------------------")
            print("------------------")
            yesno = str(input("Haluatko pelata(kyllä/en)? "))
    

# Thanks the user for playing, and welcomes them to play again

print("Kiitos pelaamisesta, tervetuloa pelaamaan uudelleen!")
