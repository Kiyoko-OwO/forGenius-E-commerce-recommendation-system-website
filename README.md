# capstone-project-3900-w16a-forgenius

# Group: forGenius W16A
# Project: E-Commerce Recommender System

## Group members:


##### Kaiyu Chen 	  z5248118  Scrum Master (Also do backend)
##### Hanqing Guan  z5213081  Developer(Backend&Database)
##### Minghao Cai   z5231859  Developer(Frontend)
##### Tianchen Yang z5248280 	Developer(Backend)
##### Wenxin Ma     z5248280 	Developer(Frontend)

## Structure:
##### /forGenius: Software backend folder.
##### /ui: Software frontend folder.
##### /UI_design: UI design's files.
##### /static: supported files for frontend.

## Setup Guide:(detailed information in User Setup guide.pdf) 
### Prerequisite

This project backend is based on Python3 and Django. The frontend is based on Nodejs and NPM. Please ensure your machine has these environments. You can check them via the command:
```
$ python3 --version 
$ node -v
$ npm -v
```

There is an example in the following picture. This is the result of running these commands in the vlab. If you use these commands and get the versions like the picture (different version is fine), your environment is ready.
<img width="275" alt="image" src="https://user-images.githubusercontent.com/50103174/141690887-d4d33fd7-f90b-4331-8e29-23ee79e8a166.png">

If you don’t have these environment in your machine, please go to https://www.python.org/downloads/ and https://nodejs.org/en/ to download and setup the environment of Python3 and NodeJS (NPM will come with the NodeJS).
And also, this project’s backend needs the VSCode to run. If you don’t have this application, please download it via https://code.visualstudio.com.

### Setup
This setup guide is based on the VLAB environment.

First of all, download the project’s zip file and extract it to a folder. Open this folder via VScode.

#### Backend
1. Installed “Python”, “Django” extensions in VSCode.
2. Setup the venv for backend in backend folder.
```
$ python3 -m venv venv
```
Select the interpreter in VScode and choose "venv" one. 
Then, open a new termianl, and input the command.
(details in User Setup guide.pdf)
```
$ pip3 install setuptools_rust
$ pip3 install pyjwt
$ pip3 install django
$ pip3 install django-cors-headers
```
3. Setup VSCode's configuration to run the backend(details in User Setup guide.pdf)


#### Frontend

Use the terminal to open the project’s folder.

Then, input the following command in the terminal.
```
$ cd ui
$ npm install --force
$ npm run serve
```
After that and wait a second, your terminal should show the following picture.
(Note: The reason why we use “npm install --force” is because in this project,  “less border” package’s version is too low; there may be some useless errors here if you use the command  without “--force”.).

#### Open
Make sure you finish all steps of backend and frontend, and both of them are running like the last picture in the last step of their instructions.

Open the URL http://localhost:xxxx/ (the local one, the last 4 numbers may be different)  provided by the “npm run serve”. 
