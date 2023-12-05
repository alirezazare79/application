from datetime import datetime

def is_palindrome(s):
    return ''.join(s.split()).lower() == ''.join(s.split()).lower()[::-1]

def application():
    saisir = ""
    while saisir !='q':
        current_datetime = datetime.now()
        current_hour = current_datetime.hour
        if current_hour < 18 :
            print("*** Bonjour et bienvenue sur cette application ***")
        else:
            print("*** Bonsoir et bienvenue sur cette application ***")

        phrase = input("Écrivez votre phrase : ")
        if is_palindrome(phrase):
            print("Bien dit !")            
        else:
            print("Votre phrase n'etez pas un palandrome ")
        
        saisir = input("Entrer q si vous vouler arreter ")
        if saisir == "q":
            print("Au revoir")
            break
            

application()
