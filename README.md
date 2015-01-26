# admindemo
Django admin test demo

##Installation

1 - Create a virtualenv
$ virtualenv --no-site-packages --distribute yarvis

2 - Activate environment
$ source yarvis/bin/activate

3 - Clone the project
$ git clone https://github.com/vquinones/admindemo

4 - Install requirements
$ cd admindemo/requirements
$ pip install -r local.txt

5 - Syncdb (this demo works with Mysql DB, but can just works with sqlite3)
$ python manage.py syncdb

6 - Start the app
$ python manage.py runserver

##URLs
Single page. Can be used as landing page

http://localhost:8000/admin/screen-configuration/
http://localhost:8000/admin/display-configuration/

Model Admin
http://localhost:8000/admin/myadmin/screen/
