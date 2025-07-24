import matplotlib.pyplot as plt
import random

from aco import AntColony


plt.style.use("dark_background")


COORDS = tuple((random.randint(0, 100), random.randint(0, 100)) for _ in range(30))


def plot_nodes(w=12, h=8):
    for x, y in COORDS:
        plt.plot(x, y, "g.", markersize=15)
    plt.axis("off")
    fig = plt.gcf()
    fig.set_size_inches([w, h])


def plot_all_edges():
    paths = ((a, b) for a in COORDS for b in COORDS)

    for a, b in paths:
        plt.plot((a[0], b[0]), (a[1], b[1]))


plot_nodes()

def run_experiment(coords, ant_count, alpha, beta, evap_rate, pheromone_const, iterations):
    plt.figure()
    plot_nodes()
    colony = AntColony(
        coords,
        ant_count=ant_count,
        alpha=alpha,
        beta=beta,
        pheromone_evaporation_rate=evap_rate,
        pheromone_constant=pheromone_const,
        iterations=iterations
    )
    path = colony.get_path()
    for i in range(len(path) - 1):
        plt.plot(
            (path[i][0], path[i + 1][0]),
            (path[i][1], path[i + 1][1]),
            "r-"
        )
    plt.title(f"Ants: {ant_count}, α: {alpha}, β: {beta}")
    plt.show()


# Eksperyment 1 – zrównoważone parametry
run_experiment(COORDS, ant_count=300, alpha=1.0, beta=2.0, evap_rate=0.4, pheromone_const=1000.0, iterations=300)

# Eksperyment 2 – szybkie parowanie, silny wpływ heurystyki
run_experiment(COORDS, ant_count=200, alpha=0.5, beta=3.0, evap_rate=0.8, pheromone_const=500.0, iterations=300)

# Eksperyment 3 – więcej mrówek, większy nacisk na feromon
run_experiment(COORDS, ant_count=500, alpha=2.0, beta=1.0, evap_rate=0.3, pheromone_const=2000.0, iterations=300)


# Wnioski z eksperymentów:
# - Większa liczba mrówek (ant_count) poprawia jakość rozwiązania, ale znacznie wydłuża czas obliczeń.
# - Wyższe beta (znaczenie heurystyki, np. odległości) pozwala szybciej znaleźć dobre trasy, ale czasem pomija optymalne.
# - Duża wartość alpha (nacisk na feromon) przy niskim beta może prowadzić do szybkiej zbieżności, ale na gorsze rozwiązania.
# - Zbalansowane parametry (alpha ≈ 1, beta ≈ 2) zwykle dają dobre wyniki.
# - Wysoki współczynnik parowania (evap_rate) powoduje większą eksplorację – mrówki testują więcej tras.
