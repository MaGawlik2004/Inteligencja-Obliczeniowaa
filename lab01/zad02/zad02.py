import random
import math
import matplotlib.pyplot as plt

odleglosc_od_celu = random.randint(50,340)
v = 50  
h = 100  
g = 9.81  

print(f"Odleglosc od celu wynosi {odleglosc_od_celu}m. Żeby cel został trafiony musisz podac taki kąt który umożliwi dolecenie pocisku na odległość w zakresie [{odleglosc_od_celu - 5}, {odleglosc_od_celu + 5}]m.")

def trajektoria(alpha_w_radianach):
    # Obliczanie trajektorii
    t_max = (v * math.sin(alpha_w_radianach) + math.sqrt((v * math.sin(alpha_w_radianach))**2 + 2 * g * h)) / g
    t_points = 100  # liczba punktów na trajektorii
    t_values = [t_max * i / (t_points - 1) for i in range(t_points)]  # przedział czasowy od 0 do t_max
    
    x_values = [v * math.cos(alpha_w_radianach) * t for t in t_values]  # współrzędna x
    y_values = [h + v * math.sin(alpha_w_radianach) * t - 0.5 * g * t**2 for t in t_values]  # współrzędna y

    # Tworzenie wykresu
    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values)
    plt.title('Trajektoria lotu pocisku')
    plt.xlabel('Odległość (m)')
    plt.ylabel('Wysokość (m)')
    plt.legend()
    plt.grid(True)
    plt.xlim(0, max(x_values) + 10)
    plt.ylim(0, max(y_values) + 20)

    # Zapisanie wykresu do pliku
    plt.savefig("trajektoria_pocisku.png")
    print("Wykres trajektorii został zapisany jako 'trajektoria_pocisku.png'.")
    return


while True:
    alpha = float(input("Podaj kąt strzału: "))
    alpha_w_radianach = math.radians(alpha)
    
    odleglosc_pocisku = v * math.cos(alpha_w_radianach) * ((v * math.sin(alpha_w_radianach) + math.sqrt((v * math.sin(alpha_w_radianach))**2 + 2 * g * h)) / g)

    if (odleglosc_od_celu - 5 <= odleglosc_pocisku <= odleglosc_od_celu + 5):
        print("Pocisk dosięgnął celu. Gratulacje!!!")
        trajektoria(alpha_w_radianach)
        break
    else:
        if (odleglosc_od_celu - 5 > odleglosc_pocisku):
            print("Pocisk nie doleciał do celu. Spróbuj ponownie.")
        else:
            print("Pocisk przeleciał za cel. Spróbuj ponownie.")
