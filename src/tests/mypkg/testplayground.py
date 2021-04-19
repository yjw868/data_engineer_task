import re
import pandas as pd


def parse_number_test(x):
    try:
        y = re.match("^\((\d*\.?\d*),(\d*\.?\d*)\),?$", x).group(1, 2)

        if y:
            return y[0], y[1]
    except AttributeError:
        return None, None


a = [
    parse_number_test(x)
    for x in r"(1.115,2.119), (1.108,2.220), (1.101,2.209), (1.110,2.209), (\xu002,2.212))".split()
]

b = [
    x
    for x in "(1.115,2.119), (1.108,2.220), (1.101,2.209), (1.110,2.209), (1.112,2.212)".split()
]

df = pd.DataFrame(a, columns=["A", "B"])
print(df)

df1 = df[~df["A"].isnull()]
print(df1)

