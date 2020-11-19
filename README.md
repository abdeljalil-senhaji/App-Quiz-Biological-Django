# App-Quiz-Biological-Django


Django quiz application on microscopy image identification - biological subject (*App-Quiz-Biological-Django*)
The user can choose to select the desired quiz (__recognize-types-microscopy__ - several levels, recognize the cell type presented, the original ones presented).
The information for the images is retrieved from the site of the Cell Image Library.
For front-end designing I have used Bootstrap 4 Form Theme and Javascript.


## Current features

Features of quiz:

- A quiz category (Microscopy Test Quiz) with several questions

- Quiz allows you to display two images next to the question

- 4 choices for each question.

- Correct answers can be displayed after each question

- An explanation for each question result can be given

- Type of multiple choice question

- Personalized message displayed for those who pass or fail a quiz

- the explore box to display all the images with the description next to each image

## Instructions


### Install miniconda

1. https://docs.conda.io/en/latest/miniconda.html
2. Download Python 3.7, Miniconda Linux 64-bit
3. bash mini...
    - Select installation path
4. Verify conda or add path to _.bashrc_

### Create a conda environment

$ conda create --name djangoenv python=3.7
$ Activate conda enviroment
$ conda activate djangoenv

### Install packages

$ conda install --name newdjango django==3.0.3
$ conda install --name newdjango sqlparse==0.3.1

Verify that django is installed : pip freeze

### create project Django : 

$ django-admin startproject (project_name)


### Create an application

- Start an application:

$ django-admin startapp (app_name)

### Migrations

To run migrations.

$ python manage.py makemigrations
$ python manage.py migrate


### Create superuser

To create super user run.

$ python manage.py createsuperuser

After running this command it will ask for username, password. You can access admin panel from localhost:8000/admin/


### Running locally

To run at localhost. It will run on port 8000 by default.

$ python manage.py runserver

## Usage

$ django-admin <command> [options] (help --commands)
$ manage.py <command> [options]
$ python -m django <command> [options]


## Author

__Abdeljalil__ __SENHAJI__ __RACHIK__ Beginner in development...

