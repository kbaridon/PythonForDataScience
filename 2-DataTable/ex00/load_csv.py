import pandas as pd
# pip install pandas


def load(path: str) -> pd.DataFrame:
    """Take a path to a csv.
    Return a DataFrame of this csv."""
    try:
        dataset = pd.read_csv(path, index_col=0)
        print("Loading dataset of dimensions", dataset.shape)
        return (dataset)
    except (FileNotFoundError, PermissionError):
        raise AssertionError("bad parameters") from None


def main():
    """Tester of load function"""
    print(load("life_expectancy_years.csv"))
    # print("=====================")
    # print(load("atasgoin"))  # Test 1: FileNotFoundError
    # print("=====================")
    # print(load("truc.csv"))  # Test 2: PermissionError
    return


if __name__ == "__main__":
    main()
