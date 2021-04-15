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

- app.main error when running with docker build
  - the app worked find with local version of python3.8
  - Initially the docker image use python3.6
  - I didn't realise the numpy and pandas dependency are quite different between those two version
  - Solution:

- 'docker build' error: "failed to solve with frontend dockerfile.v0"
  - fail to build the image after updating Docker Desktop
  - clean / Purge data didn't work
  - reinstall docker desktop which trigger wsl2 crash report
  - solution: reinstiall docker desktop and reboot the machine

- Indentation error
  - Each time on save need to run vscode convert space to tab
  - Potentially due to the conflict with javascript setting or due ot WSL remote setting
  - #TODO need to find a perennate fix in the setting.json

- **Dependency Issue**
  - the solution was working fine when test locally
  - POST request never worked from the final docker build
  - There is no obvious clue in the log which will indicate the cause
  - Solution:
    - update the docker image to python3.8
    - use numpy 1.16.5
    - user pandas 1.2.4
