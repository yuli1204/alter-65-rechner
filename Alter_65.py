from datetime import datetime
aktuelles_jahr = datetime.now().year
geburtsjahr = int(input("In welchem Jahr bist du geboren? "))

alter = aktuelles_jahr - geburtsjahr
jahr_65 = geburtsjahr + 65

print("\n--- Ergebnis ---")
print(f"Du bist ungefähr {alter} Jahre alt.")
print(f"Du wirst 65 Jahre alt im Jahr {jahr_65}.") 





