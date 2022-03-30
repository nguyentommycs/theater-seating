# theater-seating

<a name="project-setup"></a>
# Project Setup
1. Clone this repo 
    ```sh
     git clone https://github.com/nguyentommycs/movieseating.git
    ``` 

<a name="django-setup"></a>
## Django Setup

1. create a virtual environment
```sh
python -m venv env
```
2a. For Linux, activate the virtual environment<br />
```sh
source env/bin/activate
```
2b. For Windows, activate the virtual environment<br />
```sh
env\Scripts\activate.bat
```
3. install all the dependencies 
```sh
pip3 install -r requirements.txt
```
4. cd into the backend folder
```sh
cd backend
```
5. run the server
```sh
python manage.py runserver
```


<a name="react-setup"></a>
## React Setup (React must be running on another terminal)
1. cd into the frontend folder on a separate terminal
```sh 
cd frontend
``` 
2. install required dependencies. Your terminal should tell you which dependencies you're missing. Simply install the missing ones.
```sh
npm install
```
3. activate the react server
```sh
npm start
```
