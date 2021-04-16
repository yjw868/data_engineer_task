from flask import Flask
from flask import request
import json
from io import StringIO
import re
import pandas as pd
import numpy as np
import pytest
from mypkg.calculate import parse, parse_number

import app.main


# app = Flask(__name__)


# @app.route("/test", methods=["POST"])
# def test():
#     data = request.get_data()
#     return jsonfy(data)

clean_input = (
    "(1.115,2.119), (1.108,2.220), (1.101,2.209), (1.110,2.209), (1.112,2.212))"
)

corrupted_input = (
    r"(\xu002,2.212), (1.115,2.119), (1.108,2.220), (1.101,2.209), (1.110,2.209)"
)


def test_connection(client):
    response = client.get("/")
    assert response.status_code == 200


def test_cal_request(client):
    response = client.post("/test", data=clean_input)
    assert (
        response.get_data().decode("utf-8")
        == '["(1.115,2.119), (1.108,2.220), (1.101,2.209), (1.110,2.209), (1.112,2.212))"]'
    )


def test_parse_accept():
    assert parse("(1,2)") == ("1", "2")


# def test_parse_fail():
#     with pytest.raises(StringIO("(\xu002, 2,212)".decode("utf-8"))) as exc_info:
#         return exc_info


def test_parse_catch():
    y = [parse(x) for x in StringIO(clean_input)]
    assert y == ["(1.115,2.119), (1.108,2.220), (1.101,2.209), (1.110,2.209)"]


def test_data_filter():

    y = [parse_number(x) for x in StringIO(corrupted_input)]
    print(y)
    df = pd.DataFrame(y)
    print(df)
    final_input = df.to_numpy()
    print(final_input)
    assert len(df.columns) == 2

