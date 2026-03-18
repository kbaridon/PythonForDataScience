import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import matplotlib.ticker as ticker
import pandas as pd
from load_csv import load
# pip install matplotlib


def parse_number(nb: str) -> int:
    """Take a formated string and return an int"""
    if (nb.endswith("M")):
        return float(nb[:-1]) * 1_000_000
    if (nb.endswith("k")):
        return float(nb[:-1]) * 1_000


def parse_float(nb, pos) -> str:
    """Take a float and return a formated string"""
    if nb >= 1_000_000:
        val = nb / 1_000_000
        return f"{val:g}M"
    if nb >= 1_000:
        val = nb / 1_000
        return f"{val:g}k"
    return f"{nb:g}"


def do_graph(data: pd.DataFrame, key1: str, key2: str):
    """Take a Dataframe and a key value.
    Return a graph of it"""
    years = [c for c in data.columns if (int(c) <= 2050 and int(c) >= 1800)]
    data = data[years]
    pop = [parse_number(v) for v in data.loc[key1]]
    pop2 = [parse_number(v) for v in data.loc[key2]]

    plt.plot(years, pop2, label=key2, color="blue")
    plt.plot(years, pop, label=key1, color="green")
    plt.legend(loc="lower right")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population Projections")

    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(40))
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(parse_float))
    ax.yaxis.set_major_locator(MultipleLocator(20_000_000))

    plt.show()


def main():
    """Tester of do_graph function"""
    data = load("population_total.csv")
    do_graph(data, "France", "Belgium")


if __name__ == "__main__":
    main()
