import math
from datetime import datetime

def oblicz_biorytm(dni, okres):
    return math.sin(2 * math.pi * dni / okres)

def main():
    # Pobieranie danych od użytkownika
    imie = input("Jak masz na imię? ")
    rok = int(input("Podaj rok urodzenia (np. 2000): "))
    miesiac = int(input("Podaj miesiąc urodzenia (np. 5): "))
    dzien = int(input("Podaj dzień urodzenia (np. 15): "))

    # Obliczanie liczby dni od urodzenia
    data_urodzenia = datetime(rok, miesiac, dzien)
    dzisiaj = datetime.now()
    dni_zycia = (dzisiaj - data_urodzenia).days

    # Obliczanie biorytmów
    fizyczny = oblicz_biorytm(dni_zycia, 23)
    emocjonalny = oblicz_biorytm(dni_zycia, 28)
    intelektualny = oblicz_biorytm(dni_zycia, 33)

    # Wyświetlanie wyników
    print(f"\n{imie}, żyjesz już {dni_zycia} dni!")
    print(f"Biorytm fizyczny: {fizyczny:.2f}")
    print(f"Biorytm emocjonalny: {emocjonalny:.2f}")
    print(f"Biorytm intelektualny: {intelektualny:.2f}\n")

    # Sprawdzanie wyników biorytmów
    for nazwa, wartosc in zip(["fizyczny", "emocjonalny", "intelektualny"], [fizyczny, emocjonalny, intelektualny]):
        if wartosc > 0.5:
            print(f"Twój {nazwa} biorytm jest wysoki! Gratulacje!")
        elif wartosc < -0.5:
            print(f"Twój {nazwa} biorytm jest niski. Trzymaj się, będzie lepiej!")
        else:
            print(f"Twój {nazwa} biorytm jest w normie.")

    # Dodatkowe wiadomości
    if any(w > 0.5 for w in [fizyczny, emocjonalny, intelektualny]):
        print("To będzie dobry dzień!")
    elif any(w < -0.5 for w in [fizyczny, emocjonalny, intelektualny]):
        print("Nie martw się. Jutro będzie lepiej!")
    else:
        print("Masz zrównoważony dzień.")

main()
