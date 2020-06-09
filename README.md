# Shopping Django Project

In order to get it to work:

## Create a virtual env
`python -m venv store-env`

## Activate the virtual env
If you are on mac or linux: `source store-env/bin/activate` 

On windows: first run `cd store-env/Scripts` then run `activate`

## install Django
`pip install django`

## Nigrate existing changes in models
Inside this folder run: 

`python manage.py migrate`

## Run the project
`python manage.py runserver`

## Go to your browser and acess one of the urls:
* [localhost:8000/admin/](localhost:8000/admin/)
* [localhost:8000/products/home/](localhost:8000/products/home/)
* [localhost:8000/products/list/](localhost:8000/products/list/)
