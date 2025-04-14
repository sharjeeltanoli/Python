SENTENCE: str = "Panaversity is fun. I learned to program and used Python to make my "

def main():
    adjectives: str = input("\033[1;3m Please type an adjective and press enter: \033[0m")
    nouns: str = input("\033[1;3m Please type a noun and press enter: \033[0m")
    verbs: str = input("\033[1;3m  Please type a verb and press enter: \033[0m")

    print( SENTENCE + " " + adjectives + " " + nouns + " "  + verbs )

if __name__ == "__main__":
    main()