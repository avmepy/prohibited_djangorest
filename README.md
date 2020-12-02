# prohibited_djangorest
the registry of prohibited sites

2 roles: admin and non-authenticated user

Admin can add prohibited IP addresses and site domains to the database (via API).
Non-authenticated user can make requests to block this or that web-site


for example host: 127.0.0.1:8000

urls:

  - create request (available for everyone)
    [127.0.0.1:8000/api/forbidden/request/create/](127.0.0.1:8000/api/forbidden/request/create/)
    
  - list of all requests (only for admin)
    [127.0.0.1:8000/api/forbidden/request/all/](127.0.0.1:8000/api/forbidden/request/all/)
    
  - detail of request (only for admin)
    admin can make the decision (confirm/reject) (default=verifying)
    id = 1 (for example)
    [127.0.0.1:8000/api/forbidden/request/detail/1/](127.0.0.1:8000/api/forbidden/request/detail/1/)
    
  - add item to prohibited list (only for admin)
    [127.0.0.1:8000/api/forbidden/prohibited/create/](127.0.0.1:8000/api/forbidden/prohibited/create/)
    
  - prohibited list: all prohibited items (only for admin)
    [127.0.0.1:8000/api/forbidden/prohibited/all/](127.0.0.1:8000/api/forbidden/prohibited/all/)
    
  - prohibited item detail (editable) (only for admin)
    id = 1 (for examaple)
    [127.0.0.1:8000/api/forbidden/prohibited/detail/1/](127.0.0.1:8000/api/forbidden/prohibited/detail/1/)
        

to run project:

```bash python manage.py runserver```

or 

```bash python manage.py runserver 127.0.0.1:8000```

to create superuser (admin):

```bash python manage.py createsuperuser```
