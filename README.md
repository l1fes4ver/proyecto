# proyecto

 1) CREO UNA CARPETA Y LA ABRO DESDE VISUAL ESTUDIO
""mkdir venv."" ##asi me creo una carpeta dentro de DEV (me tiene que aparecer esto 'maxgarat@Maxs-Air Dev %')llamada venv, necesito estar dentro de DEV para que esto funcione
""python3.9 -m venv venv."" ##asi me creo un virtual environment en la carpetita de venv
"". venv./bin/activate"" ##asi lo activo
""pip freeze >>requirements"" ##asi me dice todo lo que tengo activado en el virtual envirnoment, osea necesito estar dentro del virtual environment para codear esto y que me aparezcan todas las cosas estas
""pip install django"" ##asi instalo django en el entorno virtual, conviene crearlo siempre dentro del entorno virtual
""django-admin startproject miproyecto"" ##asi creo el proyecto, esto me crea una carpeta llamada 'mi proyecto', se me van a crear 2 iguales entonces le cambio el nombre a una y borro la que me haya quedado vacia, asi me quedo solo con una
""git init"" ##trae a git, el '.git ignore', lo que hace es ingorarme los documentos en los que yo les asigne a gitignore
""python manage.py migrate"" ##genera la info base para que nuestra proyecto django se levante y te negera una base de datos
"""python manage.py runserver" ##me da un link a la pagina de mi proyecto, me levanta el servidor
 DESPUES DE ESTO VIENE TODO LO DEL MTV (Model, Template, Views), todo lo de las 2 clases de django, que no logre que me corra

    2) PARTE DE APPS
 ""python manage.py startapp indice"" ## esto te genera una carpeta nueva, con el nombre que vos quieras (en este caso 'indice'), la idea de esto es que cada carpeta va a estar destinada a cumplir una funcionalidad dentro de mi modelo
 --->Luego debo ir a settings.py (en la carpeta miproyecto) y agregar en apps estas dos apps con los modelos
 ""python  manage.py makemigrations""  ##esto es para que python me reconozca las clases que cree, se me va a aparecer en migrations un nuevo mini doc con las clases creadas
 ""python manage.py migrate"" ##con esto las clases creada en el paso anterior adquieren un formato especial dentro de la carpeta migration y se me crea otro archivo que muestra estas clases con su nuevo formato



 ""python manage.py shell""-------> para probar cosas por fuera del codigo
 ""usuario git"" l1fes4ver, IndependientE10


GIT

echo "# proyecto" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/l1fes4ver/proyecto.git
git push -u origin main


 ""git add.""  ##agrego cambios
 ""git commit -m "nombre"""  ##commiteo los cambios
 ""git status""

 ""git push"" ##mando todos los commits hechos a la nube, es necesario que esten todos los cambios ya comiteados antes de hacer el push
 ""git pull"" ##para traerme la ultima version del proyecto siempre antes de comenzar a trabajar me traigo los cambios y luego comienzo a trabajar 