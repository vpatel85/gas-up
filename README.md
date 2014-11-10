gas-up
======

Picking the perfect lunch destination


1. create virtual environment 
```virtualenv virtpy``` 

2. Activate virtual environment
```. ./virtpy/bin/activate```

3. install requirements 
```pip install -r requirements.txt```

4. Sync database and migrate
```python manage.py syndb```
```python manage.py migrate```

5. Collect static
```python manage.py collectstatic````

6. Start runserver
```python manage.py runserver 0.0.0.0

