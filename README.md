# Django Tutorial 01
### Based on: [Writing your first Django app Tutorial](https://docs.djangoproject.com/en/2.1/intro/tutorial01/)
 
 ### How to run the the project
 
 First, clone this repository executing the following command:
 ```sh
$ git clone https://github.com/magallegos1996/Django-Tutorial-01.git
```
Once you've cloned this repo, please change to the root directory:
 ```sh
$ cd Django-Tutorial-01
```
Then, execute the following command to create a python virtual environment
 ```sh
$ py -m venv env
```
This will create a directory called  ```cd env```. Enter to this directory using the following command
 ```sh
$ cd env
```
Next, execute the  ```activate.bat``` that is inside the ```Scripts``` directory. Please, follow this steps.
 ```sh
$ cd Scripts
$ activate.bat
```
Now, you have to return to ```Django-Tutorial-01``` folder so you can install all the requirements needed to run this project. In order to do so, from the ```Django-Tutorial-01``` directory, execute this.
 ```sh
$ pip install -r requirements.txt
```
At this point, you will be able to run the project. But first, you have to do some additional steps. 

Place yourself into ```my site``` directory
 ```sh
$ cd mysite
```
Run the following command to make migrations
 ```sh
$ py manage.py makemigrations
```
Then, run those migrations throught this command
```sh
$ py manage.py migrate
```
And finally, run the server with the follwing command
 ```sh
py manage.py runserver
```
Open your browser and go to: http://localhost:8000/polls or http://localhost:8000/users
