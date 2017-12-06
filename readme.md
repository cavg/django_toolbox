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