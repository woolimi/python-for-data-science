from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Load life expectancy dataset and show graph of France.
    """
    country = "France"
    dataset = load("life_expectancy_years.csv")
    if dataset is None:
        return
    data_fr = dataset[dataset["country"] == country]
    years = data_fr.columns[1:]
    life_expectancy = data_fr.values[0][1:]

    plt.plot(years, life_expectancy, label=country)
    plt.title(f"{country} Life expectancy Projections")
    plt.xlabel("Year")
    plt.xticks(years[::40])
    plt.ylabel("Life expectancy")
    plt.yticks(range(30, 91, 10))
    plt.show()


if __name__ == "__main__":
    main()
