toolbox
======

toolbox is a simple Django app.


Quick start
-----------

1. Add 'toolbox' to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'toolbox',
    ]

2. Include the toolbox URLconf in your project urls.py like this::

    url(r'^toolbox/', include('toolbox.urls')),

3. Run  to create the toolbox models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/toolbox/.


Features
----------

1. Errbit middleweare
    TODO: fabric recipe errbit service + mongo

    Filename: errbit_middleware.py

2. Queryset result to ExcelResponse View

    Filename: excel_response.py

3. Utilities to convert datetime from/to utc to localtime

    Filename: timezone.py


4. Fake smtp server


5. Generate PDF from URL
    Sys dep: brew install python3 cairo pango gdk-pixbuf libffi
    env vars:
        export LC_ALL=en_US.UTF-8
        export LANG=en_US.UTF-8
    requirements: WeasyPrint==0.41

6. HTML parser: Detect if text has html entities and convert to plain text


Changelog
----------

##### 0.3.1
* HTML Parser
* Pipenv dependencies manager

##### 0.3.0
* Custom Auth Backend support login with email or username

