# Main tasks

- [x] Create a public git repo
- Create responsive service
  - Calculate covariance matrix via HTTP request.
  - This is an example of working request once the container runs:
    - $ curl -X POST -H "Content-Type: text/plain" \                                                    -d '(1.115,2.119), (1.108,2.220), (1.101,2.209), (1.110,2.209), (1.112,2.212)' \      <http://localhost:5000/calculate>                                                   [[0.5040080000000002, 0.5582240000000002, 0.5562160000000002, 0.5516980000000001, 0.5522000000000001], [0.5582240000000002, 0.6182720000000002, 0.6160480000000002, 0.611044, 0.6116000000000001], [0.5562160000000002, 0.6160480000000002, 0.6138320000000002, 0.608846, 0.6094], [0.5516980000000001, 0.611044, 0.608846, 0.6039005, 0.60445], [0.5522000000000001, 0.6116000000000001, 0.6094, 0.60445, 0.6050000000000001]]
  - The request should work also in case of corrupted values included in the body of the requests:
    - curl -X POST -H "Content-Type: text/plain" \                                                    -d '(1.115,2.119), (1.108,2.220), (1.101,2.209), (1.110,2.209), (\xu002,2.212)' \      <http://localhost:5000/calculate>                                                   [[0.5040080000000002, 0.5582240000000002, 0.5562160000000002, 0.5516980000000001], [0.5582240000000002, 0.6182720000000002, 0.6160480000000002, 0.611044], [0.5562160000000002, 0.6160480000000002, 0.6138320000000002, 0.608846], [0.5516980000000001, 0.611044, 0.608846, 0.6039005]]

  - [ ] Use Numpy: v1.15.4 and Pandas: v.0.23.4
  
  - Main.py  
    **Not suppose to modify any other part of the code outside the function decorated with the endpoint router of Flash**
    - [ ] endpoint - /calculate
    - [x ] Calculate covariance matrix
    - [ ] Cleaning input if needed
      - [ ] removing **nan**
      - [ ] removing corrupted values
    - [x] Transform the data input into Padas dataframe
    - [x] Return serialised in a JSON-compliant format

  - HTTP request
    - [x] POST:  curl -X POST -H "Content-Type: text/plain" -d
    - [ ] Request should work in case of corrupted values

- docker
  - [x] use docker-compose
  - [x] use image from <https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/>
  - [x] port binding in order to make the microservice listen to port **5000**
  - [x] Copy the Flask code in the /app directory in the container (read the linked documentation of the image for further details in order to run the container).

- Test case
  - [ ] Test
