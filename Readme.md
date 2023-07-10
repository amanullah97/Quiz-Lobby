#Django-Quiz-App
Software Versions:
django==2.2.7
django-model-utils==3.1.2

"django-quiz-app: A Django-based Quiz Application for Multiple Choice Questions"

This Git repository contains a Django-based quiz application for multiple choice questions. The "django-quiz-app" allows users to participate in quizzes and answer multiple-choice questions.

### Instructions

1) Installations:
   - Ensure that Python is installed on your computer. If not, you can install it from [here](https://www.python.org).
   - Clone the repository using the following command:
     ```
     git clone https://github.com/amanullah97/Quiz-Lobby
     cd django-quiz-app
     ```

2) Installing Dependencies:
   - Install the required dependencies by running the following command:
     ```
     pip install -r requirements.txt
     ```

3) Migrations:
   - Apply migrations to set up the database by executing the following commands:
     ```
     python manage.py makemigrations
     python manage.py migrate
     ```

4) Create Superuser:
   - Create a superuser account to access the admin panel by running the command:
     ```
     python manage.py createsuperuser
     ```
   - Follow the prompts to enter a username and password for the superuser. The admin panel can be accessed at `localhost:8000/admin/`.

5) Running Locally:
   - Start the local development server by running the command:
     ```
     python manage.py runserver
     ```
   - The application will be accessible at `localhost:8000`.

This project provides a fully functional quiz application built with Django, enabling users to participate in quizzes and answer multiple-choice questions. It can be customized and extended to suit specific requirements, such as adding new quizzes or modifying the question format. The admin panel provides easy management of quizzes, questions, and user responses.



