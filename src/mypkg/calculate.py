# from flask import Flask
# from flask import request
# from flask import jsonify
# import json
from io import StringIO

import pandas as pd

# import numpy as np
import re


def parse(x):
    """
	The parser of pairs
	"""

    y = re.search("\((.*),(.*)\)", x).group(1, 2)

    if y:
        return y[0], y[1]

    return None, None


def parse_number(x):
    try:
        y = re.match("^\((\d*\.?\d*),(\d*\.?\d*)\),?$", x).group(1, 2)

        if y:
            return y[0], y[1]
    except AttributeError:
        return None, None


def catch(func, handle=lambda e: e, show_err=True, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        if not show_err:
            return handle(e)
        else:
            pass


def convt_float(x):
    try:
        return float(x[0]), float(x[1])
    except ValueError:
        return False


def filter_input(x):
    df = pd.DataFrame(x, columns=["A", "B"])
    df = df[~df["A"].isnull()]
    return df

