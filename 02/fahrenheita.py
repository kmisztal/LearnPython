x = input("Podaj temperaturę w stopniach Celsjusza: ") # Pobierz dane od użytkownika
celsius = float(x) # Konwertuj na liczbę zmiennoprzecinkową

# Oblicz temperaturę w stopniach Fahrenheita
fahrenheit = (celsius * 9/5) + 32

# Wyświetl wynik
print(f"{celsius} stopni Celsjusza to {fahrenheit} stopni Fahrenheita.")