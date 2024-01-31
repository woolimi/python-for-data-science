from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Load GDP and life expectancy dataset and show graph of
    1900 projection per country
    """
    life_dataset = load("life_expectancy_years.csv")
    gdp_dataset = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    if life_dataset is None or gdp_dataset is None:
        return
    gdp_1900 = gdp_dataset['1900']
    life_1900 = life_dataset['1900']
    plt.scatter(gdp_1900, life_1900)
    plt.title('1900')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.show()


if __name__ == "__main__":
    main()
