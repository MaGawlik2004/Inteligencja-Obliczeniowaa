from datetime import date
import math

# Input
name = input("State your name.\n")
year = int(input("State your birthday year.\n"))
month = int(input("State your birthday month.\n"))
day = int(input("State your birthday day.\n"))

# Obliczenie różnicy dni
today = date.today()
birthday = date(year, month, day)
days_difference = (today - birthday).days

# Funkcje obliczające fale
def Yp(days):
    return math.sin((2 * math.pi / 23) * days)

def Ye(days):
    return math.sin((2 * math.pi / 28) * days)

def Yi(days):
    return math.sin((2 * math.pi / 33) * days)

# Obliczenie wartości fal
Yp_today = Yp(days_difference)
Yp_tomorrow = Yp(days_difference + 1)

Ye_today = Ye(days_difference)
Ye_tomorrow = Ye(days_difference + 1)

Yi_today = Yi(days_difference)
Yi_tomorrow = Yi(days_difference + 1)

# Wyświetlanie wyników
print(f"Hello {name}! {days_difference} days have passed since your birthday!\n")

# Fala fizyczna
print(f"Your physical wave is at {round(Yp_today, 2)} today.")
if Yp_today > 0.5:
    print("Congratulations, you have a good result, enjoy the day!\n")
elif Yp_today < -0.5:
    print("Unfortunately, you have the wrong result, don't worry!\n")
    if Yp_today < Yp_tomorrow:
        print("Don't worry, tomorrow will be better!\n")

# Fala emocjonalna
print(f"Your emotional wave is at {round(Ye_today, 2)} today.")
if Ye_today > 0.5:
    print("Congratulations, you have a good result, enjoy the day!\n")
elif Ye_today < -0.5:
    print("Unfortunately, you have the wrong result, don't worry!\n")
    if Ye_today < Ye_tomorrow:
        print("Don't worry, tomorrow will be better!\n")

# Fala intelektualna
print(f"Your intellectual wave is at {round(Yi_today, 2)} today.")
if Yi_today > 0.5:
    print("Congratulations, you have a good result, enjoy the day!\n")
elif Yi_today < -0.5:
    print("Unfortunately, you have the wrong result, don't worry!\n")
    if Yi_today < Yi_tomorrow:
        print("Don't worry, tomorrow will be better!\n")

# Komentarz o czasie
print("\nIt took me about 50 minutes to complete this!")


#zajeło to 2 minuty