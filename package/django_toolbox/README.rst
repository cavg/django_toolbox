======
toolbox
=====

toolbox is a simple Django app.

Detailed documentation is in the 'docs' directory.

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
