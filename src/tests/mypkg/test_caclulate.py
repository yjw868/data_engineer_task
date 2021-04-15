from flask import Flask
from flask import request
import json
from io import StringIO
import re
import pandas as pd
import numpy as np

import app.main


# app = Flask(__name__)


# @app.route("/test", methods=["POST"])
# def test():
#     data = request.get_data()
#     return jsonfy(data)

clean_input = "(1.115,2.119)"

corrupted_input = (
    r"(1.115,2.119), (1.108,2.220), (1.101,2.209), (1.110,2.209), (\xu002,2.212)"
)


def test_connection(client):
    response = client.get("/")
    assert response.status_code == 200


def test_cal_request(client):
    response = client.post("/test", data=clean_input)
    assert response.get_data().decode("utf-8") == "test"
