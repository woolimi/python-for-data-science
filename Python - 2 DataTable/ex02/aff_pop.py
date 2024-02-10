from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def _normalize_population(population: str) -> int:
    """
    Normalize population string to number
    """
    if population[-1] == "M":
        return int(float(population[:-1]) * 1e6)
    if population[-1] == "k":
        return int(float(population[:-1]) * 1e3)
    else:
        return int(float(population))


def _normalize_year(year: str) -> int:
    """
    Normalize year string to number
    """
    return int(year)


def main():
    """
    Load total population dataset and show graph of France.
    """
    country1 = "France"
    country2 = "South Korea"
    dataset = load("population_total.csv")
    if dataset is None:
        return
    data_fr = dataset[dataset["country"] == country1]
    data_ko = dataset[dataset["country"] == country2]
    convert_population = np.vectorize(_normalize_population)
    convert_year = np.vectorize(_normalize_year)

    years = convert_year(data_fr.columns[1:])
    population_fr = convert_population(data_fr.values[0][1:])
    population_ko = convert_population(data_ko.values[0][1:])
    # get max value of y axis
    maxY = max(max(population_fr), max(population_ko)) // 1e7 * 10

    plt.plot(years, population_fr, label=country1)
    plt.plot(years, population_ko, label=country2)
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.xticks(range(years[0], 2051, 40))
    plt.xlim(years[0], 2051)
    plt.ylabel("Population")
    y_ticks = [i * 1e6 for i in range(20, int(maxY + 1), 20)]
    plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
