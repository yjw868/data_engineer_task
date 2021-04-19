# Lists of all the issues I came cross during this project

- Github initial push error
  - Error when run ```git push origin master```
  - When create the repo on github, the default name is main
  - Solution: change the name from main to master on Github
  
- Docker building error with "tiangolo/uwsgi-nginx-flask-docker"
  - pandas can't be installed with alpine version as it doesn't have the compiler to build Numpy
  - Solution: Use the full version of python image instead
    - "tiangolo/uwsgi-nginx-flask:python3.8"

- pip install dependency issue
  - This error is real hidden when testing with default app.man
  - [x]TODO Haven't figured out way to display the error directly when run the main.py. test_main etc added
  - This issue became apparent when run pytest
  - Add additional tests to check status, connection to ensure the server is running correctly

- pip install error during the docker build
  - the lastest numpy and pandas installed successfully in my venv, but failed during the build
  - After retesting then i realised the cause was due to python version in the base docker image doesn't match my venv
  
- app.main error when running with docker build
  - the app worked find with local version of python3.8
  - Initially the docker image use python3.6
  - I didn't realise the numpy and pandas dependency are quite different between those two version
  - Solution:
    - Update docker base image to 3.8
    - Use the latest numpy and pandas
    - Haven't got enough time to install python3.6 locally to test it which was required from the task

- 'docker build' error: "failed to solve with frontend dockerfile.v0"
  - fail to build the image after updating Docker Desktop
  - clean / Purge data didn't work
  - reinstall docker desktop which trigger wsl2 crash report
  - solution:
    - download the latest docker from the official website
    - reinstiall docker desktop and reboot the machine
    - Purge data

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

- Pytest failed on app.main import
  - solution: follow the structure based on <https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada>
