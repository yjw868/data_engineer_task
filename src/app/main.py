from flask import Flask
from flask import request
import json
from io import StringIO
import re
import pandas as pd
import numpy as np


app = Flask(__name__)


def parse(x):
    """
	The parser of pairs
	"""

    y = re.search("\((.*),(.*)\)", x).group(1, 2)

    if y:
        return y[0], y[1]

    return None, None


# @app.route('/calculate', methods=['POST'])
# def calculate():
#     """
#     The endpoint that perform the computation
#     """

#     if not request.get_data():
#         return "Missing message in the body of the request.", 501

#     try:
#         # Ingest the data from the body here, trasform in a Python list
#         # of tuples
#         _ = [parse(x) for x in StringIO(
#             request.get_data().decode('utf-8')).getvalue().split()]

#         # Transform the list in a Pandas dataframe, perform the
#         # calculation, return the cov matrix in the response converted
#         # into a list (should replace the empty list below)

#         return json.dumps([]), 200
#     except Exception:
#         return "internal error", 500"


@app.route("/calculate", methods=["POST"])
def calculate():
    """
	The endpoint that perform the computation
	"""

    if not request.get_data():
        return "Missing message in the body of the request.", 501

    try:
        # Ingest the data from the body here, trasform in a Python list
        # of tuples
        raw_input = [
            parse(x)
            for x in StringIO(request.get_data().decode("utf-8")).getvalue().split()
        ]

        # Transform the list in a Pandas dataframe, perform the
        # calculation, return the cov matrix in the response converted
        # into a list (should replace the empty list below)

        # raw_input type in str, need to convert them to float before convert them into DataFrame
        # TODO add a filter to remove corrupted input
        input = [(float(x), float(y)) for x, y in raw_input]
        df = pd.DataFrame(input)
        print(df)
        final_input = df.to_numpy()

        cov_matrix = np.cov(final_input)
        # jason.dumps only accpept str, convert result into str
        result = np.array2string(cov_matrix, precision=16)

        return json.dumps(result), 200
    except Exception:
        return "internal error", 500


# @app.route("/")
# def hello():
#     return "It Works!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)

