from flask import Flask
from flask import request
from flask import jsonify
import json
from io import StringIO
import re
import pandas as pd
import numpy as np

from app.invalid_usage import InvalidUsage
from app.validation import validate_greeting
from mypkg.greetings import say_hello_to
from mypkg.calculate import parse_number, filter_input


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

    try:
        # Ingest the data from the body here, trasform in a Python list
        # of tuples
        raw_input = [
            parse_number(x)
            for x in StringIO(request.get_data().decode("utf-8")).getvalue().split()
        ]

        # Transform the list in a Pandas dataframe, perform the
        # calculation, return the cov matrix in the response converted
        # into a list (should replace the empty list below)

        # raw_input type in str, need to convert them to float before convert them into DataFrame

        final_input = filter_input(raw_input)
        print(final_input)
        cov_matrix = np.cov(final_input)
        # jason.dumps only accpept str, convert result into str
        result = np.array2string(cov_matrix, precision=16)

        return json.dumps(result), 200
    except Exception:
        return "internal error", 500


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route("/")
def index():
    return "It Works! At home dir."


@app.route("/hello", methods=["POST"])
def hello():
    errors = validate_greeting(request)
    if errors is not None:
        print(errors)
        raise InvalidUsage(errors)
    greetee = request.json.get("greetee", None)
    response = {"message": say_hello_to(greetee)}
    return jsonify(response)


@app.route("/test", methods=["POST"])
def test():
    data = request.get_data().decode("utf-8")
    return json.dumps([data])
    # return "POST request"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)

