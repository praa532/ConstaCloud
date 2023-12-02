# ConstaCloud

# Django Student Information System

A simple Django project for managing student information.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)

## Requirements

Make sure you have the following installed:

- Python (3.11 recommended)
- Django
- Django REST Framework

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/praa532/ConstaCloud.git
   cd ConstaCloud

2. Install dependencies:

    ```bash
    pip install -r requirements.txt

3. Run migrations:

    ```bash
    python manage.py migrate

4. Create a superuser for admin access:

    ```bash
    python manage.py createsuperuser

5. Start the development server:

    ```bash
    python manage.py runserver

6. Open your browser and go to http://localhost:8000/admin/ to log in with the superuser credentials.

## Project Structure

ConstaCloud/
|-- marksheet/
|   |-- migrations/
|   |-- templates/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- serializers.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|-- studentmarksheet/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- users/
|   |-- migrations/
|   |-- templates/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- serializers.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|-- manage.py
|-- templates
|-- static
|-- requirements.txt
your_project/: Django project folder.
your_app/: Django app folder containing models, views, serializers, etc.
migrations/: Database migration files.
templates/: HTML templates (if using Django templates).

## Usage
1. Run the development server:

    ```bash
    python manage.py runserver

## Access the API endpoints:

# API-style response for students:

- /getstudents?class=4: Retrieve a list of students for a specific class in API-style response.

- Example:

    ```bash
    curl http://localhost:8000/getstudents?class=4
    
1. HTML-rendered page for students:

- /renderedstudents?class=4: View a paginated HTML-rendered page of students for a specific class.

- Example:

Open http://localhost:8000/getstudents?class=4 in your browser.

API-style response with data selection for students:

- /getstudents?data=name,roll,score,total,class: Retrieve a list of students in API-style response with specific data fields.

- Example:

    ```bash
    curl http://localhost:8000/getstudents?data=name,roll,score,total,class

2. Access the admin interface at http://localhost:8000/admin/ using the superuser credentials created during installation.

3. Access API endpoints at http://localhost:8000/

4. Access API endpoints at http://localhost:8000/users/register

4. Access API endpoints at http://localhost:8000/users/login

4. Access API endpoints at http://localhost:8000/getstudents


## API Endpoints
1. /users/register/: Create an account.
2. /users/login/ : Login to access the data and modify
3. /: Create students
4. getstudents/: List students.


## Contributing

Contributions are welcome! Please follow our contribution guidelines.


