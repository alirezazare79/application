from datetime import datetime


def is_palindrome(s):
    clean_phrase = ''.join(s.split()).lower()
    return clean_phrase == clean_phrase[::-1]


def application():
    saisir = ""
    while saisir.lower() != 'q':
        current_datetime = datetime.now()
        current_hour = current_datetime.hour
        greeting = "*** Bonjour et bienvenue sur cette application ***" if current_hour < 18 else "*** Bonsoir et bienvenue sur cette application ***"
        print(greeting)

        phrase = input("Écrivez votre phrase : ")
        if is_palindrome(phrase):
            print("Bien dit!")
        else:
            print("Votre phrase n'est pas un palindrome")

        saisir = input("Entrer 'q' si vous voulez arrêter ")
        if saisir.lower() == "q":
            print("Au revoir")
            break


if __name__ == "__main__":
    application()
