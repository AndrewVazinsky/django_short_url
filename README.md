## Django URL Shortener
A simple Django API project to implement an URL Shortnening service.

**Requirements:**

 - Django
 - Django Rest Framework
 - ipware

**Curl:**

URL to shorten (**YOUR_LINK** - insert your link)
```
curl -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/api/shortener/**YOUR_LINK**
```

URL's statistics (**YOUR_HASH_DATA_LINK** - insert hash data (like "6f9b96"))
```
curl -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X GET http://127.0.0.1:8000/api/statistics/**YOUR_HASH_DATA_LINK**
```

Delete URL (**YOUR_HASH_DATA_LINK** - insert hash data (like "6f9b96"))
```
curl -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X DELETE http://127.0.0.1:8000/api/delete/**YOUR_HASH_DATA_LINK**
```

**Run:**

 - Clone the project
 - Do `cd <project-folder>` and `pip install requirements.txt` 
 - Run `python manage.py makemigrations` and `python manage.py migrate`
 - Deploy test server: `python manage.py runserver` 