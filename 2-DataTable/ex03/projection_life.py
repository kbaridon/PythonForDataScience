import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import pandas as pd
from load_csv import load
# pip install matplotlib


def do_graph(gdp: pd.DataFrame, life: pd.DataFrame):
    """Take two Dataframes.
    Return a graph of it"""
    gdp = gdp["1900"]
    life = life["1900"]

    plt.plot(gdp, life, 'o')
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.title("1900")

    ax = plt.gca()
    ax.yaxis.set_major_locator(MultipleLocator(5))
    ax.set_xscale('log')
    ax.set_xticks([300, 1000, 10000])
    ax.set_xticklabels(['300', '1k', '10k'])

    plt.show()


def main():
    """Tester of do_graph function"""
    gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_data = load("life_expectancy_years.csv")
    do_graph(gdp, life_data)


if __name__ == "__main__":
    main()
