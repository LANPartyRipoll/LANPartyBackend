# LANPartyBackend

## Install packages
```
# apt install python3 python3-pip python3-venv python3-mysqldb git
```

## Prepare venv
```
# su lanpartyripoll --shell /bin/bash
$ cd ~
$ python3 -m venv backend
$ cd backend
$ source bin/activate
$ git clone https://github.com/LANPartyRipoll/LANPartyBackend.git
```

## Install Django
```
$ pip3 install Django
$ pip3 install djangorestframework
```

## Create LANPartyService/settings_secret.py
```
SECRET_KEY_SAVED='SECRET_KEY'
DATABASE_MYSQL="DBName"
USER_NAME="user"
PASSWORD= "password"
```

## Perform database migrations
The database must be empty before executing these commands.
```
$ python3 manage.py makemigrations LANPartyBackend
$ python3 manage.py migrate
```
Now, we have to fill the tables `inscripcions` and `tiquets` exporting them from the form database.

## Run the service
```
$ python3 manage.py runserver
```
