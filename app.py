print("Willkommen zur Python App für den alltäglichen Gebrauch.")

while True:
    print("\nWas möchtest du tun?")
    print("1. Währungen umrechnen")
    print("2. Flächen berechnen")
    print("3. Kopfrechnen")
    print("4. To-do-Liste erstellen")
    print("5. Lokale IP-Adresse herausfinden")
    print("6. Passwort testen")
    print("7. Taschenrechner")
    print("8. App verlassen")

    eingabe = input("Ihre Eingabe: ")
    if eingabe in ["1", "Währungen berechnen", "1.Währungen berechnen"]:
        def währungsrechner():
            print("Willkommen zum Währungs rechner.")
            währung = input("Bitte gib ein, welche Währung du berechnen willst: ")
            if währung == "Dollar":
                chf = float(input("Bitte gib deinen Betrag in CHF ein: "))
                print("Der Betrag in Dollar ist", chf * 1.13)
            elif währung == "Euro":
                chf = float(input("Bitte gib deinen Betrag in CHF ein: "))
                print("Der Betrag in Euro ist", chf * 1.05)
            elif währung == "Lek":
                chf = float(input("Bitte gib deinen Betrag in CHF ein: "))
                print("Der Betrag in Lek ist", chf * 103.83)
            elif währung == "Peso":
                chf = float(input("Bitte gib deinen Betrag in CHF ein: "))
                print("Der Betrag in Peso ist", chf * 22.98)

        währungsrechner()

    elif eingabe in ["2", "Flächen berechnen", "2.Flächen berechnen"]:
        def flächenrechner():
            breite = 0
            länge = 0
            fläche = 0

            print("Willkommen zum Flächen rechner.")
            breite = float(input("Gib deine Breite ein: "))
            länge = float(input("Gib deine Länge ein: "))

            fläche = breite * länge

            print("Deine Fläche beträgt:", fläche, "cm²")

        flächenrechner()

    elif eingabe in ["3", "Kopfrechnen", "3.Kopfrechnen"]:
        import random

        random.seed()

        anzahl = - 1
        while anzahl < 1 or anzahl > 10:
            try:
                print("Wie viele Aufgaben (1 bis 10): ")
                anzahl = int(input())
            except:
                continue

        richtig = 0

        for aufgabe in range(1, anzahl + 1):
            opzahl = random.randint(1, 4)

            if opzahl == 1:
                a = random.randint(-10, 30)
                b = random.randint(-10, 30)
                op = "+"
                c = a + b
            elif opzahl == 2:
                a = random.randint(1, 30)
                b = random.randint(1, 30)
                op = "-"
                c = a - b
            elif opzahl == 3:
                a = random.randint(1, 10)
                b = random.randint(1, 10)
                op = "*"
                c = a * b

            elif opzahl == 4:
                c = random.randint(1, 10)
                b = random.randint(1, 10)
                op = "/"
                a = c * b

            print(f"Aufgabe {aufgabe} von {anzahl}: {a} {op} {b}")

            for versuch in range(1, 4):
                try:
                    print("Bitte Lösungsvorschlag eingeben: ")
                    zahl = int(input())
                except:
                    print("Sie haben keine ganze Zahl eingegeben")
                    continue
                if zahl == c:
                    print(zahl, "ist richitg")
                    richtig = richtig + 1
                    break
                else:
                    print(zahl, "ist falsch")

            print("Ergebnis:", c)
        print(f"Richitg: {richtig} von {anzahl}")


    elif eingabe in ["4", "todo-liste erstellen", "4.todo-liste erstellen"]:

        todos = []

        while True:

            print("Was willst du tun?")

            print("(1) To-dos anzeigen")

            print("(2) To-dos hinzufügen")

            print("(3) Zurück zum Hauptmenü")

            option = input("Bitte auswählen: ")

            if option == "1":

                print("Meine Liste hat diese Elemente:")

                for todo in todos:
                    print(f"- {todo}")

            elif option == "2":

                newitem = input("Was möchtest du hinzufügen? ")

                todos.append(newitem)

            elif option == "3":

                print("Zurück zum Hauptmenü...")

                break

            else:

                print("Ungültige Eingabe. Bitte 1, 2 oder 3 wählen.")

            print("")


    elif eingabe in ["5", "Lokale IP adresse herausfinden", "5.Lokale IP adresse herausfinden"]:
        import socket
        hostname = socket.gethostname()
        myip = socket.gethostbyname(hostname)
        print('Deine Lokale IP adresse ist ' + myip)

    elif eingabe in ["6", "Passwort testen", "6.Passwort testen"]:
        import itertools
        import string
        import sys

        PASSWORT = input("Dein Passwort: ")

        buchstaben = string.ascii_letters + string.digits + string.punctuation
        print(buchstaben)


        def rate_passwort(passwort: str) -> str:
            num_versuch = 0
            for num in range(1, 10):
                for versuch in itertools.product(buchstaben, repeat=num):
                    versuch = ''.join(versuch)
                    num_versuch += 1
                    if versuch == passwort:
                        print(f"Richig geraten: Das Passwort lautet {versuch} bei {num_versuch} Versuchen")
                        return


        rate_passwort(PASSWORT)

    elif eingabe in ["7", "Taschenrechner", "7.Taschenrechner"]:
        def add(a, b):
            return a + b


        def subtract(a, b):
            return a - b


        def multiply(a, b):
            return a * b


        def divide(a, b):
            if b == 0:
                return "Fehler: Division durch Null!"
            return a / b


        def calculator():
            print("Einfacher Taschenrechner")
            print("Wähle eine Operation:")
            print("1. Addition")
            print("2. Subtraktion")
            print("3. Multiplikation")
            print("4. Division")

            choice = input("Gib die Nummer der Operation ein (1/2/3/4): ")

            if choice in ('1', '2', '3', '4'):
                try:
                    num1 = float(input("Gib die erste Zahl ein: "))
                    num2 = float(input("Gib die zweite Zahl ein: "))
                except ValueError:
                    print("Fehler: Ungültige Eingabe!")
                    return

                if choice == '1':
                    print(f"Ergebnis: {add(num1, num2)}")
                elif choice == '2':
                    print(f"Ergebnis: {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Ergebnis: {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"Ergebnis: {divide(num1, num2)}")
            else:
                print("Fehler: Ungültige Auswahl!")


        if __name__ == "__main__":
            calculator()
    print("")
    if eingabe in ["8", "App verlassen", "8.App verlassen"]:
        print("App beendet!")
        print("Bis zum nächsten mal.")
        exit()