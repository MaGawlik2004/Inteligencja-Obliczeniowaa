from datetime import date
import math

name = input("State your name.\n")
year = int(input("State your birthday year.\n"))
month = int(input("State your birthday month.\n"))
day = int(input("State your birthday day.\n"))

today = date.today()
birthday = date(year, month, day)
days_difference = (today - birthday).days

def Yp (days):
    return math.sin((2*math.pi/23)*days)

Yp_today = Yp(days_difference)
Yp_tomorow = Yp(days_difference + 1)

def Ye (days):
    return math.sin((2*math.pi/28)*days)

Ye_today = Ye(days_difference)
Ye_tomorow = Ye(days_difference + 1)

def Yi (days):
    return math.sin((2*math.pi/33)*days)

Yi_today = Yi(days_difference)
Yi_tomorow = Yi(days_difference + 1)

print(f"Hello {name}! {days_difference} days have past from your birthday!\n")

print(f"Your physical wave is at {round(Yp_today, 2)} today.")
if Yp_today > 0.5:
    print("Congratulations, you have a good result, enjoy the day!\n")

elif Yp_today < -0.5:
    print("Unfortunately, you have the wrong result, don't worry!\n")

    if Yp_today < Yp_tomorow:
        print("Don't worry, tomorrow will be better!\n")

print(f"Your emotional wave is at {round(Ye_today, 2)} today.")
if Ye_today > 0.5:
    print("Congratulations, you have a good result, enjoy the day!\n")

elif Ye_today < -0.5:
    print("Unfortunately, you have the wrong result, don't worry!\n")

    if Ye_today < Ye_tomorow:
        print("Don't worry, tomorrow will be better!\n")

print(f"Your intellectual wave is at {round(Yi_today, 2)} today.")
if Yi_today > 0.5:
    print("Congratulations, you have a good result, enjoy the day!\n")

elif Yi_today < -0.5:
    print("Unfortunately, you have the wrong result, don't worry!\n")

    if Yi_today < Yi_tomorow:
        print("Don't worry, tomorrow will be better!\n")


# Zajeło mi to około 40 minut