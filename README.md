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
```
SECRET_KEY=your: SECRET_KEY (optional)
HOST=your: HOST
PORT=your: PORT
NAME=your: NAME
USER=your: USER
PASSWORD=your: PASSWORD
DEBUG='True' or 'False'
ALLOWED_HOSTS='*'
```

##### Arguments DEBUG:
True-debugging will turn on

False-debugging will turn off


### Run

example:

```
$ python python manage.py runserver 0.0.0.0:8000
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
