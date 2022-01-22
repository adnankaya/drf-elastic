- python version 3.8
- Elasticsearch version 6.3.0

```
virtualenv -p python3.8 venv
# activate venv
pip install -r requirements.txt
python manage.py populate_db
python manage.py runserver

````
### Test
|Address|Description|
|-|-|
|http://127.0.0.1:8000/s/user/ali/|	Returns user 'ali44'|
|http://127.0.0.1:8000/s/user/adnan_/|	Returns user 'adnan_'|
|http://127.0.0.1:8000/s/category/seo/|	Returns category 'SEO optimization'|
|http://127.0.0.1:8000/s/category/progreming/|	Returns category 'Programming'|
|http://127.0.0.1:8000/s/article/linux/|	Returns article 'Installing the latest version of Ubuntu'|
|http://127.0.0.1:8000/s/article/java/|	Returns article 'Which programming language is the best?'|

### Redis
- To display the keys that are written by django
```bash
 └─ λ redis-cli -n 1
127.0.0.1:6379[1]> keys *
# output
1) "example:1:views.decorators.cache.cache_header..444444.en-us.UTC"
2) "example:1:views.decorators.cache.cache_page..GET.123.123.en-us.UTC"

```


##### Resources
- https://testdriven.io/blog/django-drf-elasticsearch/#elasticsearch-queries
- https://realpython.com/caching-in-django-with-redis/


# Contact
- adnankayace.blogspot.com
- youtube.com/c/adnankaya