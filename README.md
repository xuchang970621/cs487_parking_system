# cs487_parking_system

1. install django
2. Setting up basics (from chang, reference page: https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
    
    Already done:
      ```shell
      django-admin startproject cs487
      python manage.py startapp parking
      ```
      added index page
      
3. Datatbase (from chang, reference page: https://docs.djangoproject.com/en/3.0/intro/tutorial02/)
 
    Already done:
      ```shell
      python manage.py migrate
      python manage.py makemigrations parking
      python manage.py createsuperuser  # admin, (empty email), 123456
      ```
      added models in parking/models.py
      added parking app in cs487/settings.py
      added models to parking/admin.py
      
IMPORTANT commands:
    ```shell
    python manage.py runserver
    ```
