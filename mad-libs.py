def check():
    gameisplaying()
    adjective1 = input("Enter an adjective: ")
    if adjective1 == "1":
        print("sorry type it again")
        return
    noun1 = input("Enter a noun: ")
    if noun1 == "1":
        print("sorry type it again")

    verb1 = input("Enter a Verb (past tense): ")    
    if verb1 == "1":
        print("sorry type it again")
    else:
        print("Today I went to the zoo. I saw a(n)" + adjective1 + " " + noun1 + " " + "jumping up and down in its tree.")

def gameisplaying():
    while verb1==none:
        check()
check()