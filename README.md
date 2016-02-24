# SICON

Sistema de informacion para consecionarios 

Proyecto de WWW

Integrantes:

Brayan Rodriguez, Nelson Portilla, Juan Diego Prado, Fernando Sanchez y Alvaro Martinez

La base de datos es postgres

nombre: sicondb
usuario: siconuser
password: hola123

Cargar backup de base de datos 
psql -h localhost -U siconuser sicondb < SICON/static/backup2

#Url página internet
http://still-earth-4140.herokuapp.com/

#conexión a base de datos de heroku
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': 'd8bn3ai6qhpo8r',
'USER': 'wcmiceorbsxdsu',
'PASSWORD': '27X4BZarTc2VRjtMc8EI-YIKn6',
'HOST': 'ec2-54-225-165-132.compute-1.amazonaws.com',
'PORT': '5432',

Descargar heroku: https://devcenter.heroku.com/articles/getting-started-with-python#set-up

heroku login 
email: brayan.rodriguez.rivera@correounivalle.edu.co
password: bryan1112


git clone https://github.com/fermat986/SICON/

cd SICON

heroku create 

#Colocar todos los archivos del repositorio de heroku (https://github.com/heroku/python-getting-started.git) y la carpeta gettingstarted, en esta carpeta debe ir el settings.py y el wsgi.py del SICON. Estos archivos en la raíz.

#se editan los archivos del gettingstarted para que queden dentro de la app SICON.SICON.(...)

#Se pasa el manage.py a la carpeta raíz y se le hace lo mismo que en el paso anterior.

#En el settings.py de SICON/SICON se modifican las rutas de los INSTALLED_APPS, del TEMPLATES, el STATIC_ROOT = 'SICON/static', STATIC_URL = '/SICON/static/'

#En el urls.py de SICON/SICON 
urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )

git add .

git commit -m "mi commit"

git push heroku master

heroku ps:scale web=1

heroku open

#Cada que se haga una modificación se haga se debe hacer git add, commit y push heroku master

# Para hacer push al github, se debe hacer:
git push https://github.com/fermat986/SICON.git  

# Para hacer pull al github, se debe hacer:
git pull https://github.com/fermat986/SICON.git  

# Para clonar de heroku
heroku git:clone -a still-earth-4140

