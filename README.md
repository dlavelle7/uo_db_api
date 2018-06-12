UO Database API [![Build Status](https://travis-ci.com/dlavelle7/uo_db_api.svg?branch=master)](https://travis-ci.com/dlavelle7/uo_db_api)
===============
REST API for what will be the "uo" android app.

Dependencies
------------
* Python 3.6.5

Local Development
-----------------
```
pip install -r requirements_base.txt
python manage.py runserver --settings=uo_db_api.dev_settings
```

Unit Tests
----------
```
pip install -r requirements_test.txt
python manage.py test --settings=uo_dbapi.dev_settings
```
