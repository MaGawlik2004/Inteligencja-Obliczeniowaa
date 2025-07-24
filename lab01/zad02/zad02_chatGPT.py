import random
import math
import matplotlib.pyplot as plt

# Parametry
odleglosc_od_celu = random.randint(50, 340)
v, h, g = 50, 100, 9.81

print(f"Odległość od celu: {odleglosc_od_celu}m. Trafienie nastąpi w zakresie [{odleglosc_od_celu - 5}, {odleglosc_od_celu + 5}]m.")

def trajektoria(alpha):
    alpha_rad = math.radians(alpha)
    t_max = (v * math.sin(alpha_rad) + math.sqrt((v * math.sin(alpha_rad))**2 + 2 * g * h)) / g
    t_values = [t_max * i / 99 for i in range(100)]  # 100 punktów na wykresie

    x_values = [v * math.cos(alpha_rad) * t for t in t_values]
    y_values = [h + v * math.sin(alpha_rad) * t - 0.5 * g * t**2 for t in t_values]

    plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values)
    plt.xlabel('Odległość (m)')
    plt.ylabel('Wysokość (m)')
    plt.xlim(0, max(x_values) + 10)
    plt.ylim(0, max(y_values) + 20)
    plt.grid(True)
    plt.savefig("trajektoria_pocisku.png")
    print("Wykres zapisany jako 'trajektoria_pocisku.png'.")

while True:
    alpha = float(input("Podaj kąt strzału: "))
    alpha_rad = math.radians(alpha)
    
    odleglosc_pocisku = v * math.cos(alpha_rad) * ((v * math.sin(alpha_rad) + math.sqrt((v * math.sin(alpha_rad))**2 + 2 * g * h)) / g)

    if odleglosc_od_celu - 5 <= odleglosc_pocisku <= odleglosc_od_celu + 5:
        print("Trafienie! Gratulacje!")
        trajektoria(alpha)
        break
    print("Pocisk", "nie doleciał" if odleglosc_pocisku < odleglosc_od_celu else "przeleciał za cel", "Spróbuj ponownie.")
