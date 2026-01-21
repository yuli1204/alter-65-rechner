print("=== Einfache Taschenrechner ===")

zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib die zweite Zahl ein: "))

print("Wähle die Operation:")
print("1 - Addition (+)")
print("2 - Subtraktion (-)")
print("3 - Multiplikation (*)")
print("4 - Division (/)")

wahl = input("Deine Wahl (1/2/3/4): ")

if wahl == "1":
    ergebnis = zahl1 + zahl2
    print(f"Ergebnis: {ergebnis}")
elif wahl == "2":
    ergebnis = zahl1 - zahl2
    print(f"Ergebnis: {ergebnis}")
elif wahl == "3":
    ergebnis = zahl1 * zahl2
    print(f"Ergebnis: {ergebnis}")
elif wahl == "4":
    if zahl2 != 0:
        ergebnis = zahl1 / zahl2
        print(f"Ergebnis: {ergebnis}")
    else:
        print("Fehler: Division durch 0 ist nicht erlaubt.")
else:
    print("Ungültige Auswahl.")