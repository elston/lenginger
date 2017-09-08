#!/bin/bash
# ...
source /$PROJECT/.env/$PROJECT/bin/activate     
cd /$PROJECT
# python manage.py runserver -h 0.0.0.0 -p 8000
# python webinvoice.wsgi
python debug.py