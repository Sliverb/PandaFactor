Source code layout:
[InternNest] Source code for the project
   \--- [CreateJob] Form for creating a job. Contains the Job model.
    |-- [HomePage] Application for the home page and terms of service.
    |-- [InterNest] Project wide settings
    |-- [Profile] User profile page
    |-- [static] Globally used static files
    |-- [templates] Global template files
    |-- [UserRegisteration] Application for registering users. Contains the InternestUser model.

[env]
  Virtualenv files. This directory is ignorable. 

[Mockups]
  Home to our early design mockups I'm too afraid to delete.

Getting started:
1) Get the virtual envornment running
    env\Scripts\activate
To stop using virtualenv, type "deactivate"
2) Start the server
    python InternNest\manage.py runserver
3) In a web browser, visit:
    http://localhost:8000/

Tech Stack:
- Django 1.5.2
- South 0.8.2 (Django DB migration)
- Python 2.7.5
- JQuery 1.10.2
- Tes Test
