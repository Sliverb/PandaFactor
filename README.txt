Panda Factory

Source code layout:
[InternNest] Source code for the project
   \--- [HomePage] Application for the home page
    |-- [InterNest] Project settings
    |-- [RegisterBusiness] Ignore. Will get deleted. 
    |-- [static] Global static files
    |-- [templates] Global template files
    |-- [UserRegisteration] Application for registering users

[env]
  Virtualenv files. This directory is largely ignorable. 

[Mockups]
  Home to our early design mockups I'm too afraid to delete.

Getting started:
1) Get the virtual envornment running
    env\Scripts\activate
To stop using virtualenv, type "deactivate"
2) Start the server
    InternNest\manage.py runserver
3) In a web browser, visit:
    http://127.0.0.1:8000/register/business/

Tech Stack:
- Django 1.5.1
- Python 2.7.5
- JQuery 2.0.3 (doesn't support IE 8 and below)

© 2013 Siamese Cities