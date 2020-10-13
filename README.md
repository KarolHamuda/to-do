# Run app
```
pip3 install -r requirements
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py runserver
```
# API
`localhost:8000/api/tasks`  
Methods: GET, POST  
Params: 
* title: string
* description: string
* priority: string (hex)  

`localhost:8000/api/tasks/:task_id`  
Methods: GET, POST, PATCH, DELETE  
Params:
* title: string
* description: string
* priority: string (hex)
