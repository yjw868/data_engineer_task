from flask import Flask
from flask import request
import json
from io import StringIO
import re


app = Flask(__name__)


def parse(x):
    """
	The parser of pairs
	"""

    y = re.search("\((.*),(.*)\)", x).group(1, 2)

    if y:
        return y[0], y[1]

    return None, None


@app.route("/calculate", methods=["POST"])
def calculate():
    """
	The endpoint that perform the computation
	"""

    if not request.get_data():
        return "Missing message in the body of the request.", 501

    # try:
    # Ingest the data from the body here, trasform in a Python list
    # of tuples
    #     _ = [parse(x) for x in StringIO(
    #         request.get_data().decode('utf-8')).getvalue().split()]

    #     # Transform the list in a Pandas dataframe, perform the
    #     # calculation, return the cov matrix in the response converted
    #     # into a list (should replace the empty list below)

    #     return json.dumps([]), 200
    # except Exception:
    #     return "internal error", 500
    return "Hi"


@app.route("/")
def hello():
    return "It Works!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)

