# working with online security-panel

## How to start

Python3 should be already installed.

Use pip to install dependencies:

```
pip install -r requirements.txt
```

and

create file 'project/.env'

File type '.env':

Note: The data can be obtained from the administration of the bank "Сияние"

```
SECRET_KEY=REPLACE_ME
DEBUG=False
ALLOWED_HOSTS=*
DB_URL=postgres://login:password@host:port/name
```

##### Arguments DEBUG:
True-debugging will turn on

False-debugging will turn off



### Run

example:

```
$ python manage.py runserver 0.0.0.0:8000
```


### You will see

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
...
```

### website launch

```
$ python chrome http://127.0.0.1:8000/
```
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)


# Project Goals

Training
