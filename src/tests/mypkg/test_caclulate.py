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


def test_main_request(client):
    request_payload = (
        "(1.115,2.119), (1.108,2.220), (1.101,2.209), (1.110,2.209), (1.112,2.212)"
    )
    response = client.post("/calculate", data=request_payload)
    result = response.get_json()

    assert response.status_code == 200
    assert result is not None
    assert result == [
        [
            0.5040080000000002,
            0.5582240000000002,
            0.5562160000000002,
            0.5516980000000001,
            0.5522000000000001,
        ],
        [
            0.5582240000000002,
            0.6182720000000002,
            0.6160480000000002,
            0.611044,
            0.6116000000000001,
        ],
        [0.5562160000000002, 0.6160480000000002, 0.6138320000000002, 0.608846, 0.6094],
        [0.5516980000000001, 0.611044, 0.608846, 0.6039005, 0.60445],
        [0.5522000000000001, 0.6116000000000001, 0.6094, 0.60445, 0.6050000000000001],
    ]


def test_main_request_corrupted_data(client):
    request_payload = (
        r"(1.115,2.119), (1.108,2.220), (1.101,2.209), (1.110,2.209), (\xu002,2.212)"
    )
    response = client.post("/calculate", data=request_payload)
    result = response.get_json()

    assert response.status_code == 200
    assert result is not None
    assert result == [
        [
            0.5040080000000002,
            0.5582240000000002,
            0.5562160000000002,
            0.5516980000000001,
        ],
        [0.5582240000000002, 0.6182720000000002, 0.6160480000000002, 0.611044],
        [0.5562160000000002, 0.6160480000000002, 0.6138320000000002, 0.608846],
        [0.5516980000000001, 0.611044, 0.608846, 0.6039005],
    ]

