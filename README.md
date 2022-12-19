# Django_Project
Steps to start this project - tusing Python 3.7.8 and Django 4.1.4 - writen on the VS Code IDE

1. Migrate the Model using the following commands from the Anaconda Prompt/terminal:-
python migrate.py makemigrations DemocranceApp
python migrate.py makemigrations 
python migrate.py migrate DemocranceApp
python migrate.py migrate 

2. Create a super user as an admin by writing this command then following the steps:-
python manage.py createsuperuser

3.please, use the fixture files of the project to load some data into the project after the model migration with the following commands:-
python manage.py loaddata DemocranceApp/fixtures/Customer.json --app DemocranceApp.Customer
python manage.py loaddata DemocranceApp/fixtures/Policy.json --app DemocranceApp.Policy
python manage.py loaddata DemocranceApp/fixtures/Policy_History.json --app DemocranceApp.Policy_History

#Please note that this project is only created for Demo purposes and may contain some hard-coded sections or some un-secured code blocks added to complete the demo
