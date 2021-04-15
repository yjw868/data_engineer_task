# Lists of all the issues I came cross during this project

- Github initial push error
  - Error when run ```git push origin master```
  - When create the repo on github, the default name is main
  - Solution: change the name on Github
  
- Docker building error with "tiangolo/uwsgi-nginx-flask-docker"
  - pandas can't be installed with alpine version as it doesn't have the compiler to build Numpy
  - Solution: Use the full version of python image instead
    - "tiangolo/uwsgi-nginx-flask:python3.6"

- pip install dependency issue
  - This is error is real hidden when testing with default app.man
  - #TODO Haven't figured out way to display the error directly when run the main.py
  - This became apparent when run pytest

- pip install error during the docker build
  - the lastest numpy and pandas installed successfully in my venv, but failed during the build
  - After i bit retesting then i realised it cause was the python version in the base docker image doesn't match my venv
  - D
