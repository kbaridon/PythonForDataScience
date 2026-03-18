import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import pandas as pd
from load_csv import load
# pip install matplotlib


def do_graph(data: pd.DataFrame, key: str):
    """Take a Dataframe and a key value.
    Return a graph of it"""
    years = list(map(int, list(data)))
    plt.plot(years, data.loc[key])
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.title("France Life expectancy Projections")

    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(40))

    plt.show()


def main():
    """Tester of do_graph function"""
    data = load("life_expectancy_years.csv")
    do_graph(data, "France")


if __name__ == "__main__":
    main()
