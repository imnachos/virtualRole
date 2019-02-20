# virtualRole

Simple RPG (DnD, Pathfinder) campaign manager based on Django.

# Installation

Simply clone this repo, install the dependencies and run:

```
py manage.py makemigrations
```

```
py mana```.py migrate
```

```
py manage.py runserver
```

The server should now be running at 127.0.0.1:8000

# Running the server

The easy an recommended way is to create a .bat file in the root folder with the following content:

```
echo on
set SECRET_KEY=SOME_SUPER_SECRET_KEY
py manage.py runserver
pause
```

