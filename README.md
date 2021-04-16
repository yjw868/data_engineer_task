## data_engineer_task

This is the final repo for the DE test.

- Testing
  Run the following step to verify the final result
  - ``` git clone https://github.com/yjw868/data_engineer_task.git ```
  - ``` cd data_engineer_task ```
  - start docker then run ```docker-compose build && docker-compose up```
  - run ```curl -X POST -H "Content-Type: text/plain" \                                                    -d '(1.115,2.119), (1.108,2.220), (1.101,2.209), (1.110,2.209), (1.112,2.212)' \      http://localhost:5000/calculate```
  - Expected result "[[0.5040080000000002, 0.5582240000000002, 0.5562160000000002, 0.5516980000000001, 0.5522000000000001], [0.5582240000000002, 0.6182720000000002, 0.6160480000000002, 0.611044, 0.6116000000000001], [0.5562160000000002, 0.6160480000000002, 0.6138320000000002, 0.608846, 0.6094], [0.5516980000000001, 0.611044, 0.608846, 0.6039005, 0.60445], [0.5522000000000001, 0.6116000000000001, 0.6094, 0.60445, 0.6050000000000001]]"
  - run ```curl -X POST -H "Content-Type: text/plain" \                                                    -d '(1.115,2.119), (1.108,2.220), (1.101,2.209), (1.110,2.209), (1.112,2.212)' \      http://localhost:5000/calculate```
      - - Expected result "[[0.5040080000000002, 0.5582240000000002, 0.5562160000000002, 0.5516980000000001], [0.5582240000000002, 0.6182720000000002, 0.6160480000000002, 0.611044], [0.5562160000000002, 0.6160480000000002, 0.6138320000000002, 0.608846], [0.5516980000000001, 0.611044, 0.608846, 0.6039005]]]"

- run pytest
  - Enable venv first then pull the repo and install the requiremnets
  - ``` cd data_engineer_task/src ```
  - ```python3 -m app.main```
  - ``` python -W ignore::DeprecationWarning -m pytest tests -s -v ```
  
- TODO
  - Add pytest coverate
  - Deploy to AWS
