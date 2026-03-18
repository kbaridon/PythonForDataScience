from typing import Any


def ft_mean(tab: list[float]):
    """Take a tab and return the mean of it"""
    result = 0
    for i in tab:
        result += float(i)
    return result / len(tab)


def ft_median(tab: list):
    """Take a tab and return the median of it"""
    size = len(tab) / 2
    if (size % 1 == 0):
        return (tab[int(size - 1)] + tab[int(size)]) / 2
    return (tab[int(size - 0.5)])


def ft_quartile(tab: list[float]):
    """Take a tab and return the quartiles of it"""
    q_25 = len(tab) // 4
    q_75 = q_25 * 3
    return [float(tab[q_25]), float(tab[q_75])]


def ft_std(tab: list[float]):
    """Take a tab and return the standard deviation of it"""
    return (ft_var(tab) ** 0.5)


def ft_var(tab: list[float]):
    """Take a tab and return the variance of it"""
    mean = ft_mean(tab)
    result = 0
    for val in tab:
        result += (val - mean) ** 2
    return (result / len(tab))


def ft_statistics(*args: Any, **kwarg: Any) -> None:
    """Take a list of numbers and a list of string.
    Return the value of the strings on the numbers list.
    Are handle: mean, median, quartile, std, var"""
    possible = {"mean": ft_mean, "median": ft_median,
                "quartile": ft_quartile, "std": ft_std,
                "var": ft_var}
    tab = list(args)
    tab.sort()
    for k, val in kwarg.items():
        if (val in possible and len(tab) == 0):
            print("ERROR")
        elif (val in possible):
            print(f"{val} : {possible[val](tab)}")


def main():
    """Tester of ft_statistics function"""
    ft_statistics(1, 42, 360, 11, 64,
                  toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")
    # print("---")
    # ft_statistics()


if __name__ == "__main__":
    main()
