Prerqeuisites

The requiremnts are written in
https://github.com/Aditya-d-r/calculator/blob/main/requirements.txt

Code:

the main code is written in
https://github.com/Aditya-d-r/calculator/blob/main/app/main.py

Its a simple calculator add supporting floats for addition, substartction, multiplication and division

the test cases are written in 
https://github.com/Aditya-d-r/calculator/blob/main/app/tests/test_calculator.py

running standard test cases.

Workflow
The workfow is declared in 
https://github.com/Aditya-d-r/calculator/blob/main/.github/workflows/ci.yml

Description:
base:
We use ububtu as the base image environment.
python:
Python version is set to 3.9
pip:
the dependencies are read from the requiremnst file and installed.
test:
the tests are run on pylint

pylint:
pylint is etup only on main.py in apps.
the pass score is set to 8.

Docker build:
the build is done using docker file
https://github.com/Aditya-d-r/calculator/blob/main/Dockerfile
wich creates our base entry point using uvicorn.

docker login:
the credentials are saved in secrets

docker push:
the pushedimage is saved to docker hub
adityadrex/calculator:latest

Deployment.

the deployemnt is done on local argocd instance on minikube hence you don't see a reference here
the file taht is being used is https://github.com/Aditya-d-r/calculator/blob/main/k8s/argocd-app.yaml

the k8s service detalis are mentioned in k8s folder
